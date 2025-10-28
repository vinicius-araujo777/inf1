from colorama import Fore, Style, init
init()
g = Fore.GREEN
r = Fore.RED	
y = Fore.YELLOW	
reset = Style.RESET_ALL

def media(lnotas):
	soma = 0
	for i in lnotas:
		soma += i
	return int(soma/len(lnotas))
	
	
def vermed(mediaa):
	if mediaa >= 7:
		return f"{g}aprovado{reset}"
	elif 5 <= mediaa < 7:
		return f"{y}recuperação{reset}"
	else:
		return f"{r}reprovado{reset}"