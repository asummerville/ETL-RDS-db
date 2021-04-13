#!/usr/bin/python3

import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

api = KaggleApi()
api.authenticate()

file_name = os.getenv('file_name')

api.dataset_download_file('yamaerenay/spotify-dataset-19212020-160k-tracks', file_name=file_name, path="./")

#if file name contains .zip, unzip it

try:
    with zipfile.ZipFile(f'./{file_name}.zip', 'r') as zipref:
        zipref.extractall('./')
except:
    pass

