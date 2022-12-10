class Profissional:
  def __init__(self,nome,cpf, email, genero, especialidade):
    self._nome= nome
    self.cpf= cpf
    self.email= email
    self.genero= genero
    self.especialidade= especialidade

  def Cadastrar_profissional(self):
    self.nome= (input('\n ' "Forneça seu nome: "))
    self.cpf= (input("Forneça seu cpf: "))
    self.email= (input("Forneça seu email: "))
    self.genero= (input("Seu gênero: "))
    self.especialidade= (input( "Sua especialidade: "))

  def cadastrar_servico(self):
    self.nomeServico= ( input('\n ' "Forneça o nome do seu serviço: "))
    self.descricao = (input('\n ' "Descreva um pouco do seu serviço: "))
    self.valor = float(input("\n forneça o valor do seu servico: "))
    print('\n' f' Titulo= {self.nomeServico}')
    print('\n' f' Descrição= {self.descricao}')
    print ('\n' f' Valor= {self.valor}') 
    print ('\n' "Seu serviço está cadastrado em nosso aplicativo")

class EnderecoProfissional:
  def __init__ (self, rua, bairro, cidade, numero):
    self.rua= rua
    self.bairro= bairro
    self.cidade= cidade
    self.numero= numero

  def informar_endereco(self):
    self.rua= ( input('\n ' "Forneça sua rua: "))
    self.bairro= (input(" Forneça seu bairro: "))
    self.cidade= (input(" Forneça sua cidade: "))
    self.numero= (input(" Forneça o numero da casa: "))
    print("\n Endereço Cadastrado")
