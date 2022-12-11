from Class.Client import Client
from getpass import getpass
import json
import datetime


def updateState():
    print("Service: Update State")

    try:
        token = input("Ingrese token: ")
        print("Obteniendo lista de objetos perdidos y encontrados... \n")
        b = Client("blogo")
        things = b.exec_client(debug=True, climsg=json.dumps({
            "token": token
        }))
        print(things, "\n")

        try:
            thing_id = input("Ingrese id del objeto: ")
            climsg = {
                "thing_id": thing_id,
                "token": token
            }
            a = Client("blugu")
            msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
            print("###################################\n\n",
                  msg, "\n\n###################################")
        except Exception as e:
            print("Error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        exit()
