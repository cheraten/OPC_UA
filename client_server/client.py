import sys
sys.path.insert(0, "..")
import time


from opcua import Client


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()
        root = client.get_root_node()
        print("Objects node is: ", root)
        print("Children of root are: ", root.get_children())
        myvar = root.get_child(["0:Objects", "2:Object", "2:Variable"])
        obj = root.get_child(["0:Objects", "2:Object"])
        print("myvar is: ", myvar)
        print("myobj is: ", obj)

        var = client.get_node("ns=2;i=2")
        while True:
                value = var.get_value()
                print("{0:.1f} units".format(value))
                time.sleep(1)
    finally:
        client.disconnect()
