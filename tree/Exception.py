#! /usr/bin/env python3
class warning(Exception):
    Mensaje = None
    def __init__(self, msg):
        Mensaje = msg
    def suma(self, x,y):
        try:
            return x+y
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Operacion no validad, tipos de datos no correctos")
        except Exception as inst:
            print(type(inst))     
        else:
            print("Operacion Valida !!!")

def main():
    mymsg = warning("Hola")
    print(mymsg.suma(2,"hola"))

if __name__ == "__main__":
    main()