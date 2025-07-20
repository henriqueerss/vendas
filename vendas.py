# Escreva um programa que leia o valor de uma 
# Ler venda
venda = float(input("Digite a venda: \n"))

# Se venda > 500 então:
if venda > 500:
    # desconto = venda * 20 / 100
    desconto = venda * 0.20
    
    # venda = venda - desconto
    venda -= desconto

# Exibir venda com desconto
# Exibir o valor da venda com desconto
print(f"Venda com desconto: {venda:.2f}")