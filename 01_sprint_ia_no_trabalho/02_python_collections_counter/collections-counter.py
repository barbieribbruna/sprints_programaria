from collections import Counter # importa a classe 'Counter' da biblioteca 'collections' | 'Counter' conta automaticamente quantas vezes cada elemento aparece

def contar_letras(palavra): # função que recebe uma palavra e conta as letras dessa palavra
    return Counter(palavra) # 'Counter' percorre toda a palavra e cria um dicionário automaticamente (ex: 'codigo' -> {'c':1, 'o':2, 'd':1, 'i':1, 'g':1})

# exemplo de uso
palavra = "codigo" # varivável 'palavra' contendo a palavra que será analisada
contagem = contar_letras(palavra) # chama a função acima e guarda o resultado na variável 'contagem'

print(f"A letra 'o' aparece {contagem.get('o', 0)} vezes na palavra '{palavra}'.") # contagem.get('o', 0) exibe quantas vezes a letra 'o' aparece na palavra e, caso inexistente, retorna 0

print("\nContagem de todas as letras:") # exibe um título antes de mostrar todas as letras
for letra, quantidade in contagem.items(): # .items() percorre o dicionário retornando a letra (chave) e a quantidade (valor)
    print(f"'{letra}' : {quantidade} vez(es)!") # exibe cada letra e quantas vezes ela apareceu na palavra