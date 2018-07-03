import MySQLdb
from datetime import datetime

class DAO:
    def __init__(self):
        # definicoes:
        self.con = MySQLdb.connect(host="localhost", user="root", passwd="")

    def criarTabelas(self):
        print("Manutenciando banco...")
        self.con.cursor().execute("CREATE DATABASE IF NOT EXISTS medicoes")
        self.con.select_db("medicoes")
        cursor = self.con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Configuracoes(Id int not null auto_increment primary key, IP varchar(16))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Dispositivos(Id_Disp int not null auto_increment primary key,MQTT_name varchar(10), ativo boolean not null default 1, Id_icone varchar(2), Porcentagem_meta varchar(3), Desliga_auto boolean not null default 1, Notifica boolean not null default 1)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Medicao_diaria(Id int not null auto_increment primary key,Id_disp varchar(10), hora varchar(10), kwh varchar(10))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Medicao_mensal(Id int not null auto_increment primary key,Id_disp varchar(10), dia varchar(10), kwh_dia varchar(10))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Historico_medicoes(Id int not null auto_increment primary key, ano varchar(4), mes varchar(2), Id_disp varchar(10), Gasto_monetario float(10))")

    def inserirMedicao(self,dispositivo, horario, consumo):
        self.con.select_db("medicoes")
        cursor = self.con.cursor()
        sintaxeSQL = "INSERT INTO Medicao_diaria(Id_disp, hora, kwh) VALUES('{}','{}','{}');".format(dispositivo,horario,consumo)
        cursor.execute(sintaxeSQL)
        self.con.commit()

    def balancoDoBanco(self):
        now = datetime.now()
        self.con.select_db("medicoes")
        cursor = self.con.cursor()
        sintaxeSQL = "SELECT distinct Id_disp FROM Medicao_diaria"
        cursor.execute(sintaxeSQL)
        idDisp = cursor.fetchall()

        #teste

        for row in idDisp:
            print(row)

        if(str(now.day)=="1"):
            print("HOJE È DIA UM, Passando os Dados da tabela Medicoes_mensal para a tabela Historico_medicoes")
        else:
            print("Hoje não é dia 1, hoje é: " + str(now.day))

    def listaDeDispositivos(self):
        self.con.select_db("medicoes")
        cursor = self.con.cursor()
        sintaxeSQL = "SELECT distinct Id_disp FROM Dispositivos"
        cursor.execute(sintaxeSQL)
        idDisp = cursor.fetchall()
        lista = "";
        for row in idDisp:
            id = str(row).replace("(", "");
            id = id.replace(")","") ;
            id = id.replace(",", "");
            lista += id + "%";
        return lista


pass