import DAO
import schedule

def balancodobanco():
    print("Executando tarefa agendada do balanco do banco")
    banco = DAO.DAO()
    banco.balancoDoBanco()
schedule.every(1).minutes.do(balancodobanco)