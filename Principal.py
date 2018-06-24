import GerenciarMQTT
import DAO
import Tarefas

def main():
    Banco = DAO.DAO()
    Banco.criarTabelas()
    GMqtt = GerenciarMQTT.GerenciarMQTT()
    Tf = Tarefas()


main()