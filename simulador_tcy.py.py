#Desafio 2 


def dados_de_ataque (ataque, hp_do_defensor, nome_atacante):
    danos_causados = ataque - hp_do_defensor 
    print(f"{nome_atacante} atacou causando {danos_causados} de dano")
    return hp_do_defensor

def dados_de_defesa(nome_defensor , pontos_de_defesa):
    defesa= pontos_de_defesa * 2
    print (f"O {nome_defensor} se defendeu com {pontos_de_defesa}")
pontos_de_defesa= dados_de_ataque - dados_de_defesa


def exibir_placar(nome1,hp1, nome2,hp2):
    print(f"--- Placar: {nome1}: {hp1} HP {nome2}: {hp2} HP ---")

def main():
    print("Monstro 1")
    nome1= input("Nome do Monstro 1:"). strip()
    hp1= int(input(f"HP de {nome1}:"))
    ataque1= int(input(f"Pontos de ataque de {nome1}:"))
    hp1= pontos_de_vida ("Monstro 1") 
    
    print("Monstro 2")
    nome2= input("Nome do monstro 2:").strip()
    hp2= int(input(f"HP de {nome2}:"))
    ataque2= int(input(f"Pontos de ataque de {nome2}:"))
    hp2= pontos_de_vida ("Monstro 2")

#Restrição 
#Os pontos de vida - HP - não podem ser negativos 
pontos_de_vida= dados_de_ataque - pontos_de_defesa
if pontos_de_vida <0:
    print("Os pontos de vida não podem ser menores que 0")
elif pontos_de_defesa > 0:
    print ("Tente novamente, o programa aceita números == 0 ")
    
if dados_de_ataque <=0:
    print("Insira um valor válido, o programa não poderá continuar")
    

#Duelo
nome1= "Monstro 1"
nome2= "Monstro 2"
hp1= pontos_de_vida ("Monstro 1") 
hp2= pontos_de_vida ("Monstro 2")
while hp1 > 0 and hp2 > 0:
        print(f"Continue a jogada")

#Monstro 1 ataca o monstro 2 
hp2 = hp2 - (dados_de_ataque - pontos_de_defesa)
print (f"HP do{nome2}: {hp2}")
hp1 = hp1 - (dados_de_ataque - pontos_de_defesa)
print(f"HP do{nome1}: {hp1}")

#Vitória
print("Fim de jogo")
if hp1 >0:
     print(f"{nome1} é o grande vencedor do duelo!")
else: 
     print(f"{nome2} é o grande vencedor do duelo!")
      
    
