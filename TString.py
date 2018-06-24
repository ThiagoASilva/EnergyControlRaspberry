class TString:
    def __init__(self):
        x=10

    def obterassunto(self, linha):
        linha0 = linha.split("'")
        linha1 = linha0[1].replace("'","")
        linhaFinal = linha1.split("/")
        return linhaFinal[1]

    def obterargumentos(self, linha):
            linha0 = linha.split("'")
            linha1 = linha0[1].replace("'","")
            linha2 = linha1.split("/")
            linhaFinal = linha2[2].split("%")
            return linhaFinal

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
