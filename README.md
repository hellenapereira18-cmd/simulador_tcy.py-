# simulador_tcy.py
Desafio 2 da trilha de python 2026.1

Esse código foi elaborado para estabelecer o vencendor de um duelo entre dois monstros, os danos serão analisados de forma dinâmica, 
até que os pontos de vida (HP) de um dos monstrons sejam iguais a zero.
O programa exibirá:
while hp1 > 0 and hp2 > 0:
  print(f"Continue a jogada")

#Explicação de execução:
1) O usuário insere o nome, pontos de vida(HP), pontos de ataque para ambos os monstros do duelo.
2) Se algum desses pontos forem menores ou iguais a zero, o programa avisa o usuário e encerra a execução.
Exemplo no código:
if pontos_de_vida < 0:
  print ("Os pontos de vida não podem ser menores que 0")
elif pontos_de_defesa >0:
   print("Tente novamente, o programa não aceita números == 0")
if dados_de_ataque <=0:
  print("Insira um valor válido, o programa não poderá continuar")
3) O loop de repetição (while): o duelo ocorre em uma estrutura de repetição que continua ativa enquanto os monstros possuírem HP maior que zero.

O mostro 1 ataca o monstro 2, 
Se o monstro 2 sobreviver, ele contra-ataca o monstro 1. 
O HP de nenhum monstro pode ser negativo (o sistema força o valor ser igual a zero).

#Exibição do placar e vitória
No fim do duelo, o placar é atualizado. Quando o laço termina, uma condicional identifica o monstro vencedor e o declara como mostro vencedor
Exemplo:
print("Fim de jogo")
if hp1 >0:
  print(f"{nome'} é o grande vencedor do duelo!")
else:
  print(f"{nome2} é o grande vencedor do duelo!")

#Lista
As lista foram criadas para definir as funções executadas durante o duelo. 
Exemplo do código:
def exibir_placar(nome1,hp1,nome2,hp2):
  print(f"---Placar: {nome1}: {hp1}, HP {nome2}: {hp2} HP ---")


RESPOSTAS ÀS PERGUNTAS TEÓRICAS
1) O laço for cria um loop de repetição que conhecemos, ou seja sabemos quantas vezes ocorrerá a repetição, além de percorrer itens de uma lista. De forma geral, ele estabelece um limite.
Já o laço while cria um loop, até a condição deixar de ser True e não sabemos quantas vezes ocorrerá a repetição. O laço while foi a melhor condição para o duelo, porque não tem como definir
a duração da batalha.
2) A função return volta a função do print para o código. Se a função matemática não possuir o return, ela será perdida, pois não poderá retornar ao código.
3) Um loop infinito ocorre quando o laço while não deixa de ser True, isso faz com que o código fique executando a mesma condição. Para evitar isso, devemos ter as condicionais if, else, elif para auxiliar
nas tomadas de decisões.  
