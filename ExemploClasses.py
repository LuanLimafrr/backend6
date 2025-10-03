class Carro:
    rodas = 4  # atributo de classe
    def __init__(self, marca, ano):
        self.marca = marca  # atributo de instância
        self.ano = ano  # atributo de instância
        
        
    def ligar (self):
        print(f'O Seu {self.marca} {self.ano} está ligado')
        
    
    
c1 = Carro("Honda", "2018")
c2 = Carro("Renault", "2012")

print(c1.marca, c1.ano)
print(c2.marca, c2.ano)
print(c1.rodas)
print(c2.rodas)
c1.ligar()
c2.ligar()


c1.rodas = 3
c2.rodas = 3

print(c1.rodas)
print(c2.rodas)

