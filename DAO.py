import MySQLdb
class DAO:
    def __init__(self):
        # definicoes:
        self.con = MySQLdb.connect(host="localhost", user="root", passwd="")

    def criarTabelas(self):
        print("Manutenciando banco...")
        self.con.cursor().execute("CREATE DATABASE IF NOT EXISTS medicoes")
        self.con.select_db("medicoes")
        cursor = self.con.cursor()
#        cursor.execute("CREATE TABLE IF NOT EXISTS Configuracoes(Id int not null auto_increment primary key,Id_disp varchar(10), hora varchar(10), kwh varchar(10))")
#        cursor.execute("CREATE TABLE IF NOT EXISTS Dispositivos(Id int not null auto_increment primary key,Id_disp varchar(10), hora varchar(10), kwh varchar(10))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Medicao_diaria(Id int not null auto_increment primary key,Id_disp varchar(10), hora varchar(10), kwh varchar(10))")
#        cursor.execute("CREATE TABLE IF NOT EXISTS Medicao_mensal(Id int not null auto_increment primary key,Id_disp varchar(10), hora varchar(10), kwh varchar(10))")
#        cursor.execute("CREATE TABLE IF NOT EXISTS Historico_medicoes(Id int not null auto_increment primary key,Id_disp varchar(10), hora varchar(10), kwh varchar(10))")

    def inserirMedicao(self,dispositivo, horario, consumo):
        self.con.select_db("medicoes")
        cursor = self.con.cursor()
        sintaxeSQL = "INSERT INTO Medicao_diaria(Id_disp, hora, kwh) VALUES('{}','{}','{}');".format(dispositivo,horario,consumo)
        cursor.execute(sintaxeSQL)
        self.con.commit()
pass