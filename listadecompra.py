import os #importei a biblioteca (os) 

lista = [] # lista inicia vazia 

while True: #laço de repetição para que a ação fique se repetindo 
    
    print('SUPERMERCADO RB')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()# opções do usuario 
    #criação de blocos para inserir dados na lista 
    if opcao == 'i':
        os.system('cls') # usei o método system e o (cls) para limpa a biblioteca .
        valor = input('Nome e preço: ')
        lista.append(valor) 
  
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ' )
        try: 
            indice = int(indice_str)
            del lista[indice]#apaga dados da lista 
            #capitura erros com execept 
        except ValueError:#corrigir erro
            print('Por favor digite número int.')
        except IndexError:#corrigir erro
            print('Índice não existe na lista')
        except Exception:#corrigir erro
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        for i, valor in enumerate(lista):
            print(i,valor)
    else:
        print('Por favor, escolha i, a ou l.')
