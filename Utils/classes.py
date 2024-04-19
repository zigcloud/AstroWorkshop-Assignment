from pathlib import Path
from astropy.io import fits
from numpy import ndarray
from typing import Tuple, List

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass
class InternalFits(object):
    path: Path = None
    header: fits.header.Header = None
    data: ndarray = None


@dataclass_json
@dataclass
class FrameCoords:
    x: float
    y: float
    x_min: float
    y_min: float
    x_max: float
    y_max: float


@dataclass_json
@dataclass
class EquatorialCoords:
    ra: float
    dec: float


@dataclass_json
@dataclass
class FrameObject:
    """
    Class for internal FrameObject json
        str = FrameObject().to_json()
        obj = FrameObject.from_json(str)
    """
    object_name: str = ""
    star: bool = False
    frame_coords: FrameCoords = None
    ecs_coords: EquatorialCoords = None
    shape_factor: float = 0.
    area: float = 0.
    angle: float = 0.
    intercept: float = 0.
    intensity: float = 0.
    brightness_error: float = 0.
    background_flux: float = 0.
    magnitude: float = 0.
    magnitude_error: float = 0.
    mjd: float = 0.
    snr: float = 0.
    standard_r_magnitude: float = 0.
    standard_r_magnitude_error: float = 0.
    rectangle_size: Tuple[float, float] = None
    longitude: float = 0
    binning: int = 0


@dataclass_json
@dataclass
class Frame:
    codaiub: str = ""
    codmpc: str = ""
    codtdm: str = ""
    obs: str = ""
    telescope: str = ""
    filter: str = ""
    exptime: float = 0.
    frame_objects: List[FrameObject] = None
    validation: bool = False
    message_id: str = ""
    customer_id: str = ""
    stare_and_chase: bool = False
    iod: bool = False

