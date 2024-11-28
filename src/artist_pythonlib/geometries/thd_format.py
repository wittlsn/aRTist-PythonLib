import numpy as np
from scipy.spatial.transform import Rotation

try:
    from thd_json.header import generate_header
    from thd_json.projection import get_projection_dict
except ModuleNotFoundError:
    from warnings import warn

    warn(
        "The optional modules of `thd` is not installed. THD Json geometry is not available."
    )


def thd_projection_geometry(api) -> dict:
    """Returns the current projection geometry of the scene. All positions are in [mm].

    Returns:
        dict: Dictionary of the projection geometry. Keys are: 'focal_spot_position_mm',
        'focal_spot_orientation_matrix', 'detector_center_position_mm',
        'detector_center_orientation_matrix', 'detector_center_orientation_quat',
        'detector_count_px' and 'detector_resolution_mm'
    """
    source_position = np.array(api.get_position("S"))
    source_orientation = np.array(api.get_rotation_matrix("S"))
    detector_position = np.array(api.get_position("D"))
    detector_orientation = np.array(api.get_rotation_matrix("D"))

    detector_resolution = api.get_detector_resolution()
    detector_pixel_count = api.get_detector_pixel_count()

    json_header = generate_header()

    image_path = f"{json_header.uuid}.tif"
    data_dict = get_projection_dict(
        image_path,
        source_position,
        detector_position,
        Rotation.from_matrix(detector_orientation).as_quat(),
        np.asarray(detector_pixel_count),
        np.asarray(detector_resolution),
        json_header,
        Rotation.from_matrix(source_orientation).as_quat())
   

    return data_dict
