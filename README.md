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

![image](https://user-images.githubusercontent.com/1951843/57887842-8e0b1400-77fe-11e9-8c42-c031aa794c70.png)

Credits to University of Minnesota for the aerial images archive.
