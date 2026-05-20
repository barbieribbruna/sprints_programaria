def contar_letras(palavra): # função que recebe uma palavra e conta quantas vezes cada letra aparece    
    
    contagem = {} # cria um dicionário vazio para armazenar letra (chave) e quantidade (valor)    
    
    for letra in palavra: # o 'for' percorre cada letra da palavra (ex: 1ª volta -> letra = 'c')        
        if letra in contagem: # verifica se a letra já existe dentro do dicionário            
            contagem[letra] += 1 # se existir a letra dentro do dicionário, soma-se +1 na quantidade atual           
        else: # se a letra não existir dentro do dicionário, cai na contagem abaixo            
            contagem[letra] = 1 # a letra é criada no dicionário com valor inicial 1            
    return contagem # retorna o dicionário completo com as contagens

# exemplo de uso
palavra = "codigo" # variável 'palavra' contendo a palavra que será analisada

resultado = contar_letras(palavra) # chama a função e armazena o resultado na variável 'resultado'

print(f"A letra 'o' aparece {resultado.get('o', 0)} vezes na palavra '{palavra}'. ") # exibe quantas vezes aparece a letra 'o' | .get('o', 0) procura a letra 'o' no dicionário | se não encontrar, retorna 0

print("\nContagem de todas as letras:") # exibe a contagem de todas as letras

for letra, quantidade in resultado.items(): # .items() percorre chave (letra) e valor (quantidade) no dicionário ao mesmo tempo
    print(f"'{letra}' : {quantidade} vez(es)") # mostra cada letra e sua quantidade