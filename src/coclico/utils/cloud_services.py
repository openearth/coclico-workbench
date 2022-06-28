import os

import xarray as xr


def dataset_from_google_cloud(
    zarr_storename: str,
    bucket_name: str = "dgds-data-public",
    bucket_proj: str = "coclico",
) -> xr.Dataset:
    """Read zarr store from Google Cloud Services into xarray

    Args:
        zarr_storename (str): _description_
        bucket_name (str): Deltares open  bucket
        bucket_proj (str):

    Returns:
        xr.Dataset: Zarr store opened as xarray dataset (not loaded yet)
    """
    uri = os.path.join("gs://" + bucket_name, bucket_proj, zarr_storename)
    return xr.open_zarr(uri)
