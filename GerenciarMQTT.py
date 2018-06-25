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
        self.TopicoComando="TCCCOMANDO"
        self.Marca = "[EnergyControl]"
        self.Banco = DAO.DAO()
        #Fim Definicoes------
        self.iniciarMqtt()

    def on_connect(self, client, userdata, flags, rc):
        print(self.Marca + "##STATUS## Conectado ao Broker. Resultado de conexao: " + str(rc))
        # faz subscribe automatico no topico
        self.cliente.subscribe(self.TopicoSubscribe)
        self.cliente.subscribe(self.TopicoComando)

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

    def enviarMensagem(self, mensagem):
        self.cliente.publish(self.TopicoComando, mensagem)
        print(self.Marca + "##MENSAGEM ENVIADA## " + mensagem)


    def definirMensagensR(self, MensagemRecebida):
        linhaN = TString.TString()
        assunto = linhaN.obterassunto(MensagemRecebida)

        if linhaN.obterdispositivo(MensagemRecebida)!="ENERGYCONTROL":
            #SEPARANDO OS ASSUNTOS

            #MEDICAO
            if assunto=="medicao":
                print("O Assundo é Medicao")
                now = datetime.now()
                dispositivo = linhaN.obterdispositivo(MensagemRecebida)
                horario = str(now.minute) + ":" + str(now.second)
                consumo = linhaN.obterargumentos(MensagemRecebida)
                self.Banco.inserirMedicao(dispositivo,horario,consumo[0])

            #Comando para o dispositivo
            elif assunto=="comando_dispositivo":
                print("O Assunto é um comando")
                argumentos = linhaN.obterargumentos(MensagemRecebida)
                dispositivo = argumentos[0]
                comando = argumentos[1]
#                mensagem = "ENERGYCONTROL/"+dispositivo+"/"+comando+"/"
                mensagem = "ESPTomada1"

                self.enviarMensagem(mensagem)
        else:
                print("Mensagem propia rcebida")


pass