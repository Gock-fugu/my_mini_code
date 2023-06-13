import random, itertools
Decks=random.sample([''.join(card) for card in itertools.product([x for n in ([str(i) for i in range(2, 11)],['J', 'Q', 'K', 'A']) for x in n], ['♠️', '♣️', '♥️', '♦️'])]*6, 312)

class BlackJack():
    def __init__(self, leave_cards=[], Player=[], Diler=[]):
        self.leave_cards=leave_cards
        self.Player=Player
        self.Diler=Diler
    
    def Play(self):
        players = int(input("Скілька гравців будуть грати?"))
        for player in range(players):
            for i in range(2):
                self.Diler.append(Decks.pop(0))
                self.Player.append(Decks.pop(0))
            print(f"{self.Player}\n{self.Diler[0]}")
            while True:
                HIT = input("Hit?")
                if HIT.lower() == 'yes':
                    self.Player.append(Decks.pop(0))
                    print(self.Player)
                    
                elif HIT.lower() == 'no':#теба тробити віднімання очків при умові що сума очків більша 21 і наявність туза в рукаві
                    player+=1
                    self.Diler.append(Decks.pop(0)) if sum([int(c[0]) if c[0].isdigit() else (10 if c.count('10' or 'J' or 'Q' or 'K')==1 else 11) for c in self.Diler])<17 else None
                    print(f"{self.Player}, {self.Diler}\n {[int(c[0]) if c[0].isdigit() else (10 if '10' or 'J' or 'Q' or 'K' in c else 11) for c in self.Player]}, {[int(c[0]) if c[0].isdigit() else (10 if '10' or 'J' or 'Q' or 'K' in c else 11) for c in self.Diler]}")
                    self.Player.clear(), self.Diler.clear()
                    break
for i in range(1000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_0000):    
    BlackJack().Play()
