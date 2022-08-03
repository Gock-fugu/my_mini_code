from random import choice
cards=['2♠️', '3♠️', '4♠️', '5♠️', '6♠️', '7♠️', '8♠️', '9♠️', '10♠️', 'J♠️', 'Q♠️', 'K♠️', 'A♠️', '2♥️', '3♥️', '4♥️', '5♥️', '6♥️', '7♥️', '8♥️', '9♥️', '10♥️', 'J♥️', 'Q♥️', 'K♥️', 'A♥️', '2♣️', '3♣️', '4♣️', '5♣️', '6♣️', '7♣️', '8♣️', '9♣️', '10♣️', 'J♣️', 'Q♣️', 'K♣️', 'A♣️', '2♦️', '3♦️', '4♦️', '5♦️', '6♦️', '7♦️', '8♦️', '9♦️', '10♦️', 'J♦️', 'Q♦️', 'K♦️', 'A♦️',]
leave_cards=[]
Player=[]
points_players=[]
def new_ochko():
    p=1
    while True:
        question=input("Готові зіграти в очко? Пиши тільки yes або no.")
        if question.lower() == 'yes':
            players=int(input("Скілька гравців будуть грати?"))
            while p <= players:
                print(f"{p}-й гравець тягне карти")
                question_2=input("Витягуєш карту?")
                if question_2.lower() == 'yes':
                    a=choice(cards)
                    print(a)
                    leave_cards.append(a)
                    if a[0]=='J':
                        Player.append(2)
                    elif a[0]=='Q':
                        Player.append(3)
                    elif a[0]=='K':
                        Player.append(4)
                    elif a[0]=='A':
                        Player.append(11)
                    elif a[0]=='1':
                        Player.append(10)
                    else:
                        Player.append(int(a[0]))
                    cards.remove(a)
                elif question_2.lower() == 'no':
                    print(f"{p}-й гравець набрав:", sum(Player))
                    points_players.append(sum(Player))
                    Player.clear()
                    p+=1
            for index, c in enumerate(points_players):
                if c>=22:
                    points_players[index]=round(points_players[index]*0)
            if sum(points_players) == 0:
                print("Ви всі в програші")
            else:
                print(f"переміг {points_players.index(max(points_players))+1} гравець")         
            points_players.clear()
            while len(leave_cards) != 0:
                card=leave_cards.pop(0)
                cards.append(card)
            p=1
        elif question.lower() == 'no':
            break
new_ochko()
