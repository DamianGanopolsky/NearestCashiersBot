import csv
#import requests
import telegram

bot = telegram.Bot(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA')

from geolib import geohash

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
        return geohash.encode(self.longitude,self.latitude,7)

class Map:
    def __init__(self):
        self.locations = {}

    def add_cashier(self,cashier):
        print("New geohash:",cashier.calculateGeohash())
        self.locations.setdefault(cashier.calculateGeohash(), []).append(cashier)
        #self.locations[cashier.calculateGeohash()]=cashier
        print("Cashier value now:",self.locations[cashier.calculateGeohash()])
        #self.locations[cashier.calculateGeohash()].append(cashier)
    def print_all_cashiers(self):
        for key,value in self.locations.items():
            print(key,value[0].getData())

def foo():

    print(bot.get_me())
    updates= bot.get_updates()
    print(updates[0])
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

            print("CASHIER data:",cashier.getData())
            #locations[geohash.encode(row[1],row[2],7)]= cashier

    print("ALl cashiers:",geoMap.print_all_cashiers())

if __name__ == '__main__':
    #locations ={}
    #locations.setdefault("a", []).append("1")
    #locations.setdefault("a", []).append("4")
    #locations.setdefault("b", []).append("9")
    #print(locations)
    foo()
