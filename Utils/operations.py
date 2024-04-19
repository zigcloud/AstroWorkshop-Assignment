import pathlib

from typing import List, Union
from .classes import FrameObject, Frame


def json_open(json_path: Union[str, pathlib.Path]) -> Frame:
    if isinstance(json_path, str):
        json_path = pathlib.Path(json_path)

    if json_path.is_file() and json_path.exists():
        with open(json_path, 'r') as f:
            input_json = f.read()
            try:
                frame = Frame.from_json(input_json)
                return frame
            except:
                # TODO - find the specific error
                print(f"Could not load {json_path}! JSON format is probably wrong!")
    else:
        raise Exception(f"Provided path ({json_path}) which should be representing "
                        f"a FRS JSON is not a file or it does not exist!")




def json_open_dir(json_dir_path: Union[str, pathlib.Path]) -> List[Frame]:
    if isinstance(json_dir_path, str):
        json_dir_path = pathlib.Path(json_dir_path)

    if json_dir_path.is_dir() and json_dir_path.exists():
        frames = list()

        for file in json_dir_path.iterdir():
            if file.suffix == ".json":
                frames.append(json_open(file.absolute()))
    else:
        raise Exception(f"Provided path ({json_dir_path}) which should be representing "
                        f"a directory containing FRS JSONs is not a directory or it does not exist!")

    return frames


def json_write(frame_objects: List[FrameObject], output_json_dir: Union[str, pathlib.Path],
               output_json_name: str):
    if isinstance(output_json_dir, str):
        output_json_dir = pathlib.Path(output_json_dir)

    if output_json_dir.is_dir() and output_json_dir.exists():
        if not output_json_name.endswith(".json"):
            output_json_name += ".json"
        full_output_path = output_json_dir.joinpath(output_json_name)

        with open(full_output_path, 'r') as f:
            print(FrameObject.schema().dumps(frame_objects, many=True), file=f)
    else:
        raise Exception(f"Provided path ({output_json_dir}) which should be representing "
                        f"a directory for output FRS JSONs is not a directory or it does not exist!")


