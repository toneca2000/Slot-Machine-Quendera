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
        print("You have ", creds, "credits")
        answer = input("Do you wish to continue ? ")
        while ((answer != 'yes' ) and (answer != 'no') and (answer != 'No') and (answer != 'Yes') ):
            answer = input("Invalid answer! ")
        if((answer == 'no') or (answer == 'No')):
            print("Thank you for playing!")
            return
    
    print("You lost!")
        
        
def swing(bet):
    swing_out1 = Slot(157)
    swing_out2 = Slot(157)
    swing_out3 = Slot(157)
    print( swing_out1.simbol_out, swing_out2.simbol_out, swing_out3.simbol_out)
    if ((swing_out1.simbol_out == swing_out2.simbol_out) and (swing_out2.simbol_out == swing_out3.simbol_out)):
        print("Parabens!")
        if(swing_out1.simbol_out == '#'):
            return bet*5
        if(swing_out1.simbol_out == '$'):
            return bet*10
        if(swing_out1.simbol_out == '%'):
            return bet*20
        if(swing_out1.simbol_out == '&'):
            return bet*70
        if(swing_out1.simbol_out == '@'):
            return bet*200
        if(swing_out1.simbol_out == '§'):
            return bet*1000
        if(swing_out1.simbol_out == '£'):
            return bet*100000
    else:
        print("Too bad !")
        return 0



game()