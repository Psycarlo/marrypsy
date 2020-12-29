from os import listdir
from os.path import isfile, join
from PIL import Image
# Inserts image and stats in firebase

# Brainstorm: This script open the images in the folder
# one by one. After user closes the image, the program ask
# the user about the images stats. Stats are hardcoded - meaning
# that the user will pick one for each category.
# After that, the user will be prompt to review and submit.


def show_image(img_path):
    try:
        img = Image.open(img_path)
        img.show()
    except IOError:
        print('Error (1)')


def get_all_folder_images(folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.lower().endswith(('.png', '.jpg'))]


# show_image('../content/female/1.jpg')
print(get_all_folder_images('../content/female'))
