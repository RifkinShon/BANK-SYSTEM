
def task_id(file_path_txt):

    try:
        # קריאה מהקובץ
        with open(file_path_txt, 'r') as file:
            current_id = file.read()

    except FileNotFoundError:
        print(f"File '{file_path_txt}' not found. Creating a new file.")
        current_id = "1"
        txt_data = 1
        try:
            with open(file_path_txt, 'w') as file:
                file.write(str(txt_data))
                # print(f".txt file '{file_path}' has been created successfully")
        except FileExistsError:
            print("That file already exists")


    except PermissionError:  # אין רשות סוגר תוכנה
        print("You do not have permission to read that file")
        exit()
    try:
        print(f"Current ID read from file: {current_id}")
        id_int = int(current_id)
        id_int_current = id_int
        id_int += 1

        # בודק שיש משימות קובץ  #
        import json
        file_path = "tasks.json"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)  # תיקון: לא להשתמש ב-file.read()

                # בודקים אם המפתח "tasks" קיים ומכיל רשימה
                if "tasks" in data and isinstance(data["tasks"], list):
                    content = data["tasks"]
                else:
                    content = []
        except (FileNotFoundError, PermissionError, json.JSONDecodeError):
            content = []
        if len(content) == 0:
            id_int_current = 1
            id_int = 2

        with open(file_path_txt, 'w') as file:
            file.write(str(id_int))
        return id_int_current

    except ValueError:

        id_int_current = 1
        id_int_current_plus = id_int_current + 1
        with open(file_path_txt, 'w') as file:
            file.write(str(id_int_current_plus))
        print(f".txt file '{file_path_txt}' has been created successfully")
        return id_int_current

task_id("transactionId.txt")