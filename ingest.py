#!/usr/bin/python3

import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

api = KaggleApi()
api.authenticate()

file = str(os.getenv('file'))

api.dataset_download_file('yamaerenay/spotify-dataset-19212020-160k-tracks', file_name=file, path="./")

with zipfile.ZipFile(f'./{file}.zip', 'r') as zipref:
    zipref.extractall('./')