import json
import os

class DbInterface:
    FILE_NAME = 'storage.data'

    def __new__(cls, *args, **kwargs):
        if not os.path.exists(cls.FILE_NAME):
            with open(cls.FILE_NAME, 'w'):
                pass
        
        return super(DbInterface, cls).__new__(cls, *args, **kwargs)

    def get_val(self, key):
        data = self.__read_file()

        if key not in data.keys():
            raise KeyError('[ERROR] No such key in DB!!!')
        
        return data[key] 
        
    def set_val(self, key, value):
        if os.stat(self.FILE_NAME).st_size == 0:
            self.__save_data({key: [value]})
        else:
            data = self.__read_file()

            if key in data.keys():
                data[key].append(value)
            else:
                data[key] = [value]

            self.__save_data(data)

    def get_all(self):
        try:
            return self.__read_file()
        except:
            return {}
        
    def __read_file(self):
        if os.stat(self.FILE_NAME).st_size == 0:
            raise Exception('[ERROR] DB is empty!!!')
            
        with open(self.FILE_NAME, 'r+') as f:
            return json.load(f)

    def __save_data(self, data: dict):
        with open(self.FILE_NAME, 'w') as f:
            json.dump(data, f)
