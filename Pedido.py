class Pedido:
  def __init__(self, horario, endereco,Tservico,Tpagamento):
    self.horario = horario
    self.endereco= endereco
    self.Tservico= Tservico
    self.Tpagamento= Tpagamento

  def marcar_horario(self):
    self.data= (input("\n""Que data você está procurando para solicitar o serviço: " ))
    print(input("\n" "seu pedido foi recebido" f' ficou para o dia:  {self.data}'))

  def escolher_pagamentos(self):
    print ("\n""---------------Formas de pagamento----------------------" "\n""1- Cartão de Credito" , "\n""2- Cartão de Débito", "\n""3- Cartão de Credito", "\n""4- Transferência Bancária")
    self.TPagamento= (input("\n""Que forma de pagamento você deseja realizar: "))
    print("\n Forma de Pagamento aceita, agora pode acompanhar seu pedido. ")

def escolher_servicos(self):
  self.Tservicos= (input("\n" "Qual tipo de serviço você está procurando:"))
  print("\n""você solicitou "f'{self.Tservicos}' "está no valor de:" f' {self.valor}')
  