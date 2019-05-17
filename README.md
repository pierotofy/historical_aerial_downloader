# Historical Aerial Downloader

A very rough script to download and add EXIF georeferencing information to historical aerial images archives.

## Installation

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You also need to install `exiftool`.

## Usage

Modify CSV_URL, URL_PREFIX and IMAGE_EXT in `run.py` and then run:

```
python run.py
```

Results will be stored in `results/`.

Note that this is not a general purpose script.

Once downloaded with this script, historical aerial stereo-images can be processed with [OpenDroneMap](https://opendronemap.org) to create georeferenced, orthorectified images such as the one shown below:

![anim](https://user-images.githubusercontent.com/1951843/57937420-e8a27f80-7893-11e9-8707-2915d7223e46.gif)

![image](https://user-images.githubusercontent.com/1951843/57937480-08d23e80-7894-11e9-8864-e864d8fbb5c1.png)

You can download the resulting GeoTIFF from https://drive.google.com/open?id=18UhkAR5jggOtgNvBzadEz-P-bymu14_m

Credits to University of Minnesota for the aerial images archive.
