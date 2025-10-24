def media(lnotas):
	soma = 0
	for i in lnotas:
		soma += i
	return int(soma/len(lnotas))
	
	
def vermed(media):
	if media >= 7:
		return "aprovado"
	elif media == 5 or media <= 6.9:
		return "recuperação"
	else:
		return "reprovado"