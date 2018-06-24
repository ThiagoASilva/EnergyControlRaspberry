from datetime import datetime
class Tempo:
    def __init__(self):
        x=10

    def dia(self):
        now = datetime.now()
        return now.day

    def mes(self):
        now = datetime.now()
        return now.month

    def ano(self):
        now = datetime.now()
        return now.year

    def hora(self):
        now = datetime.now()
        return now.hour

    def minutos(self):
        now = datetime.now()
        return now.minute

    def segundos(self):
        now = datetime.now()
        return now.second