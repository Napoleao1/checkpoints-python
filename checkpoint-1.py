import random

numero_secreto = random.randint(1, 100)
tentativas = 0
limite_tentativas = 7

print(f"Bem-vindo! Você tem {limite_tentativas} tentativas para adivinhar o número entre 1 e 100.")

while True:

    numero_escolhido = int(input("digite um numero para adivivinhar o numero secreto: "))
    tentativas += 1

    if numero_escolhido == numero_secreto:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
        break
    
    if tentativas >= limite_tentativas:
        print(f"suas tentativas acabaram o numero secreto era {numero_secreto}")
        break
    
    elif numero_escolhido < numero_secreto:
        print("o numero é um pouco MAIOR ")       
        
    else:
        print("o numero é um pouco MENOR ")            
        
        
        
    print(f"Tentativas restantes: {limite_tentativas - tentativas}")
    
    