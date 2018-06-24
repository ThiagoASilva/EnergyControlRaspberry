import GerenciarMQTT
import DAO

def main():
    Banco = DAO.DAO()
    Banco.criarTabelas()
    GMqtt = GerenciarMQTT.GerenciarMQTT()


main()