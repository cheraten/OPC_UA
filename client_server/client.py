import time
from opcua import Client


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    client.connect()
    var = client.get_node("ns=2;i=2")

    while True:
        value = var.get_value()
        print("{0:.1f} units".format(value))
        time.sleep(1)

    client.disconnect()
