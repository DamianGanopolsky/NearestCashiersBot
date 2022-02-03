
import NearestCashiers
import TelegramBot
import os
import uvicorn
from threading import Thread

if __name__ == '__main__':
    #port = os.environ.get('PORT',5000)
    #uvicorn.run(NearestCashiers.run(), host = '0.0.0.0', port=port)
    thread = Thread(target = TelegramBot.run())
    thread.start()
    thread.join()
    #NearestCashiers.run()