import random, itertools
class BlackJack():
    def __init__(self, leave_cards=[], Player=[], points_players=[]):
        self.leave_cards=leave_cards
        self.Player=Player
        self.points_players=points_players
    
    def Play(self):
        Decks=random.sample([''.join(card) for card in itertools.product([x for n in ([str(i) for i in range(2, 11)],['J', 'Q', 'K', 'A']) for x in n], ['♠️', '♣️', '♥️', '♦️'])], 52)
        while True:
            question=input("Готові зіграти в очко? Пиши тільки yes або no.")
            if question.lower() == 'yes':
                p=1
                players=int(input("Скілька гравців будуть грати?"))
                while p <= players:
                    print(f"{p}-й гравець тягне карти")
                    question_2=input("Витягуєш карту?")
                    if question_2.lower() == 'yes':
                        a=random.choice(Decks)
                        print(a)
                        self.leave_cards.append(a)
                        self.Player.append(int(a[0] if a[0].isdigit() else(10 if a[0] in ['J', 'Q', 'K'] else 11)))
                    elif question_2.lower() == 'no':
                         
                        print(f"{p}-й гравець набрав: {sum(self.Player)}")
                        self.points_players.append(sum(self.Player) if sum(self.Player)<21 else (sum(self.Player)-10 if 11 in self.Player else sum(self.Player)))
                        self.Player.clear()
                        p+=1
            elif question.lower() == 'no':
                break
            BlackJack().WINNER(), BlackJack().CLS()
            
    def WINNER(self):
        self.points_players= [p if p<=21 else p*-1 for i, p in enumerate(self.points_players)]
        print(f"переміг {self.points_players.index(max(self.points_players))+1} гравець" if sum(self.points_players)>0 else "Ви всі лохи")
        print(self.points_players)        
        
    def CLS(self):
        self.points_players.clear(), self.leave_cards.clear()

BlackJack().Play()
