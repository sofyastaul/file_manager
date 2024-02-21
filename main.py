import file_manager

print("Добро пожаловать в файловый менеджер")
while True:
    command = input("Введите команду: ")
    if command == "create_folder":
        folder_name = input("Введите имя папки: ")
        file_manager.create_folder(folder_name)
    elif command == "delete_folder":
        folder_name = input("Введите имя папки: ")
        file_manager.delete_folder(folder_name)
    elif command == "move_to_folder":
        folder_name = input("Введите имя папки: ")
        file_manager.move_to_folder(folder_name)
    elif command == "move_up":
        file_manager.move_up()
    elif command == "current_folder":
        file_manager.current_folder()
    elif command == "create_file":
        file_name = input("Введите имя файла: ")
        file_manager.create_file(file_name)
    elif command == "write_to_file":
        file_name = input("Введите имя файла: ")
        text = input("Введите текст для записи: ")
        file_manager.write_to_file(file_name, text)
    elif command == "view_file":
        file_name = input("Введите имя файла: ")
        file_manager.view_file(file_name)
    elif command == "delete_file":
        file_name = input("Введите имя файла: ")
        file_manager.delete_file(file_name)
    elif command == "copy_file":
        file_name = input("Введите имя файла: ")
        destination_folder = input("Введите имя папки назначения: ")
        file_manager.copy_file(file_name, destination_folder)
    elif command == "move_file":
        file_name = input("Введите имя файла: ")
        destination_folder = input("Введите полное имя папки назначения: ")
        file_manager.move_file(file_name, destination_folder)
    elif command == "rename_file":
        old_name = input("Введите текущее имя файла: ")
        new_name = input("Введите новое имя файла: ")
        file_manager.rename_file(old_name, new_name)
    elif command == "":
        file_manager.show_current_folder_name()
    elif command == "exit":
        print("До свидания!")
        break
    else:
        print("Неизвестная команда. Пожалуйста, попробуйте еще раз!")
