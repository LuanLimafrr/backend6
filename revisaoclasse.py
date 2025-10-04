class Pessoa:
    cabelo = 'loiro'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def imprimir (self):
        print(f'seu nome é {self.nome} e tem {self.idade} anos')
    
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)   
        self.curso = curso              


    def imprimir(self):
        super().imprimir()  # chama imprimir da classe Pessoa
        print(f"e está cursando {self.curso}")



# Para Pessoa
nome_p = input("Digite seu nome: ")
idade_p = int(input("Digite sua idade: ")) 
p1 = Pessoa(nome_p, idade_p)



# Para Aluno
nome_a = input("Digite o nome do aluno: ")
idade_a = int(input("Digite a idade do aluno: "))
curso_a = input("Digite o curso do aluno: ")
a1 = Aluno(nome_a, idade_a, curso_a)




p1.imprimir()
a1.imprimir()




