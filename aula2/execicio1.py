#Missão 1:
#Criar uma função "Cadastrar Usuário".
#Que retorne um dicionário de usuários.
#O dicionário deve conter a propriedades:
# - nome
# - email
# - idade
# e os valores devem ser digitados 
# pelo usuário do através do terminal (input)
#
import datetime
import subprocess
import time
import random 
def cadastrar_usuario():
	novo_usuario = {
		'data cadastro': datetime.datetime.now(),
		'nome': input('Digite seu nome: '),
		'email': input('Digite seu e-mail: '),
		'idade': input('Digite sua idade')
	}
	return novo_usuario
probabilidade = random.random()
if probabilidade < 0.8:
	cadastrar_usuario()
else:
	print ('Opa, nao deu sorte...')
exit()

novo_usuario = cadastrar_usuario()
subprocess.run ({'clear'})
start_time = time.clock()
time.sleep(10.0)
print ('tempo gasto = {}'.format(time.clock() - start_time))
d = novo_usuario['data cadastro']
print(d.strftime('%B %d, %Y'))
exit()


	
