# w es por write o escritura
f = open('empresas.txt','w')
f.write('104555450, Pokemon Company, Pokeword Avenue')
f.close()

#a es por append
fa = open('empresas.txt','a')
fa.write('\n')
fa.write('2030405060, Frieren, Champs Elysee')
fa.close()

# r es por lectura
fr = open('empresas.txt', 'r')
data_empresas = fr.read()
print(data_empresas)
fr.close()