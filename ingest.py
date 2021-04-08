#!/usr/bin/python3

import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

file = str(os.getenv('file'))

data = api.dataset_download_file('owner/dataset', file_name=file)