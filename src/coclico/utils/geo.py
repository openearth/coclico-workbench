from typing import Dict, List

import geopandas as gpd
import shapely


def bbox_to_geometry(bbox: List[float]) -> Dict:
    """Use shapely.geometry.shape to cast to shapeley geom"""
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [bbox[2], bbox[1]],
                [bbox[2], bbox[3]],
                [bbox[0], bbox[3]],
                [bbox[0], bbox[1]],
                [bbox[2], bbox[1]],
            ]
        ],
    }


def geo_bbox(
    bbox: List[float],
    src_crs: str = "EPSG:4326",
    dst_crs: str = "EPSG:4326",
) -> gpd.GeoDataFrame:
    """Bounding box wrapping inside GeoPandas GeoDataFrame

    Args:
        bbox (List[float]): list of coordinates formatted as [minx, miny, maxx, maxy]
        src_crs (_type_, optional): crs of the provided bbox coordinates. Defaults to "EPSG:4326".
        dst_crs (_type_, optional): output crs. Defaults to "EPSG:4326".

    Returns:
        gpd.GeoDataFrame: bounding box wrapped inside GeoPandas GeoDataFrame.
    """
    bbox = bbox_to_geometry(bbox)
    bbox = shapely.geometry.shape(bbox)
    return gpd.GeoDataFrame(geometry=[bbox], crs=src_crs).to_crs(dst_crs)
