# from multiprocessing import Process
import threading

from just_loop import just_loop
from ws_client import WebSocketClient

if __name__ == '__main__':
    ws_client = WebSocketClient()
    #
    ws_client.init()
    # Process(target=just_loop, args=(ws_client,)).start()
    threading.Thread(target=just_loop, args=(ws_client,)).start()
    ws_client.run_forever()
