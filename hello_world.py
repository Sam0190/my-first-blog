print('Ciao, Django girls!')
	
if 5 > 2:
     print('5 è infatti maggiore di 2') 
else:
     print('5 non è maggiore di 2')
	
volume = 57
if volume < 20:
    print("Piuttosto basso.")
elif 20 <= volume < 40:
    print("Adatto per musica di sottofondo")
elif 40 <= volume < 60:
    print("Perfetto, posso apprezzare ogni dettaglio")
elif 60 <= volume < 80:
    print("Ideale per le feste")
elif 80 <= volume < 100:
    print("Un po' altino!")
else:
    print("Oddio, le mie orecchie! :(")
	
def ciao():
    print('Ciao!')
    print('Come stai?')

ciao()

def ciao(nome):
    if nome == 'Ola':
        print('Ciao Ola!')
    elif nome == 'Sonja':
        print('Ciao Sonja!')
    else:
        print('Ciao ' + nome + '!')

ciao('Sam')

ragazze = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Tu']
for nome in ragazze:
    ciao(nome)
    print('Prossima ragazza')

for i in range(1, 6):
    print(i)