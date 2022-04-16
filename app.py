#print('hello world!')
#nome = input('Digite seu nome: ')
#print('É um prazer te conhecer, {}!' .format(nome))

#n1 = int(input('digite um numero: '))
#n2 = int(input('digite um numero: '))
#n3 = n1 + n2
#print('A soma entre {} e {} vale {}' .format(n1, n2, n3))


""""
var = input('digite algo: ')
print('É um numero? ', var.isnumeric())
print('É alfabético ', var.isalpha())
print('É alfanumerico? ', var.isalnum())
print('Está maiuscula? ', var.isupper())
print('Está minuscula? ', var.islower())
print('Está capitalizada? ', var.istitle())
"""


"""
#desafio 005
var = int(input('digite um numero inteiro: '))
print('O sucessor é {}' .format(var+1))
print('O antecessor é {}' .format(var-1))
"""
"""
#desafio 006
var = int(input('digite um numero inteiro: '))
print('O dobro é {}' .format(var*2))
print('O triplo é {}' .format(var*3))
print('A sua raiz quadrada é {:.2f}' .format(var**(1/2)))
"""
"""
#desafio 007
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A média é {}' .format(media))
"""
"""
#desafio 008
met = float(input('Digite um valor em metros: '))
centimeter = met * 100
milimeter = centimeter * 1000
print('{} metros tem {} centimetros e {} milimetros' .format(met, centimeter, milimeter))
"""
"""
#desafio 009
num = int(input('Digite o valor da tabuada: '))
print('{} X {:2} = {}' .format(num, 1, num*1))  #:2 posicionamento da variavel
print('{} X {:2} = {}' .format(num, 2, num*2))
print('{} X {:2} = {}' .format(num, 3, num*3))
print('{} X {:2} = {}' .format(num, 4, num*4))
print('{} X {:2} = {}' .format(num, 5, num*4))
print('{} X {:2} = {}' .format(num, 6, num*6))
print('{} X {:2} = {}' .format(num, 7, num*7))
print('{} X {:2} = {}' .format(num, 8, num*8))
print('{} X {:2} = {}' .format(num, 9, num*9))
print('{} X {:2} = {}' .format(num, 10, num*10))
"""

