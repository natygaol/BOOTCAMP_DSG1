class User:
  __email = 'naty@gmail.com'  
  __password = '278278'
  
  def __init__(self):
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