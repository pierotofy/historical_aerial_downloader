import csv
import argparse
import requests
import shutil
import os
import subprocess

parser = argparse.ArgumentParser(description='Historical Downloader')
args = parser.parse_args()

CSV_URL='http://geo.lib.umn.edu/Hennepin_County/y1940/Hennepin_1940.csv'
URL_PREFIX='http://geo.lib.umn.edu/Hennepin_County/y1940/'
IMAGE_EXT='jpg'

def run(cmd):
    print(cmd)
    p = subprocess.Popen(cmd, shell=True)
    retcode = p.wait()
    if retcode < 0:
        raise Exception("Child was terminated by signal {}".format(-retcode))
    elif retcode > 0:
        raise Exception("Child returned {}".format(retcode))

r = requests.get(CSV_URL)
csv_file = os.path.basename(CSV_URL)
with open(csv_file, 'wb') as f: 
    f.write(r.content)
    print("Downloaded " + csv_file)

if os.path.exists("results"):
    print("Removing results/")
    shutil.rmtree("results")

os.mkdir("results")

print("Starting to process...")
errors = 0

with open(csv_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            lat, lon = map(float, row[0:2])
            image = row[4] + "." + IMAGE_EXT
            url = URL_PREFIX + image
            line_count += 1
            
            # Download
            file = os.path.join("results", image)
            try:
                r = requests.get(url)
                with open(file, 'wb') as f: 
                    f.write(r.content)
                    print("Downloaded " + image)

                lon_ref = 'E' if lon > 0 else 'W'
                lat_ref = 'N' if lat > 0 else 'S'

                run("exiftool -overwrite_original_in_place "
                    "-GPSLongitude=\"%s\" "
                    "-GPSLatitude=\"%s\" "
                    "-GPSAltitude=\"100\" "
                    "-GPSLongitudeRef=\"%s\" "
                    "-GPSLatitudeRef=\"%s\" "
                    "-GPSAltitudeRef=\"above sea level\" "
                    "%s" % (lon, lat, lon_ref, lat_ref, file))            
            except Exception as e:
                if os.path.exists(file):
                    os.remove(file)
                print("Skipping %s: %s" % (file, str(e)))
                errors += 1
    print(f'Processed {line_count} lines, skipped {errors}.')
