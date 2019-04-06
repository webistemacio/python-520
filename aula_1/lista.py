lista_vazia = []
lista_populada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append(4)
lista_vazia.append(5)
lista_vazia.append(6)
lista_vazia.append(7)
lista_vazia.append(8)
lista_vazia.append(9)
lista_vazia.append(10)

print(lista_populada)
print(lista_vazia)

#Printa 5o elemento:
print (lista_vazia[4])
#Printa lista
for n in lista_vazia:
    print('imprimindo o número ' + str(n))
print('Fim do Loop')

#Exercício:
#Escreva um programa que cadastre 10 usuários 

Lista_usuario = []
for n in range(10):
	usuario = {
		'nome': input('Digite seu nome: '),
		'idade': input('Digite sua idade: '),
		'email': input('Digite seu E-mail: ')

	}
	Lista_usuario.append(usuario)
for n in Lista_usuario:
	print('Usuario {} cadastrado com sucesso !'.format(n['nome']))


#E Salve eles em uma lista.
#Após os 10 serem cadastrados, exiba
#os dados dos usuários cadastrados.