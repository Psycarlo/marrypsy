from os import listdir, remove, system, name
from os.path import isfile, join
from PIL import Image
import json

from firebase_admin import credentials, initialize_app, storage, firestore

CREDENTIALS_FILE = './marrypsy-config.json'
MY_CREDENTIALS = credentials.Certificate(CREDENTIALS_FILE)
CURRENT_FILE_NAME_FEMALE = 0
CURRENT_FILE_NAME_MALE = 0
IMAGES_PATH = '../content'

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


def get_json_file_data(file_path):
    with open(file_path, "r") as f:
        return json.loads(f.read())


def get_current_file_names():
    with open("currentFileName.txt", "r+") as f:
        lines = f.readlines()
        for l in lines:
            s, n = l.strip().split(' ')
            set_current_file_name(s, n)


def sync_file_name(sex):
    # Get last file number from firebase and sync if needed
    pass


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


def is_input_valid(user_input, number_choices):
    try:
        a = int(user_input)
        if a < 1 or a > number_choices:
            return False
        return True
    except ValueError:
        return False


def prompt_and_get_stats(sex, categories={}):
    res = {}
    print('Input the stats for this {}\n'.format(sex))
    input('Hit [ENTER] to start >')
    clear_terminal()
    for outer in categories.keys():
        for inner in categories[outer].keys():
            print('[ {} ]\n'.format(outer.upper()))
            print('[?] {}:'.format(inner.capitalize()))
            counter = 1
            for choice in categories[outer][inner]:
                print(' {}) {}'.format(counter, choice.capitalize()))
                counter += 1
            user_answer = input('Answer: ')
            while not is_input_valid(user_answer, len(categories[outer][inner])):
                user_answer = input('[!] Error, try again: Awnser: ')
            if outer not in res.keys():
                res[outer] = {}
            res[outer][inner] = categories[outer][inner][int(
                user_answer) - 1]
            clear_terminal()
    res["sex"] = sex
    res["imgName"] = get_current_file_name(sex)
    return res


def confirm_stats(stats):
    clear_terminal()
    print('[ CONFIRMATION ]\n')
    print(json.dumps(stats, indent=2))

    confirmation = input('Save? Y/n ')
    if confirmation.lower() == 'n':
        return False
    return True


def get_all_folder_images(folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.lower().endswith(('.png', '.jpg'))]


def prompt_start_or_continue(text):
    clear_terminal()
    answer = input('{}? Y/n\n> '.format(text))
    if answer.lower() == 'n':
        clear_terminal()
        print('Thanks and see you later!')
        return False
    return True


def should_exit_program(bool=True):
    if bool:
        exit(0)


def choose_sex():
    print('\nWhat you want to evaluate?')
    print(' [F]emales   [Default]')
    print(' [M]ales ')
    answer = input('Answer: ')
    while answer.lower() not in 'fm':
        answer = input('Choose f for female or m for male. Answer: ')
    if answer == 'f':
        return 'female'
    return 'male'


def print_welcome():
    print('        [ Welcome to MarryPsy stats evaluator ]  \n\n')
    print(' You will be looking at photos and describing what you see')
    print('                       Ready?')


def clear_terminal():
    system('cls' if name == 'nt' else 'clear')


def main():
    clear_terminal()
    print_welcome()
    chosen_sex = choose_sex()
    should_exit_program(not prompt_start_or_continue('Start'))
    clear_terminal()
    all_images = get_all_folder_images('{}/{}'.format(IMAGES_PATH, chosen_sex))
    for i in all_images:
        show_image('{}/{}/{}'.format(IMAGES_PATH, chosen_sex, i))
        confirm_stats(prompt_and_get_stats(chosen_sex, get_json_file_data(
            'categories.json')['categories'][chosen_sex]))
        should_exit_program(not prompt_start_or_continue('Continue'))

    # show_image('../content/female/1.jpg')
    # add_image_to_storage('../content/female/1.jpg')
    # write_current_file_names()
    # add_image_to_storage('../content/female/1.jpg', 'female')
    # get_current_file_names()
    # delete_image('../content/female/4.jpg')
    # print(prompt_continue())
    # print(get_json_file_data('categories.json')['categories']['female'].keys())
    # print(prompt_and_get_stats('female', get_json_file_data(
    #    'categories.json')['categories']['female']))
    # confirm_stats(prompt_and_get_stats('female', get_json_file_data(
    #    'categories.json')['categories']['female']))
    # print(is_input_valid('4', 3))


if __name__ == '__main__':
    main()
