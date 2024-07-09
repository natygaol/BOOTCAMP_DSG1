class EmpresaDAO:
  def __init__(self):
    self.lista_empresas = []
    
  def registrar_empresa(self, empresa):
    self.lista_empresas.append(empresa)

  def mostrar_empresas(self):
    return self.lista_empresas
  
  def actualizar_empresa(self,nuevo_empresa,index):
      self.lista_empresas[index] = nuevo_empresa

  def eliminar_empresa(self,index):
      del self.lista_empresas[index]