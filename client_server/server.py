import time
from opcua import ua, Server


if __name__ == "__main__":
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    ns = server.register_namespace("Concepts")
    objects = server.get_objects_node()
    myobj = objects.add_object(ns, "Object")
    myvar = myobj.add_variable(ns, "Variable", 0.0)
    myvar.set_writable()

    server.start()
    
    while True:
        value = myvar.get_value()
        print("{0:.1f} units".format(value))
        time.sleep(1)

    server.stop()
