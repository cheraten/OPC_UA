import time
from opcua import Client


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    client.connect()
    var = client.get_node("ns=2;i=2")

    count = 0
    while True:
        try:
            time.sleep(1)
            count += 0.1
            print("{:8.1f} units".format(count))
            var.set_value(count)
        except KeyboardInterrupt:
            print("Closing connection...")
            break

    client.disconnect()
    print("Connection closed")
