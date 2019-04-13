lista_de_gatos = [

{
	'nome': 'gato',
	'peso': 5000,
	'idade':6,
	'apelido': 'sedoso',

},
{
	'nome':'fernando',
	'peso': 3750,
	'idade':3,
	'apelido': 'brilhoso'
}
]
def get_input_as_int(mensagem, erro):
	user_input = input(mensagem)
	try:
		return int(user_input)
	except ValueError:
		raise ValueError(erro)
	#for token in user_input:
		#print('Caracter atual: {}'.format(token))
		#if token not in '0123456789':
		#	print('Caracter invalido encontrado')
		#	print ('Algoritmo finalizado com erro')
		#	return -1
	#return int(user_input)
def tratamento_de_tentativas(numero_tentativas):
	for tentativa in range(numero_tentativas):
		try:
			return get_input_as_int(mensagem,'Digite um número')
		except ValueError as erro:
			print('Um erro aconteceu')
			print(erro)
	print('Voce errou o input {} vezes.'.format(numero_tentativas))
	print("O programa sera encerrado")
	exit()

valor_retorno = tratamento_de_tentativas(3)
	#solucao nutella:
	#if user_input.isdigit():
	#	return int(user_input)
exit()

novo_gato = {
	'nome': input('Digite o nome:\n'),
	'peso': tratamento_de_tentativas(
5,'Digite o peso: ', 'O peso deve ser um numero maior que 0'
		),
	'idade':(
3,'Digite a idade: ', 'A idade deve ser um numero maior que 10'
		) ,
	'apelido': input('Digite o apelido:\n'),

}
lista_de_gatos.append(novo_gato)
for gato in lista_de_gatos:
	if gato['peso']>4000:
		print('Esse é o gato')
	else:
		print('Ela é a Malawi')

exit()
#Teste de sanidade do interpretador:
print('hello, word')