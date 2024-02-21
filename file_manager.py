import os
import shutil
from settings import WORKING_DIRECTORY
from settings import WORKING_DIRECTORY_IZN
from settings import WORKING_DIRECTORY_PAPKA

def create_folder(folder_name):
    path = os.path.join(WORKING_DIRECTORY, folder_name)
    os.mkdir(path)
    print("Команда выполнена")

def delete_folder(folder_name):
    try:
        path = os.path.join(WORKING_DIRECTORY, folder_name)
        os.rmdir(path)
        print("Команда выполнена")
    except OSError as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def move_to_folder(folder_name):
    try:
        global WORKING_DIRECTORY
        new_path = os.path.join(WORKING_DIRECTORY, folder_name)
        if not os.path.isdir(new_path):
            print("Ошибка! Попробуйте воспользоваться командой заново!")
            return
        WORKING_DIRECTORY = new_path
        print("Команда выполнена")
    except Exception as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def move_up():
    global WORKING_DIRECTORY
    global WORKING_DIRECTORY_IZN
    global WORKING_DIRECTORY_PAPKA
    parent_directory = os.path.dirname(WORKING_DIRECTORY)
    if parent_directory == WORKING_DIRECTORY_PAPKA:
        print("Вы находитесь в корневой папке. Невозможно переместиться вверх.")
    else:
        WORKING_DIRECTORY = parent_directory
        print("Команда выполнена")

def current_folder():
    print("Текущая папка:", WORKING_DIRECTORY)

def create_file(file_name):
    path = os.path.join(WORKING_DIRECTORY, file_name)
    open(path, 'w').close()
    print("Команда выполнена")

def write_to_file(file_name, text):
    try:
        path = os.path.join(WORKING_DIRECTORY, file_name)
        with open(path, 'w') as file:
            file.write(text)
        print("Команда выполнена")
    except OSError as e:
        print(f"Ошибка! Попробуйте воспользоваться командой заново!")

def view_file(file_name):
    try:
        path = os.path.join(WORKING_DIRECTORY, file_name)
        with open(path, 'r') as file:
            print(file.read())
        print("Команда выполнена")
    except OSError as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def delete_file(file_name):
    try:
        path = os.path.join(WORKING_DIRECTORY, file_name)
        os.remove(path)
        print("Команда выполнена")
    except OSError as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def copy_file(file_name, destination_folder):
    global WORKING_DIRECTORY_IZN
    try:
        source = os.path.join(WORKING_DIRECTORY, file_name)
        if not os.path.isfile(source):
            raise FileNotFoundError("Файл не найден")
        
        if not destination_folder.startswith(WORKING_DIRECTORY_IZN):
            raise ValueError(f"Путь назначения должен начинаться с {WORKING_DIRECTORY_IZN}")
        
        destination = os.path.join(destination_folder, file_name)
        
        if not os.path.exists(os.path.dirname(destination)):
            raise FileNotFoundError("Указанного пути назначения не существует")

        shutil.copyfile(source, destination)
        print("Команда выполнена")

    except FileNotFoundError as e:
        print("Указанного пути не существует")
    
    except ValueError as e:
        print(f"Путь назначения должен начинаться с {WORKING_DIRECTORY_IZN}")
    
    except Exception as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def move_file(file_name, destination_folder):
    global WORKING_DIRECTORY_IZN
    try:
        source = os.path.join(WORKING_DIRECTORY, file_name)
        if not os.path.isfile(source):
            raise FileNotFoundError("Файл не найден")
        
        if not destination_folder.startswith(WORKING_DIRECTORY_IZN):
            raise ValueError(f"Путь назначения должен начинаться с {WORKING_DIRECTORY_IZN}")
        
        destination = os.path.join(destination_folder, file_name)
        
        if not os.path.exists(os.path.dirname(destination)):
            raise FileNotFoundError("Указанного пути назначения не существует")

        shutil.move(source, destination)
        print("Команда выполнена")

    except FileNotFoundError as e:
        print("Указанного пути не существует")
    
    except ValueError as e:
        print(f"Путь назначения должен начинаться с {WORKING_DIRECTORY_IZN}")
    
    except Exception as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def rename_file(old_name, new_name):
    try:
        old_path = os.path.join(WORKING_DIRECTORY, old_name)
        new_path = os.path.join(WORKING_DIRECTORY, new_name)
        os.rename(old_path, new_path)
        print("Команда выполнена")
    except OSError as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")

def rename_file(old_name, new_name):
    try:
        old_path = os.path.join(WORKING_DIRECTORY, old_name)
        new_path = os.path.join(WORKING_DIRECTORY, new_name)
        os.rename(old_path, new_path)
        print("Команда выполнена")
    except OSError as e:
        print("Ошибка! Попробуйте воспользоваться командой заново!")
