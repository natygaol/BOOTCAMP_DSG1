class User:
  
  #atributos son privados con __
  __email = 'naty@gmail.com'  
  __password = '278278'
  
  def __init__(self):
    #cuando no requiero declarar los atributos, se coloca pass
    pass
  
  def login(self, email, password):
    if(self.__email == email and self.__password == password):
      print(f"Bienvenido {self.__email}")
    else:
      print('datos incorrectos')

print('login users')
email = input('ingrese email :')
password = input('ingrese password :')

user = User()
user.login(email, password)