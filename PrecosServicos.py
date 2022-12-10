class PrecoServicos:
  def __init__(self,precos):
    self.precos=precos
  
  def FornecerPrecos():
    return 0
    
class ManicurePreco:
  def __init__(self,valorM):
    self.valorM=valorM

  def FornecerPrecos(self):
    print (' Preco= 100')

class EsteticistaPreco:
  def __init__(self,valorE):
    self.valorM=valorE

  def FornecerPrecos(self):
    print (' Preço = 150')

class CabelereiraPreco:
  def __init__(self,valorC):
    self.valorM=valorC

  def FornecerPrecos(self):
    print(' Preço = 250')

class MaquiadoraPreco:
  def __init__(self,valorMi):
    self.valorMa=valorMi

  def FornecerPrecos(self):
    print(' Preço= 150')

class MassagistaPreco:
  def __init__(self,valorMi):
    self.valorMi=valorMi

  def FornecerPrecos(self):
    print (' Preco= 180')

class DesignerSobrancelhaPreco:
  def __init__(self,valorDs):
    self.valorDs=valorDs

  def FornecerPrecos(self):
    print (' Preco= 55')

class especialidades :
  def __init__(self, nomeEspecialidade,preco ):
    self.nomeEspecialidade= nomeEspecialidade
    self.preco= preco
   
  def escolher_especialidade(self):
    especialidade = int(input('\n 1-Massagista \n 2-Cabelereira \n 3-Maquiadora \n 4-Esteticista \n 5-Manicure \n 6- Designer de sobrancelha \n \n QUAL ESPECIALIDADE VOCÊ ESTÁ PROCURANDO? \n ' ))
    
    if especialidade== 1:
      print( ' especialidade (Massagista)')
    if especialidade == 2:
      print(' especialidade (Cabeleira)')
    if especialidade==3:
      print(' especialidade (Maquiadora)')
    if especialidade==4:
      print(' especialidade (esteticista)')
    if especialidade==5:
      print(' especialidade (Manicure)')
    if especialidade==6:
      print(' especialidade (designer de sobrancelha)')
   

