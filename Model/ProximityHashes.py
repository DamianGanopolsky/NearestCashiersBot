from geolib import geohash
import math


def in_circle_check(latitude, longitude, centre_lat, centre_lon, radius):
    x_diff = longitude - centre_lon
    y_diff = latitude - centre_lat

    if math.pow(x_diff, 2) + math.pow(y_diff, 2) <= math.pow(radius, 2):
        return True

    return False


def get_centroid(latitude, longitude, height, width):
    y_cen = latitude + (height / 2)
    x_cen = longitude + (width / 2)

    return x_cen, y_cen


def convert_to_latlon(y, x, latitude, longitude):
    pi = 3.14159265359

    r_earth = 6371000

    lat_diff = (y / r_earth) * (180 / pi)
    lon_diff = (x / r_earth) * (180 / pi) / math.cos(latitude * pi / 180)

    final_lat = latitude + lat_diff
    final_lon = longitude + lon_diff

    return final_lat, final_lon


def get_geohashes_neighbours(latitude, longitude, radius, precision):
    x = 0.0
    y = 0.0

    points = []
    geohashes = []

    grid_width = [5009400.0, 1252300.0, 156500.0, 39100.0, 4900.0, 1200.0, 152.9, 38.2, 4.8, 1.2, 0.149, 0.0370]
    grid_height = [4992600.0, 624100.0, 156000.0, 19500.0, 4900.0, 609.4, 152.4, 19.0, 4.8, 0.595, 0.149, 0.0199]

    height = (grid_height[precision - 1]) / 2
    width = (grid_width[precision - 1]) / 2

    lat_moves = int(math.ceil(radius / height))  # 4
    lon_moves = int(math.ceil(radius / width))  # 2

    for i in range(0, lat_moves):

        temp_lat = y + height * i

        for j in range(0, lon_moves):

            temp_lon = x + width * j

            if in_circle_check(temp_lat, temp_lon, y, x, radius):
                x_cen, y_cen = get_centroid(temp_lat, temp_lon, height, width)

                lat, lon = convert_to_latlon(y_cen, x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(-y_cen, x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(y_cen, -x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(-y_cen, -x_cen, latitude, longitude)
                points += [[lat, lon]]

    for point in points:
        geohashes += [geohash.encode(point[0], point[1], precision)]

    else:
        return ','.join(set(geohashes))
