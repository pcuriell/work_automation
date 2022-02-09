import zipfile
import os

zip_files = [file for file in os.listdir() if '.zip' in file]
output_dir = os.getcwd()

for file in zip_files:
  with zipfile.ZipFile(file) as zip_ref:
    zip_ref.extractall(output_dir)
  
