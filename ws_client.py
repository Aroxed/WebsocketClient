import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time


class WebSocketClient:
    def __init__(self):
        self.ws = None

    def init(self):
        #websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/chat/a1/",
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)

    def run_forever(self):
        self.ws.run_forever()

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        print("### open ###")
        #self.ws = ws

    def send(self, message):
        if self.ws is not None and self.ws.sock is not None and self.ws.sock.connected:
            self.ws.send('{"message": "%s"}' % message)
