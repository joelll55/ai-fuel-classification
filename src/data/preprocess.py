import rasterio

def get_main_profile(raster_path):
    """
    Define the main 10m SENTINEL-2 grid.

    Parameters:
    raster_path (str): Path to the raster file.

    Returns:
    tuple: A tuple containing the main profile of the raster and its bounds.
    """
    with rasterio.open(raster_path) as src:
        return src.profile.copy(), src.bounds
    
def align_raster_to_main():
    """
    Align any raster to the main 10m SENTINEL-2 grid.

    Returns:
    None
    """
    # Implementation for aligning raster to the main grid goes here
    pass