from musica import Musica
class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favoritos = []


    def adicionar_musica(self,musica):
        #validação
        if not isinstance(musica,Musica):
            raise TypeError("É necessario informar um objeto de classe Musica")
        self.musica.append(self.musica)
        self.reproducoes[musica] = 0 #personalizar da forma que quiser
        # chamar um metodo de favorito aqui 
        print(f"A música {musica} foi adicionada ao catalogo de musicas")

    





