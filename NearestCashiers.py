import csv
#import requests
import telegram

bot = telegram.Bot(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA')

from geolib import geohash
import math



def in_circle_check(latitude, longitude, centre_lat, centre_lon, radius):

    x_diff = longitude - centre_lon
    y_diff = latitude - centre_lat

    if (math.pow(x_diff, 2) + math.pow(y_diff, 2) <= math.pow(radius, 2)):
        return True

    return False


def get_centroid(latitude, longitude, height, width):

    y_cen = latitude + (height / 2)
    x_cen = longitude + (width / 2)

    return (x_cen, y_cen)


def convert_to_latlon(y, x, latitude, longitude):

    pi = 3.14159265359

    r_earth = 6371000

    lat_diff = (y / r_earth) * (180 / pi)
    lon_diff = (x / r_earth) * (180 / pi) / math.cos(latitude * pi/180)

    final_lat = latitude+lat_diff
    final_lon = longitude+lon_diff

    return (final_lat, final_lon)


def create_geohash(latitude, longitude, radius, precision):

    x = 0.0
    y = 0.0

    points = []
    geohashes = []

    grid_width = [5009400.0, 1252300.0, 156500.0, 39100.0, 4900.0, 1200.0, 152.9, 38.2, 4.8, 1.2, 0.149, 0.0370]
    grid_height = [4992600.0, 624100.0, 156000.0, 19500.0, 4900.0, 609.4, 152.4, 19.0, 4.8, 0.595, 0.149, 0.0199]

    height = (grid_height[precision - 1])/2
    width = (grid_width[precision-1])/2

    lat_moves = int(math.ceil(radius / height)) #4
    lon_moves = int(math.ceil(radius / width)) #2

    for i in range(0, lat_moves):

        temp_lat = y + height*i

        for j in range(0,lon_moves):

            temp_lon = x + width*j

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

class Cashier:

    def __init__(self,data):
        self.longitude=data[1]
        self.latitude=data[2]
        self.name=data[3]
        self.type=data[4]
        self.address=data[10]+' '+data[11]

    def getData(self):
        return self.name,self.address

    def calculateGeohash(self):
        return geohash.encode(self.latitude,self.longitude,7)

class Map:
    def __init__(self):
        self.locations = {}

    def add_cashier(self,cashier):
        print("New geohash:",cashier.calculateGeohash())
        self.locations.setdefault(cashier.calculateGeohash(), []).append(cashier)
        #self.locations[cashier.calculateGeohash()]=cashier
        print("Cashier value now:",self.locations[cashier.calculateGeohash()])
        #self.locations[cashier.calculateGeohash()].append(cashier)

    def get_nearest_cashiers(self,queryLatitude,queryLongitude):
        proximityGeohashes= create_geohash(queryLatitude, queryLongitude, 500,7).split(",")
        nearestBanks=[]
        count=0
        for proximityHash in proximityGeohashes:
            if proximityHash in self.locations:
                for bank in self.locations[proximityHash]:
                    nearestBanks.append(bank.getData())
                    count += 1
                    if count >= 3:
                        return nearestBanks

        #print("List of geohashes:",proximityGeohashes.split(","))

    def print_all_cashiers(self):
        for key,value in self.locations.items():
            print(key,value[0].getData())

def foo():

    print(bot.get_me())
    updates= bot.get_updates()
    #print(updates[0])
    geoMap = Map()

    #print(geohash.neighbours(geohash.encode(-58.3709017854754, -34.605812942035, 7)))
    #bot.send_message(text='hi',chat_id=1468306063)
    with open('cajeros-automaticos.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0

        # En row voy a tener cada fila del csv
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            if line_count > 5:
                break

            if(row[6] != 'CABA'):
                continue

            cashier = Cashier(row)
            geoMap.add_cashier(cashier);

    print("ALl cashiers:",geoMap.print_all_cashiers())
    print(geoMap.get_nearest_cashiers(-34.6050839250446, -58.3709757833981))

if __name__ == '__main__':
    #print(create_geohash(-34.605812942035,-58.3709017854754,500,7))

    #print(geohash.encode(-34.6050839250446, -58.3709757833981, 7))


    #print(geohash.encode(-34.61116298318, -58.387486522984, 7))
    foo()
