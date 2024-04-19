from Utils.operations import *

from pathlib import Path

dataPath = Path('/Users/matoz/Documents/ASTROS/ESAPECS5/AstroWorkshop/TestData/Jsons')

dataJsons = json_open_dir(dataPath)


for file in dataJsons:
    print(file.frame_objects[0].object_name)
    for frame_object in file.frame_objects:
        print(frame_object.ecs_coords)
