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
    # To share this script with others, the sync must happen
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


def add_stats_to_db(sex, stats):
    global db

    # TODO
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })


def add_data_to_firebase(img_path, sex, stats):
    print('Saving data...')
    add_image_to_storage(img_path, sex)
    add_stats_to_db(sex, stats)
    increment_current_file_name(sex)


def delete_image(img_path):
    remove(img_path)


def show_image(img_path):
    try:
        img = Image.open(img_path)
        print('< Opening image: {} >\n'.format(img_path.split('/')[-1]))
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
    print('Pick the stats for this {}\n'.format(sex))
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


def confirm_save_stats(stats):
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
        write_current_file_names()
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
        i_path = '{}/{}/{}'.format(IMAGES_PATH, chosen_sex, i)
        show_image(i_path)
        stats = None
        confirmed = False
        was_canceled = False
        while not confirmed:
            if was_canceled:
                should_exit_program(
                    not prompt_start_or_continue('You denied the confirmation...\nDo it again?'))
            stats = prompt_and_get_stats(chosen_sex, get_json_file_data(
                'categories.json')['categories'][chosen_sex])
            confirmed = confirm_save_stats(stats)
            if confirmed == False:
                was_canceled = True
        add_data_to_firebase(i_path, chosen_sex, stats)  # TODO: more logic?
        # TODO: delete image?
        should_exit_program(not prompt_start_or_continue('Continue'))


if __name__ == '__main__':
    main()
