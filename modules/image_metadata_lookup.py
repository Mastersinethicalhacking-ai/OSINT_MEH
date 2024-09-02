from PIL import Image
from PIL.ExifTags import TAGS

def lookup(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f"{tag_name}: {value}")
    else:
        print("No metadata found.")

