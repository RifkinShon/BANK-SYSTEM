
import json




class FileManager:
    
    def __init__(self, file_path,data_dict):
        self.file_path = file_path
        self.data_dict=data_dict


    def ensure_file_exists(self):
     import os
     import json
     if not os.path.exists(self.file_path):
         print(f"JSON file '{self.file_path}' does not exist. Creating a new file.")
         with open(self.file_path, 'w') as file:
             json.dump(self.data_dict, file, indent=2)
         print(f"JSON file '{self.file_path}' has been created successfully")
         return
     else:
        print(f"JSON file '{self.file_path}' already exists.")

    def save_data(self):
        with open(self.file_path, 'w') as file:
                json.dump(self.data_dict, file, indent=2)
                print(f"JSON file '{self.file_path}' has been saved successfully")
                return
    def load_data(self):
        import json
        try:
            with open(self.file_path, 'r') as file:
                self.data_dict = json.load(file)
                print(f"Data loaded successfully from '{self.file_path}'")
                return self.data_dict
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{self.file_path}'.")
            return None
    def json_to_csv(self): 
        
        import csv
        csv_file_path = self.file_path.replace('.json', '.csv')
        data_dict = self.load_data()
        
        for key, task_list in data_dict.items():
            headers = task_list[0].keys()
            with open(csv_file_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(task_list)
    @staticmethod
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



dict_W={
            "id": 65,
            "title": "89",
            "Description": "Milk, eggs, bread",
            "status": "todo",
            "creativeTime": "2026-03-05 10:30:00",
            "UpdateTime": "2026-03-05 10:30:00"
        }  

F1=FileManager("JJ.json",{"tasks": []})
F1.ensure_file_exists()
F1.load_data()
F1.json_to_csv()