"""
#desafio 010
brl = float(input("digite um valor em reais que queira converter: "))
dolar = brl / 3.27
print('O valor em Dolar equivale a ${}' .format(dolar))
"""
"""
#desafio 011
width = float(input('Digite a largura da parede: '))
heigth = float(input('Digite a altura da parede: '))
area = width * heigth
liter = area / 2
print('A área da parede é {:.2f}m² e a quantidade de tinta necessária é de {:.2f} litros' .format(area, liter))
"""
"""
#desafio 012
brl = float(input("Digite o valor do produto que deseja calcular o desconto: "))
desc = brl * 0.95
print('O valor do produto com 5% de desconto é de R$:{:.2f}' .format(desc))
"""
"""
#desafio 013
brl = float(input("Digite o valor do salário que deseja calcular o aumento: "))
aum = brl * 1.15
print('O valor do salário com aumento é de R$:{:.2f}' .format(aum))
"""
"""
#desafio 014
celcius = float(input('Digite a temperatura em °C: '))
faren = (celcius * 1.8) + 32
print('{:.2f}°C equivale a {:.2f}°F' .format(celcius, faren))
"""
"""
#desafio 015
da = int(input('Digite a quantidade de dias de aluguel: '))
km = int(input('Digite a quantidade de quilômetros rodados: '))
cost = da * 60 + km * 0.15
print('O total a pagar é de R${}' .format(cost))
"""
"""
import math
#from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}' .format(num, raiz))
"""
"""
#desafio 016
import math
num = float(input('Digite um numero real: '))
print('A parte inteira de {} é {}' .format(num, math.trunc(num)))
print('A parte inteira de {} é {}' .format(num, int(num))) #retirando a parte inteira sem usar import
"""
"""
#desafio 017
from math import sqrt
cttop = float(input('Digite o valor do cateto oposto: '))
cttad = float(input('Digite o valor do cateto adjacente: '))
hipotenuse = sqrt((cttop**2)+(cttad**2))
print('O valor da Hipotenusa é {:.2f}' .format(hipotenuse))
"""
"""
#desafio 018
import math
angl = float(input('Digite o valor do angulo em °\n'))
angl = math.radians(angl)   #converter em radianos
seno = math.sin(angl)
cosseno = math.cos(angl)
tangente = math.tan(angl)
print('O seno é {:.2f}, \no cosseno é {:.2f} \na tangente é {:.2f}' .format(seno, cosseno, tangente))
"""
"""
#desafio 019
import random
name1 = input('Digite o nome do aluno: ')
name2 = input('Digite o nome do aluno: ')
name3 = input('Digite o nome do aluno: ')
name4 = input('Digite o nome do aluno: ')
nomes = [name1, name2, name3, name4]
print('O nome sorteado é {}' .format(random.choice(nomes)))
"""
"""
#desafio 020
import random
name1 = input('Digite o nome do aluno: ')
name2 = input('Digite o nome do aluno: ')
name3 = input('Digite o nome do aluno: ')
name4 = input('Digite o nome do aluno: ')
nomes = [name1, name2, name3, name4]
random.shuffle(nomes)
print('O primeiro a apresentar é {}, o segundo a apresentar é {}, o terceiro a apresentar é {} e o ultimo a aprensentar é {}' .format(nomes[0], nomes[1], nomes[2], nomes[3]))
"""
"""
#desafio 021
import pygame
pygame.init()
pygame.mixer.music.load('pri.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
"""
"""
#desafio 022
nome = str(input("Digite seu nome completo: \n")).strip
maiusc = nome.upper()
minusc = nome.lower()
separar = nome.split()
juntar = "".join(separar)
qtdcarac = len(juntar)
firstname = len(separar[0])
print("todas letras maiusculas:\n {}" .format(maiusc))
print("todas letras minusculas:\n {}" .format(minusc))
print("quantidade de letras do nome todo sem espaços:\n {}" .format(qtdcarac))
print("quantidade de letras do primeiro nome:\n {}" .format(firstname))
"""
'''
#desafio 023
num = int(input("digite um numero entre 0 e 9999: "))
milhar = int(num/1000)
centena = int(((num/1000) - milhar) * 10)
dezena = int(((((num/1000) - milhar) * 10) - centena) * 10)
unidade = int(((((((num/1000) - milhar) * 10) - centena) * 10) - dezena) * 10)
print("unidade: {}" .format(unidade))
print("dezena:  {}" .format(dezena))
print("centena: {}" .format(centena))
print("milhar:  {}" .format(milhar))

#outra forma de fazer

num = input("digite um numero entre 0 e 9999: ")
print("unidade: {}" .format(num[3]))
print("dezena:  {}" .format(num[2]))
print("centena: {}" .format(num[1]))
print("milhar:  {}" .format(num[0]))
'''
'''
#desafio 024
cida = input("Digite o nome da cidade: ")
cidade = cida.upper()
print(cidade[:5] == 'SANTO')
'''
'''
#desafio 025
nome = input("Digite o nome completo: ")
nome_mod = nome.upper()
var = nome_mod.find('SILVA')
print(var != -1)
#OR
#print("tem silva? {}" .format('silva' in nome.lower()))
'''

'''
#desafio 026
frase = input("digite uma frase: ").lower().strip()
quant = frase.count('a')
track = frase.find('a') + 1
trackult = frase.rfind('a') + 1

print("o algarismo A aparece     {} vezes" .format(  quant  ))
print("a posição do prineiro A é {}" .format( track   ))
print("a posição do ultimo A é   {}" .format( trackult   ))
'''
'''
#desafio 027
nome = input("digite o nome completo de uma pessoa: ").strip()
quebra = nome.split()
partes = len(quebra)
print("O primeiro nome é: {}" .format(quebra[0]))
print("O ultimo nome é: {}" .format(quebra[partes - 1]))
'''

