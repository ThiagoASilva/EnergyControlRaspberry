import GerenciarMQTT
import DAO
#import Tarefas

def main():
    print("Principal, main{... começou")
    Banco = DAO.DAO()
    Banco.criarTabelas()
    GMqtt = GerenciarMQTT.GerenciarMQTT()
    print("Principal, main {... chegou até o fim")


#def tarefas():
#    print("Principal, tarefas {... comecou")
#    Tf = Tarefas.Tarefas()
#    print("Principal, tarefas {... chegou até o fim")


main()
#tarefas()