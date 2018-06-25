class TString:
    def __init__(self):
        x=10

    def obterassunto(self, linha):
        if (linha.find("/") != -1):
            if(linha.find("'")!= -1):
                linha0 = linha.split("'")
                linha1 = linha0[1].replace("'","")
            else:
                linha1 = linha

            linhaFinal = linha1.split("/")
            return linhaFinal[1]
        else:
            return ""

    def obterargumentos(self, linha):
        if(linha.find("/")!= -1):
            if(linha.find("'")!=-1):
                linha0 = linha.split("'")
                linha1 = linha0[1].replace("'","")
            else:
                linha1 = linha

            linha2 = linha1.split("/")
            linhaFinal = linha2[2].split("%")
            return linhaFinal
        else:
            return ""

    def numargumentos(self,linha):
        linha0 = linha.split("/")
        if(linha0[2]==""):
            return ""
        else:
            return str(linha.count("%"))

    def obterdispositivo(self,linha):
        linha0 = linha.split("'")
        linha1 = linha0[1].replace("'","")
        linhaFinal = linha1.split("/")
        return linhaFinal[0]
