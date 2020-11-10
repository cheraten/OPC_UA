import time
from opcua import ua, Server


if __name__ == "__main__":
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    ns = server.register_namespace("Concepts")
    objects = server.get_objects_node()

    myobj = objects.add_object(ns, "Object")
    myvar = myobj.add_variable(ns, "Variable", 0.0)

    server.start()
    
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            print("{:8.1f} units".format(count))
            myvar.set_value(count)
    finally:
        server.stop()
