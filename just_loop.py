import datetime
import time


def just_loop(web_socket_client):
    while True:
        print("o")
        web_socket_client.send("Current time is: %s" % str(datetime.datetime.now()))
        time.sleep(1)
