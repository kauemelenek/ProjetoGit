
pedido = float(input('Qual o valor total do pedido?: '))
gorjeta = int(input('Qual a porcentagem de gorjeta que você gostaria de adicionar? 10, 12 ou 15?: '))
pessoas = int(input('Quantas pessoas vão dividir a conta?: '))


total_a_apagar = round((gorjeta / 100) * pedido + pedido, 2)
total_individual = round((pedido / 5) + ((pedido * gorjeta / 100) / 5), 2)
total_individual = "{:.2f}".format(total_individual) #Usamos aquele formato para colocar 2 casas decimais após a virgula

print(f'O total deu {total_a_apagar} reais, enquanto o total individual deu {total_individual} reais, ambos com '
      f'adição de gorjeta')
