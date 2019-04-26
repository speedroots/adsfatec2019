'''
Autor: Rafael Marques de Almeida
Projeto: 1ª Parte Chatbot pelo Telegram
Curso: Análise e Desenvolvimento de Sistemas
Interação Humano Computador(IHC) - Professor Giuliano Araújo Bertoti
'''
# VARS - Links
choque_eletrico = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/choque-eletrico.html'
convulsoes = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/convulsoes.html'
desmaio = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/desmaios.html'
envenenamento = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/envenenamento-e-intoxicacao.html'
estado_de_choque = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/estado-de-choque.html'
fraturas = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/fraturas.html'
hemorragias = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/hemorragias.html'
parada_cardiaca = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/parada-cardiaca.html'
parada_respiratoria = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/parada-respiratoria.html'
queimadura = 'http://primeiros-socorros.info/primeiros-socorros-como-agir/queimaduras.html'

#VAR - Principal
first_msg = """Bem-vindo, digite uma das opções abaixo para obter informações em como proceder com primeiros socorros:\n
Choque Elétrico: - Digite 1 ou choque eletrico por extenso;\n
Convulsões: - Digite 2 ou convulsoes por extenso;\n
Desmaio: - Digite 3 ou desmaio por extenso;\n
Envenenamento: - Digite 4 ou envenenamento por extenso;\n
Estado de Choque: - Digite 5 ou estado de choque por extenso;\n
Fraturas: - Digite 6 ou fraturas por extenso;\n
Hemorragias: - Digite 7 ou emorragia por extenso;\n
Parada Cardíaca: - Digite 8 ou parada cardiaca por extenso;\n
Parada Respiratória: - Digite 9 ou parada respiratoria por extenso;\n
Queimadura: - Digite 10 ou queimadura por extenso;\n"""

class Estimulus(object):
    def __init__(self, frases):
        super(Estimulus, self).__init__()       
        self.frases = {''}

    def escuta(self,frase=None):
        if frase == None:
            frase = input('>: ')
        frase =str(frase)
        frase = frase.lower()

        return frase

    def pensa(self,frase):

        if frase in self.frases:
            return self.frases[frase]

        if frase == '/start':
            return first_msg

        if frase == 'choque eletrico' or frase == '1':
            return choque_eletrico
        if frase == 'convulsoes' or frase == '2':
            return convulsoes
        if frase == 'desmaio' or frase == '3':
            return desmaio
        if frase == 'envenenamento' or frase == '4':
            return envenenamento
        if frase == 'estado de choque' or frase == '5':
            return estado_de_choque
        if frase == 'fraturas' or frase == '6':
            return fraturas
        if frase == 'hemorragias' or frase == '7':
            return hemorragias
        if frase == 'parada cardiaca' or frase == '8':
            return parada_cardiaca
        if frase == 'parada respiratoria' or frase == '9':
            return parada_respiratoria
        if frase == 'queimadura' or frase == '10':
            return queimadura

        else:
            return first_msg