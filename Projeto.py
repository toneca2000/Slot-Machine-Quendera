from random import randrange

class Slot:
    simbols = 7
    simbol_out = '#'
    number_out = 157
    def __init__(self,number_out):
        self.simbol_out = self.swing()
    def swing(self):
        self.number_out = randrange(1, 157)
        if(0 < self.number_out < 51 ):
            return '#'
        if(50 < self.number_out < 91 ):
            return '$'
        if(90 < self.number_out < 121 ):
            return '%'
        if(120 < self.number_out < 141 ):
            return '&'
        if(140 < self.number_out < 151 ):
            return '@'
        if(150 < self.number_out < 156 ):
            return '§'
        if(self.number_out == 156):
            return '£'

def game():
    creds = input("Quantos créditos quer depositar? ")  
    creds = int(creds) 
    while (creds <= 0):
        creds = input("Apresente um número válido! ")  
        creds = int(creds) 
    while (creds > 0):
        bet = input("Quantos créditos quer apostar? ")
        bet = int(bet)
        while((bet <= 0) or (creds - bet < 0)):
            bet = input("Apresente uma resposta válida ! ")
            bet = int(bet) 
        creds = creds - bet
        bet = swing(bet)
        creds += bet
        print("Tu tens ", creds, "creditos")
        if(creds!=0 ):
            answer = input("Quer continuar ? ")
            while ((answer != 'sim' ) and (answer != 'não') and (answer != 'Não') and (answer != 'Sim') ):
                answer = input("Resposta Inválida! ")
            if((answer == 'não') or (answer == 'Não')):
                print("Obrigado por jogar!")
                return
    
    print("Perdeste!")
        
        
def swing(bet):
    slot = Slot(157)
    print( slot.swing(), slot.swing(), slot.swing())
    if ((slot.swing() == slot.swing()) and (slot.swing() == slot.swing())):
        print("Parabens!")
        if(slot.swing() == '#'):
            return bet*5
        if(slot.swing() == '$'):
            return bet*10
        if(slot.swing() == '%'):
            return bet*20
        if(slot.swing() == '&'):
            return bet*70
        if(slot.swing() == '@'):
            return bet*200
        if(slot.swing() == '§'):
            return bet*1000
        if(slot.swing() == '£'):
            return bet*100000
    else:
        print("Azar !")
        return 0



game()