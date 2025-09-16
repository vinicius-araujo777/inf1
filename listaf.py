#Questão 1
#nome = input("digite seu nome: ")
#def oi(nome):
#	return(f"ola {nome}, seja bem vindo ao curso de logica de programação")
#print(oi(nome))


#Questão 2
#a = int(input("digite um numero "))
#def par_impar(a):
#	if a %2 == 0:
#		return (f"{a} é par")
#	else:
#		return(f"{a} é impar")
#print(par_impar(a))


#Questão 3
#a = int(input("digite um numero "))
#b = int(input("digite um numero "))
#def maior(a,b):
#	if a > b:
#		return (f"{a} é maior que {b}")
#	elif a < b:
#		return (f"{b} é maior que {a}")
#	else:
#		return (f"{a} é igual a {b}")
#print(maior(a,b))


#Questão 4
#n = int(input("digite um numero "))
#for i in range(1,11):
#	print(f"{n} x {i} = {n*i}")


#Questão 5
#n = 10
#while n >= 1:
#	print(n)
#	n -= 1
#print("PAYSANDUUU!!!!")


#Questão 6
#def media(med):
#	return (f"sua media foi {med}")
	
#l = int(input("digite sua nota (digite 0 para parar) "))
#qn = 0
#tn = 0
#while l >= 1:
#	tn += l
#	qn += 1
#	l = int(input("digite sua nota (digite 0 para parar) "))
#med = tn/qn
#print(media(med))


#Questão 7
#def fatorial(f):
#	return (f"o fatorial do seu numero é {f}")
	
#n = int(input("digite um numero para saber seu fatorial "))
#f = 1
#cn = n
#while cn >= 1:
#	f *= cn
#	cn -= 1
#print(fatorial(f))


#Questão 8
#def saber_vogal(c):
#	return(f"sua palavra tem {c} vogais")

#p = input("digite uma palavra ")
#c = 0
#for l in p:
#	if l in "a,e,i,o,u":
#		c += 1
#print(saber_vogal(c))

#import random
#n = random.randint(1,20)
#ne = int(input("digite um numero "))
#if n == ne:
#	print("parabens voce acertou ")
#elif ne > n:
#	print("o numero escolhido é maior ")
#elif ne < n:
#	print("o numero escolhido é menor")


#Questão 10
#def somapar(a):
#	soma = 0
#	for i in range(1, a+1):
#		if i %2 == 0:
#			soma += i
#	return soma
			
#a = int(input("digite um numero "))
#print(somapar(a))


#Questão 11
#def calcular(n1,n2):
#	if op == "+":
#		return(n1+n2)
#	elif op == "×":
#		return(n1*n2)
#	elif op == "-":
#		return(n1-n2)
#	elif op == "÷":
#		return(n1/n2)
#n1 = int(input("numero "))
#n2 = int(input("numero "))
#op = input("+,-,×,÷ ")
