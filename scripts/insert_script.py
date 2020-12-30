from os import listdir, remove
from os.path import isfile, join
from PIL import Image

from firebase_admin import credentials, initialize_app, storage, firestore

CREDENTIALS_FILE = './marrypsy-config.json'
MY_CREDENTIALS = credentials.Certificate(CREDENTIALS_FILE)
CURRENT_FILE_NAME_FEMALE = 0
CURRENT_FILE_NAME_MALE = 0

initialize_app(MY_CREDENTIALS, {'storageBucket': 'marrypsy-34678.appspot.com'})

db = firestore.client()

# from google.cloud import storage  # Getting module errors
# from firebase import firebase # Getting module errors
# Inserts image and stats in firebase

# Brainstorm: This script open the images in the folder
# one by one. After user closes the image, the program ask
# the user about the images stats. Stats are hardcoded - meaning
# that the user will pick one for each category.
# After that, the user will be prompt to review and submit.

# marrypsy-34678.appspot.com


def get_current_file_names():
    with open("currentFileName.txt", "r+") as f:
        lines = f.readlines()
        for l in lines:
            s, n = l.strip().split(' ')
            set_current_file_name(s, n)


def write_current_file_names():
    with open("currentFileName.txt", "r+") as f:
        f.truncate(0)
        f.write("female {}\n".format(CURRENT_FILE_NAME_FEMALE))
        f.write("male {}\n".format(CURRENT_FILE_NAME_MALE))


def get_current_file_name(sex):
    global CURRENT_FILE_NAME_FEMALE, CURRENT_FILE_NAME_MALE

    if sex == "female":
        return CURRENT_FILE_NAME_FEMALE
    elif sex == "male":
        return CURRENT_FILE_NAME_MALE
    return None


def set_current_file_name(sex, numb):
    global CURRENT_FILE_NAME_FEMALE, CURRENT_FILE_NAME_MALE

    if sex == "female":
        CURRENT_FILE_NAME_FEMALE = numb
    elif sex == "male":
        CURRENT_FILE_NAME_MALE = numb


def increment_current_file_name(sex):
    global CURRENT_FILE_NAME_FEMALE, CURRENT_FILE_NAME_MALE

    if sex == "female":
        CURRENT_FILE_NAME_FEMALE += 1
    elif sex == "male":
        CURRENT_FILE_NAME_MALE += 1


def add_image_to_storage(img_path, sex):
    bucket = storage.bucket()
    current_file_name = get_current_file_name(sex)
    blob = bucket.blob(
        '{}/{}'.format(sex, current_file_name))
    blob.upload_from_filename(img_path)
    blob.make_public()
    increment_current_file_name(sex)


def add_stats_to_db(sex, stats):
    global db

    # TODO
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })


def delete_image(img_path):
    remove(img_path)


def show_image(img_path):
    try:
        img = Image.open(img_path)
        img.show()
    except IOError:
        print('Error (1)')


def get_all_folder_images(folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.lower().endswith(('.png', '.jpg'))]


def prompt_continue():
    answer = input('Continue? Y/n\n> ')
    if answer.lower() == 'n':
        return False
    return True


def main():
    # show_image('../content/female/1.jpg')
    print(get_all_folder_images('../content/female'))
    # add_image_to_storage('../content/female/1.jpg')
    # write_current_file_names()
    # add_image_to_storage('../content/female/1.jpg', 'female')
    # get_current_file_names()
    # delete_image('../content/female/4.jpg')
    print(prompt_continue())


if __name__ == '__main__':
    main()
