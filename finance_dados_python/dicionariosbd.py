dicionario_vazio = {}


dicionario_povoado = dict({'nome': 'Lucas', 'sobrenome': 'Morais' })

print(dicionario_povoado)
dicionario_com_listas = {'empresas_novo_mercado':['Weg', 'Renner', 'Vale'],
'empresas_em_outros_segmentos': ['Petrobras', 'XP']}


dicionario_numerico = {1:' Lucas', 2:'Helen', 3:'aleatório'}


dicionario_empresas_na_carteira = {True: ['Pão de açucar', 'Weg'], False:['Lojas Renner', 'Suzano']}




#print(dicionario_numerico[2])
#print(dicionario_numerico.get(2))
#print(dicionario_numerico[1])
print(dicionario_povoado.get('nome'))