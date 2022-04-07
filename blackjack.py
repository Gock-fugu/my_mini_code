from random import choice
cards=['2♠️', '3♠️', '4♠️', '5♠️', '6♠️', '7♠️', '8♠️', '9♠️', '10♠️', 'J♠️', 'Q♠️', 'K♠️', 'A♠️', '2♥️', '3♥️', '4♥️', '5♥️', '6♥️', '7♥️', '8♥️', '9♥️', '10♥️', 'J♥️', 'Q♥️', 'K♥️', 'A♥️', '2♣️', '3♣️', '4♣️', '5♣️', '6♣️', '7♣️', '8♣️', '9♣️', '10♣️', 'J♣️', 'Q♣️', 'K♣️', 'A♣️', '2♦️', '3♦️', '4♦️', '5♦️', '6♦️', '7♦️', '8♦️', '9♦️', '10♦️', 'J♦️', 'Q♦️', 'K♦️', 'A♦️',]
leave_cards=[]
first_player=[]
points_players=[]
def new_ochko():
    p=1
    while True:
        question=input("Готові зіграти в очко? Пиши тільки так або ні.")
        if question.lower() == 'так':
            players=int(input("Скілька гравців будуть грати?"))
            while p <= players:
                print(f"{p}-й гравець тягне карти")
                question_2=input("Витягуєш карту?")
                if question_2.lower() == 'так':
                    a=choice(cards)
                    print(a)
                    if a == '2♠️' or a == '2♥️' or a == '2♣️' or a == '2♦️':
                        first_player.append(2)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '3♠️' or a == '3♥️' or a == '3♣️' or a == '3♦️':
                        first_player.append(3)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '4♠️' or a == '4♥️' or a == '4♣️' or a == '4♦️':
                        first_player.append(4)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '5♠️' or a == '5♥️' or a == '5♣️' or a == '5♦️':
                        first_player.append(5)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '6♠️' or a == '6♥️' or a == '6♣️' or a == '6♦️':
                        first_player.append(6)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '7♠️' or a == '7♥️' or a == '7♣️' or a == '7♦️':
                        first_player.append(7)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '8♠️' or a == '8♥️' or a == '8♣️' or a == '8♦️':
                        first_player.append(8)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '9♠️' or a == '9♥️' or a == '9♣️' or a == '9♦️':
                        first_player.append(9)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == '10♠️' or a == '10♥️' or a == '10♣️' or a == '10♦️':
                        first_player.append(10)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == 'J♠️' or a == 'J♥️' or a == 'J♣️' or a == 'J♦️':
                        first_player.append(2)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == 'Q♠️' or a == 'Q♥️' or a == 'Q♣️' or a == 'Q♦️':
                        first_player.append(3)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == 'K♠️' or a == 'K♥️' or a == 'K♣️' or a == 'K♦️':
                        first_player.append(4)
                        leave_cards.append(a)
                        cards.remove(a)
                    elif a == 'A♠️' or a == 'A♥️' or a == 'A♣️' or a == 'A♦️':
                        first_player.append(11)
                        leave_cards.append(a)
                        cards.remove(a)
                elif question_2.lower() == 'ні':
                    print(f"{p}-й гравець набрав:", sum(first_player))
                    points_players.append(sum(first_player))
                    while len(first_player) != 0:
                        del first_player[0]
                    p+=1
            for index, c in enumerate(points_players):
                if c>=22:
                    points_players[index]=round(points_players[index]*0)
            if sum(points_players) == 0:
                print("Ви всі в програші")
            else:
                win=points_players.index(max(points_players))
                print(f"переміг {win+1} гравець")         
                
                    
                    
            while len(points_players) !=0:
                del points_players[0]
            while len(leave_cards) != 0:
                card=leave_cards.pop(0)
                cards.append(card)
            p=1
        elif question.lower() == 'ні':
            break
new_ochko()