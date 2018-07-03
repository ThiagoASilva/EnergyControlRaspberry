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
        self.TopicoStatus="STATUS";
        self.Marca = "[EnergyControl]"
        self.Banco = DAO.DAO()
        #Fim Definicoes------
        self.iniciarMqtt()

    def on_connect(self, client, userdata, flags, rc):
        print(self.Marca + "##STATUS## Conectado ao Broker. Resultado de conexao: " + str(rc))
        # faz subscribe automatico no topico
        self.cliente.subscribe(self.TopicoSubscribe)
        self.cliente.subscribe(self.TopicoComando)
        self.cliente.subscribe(self.TopicoStatus)

    # callback - mensagem recebida do broker
    def on_message(self, client, userdata, msg):
        MensagemRecebida = str(msg.payload)
        print(self.Marca + " ##MENSAGEM RECEBIDA## Topico: " + msg.topic + " / Mensagem: " + MensagemRecebida)
        self.definirMensagensR(MensagemRecebida, msg.topic)

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

    def enviarMensagem(self, mensagem, topico):
        self.cliente.publish(topico, mensagem)
        print(self.Marca + "##MENSAGEM ENVIADA## " + mensagem)


    def definirMensagensR(self, MensagemRecebida, topico):
        linhaN = TString.TString()
        assunto = linhaN.obterassunto(MensagemRecebida)

        if linhaN.obterdispositivo(MensagemRecebida)!="ENERGYCONTROL":
            #SEPARANDO OS ASSUNTOS

            if(topico=="TCCCOMANDO"):
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
                    mensagem = "ENERGYCONTROL/ESPTomada1/"+comando+"/"
#                   mensagem = "ESPTomada1"

                    self.enviarMensagem(mensagem, self.TopicoComando)
                #Enviar lista Dispositivos
                elif assunto=="comando_base":
                    print("O Assunto é um comando para a base");
                    if(linhaN.obterargumentos(MensagemRecebida)[0]=="obter-lista-de-dispositivos"):
                        dispositivo = linhaN.obterdispositivo(MensagemRecebida)
                        lista = self.Banco.listaDeDispositivos();
                        mensagem = "ENERGYCONTROL/"+dispositivo+"/lista-dispositivos/"+lista;
                        self.enviarMensagem(mensagem, self.TopicoStatus);

        else:
                print("Mensagem propia rcebida")


pass