import os
from PIL import Image
import sys

if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = input('Please enter full path to the destination folder:\n')

if len(sys.argv) > 2:
    width = int(sys.argv[2])
else:
    width = 800


files = [os.path.join(folder, file) for file in os.listdir(
    folder) if 'jpeg' in file or 'JPG' in file or 'JPEG' in file or 'jpeg' in file or 'png' in file]

print(f'{len(files)} JPEG files found.')
print(f'Resizing to {width} px width.')


for file in files:

    img = Image.open(file)

    if img.size[0] > width:

        y_ratio = img.size[1]/img.size[0]
        print(f'{file} {img.size} resizing to {(width,int(width*y_ratio))}')
        img = img.resize((width, int(width*y_ratio)))
#         img.save(new_name,'jpeg')
        img.save(file, optimize=True, quality=85)
