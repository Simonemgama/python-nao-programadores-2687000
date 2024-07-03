pessoa = {'nome':'Simone', 
          'idade':51, 
          'ano_formatura':2006, 
          'linguagens_programacao':['python', 'r', 'javascript', 'ruby'], 
          'brasileira':True, 
          'hobby':['Jogar Tenis', 'ler', 'ouvir música'], 
          'animal_estimacao':True}

# Imprima na tela o valor equivalente a chave "hobby"
print(pessoa['hobby'])

# Imprima na tela uma lista apenas com os valores do dicionário
valores = list(pessoa.values())
print(valores)

# Imprima na tela uma lista apenas com as chaves do dicionário
chaves = list(pessoa.keys())
print(chaves)

# Insira um novo par chave-valor no dicionário
pessoa['altura'] = 1.57
print(pessoa)