#CONDIÇÕES
"""
#desafio 028
import random
numero = int(input("Tente adivinhar o numero que o CPU gerou entre 0 e 5!"))
cpunum = int(random.randrange(0,5))
if numero == cpunum:
    print("O numero sorteador foi {}, você acertou" .format(cpunum))
else:
    print("O numero sorteador foi {}, você errou" .format(cpunum))
"""
"""
#desafio 029
velocida = int(input("Digite o valor da velocidade: "))
if velocida > 80:
    multa = (velocida - 80) * 7
    print("Você foi multado e a multa pelo excesso de velocidade é de: R$:{}.00" .format(multa))
"""
"""
#desafio 030
num = int(input("Digite um valor para saber se é par ou impar: "))
if num%2 == 0:
    print("{} é par" .format(num))
else:
    print("{} é ímpar" .format(num))
"""
"""
#desafio 031
km = int(input("Digite a quilometragem da viagem: "))
if km <= 200:
    km = km * 0.5
    print("O valor dessa viagem é R$:{:.2f}" .format(km))
else:
    km = km * 0.45
    print("O valor dessa viagem é R$:{:.2f}" .format(km))
"""
"""
#desafio 032
from datetime import date
while 1:
    bissexto = int(input("digite o ano que deseja saber se é Bissexto, ou digite 0 para analisar o ano atual: "))
    if bissexto == 0:
        bissexto = date.today().year
    if bissexto%4 == 0 and bissexto%100 != 0 or bissexto%400 == 0:
        print("o ano {} é bissexto" .format(bissexto))
    else:
        print("o ano {} nao é bissexto" . format(bissexto))
"""
"""
#desafio 033
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if num1 < num2:
    if num1 < num3:
        menor = num1
    else:
        menor = num3
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

if num1 > num2:
    if num1 > num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3

print("O menor numero é {} e o maior é {}" .format(menor, maior))
"""
"""
#desafio 034
salario = float(input("Digite o valor do salário: "))
if salario <= 1250:
    salario = salario * 0.1
else:
    salario =  salario * 0.15

print("O aumento de salario é: {}" .format(salario)) 
"""
"""         
#desafio 035
print("-="*20)
print("       analisador de triangulos")
print("-="*20)
r1 = int(input("     Digite um tamanho de reta: "))
r2 = int(input("     Digite um tamanho de reta: "))
r3 = int(input("     Digite um tamanho de reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("pode formar triangulo")
else:
    print("nao pode formar triangulo")
"""         
""" 
#desafio 036
valor = float(input("digite o valor da casa: "))
salario = float(input("digite o valor do salario: "))
anos = int(input("Em quantos anos ele vai pagar: "))
tempo = anos * 12
total = valor/tempo
if salario * 0.3 >= total:
    print("Para pagar uma casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f} \nO emprestimo foi CONCEBIDO!" .format(valor, anos, total))
else:
    print("Para pagar uma casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f} \nO emprestimo NEGADO!" .format(valor, anos, total))
""" 
"""
#desafio 037
numero = int(input("Digite um numero inteiro: "))    
menu = int(input("Digite 1 para converter para binario \nDigite 2 para converter para octal \nDigite 3 para converter para hexadecimal \n"))
if menu == 1:
    print("{} convertido para BINÁRIO é {}" .format(numero, bin(numero)[2:]))   #inibindo parte do texto
elif menu == 2:
    print("{} convertido para BINÁRIO é {}" .format(numero, oct(numero)[2:]))
elif menu == 3:
    print("{} convertido para BINÁRIO é {}" .format(numero, hex(numero)[2:]))
else:
    print("seleção inválida")
"""
"""
#desafio 038
num1 = int(input("digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
if num1 < num2:
    print("O segundo valor é maior")
elif num1 > num2:
    print("O primeiro valor é maior")
else:
    print("os valores são iguais.")
"""
"""
#desafio 039
from datetime import date, datetime
ano = int(input("Digite o valor do ano de nascimento: "))
atual = date.today().year                   #pegando o ano atual
ano = atual - ano
if ano < 18:
    print("Ainda vai se alistar")
elif ano == 18:
    print("Hora de se alistar")
else:
    print("passou do tempo de se alistar")
"""
"""     
#desafio 040
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
if media < 5:
    print("Reprovado")
elif media >= 5 and media < 7:
    print("recuperação")
else:
    print("Aprovado")
"""     
"""     
#desafio 041
ano = int(input("Digite o valor da idade: "))
ano = 2022 - ano
print(ano)
if ano <= 9:
    print("MIRIM")
elif ano <= 14:
    print("INFANTIL")
elif ano <= 19:
    print("JUNIOR")
elif ano <= 20:
    print("SÊNIOR")
else:
    print("MASTER")
"""    
"""    
#desafio 042
print("-="*20)
print("       analisador de triangulos")
print("-="*20)
r1 = int(input("     Digite um tamanho de reta: "))
r2 = int(input("     Digite um tamanho de reta: "))
r3 = int(input("     Digite um tamanho de reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("pode formar triangulo")
    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 and r2 != r3:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("nao pode formar triangulo")
"""       
"""
#desafio 043
peso = float(input("Digite o seu peso em (Kg): "))
altura = float(input("Digite a sua altura em (m): "))
imc = peso/(altura*altura)
if imc < 18.5:
    print("O IMC é {:.1f}" .format(imc))
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("O IMC é {:.1f}" .format(imc))
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("O IMC é {:.1f}" .format(imc))
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("O IMC é {:.1f}" .format(imc))
    print("Obesidade")
else:
    print("O IMC é {:.1f}" .format(imc))
    print("Obesidade Morbida")
"""
"""
#desafio 044
valor = float(input("Digite o valor a ser pago: "))
pagamento = int(input("Digite 1 para pagamento em dinheiro/cheque \nDigite 2 para pagamento à vista no cartão \nDigite 3 para pagamento em até 2x no cartao \nDigite 4 para pagamento em 3x ou mais no cartao \n"))

if pagamento == 1:
    valor = valor * 0.9
    print("O valor a ser pago é {}" .format(valor))
elif pagamento == 2:
    valor = valor * 0.95
    print("O valor a ser pago é {}" .format(valor))
elif pagamento == 3:
    print("O valor a ser pago é {}" .format(valor))
elif pagamento == 4:
    valor = valor * 1.2
    print("O valor a ser pago é {}" .format(valor))
else:
    print("forma de pagamento inválida")
"""
'''
#desafio 045
import random
while 1:
    jogador = int(input("Digite: \n1 para pedra \n2 para papel \n3 para tesoura \n"))
    itens = "PEDRA PAPEL TESOURA"
    itens = itens.split()
    cpunum = int(random.randrange(1,3))
    print("-="*20)
    if jogador == cpunum:
        print("EMPATE! Você e o CPU escolheram {}" .format(itens[jogador - 1]))
    elif jogador == 1 and cpunum == 2:
        print("CPU venceu")
    elif jogador == 1 and cpunum == 3:
        print("Você venceu!")
    elif jogador == 2 and cpunum == 1:
        print("Você venceu!") 
    elif jogador == 2 and cpunum == 3:
        print("CPU venceu")
    elif jogador == 3 and cpunum == 1:
        print("CPU venceu!")
    elif jogador == 3 and cpunum == 2:
        print("Você venceu!")
    else:
        print("jogada invalida")
    print("-="*20)
'''
"""
#desafio 046
from time import sleep
numeros = ("dez", "nove", "oito", "sete", "seis", "cinco", "quatro", "tres", "dois", "um", "zero")
print("contagem regressiva ...")
for c in range(0,11):
    print(numeros[c])
    sleep(0.5)
"""
"""
#desafio 047
for c in range(1,51):
    if c%2 == 0:
        print(c)
"""
"""
#desafio 048
sum = 0
for c in range(1,501):
    if c%3 == 0 and c%2 != 0:
        sum = sum + c
print(sum)
#outra maneira
soma = 0
for c in range(3,501, 6):
    soma = c + soma
print(soma)
"""
"""
#desafio 049
tabuada = int(input("Digite o valor do numero que deseja calcular a tabuada: "))
for c in range(1,11):
    print("{} x {:2}  = {}" .format(tabuada, c, tabuada * c))   #:2 posição do texto
"""
"""
#desafio 050
var = 0
for c in range(0, 6):
    variavel = int(input(f"Digite {c+1}º valor para ser somado: "))
    if variavel%2 == 0:
        var = var + variavel
print(var)
"""
"""
#desafio 051
a1 = int(input("Digite o primeiro termo: "))
razao = float(input("Digite a razão da progressão aritmética: "))
#print("o 1º termo é: {}" .format(a1))
for c in range(1, 11):
    print("{}" .format(a1), end= " → ")
    a1 = razao + a1
print("Acabou! \n")
"""
"""
#desafio 052
num = int(input("Digite um numero inteiro: "))
cont = 0
for c in range(num, 1, -1):
    if num%c == 0:
        cont = cont + 1
if cont > 2:
    print("O numero não é primo!")
else:
    print("O numero é primo!")
"""
"""
#desafio 053
frase = str(input("Digite uma frase: ")).lower().split()
frase = "".join(frase)
tam = len(frase)
cont = 0
metade = int(tam/2)
for c in range (0, metade):
    if frase[c] != frase[tam - c - 1]:
        cont = cont + 1
if cont > 0:
    print("Não é palindromo!")
else:
    print("A frase é palindromo!")
"""
"""
#desafio 054
from datetime import date, datetime
atual = date.today().year 
cont = 0
cont2 = 0
for c in range(0,7):
    ano = int(input("Digite o ano de nascimento: "))
    if (atual - ano) < 21:
        cont = cont + 1
    else:
        cont2 += 1   
print(f"{cont} pessoas que não atingiram a maioridade")
print(f"{cont2} pessoas que atingiram a maioridade")
"""
"""
#desafio 055
maior = 0
menor = 0
for c in range (0, 5):
    peso = int(input("Digite o peso: "))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
print(f"O maior peso é {maior} e o menor peso é {menor}")
"""
"""
#desafio 056
cont = 0
old = 0
cont_M = 0
for c in range(0, 4):
    print(f"----- {c +1}ª pessoa -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    cont = idade + cont
    if idade > old and sexo == "M":
        old = idade
        nome2 = nome
    if idade < 20 and sexo == "F":
        cont_M = cont_M + 1
print(f"\nA media de idade do grupo é {cont/4} anos\n O nome do homem mais velho é {nome2}.\n Ao todo existem {cont_M} mulheres com menos de 20 anos")
"""
"""
#desafio 057
c = 1
while c == 1:
    sex = str(input("Qual sexo [M/F]")).upper().strip()
    if sex == "M" or sex == "F":
        print(f"O sexo é {sex}")
        c = 0
"""
"""
#desafio 058
import random
numero = int(input("Tente adivinhar o numero que o CPU gerou entre 0 e 10!"))
cpunum = int(random.randrange(0,10))
c = 1
while c != 0:
    if numero == cpunum:
        print("O numero sorteador foi {}, você acertou na {}ª tentativa" .format(cpunum, c))
        c = 0
    else:
        numero = int(input("Você errou! \nTente novamente:"))
        c += 1
"""
"""
#desafio 059
num1 = float(input("Digite o valor: "))
num2 = float(input("Digite o valor: "))
while 1:
    print("Digite: \n[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos numeros \n[5]Sair do programa")    
    sel = int(input())
    if sel == 1:
        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}")
    elif sel == 2:
        mult = num1 * num2
        print(f"{num1} * {num2} = {mult}")
    elif sel == 3:
        if num1 > num2:
            print(f"O maior é {num1}")
        else:
            print(f"O maior é {num2}")
    elif sel == 4:
        num1 = float(input("Digite o novo valor: "))
        num2 = float(input("Digite o novo valor: "))
    elif sel == 5:
        break
    else:
        print("Seleção inválida")
"""
"""
#desafio 060
fatorial = int(input("Digite o numero para calcular o fatorial: "))
for c in range (fatorial, 1, -1):
    fatorial = fatorial * (c-1)
print(f"O fatorial é {fatorial}")
"""
"""
#desafio 061
a1 = int(input("Digite o primeiro termo: "))
razao = float(input("Digite a razão da progressão aritmética: "))
c = 0
#print("o 1º termo é: {}" .format(a1))
while c < 10:
    print("{}" .format(a1), end= " → ")
    a1 = razao + a1
    c += 1
print("Acabou! \n")
"""
#desafio 062 "Melhorar o desafio 061 perguntando se o usuario quer adicionar mais numeros"

