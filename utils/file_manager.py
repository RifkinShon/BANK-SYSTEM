
import json
import os




   
class FileManager:
    
    def __init__(self, file_path,data_dict):
        self.file_path = file_path
        self.data_dict=data_dict



   
    def ensure_file_not_empty(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) == 0:
            print(f"JSON file '{self.file_path}' is empty. Initializing with an empty dictionary.")
            return True
        else:
            print(f"JSON file '{self.file_path}' is not empty.")
            return False



   
    def ensure_file_exists(self):
        import os
        import json
        if not os.path.exists(self.file_path):
            print(f"JSON file '{self.file_path}' does not exist. Creating a new file.")
            with open(self.file_path, 'w') as file:
                json.dump({}, file, indent=2)
            print(f"JSON file '{self.file_path}' has been created successfully")
            return True
        else:
            print(f"JSON file '{self.file_path}' already exists.")
            return False


    def save_data(self):
        existing = self.load_data()
        
        if existing is None:       
            existing = {}
            print("there is no data")
        
        for key in self.data_dict:
            if key in existing:
                existing[key].extend(self.data_dict[key]) 
            else:
                existing[key] = self.data_dict[key]        
        
        with open(self.file_path, 'w') as file:
                json.dump(existing, file, indent=2)
                print(f"JSON file '{self.file_path}' has been saved successfully")
                return

    def load_data(self):
        try:
            # בדיקה האם הקובץ קיים וגם ריק
            if os.path.exists(self.file_path) and os.path.getsize(self.file_path) == 0:
                return {} # מחזיר מילון ריק במקום לקרוס
                
            with open(self.file_path, 'r') as file:
                data_dict = json.load(file)
                print(f"Data loaded successfully from '{self.file_path}'")
                return data_dict
                
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.file_path}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File '{self.file_path}' is not a valid JSON file.")


    def delete_data(self):
        existing = self.load_data()
        
        if existing is None:
            print("No data found in file")
            return
        
        # מוציא את account_number מתוך {"accounts": [checking_dict_transference]}
        for key in self.data_dict:
            if isinstance(self.data_dict[key], list):
                account_to_delete = self.data_dict[key][0].get("account_number")
                break
        
        for key in existing:
            if isinstance(existing[key], list):
                existing[key] = [
                    item for item in existing[key]
                    if item.get("account_number") != account_to_delete
                ]
        try:
            with open(self.file_path, 'w') as file:
                json.dump(existing, file, indent=2)
                print(f"JSON file '{self.file_path}'   deleted data successfully")
                return
        except Exception as e:
            print(f"An error occurred while deleting data from '{self.file_path}': {e}")
            return
















    def delete_file(self):
        import os
        try:
            os.remove(self.file_path)
            print(f"File '{self.file_path}' deleted successfully")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found")


    def edit_data(self):
        existing = self.load_data()
        
        if existing is None:
            print("No data found in file")
            return
        
        # מוציא את account_number, attribute, value מתוך self.data_dict
        for key in self.data_dict:
            if isinstance(self.data_dict[key], list):
                account_number = self.data_dict[key][0].get("account_number")
                attribute = self.data_dict[key][0].get("attribute")
                value = self.data_dict[key][0].get("value")
                break
        
        found = False
        for key in existing:
            if isinstance(existing[key], list):
                for item in existing[key]:
                    if item.get("account_number") == account_number:
                        item[attribute] = value  # ← מחליף את הערך
                        found = True
        
        if not found:
            print(f"Account '{account_number}' not found in '{self.file_path}'")
            return
        
        with open(self.file_path, 'w') as file:
            json.dump(existing, file, indent=2)
            print(f"JSON file '{self.file_path}' edited successfully")



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
            file_path = "files/transactions.json"
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)  # תיקון: לא להשתמש ב-file.read()

                    # בודקים אם המפתח "transactions" קיים ומכיל רשימה
                    if "transactions" in data and isinstance(data["transactions"], list):
                        content = data["transactions"]
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
