import DAO
import schedule
import time
import threading
import GerenciarMQTT

class Tarefas:
    def __init__(self):
        print("Tarefas, __Init__{... Iniciou")
        self.iniciar()

    def balancodobanco(self):
        print("Executando tarefa agendada do balanco do banco")
        banco = DAO.DAO()
        banco.balancoDoBanco()

    def iniciar(self):
        print("Iniciando a programacao de tarefas")
#        job_thread = threading.Thread(target=GerenciarMQTT.GerenciarMQTT)
#        job_thread.start()

        schedule.every(1).minutes.do(self.balancodobanco)

        while True:
            schedule.run_pending()
            time.sleep(1)