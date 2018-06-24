import GerenciarMQTT
import DAO
import Tarefas
import threading

def main():
    print("Principal, main{... começou")
    Banco = DAO.DAO()
    Banco.criarTabelas()
    fila_MQTT = threading.Thread(target=GerenciarMQTT.GerenciarMQTT)
    fila_MQTT.start()
    Tf = Tarefas.Tarefas()
    print("Principal, main {... chegou até o fim")


def tarefas():
    print("Principal, tarefas {... comecou")
    Tf = Tarefas.Tarefas()
    print("Principal, tarefas {... chegou até o fim")


main()
