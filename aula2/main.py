import aleatorio
def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u = aleatorio.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

	lista_de_usuarios = gerar_lista_usuarios(100)
	