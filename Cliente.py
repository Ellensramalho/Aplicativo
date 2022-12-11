class Cliente: #class Cliente
  def __init__(self,nome,cpf, email, genero):
    self._nome= nome
    self.cpf= cpf
    self.email= email
    self.genero= genero
    
  def cadastrarCliente(self):
    self.nome= (input('\n ' "Forneça seu nome: "))
    self.cpf= (input( " Forneça seu cpf: "))
    self.email= (input( " Forneça seu email: "))
    self.genero= (input( " Seu gênero: "))

    print('\n' f'Nome= {self.nome}, cpf= {self.cpf}, email={self.email}, genero= {self.genero} ' )

  def solicitar_servico(self):
    self.nome= (input("Forneça seu nome: "))
    print('\n' f'{self.nome},agora está solicitando serviço, aguarde')
  
  def cancelarservico(self):
    print("\n 1- cancelar, 2- não cancelar")
    cancelar= int (input("\n você quer cancelar serviço? "))
    if cancelar == 1:
      print("\n Você cancelou o servico")
    if cancelar == 2:
      print("\n Pedido não cancelado")

  def avaliar_servico(self):
    print('\n Avalie o serviço: \n 1-Não gostei do serviço \n 2- Achei Razoável \n 3- Bom \n 4- Ótimo \n 5- Maravilhoso')
    avaliacao= int(input('\n O que achou do atendimento: '))
    print('\n Agradecemos o seu feedback')

class Endereco :
  def __init__ (self, rua, bairro, cidade, numero):
    self.rua= rua
    self.bairro= bairro
    self.cidade= cidade
    self.numero= numero
    
  def informar_Endereco(self):
    self.rua= ( input('\n ' "Forneça sua rua: "))
    self.bairro= (input(" Forneça seu bairro: "))
    self.cidade= (input(" Forneça sua cidade: "))
    self.numero= (input(" Forneça o numero da casa: "))
    print("\n Endereço Cadastrado")
