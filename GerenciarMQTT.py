import paho.mqtt.client as mqtt
from datetime import datetime
import TString
import DAO

class GerenciarMQTT:

    def __init__(self):
        #Definicoes------
        self.Broker = "192.168.0.18 "  # ou use"iot.eclipse.org"
        self.PortaBroker = 1883
        self.KeepAliveBroker = 60
        self.TopicoSubscribe = "TCCMEDICAO"
        self.Marca = "[EnergyControl]"
        self.Banco = DAO.DAO()
        #Fim Definicoes------
        self.iniciarMqtt()



    def on_connect(self, client, userdata, flags, rc):
        print(self.Marca + "##STATUS## Conectado ao Broker. Resultado de conexao: " + str(rc))
        # faz subscribe automatico no topico
        self.cliente.subscribe(self.TopicoSubscribe)

    # callback - mensagem recebida do broker
    def on_message(self, client, userdata, msg):
        MensagemRecebida = str(msg.payload)
        print(self.Marca + " ##MENSAGEM RECEBIDA## Topico: " + msg.topic + " / Mensagem: " + MensagemRecebida)
        self.definirMensagensR(MensagemRecebida)

    def iniciarMqtt(self):
        print(self.Marca + "##STATUS## Iniciando MQTT...")
        # inicaliza MQTT:
        self.cliente = mqtt.Client()
        self.cliente.on_connect = self.on_connect
        self.cliente.on_message = self.on_message
        self.cliente.username_pw_set("systemem", "kwhy123")
        self.cliente.connect(self.Broker, 1883, 60)
        self.principal()

    # Programa principal
    def principal(self):
        self.cliente.loop_forever()

    def definirMensagensR(self, MensagemRecebida):
        linhaN = TString.TString()
        assunto = linhaN.obterassunto(MensagemRecebida)

        #SEPARANDO OS ASSUNTOS

        #MEDICAO
        if assunto=="medicao":
            print("O Assundo é Medicao")
            now = datetime.now()
            dispositivo = linhaN.obterdispositivo(MensagemRecebida)
            horario = str(now.minute) + ":" + str(now.second)
            consumo = linhaN.obterargumentos(MensagemRecebida)
            self.Banco.inserirMedicao(dispositivo,horario,consumo[0])
pass