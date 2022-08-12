import io
import json


class GameMap:
    def __init__(self, map_file_path):
        self.map_file = open(map_file_path)
        self.map_data = json.load(self.map_file)

        self.map_file.close()

    def show_map_data(self):
        print(self.map_data)

