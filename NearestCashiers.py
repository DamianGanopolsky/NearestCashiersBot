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

def foo():

    print(bot.get_me())
    updates= bot.get_updates()
    print(updates[0])
    print(geohash.encode(-58.3709017854754, -34.605812942035, 7))
    locations = {}

    print(geohash.neighbours(geohash.encode(-58.3709017854754, -34.605812942035, 7)))
    #bot.send_message(text='hi',chat_id=1468306063)
    with open('cajeros-automaticos.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0

        # En row voy a tener cada fila del csv
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            if line_count > 4:
                break

            if(row[6] != 'CABA'):
                continue

            cashier = Cashier(row)
            print(cashier.getData())
            print("Row:",row)
            print("Row fields are:",row[1],row[2])
            print(geohash.encode(row[1],row[2],7))


if __name__ == '__main__':
    foo()