"""
#desafio 063
ant = 1
atu = 0
fibbo = int(input("Digite a quantidade de n inteiros que quer ver da sequencia Fibonacci: "))
if fibbo == 0:
    print("0")
else:
    for c in range(1, fibbo):
        atu = atu + ant
        ant = atu - ant
    print(atu)
"""
"""
#desafio 064
cont = 0
soma = 0
c = 0
while c != 999:
    c = int(input("Digite um numero: \n"))
    if c == 999:
        break
    soma = c + soma
    cont += 1
print(f"A soma dos numeros difitados é: {soma}")
print(f"A quantidade de numeros digitados foi: {cont}")
"""
"""
#desafio 065
quest = "s"
maior = 0
menor = 0
media = 0
cont = 0
soma = 0
while quest == "s":
    cont += 1
    quest = str(input("Você deseja digitar um valor [S/N]: ")).lower()
    if quest != "s":
        break
    valor = int(input("Digite um valor: "))
    if cont == 1:
        maior = valor
        menor = valor
    if maior > 
    soma = soma + valor
    media = soma / cont
print(f"A media é {media} e a soma é {soma}")
"""
"""
#desafio 066
cont = 0
soma = 0
c = 0
while c != 999:
    c = int(input("Digite um numero: \n"))
    if c == 999:
        break
    soma = c + soma
    cont += 1
print(f"A soma dos numeros difitados é: {soma}")
print(f"A quantidade de numeros digitados foi: {cont}")
"""
"""
#desafio 067
num = 0
while num >= 0:
    print("-"*20)
    print('Digite o valor da tabuada: ')
    print("-"*20)
    num = int(input())
    if num < 0:
        break
    else:
        print('{} X {:2} = {}' .format(num, 1, num*1))  #:2 posicionamento da variavel
        print('{} X {:2} = {}' .format(num, 2, num*2))
        print('{} X {:2} = {}' .format(num, 3, num*3))
        print('{} X {:2} = {}' .format(num, 4, num*4))
        print('{} X {:2} = {}' .format(num, 5, num*4))
        print('{} X {:2} = {}' .format(num, 6, num*6))
        print('{} X {:2} = {}' .format(num, 7, num*7))
        print('{} X {:2} = {}' .format(num, 8, num*8))
        print('{} X {:2} = {}' .format(num, 9, num*9))
        print('{} X {:2} = {}' .format(num, 10, num*10))
print("-"*20)
print('PROGRAMA ENCERRADO! ')
print("-"*20)
"""
"""
#desafio 068
import random
pess = str(input("Digite Par ou Impar [P/I]: "))
if pess == "p":
    pess = "par"
else:
    pess = "impar"

cpu = ["par", "impar"]
cont = 0
random.choice(cpu)

if pess == "par" and cpu == "impar":
"""    
"""
#desafio 072
while 1:
    numero = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", " dez", " onze", " doze", " treze", " quatorze", " quinze", " dezesseis", " dezessete", " dezoito", " dezenove", " vinte") 
    num = int(input("digite um numero entre 0 e 20 ou uma letra para encerrar o programa: "))
    if num >= 0 and num <= 20:
        print(f"O numero digitado foi {numero[num]}")
    else: 
        print("Entrada inválida, tente novamente!")
"""        

