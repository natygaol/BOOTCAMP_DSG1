class Automovil:
  def __init__(self, aa, pl, col, mar):
    self.anio = aa
    self.placa = pl
    self.color = col
    self.marca = mar

  def encender(self):
    print('encender ' + self.marca)
    
  def apagar(self):
    print('apagar '+ self.marca)

#objetos
vw = Automovil(1970, 'CH1234', 'Amarillo', 'Volkswagen')
vw.encender()
vw.apagar()