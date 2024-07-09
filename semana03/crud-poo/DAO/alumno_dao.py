class AlumnoDAO:
  def __init__(self):
    self.lista_alumnos = []
    
  def registrar_alumnos(self, alumno):
    self.lista_alumnos.append(alumno)

  def mostrar_alumnos(self):
    return self.lista_alumnos
  
  def actualizar_alumno(self, email, nuevo_alumno):
    for i, alumno in enumerate(self.lista_alumnos):
      if alumno.email == email:
        self.lista_alumnos[i] = nuevo_alumno
        return True
    return False

  def eliminar_alumno(self, email):
    for i, alumno in enumerate(self.lista_alumnos):
      if alumno.email == email:
        del self.lista_alumnos[i]
        return True
    return False