# w es por write o escritura
f = open('alumnos.txt','w')
f.write('nataly garcia, naty@gmail.com, 9887899')
f.close()

#a es por append
fa = open('alumnos.txt','a')
fa.write('\n')
fa.write('naty garcia, holis@gmail.com, 9887899')
fa.close()

# r es por lectura
fr = open('alumnos.txt', 'r')
data_alumnos = fr.read()
print(data_alumnos)
fr.close()