#desafio 073
"""        
#desafio 074 (adicionando valores em tuplas)
from random import randint
maior = 0
menor = 10
valor = (randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for c in range(0, 5):
    if valor[c] < menor:
        menor = valor[c]
    if valor[c] > maior:
        maior = valor[c]   
print(f"{valor}, o maior é {maior} e o menor é {menor}")
"""        
"""
#desafio 075
num =  (int(input("Digite um numero: ")),
        int(input("Digite um numero: ")), 
        int(input("Digite um numero: ")), 
        int(input("Digite um numero: ")))
print(f"Você digitou {num}")
print(f"O numero 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O numero 3 apareceu na {num.index(3) + 1}ª posição")
else:
    print(f"O numero 3 não apareceu")
print("Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
"""
"""
#desafio 076
lista =    ("lapis", 1.75,
            "borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Transferidor", 4.20)
print("-" * 40)
print("Listagem de preços")            
print("-" * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")             #":30" define que a linha vai ter 30 caracteres ".<" define que vou colocar pontos
    else:
        print(f"R${lista[pos]:>7.2f}")                  #":2.f" 
print("-" * 40)
"""
"""
#desafio 077
palavras = ("Aprender", "programar", "linguagem", 
            "python", "curso", "gratis", 
            "estudar", "praticar", "trabalhar")
for p in palavras:
    print(f"\nNa palavra {p.upper():.<10} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
"""          
"""
#desafio 078
var = []
for c in range(0, 5):
    var.append(int(input("Digite um numero: ")))
print(var)
minim = min(var)
maximo = var.index(max(var))
print(f"O maior valor é {max(var)} que esta na posição {var.index(max(var))}, e o menor valor é {min(var)} que esta na posição {var.index(min(var))}")
"""
"""
#desafio 079
cond = 0
var = []
while cond == 0:
    numero = int(input("Digite um valor: "))
    if numero in var:
        print("Valor repetido!")
    else:
        var.append(numero)
    condi = str(input("deseja digitar um novo valor?  [S/N]")).upper().strip()
    if condi == "S":
        cond = 0
    else:
        cond = 1
print(f"os valores sao {var}")
"""
"""
#desafio 080 **
var = []
var2 = []
for c in range(0, 5):
    numero = int(input("Digite um numero: "))
    var.append(numero)
for c in range(0, 5):
    var2.append(min(var))
    var.remove(min(var))
print(var2)
"""
"""
#desafio 081
cond = 0
c = 0
var = []
while cond == 0:
    numero = int(input("Digite um valor: "))
    var.append(numero)
    condi = str(input("deseja digitar um novo valor?  [S/N]")).upper().strip()
    if condi == "S":
        cond = 0
    else:
        cond = 1
    c += 1 
print("-=" * 25)
print(f"Você digitou {c} elementos.")
var = sorted(var, reverse=True)
print(f"Os valores em ordem descrescente são {var}")
if 5 in var:
    print(f"O valor 5 faz parte da lista")
else:
    print(f"O valor 5 nao faz parte da lista")
print("-=" * 25)
"""

#desafio 082

cond = 0
c = 9
varpar = []
varimpar = []
var = [1,2,3,4,5,6,7,8,9]
"""
while cond == 0:
    numero = int(input("Digite um valor: "))
    var.append(numero)
    condi = str(input("deseja digitar um novo valor?  [S/N]")).upper().strip()
    if condi == "S":
        cond = 0
    else:
        cond = 1
    c += 1

for cont in range(0, c):
    if var.index[cont] % 2 == 0:
        varpar.append(var.index[cont])
    else:
        varimpar.append(var.index[cont])
"""
print(var.index(0))
print("-=-" *25)
print(varimpar)
print(varpar)
print(var)
print("-=-" *25)