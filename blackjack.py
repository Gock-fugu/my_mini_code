import random, itertools, time, sqlite3
Decks=random.sample([''.join(card) for card in itertools.product([x for n in ([str(i) for i in range(2, 11)],['J', 'Q', 'K', 'A']) for x in n], ['♠️', '♣️', '♥️', '♦️'])]*6, 312)
conn = sqlite3.connect('Coins_player.db')
cursor=conn.cursor()
class BlackJack():
    def __init__(self, Player=[], Diler=[], Player_list={}):
        self.Player=Player
        self.Diler=Diler
        self.Player_list=Player_list
    
    def Register(self, player_list=[]):
        global conn, cursor
        while len(player_list) != 5:
            Name = input("Впиши ім'я:")
            if Name.lower() == 'no':
                break
            else:
                cursor.execute("SELECT COUNT(*) FROM Coins WHERE name = ?", (Name,))
                if cursor.fetchone()[0] == 0:
                    cursor.execute("INSERT INTO Coins (name, price) VALUES (?, ?)", (Name, 500)) 
                    conn.commit()
                player_list.append(Name)
        cursor.execute(f"SELECT * FROM Coins WHERE name IN ({', '.join(['?'] * len(player_list))})", player_list)
        rows=cursor.fetchall()
        for row in rows:
            self.Player_list[row[0]]=row[1]
        return self.Player_list
    
    def Play(self):
        self.Register()
        print(self.Player_list)
        for player, coins in self.Player_list.items():
            print(f'Зараз грає {player} і ваша сума {coins}. Мінімальна ставка 25')
            coins -= 25
            Bank=25
            for i in range(2):
                self.Diler.append(Decks.pop(0))
                self.Player.append(Decks.pop(0))
            print(f"{self.Player}\n{self.Diler[0]}")
            while True:
                HIT = input("Hit or Surrender?")
                if HIT.lower() == 'yes':
                    coins -= 25
                    Bank+=25
                    self.Player.append(Decks.pop(0))
                    print(self.Player)

                elif HIT.lower() == 'surrender':    
                    print(f'Ви програли {player}')
                    break
                elif HIT.lower() == 'no':#треба зробити віднімання очків при умові що сума очків більша 21 і наявність туза в рукаві
                    self.Diler.append(Decks.pop(0)) if sum([int(c[0]) if (c[0].isdigit() and int(c[0])>1) else (10 if ('10' in c or 'J' in c or 'Q' in c or 'K' in c) else 11) for i, c in enumerate(self.Diler)]) < 17 else None
                    sum_Players, sum_Dilers = sum([int(c[0]) if (c[0].isdigit() and int(c[0])>1) else (10 if ('10' in c or 'J' in c or 'Q' in c or 'K' in c) else 11) for i, c in enumerate(self.Player)]), sum([int(c[0]) if (c[0].isdigit() and int(c[0])>1) else (10 if ('10' in c or 'J' in c or 'Q' in c or 'K' in c) else 11) for i, c in enumerate(self.Diler)])
                    print(f"{self.Player}, {self.Diler}")
                    Condition=sum_Players>sum_Dilers and sum_Players<22
                    print("Переміг гравець" if Condition==True else "Переміг Дилер")
                    self.Player_list[player]=coins+Bank*2 if Condition==True else coins
                    self.Player.clear(), self.Diler.clear()
                    print(player, self.Player_list[player])
                    cursor.execute(f"UPDATE Coins SET price = {self.Player_list[player]} WHERE name = '{player}'")

                    conn.commit()
                    break
        self.Player_list.clear()

for i in itertools.count():    
    BlackJack().Play()
