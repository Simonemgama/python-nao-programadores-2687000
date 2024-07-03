# Crie uma lista apenas com elementos numéricos
numerica = [1, 2, 3, 4, 5]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
pessoa = ['Simone', 51, 1973, ['python', 'r', 'javascript', 'ruby'], True, ['nadar', 'ler', 'pedalar'], False]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(pessoa[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_indice_par = pessoa[::2]
print(elementos_indice_par)
# Remova da lista o último item
pessoa.pop()
print(pessoa)
# Insira na lista um novo item
pessoa.append('calopsita')
print(pessoa)
# Remova da lista um item específico
pessoa.remove(1973)
print(pessoa)