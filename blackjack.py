import random, itertools, time, sqlite3
Decks=random.sample([''.join(card) for card in itertools.product([x for n in ([str(i) for i in range(2, 11)],['J', 'Q', 'K', 'A']) for x in n], ['♠️', '♣️', '♥️', '♦️'])]*6, 312)

class BlackJack():
    def __init__(self, Player=[], Diler=[]):
        self.Player=Player
        self.Diler=Diler
    
    def REGISTER(self, Player_list=None):
        if Player_list is None:
            Player_list = []
        conn = sqlite3.connect('Coins_player.db')
        cursor=conn.cursor()
        while len(Player_list)!=5:
            Name=input("Впиши ім'я:")
            if Name.lower()=='no':
                break
            else:
                cursor.execute("SELECT COUNT(*) FROM Coins WHERE name = ?", (Name,))
                if cursor.fetchone()[0] == 0:
                    cursor.execute("INSERT INTO Coins (name, price) VALUES (?, ?)", (Name, 500)) 
                    conn.commit()
                Player_list.update(Name)
        conn.close()
        return Player_list

    def Play(self):
        Player_list=self.REGISTER()
        print(Player_list)
        for player in Player_list:
            print(f'Зараз грає {player}')
            for i in range(2):
                self.Diler.append(Decks.pop(0))
                self.Player.append(Decks.pop(0))
            print(f"{self.Player}\n{self.Diler[0]}")
            while True:
                HIT = input("Hit?")
                if HIT.lower() == 'yes':
                    self.Player.append(Decks.pop(0))
                    print(self.Player)
                    
                elif HIT.lower() == 'no':#треба зробити віднімання очків при умові що сума очків більша 21 і наявність туза в рукаві
                    self.Diler.append(Decks.pop(0)) if sum([int(c[0]) if (c[0].isdigit() and int(c[0])>1) else (10 if ('10' in c or 'J' in c or 'Q' in c or 'K' in c) else 11) for i, c in enumerate(self.Diler)]) < 17 else None
                    print(f"{self.Player}, {self.Diler}\n {sum([int(c[0]) if (c[0].isdigit() and int(c[0])>1) else (10 if ('10' in c or 'J' in c or 'Q' in c or 'K' in c) else 11) for i, c in enumerate(self.Player)])}, {sum([int(c[0]) if (c[0].isdigit() and int(c[0])>1) else (10 if ('10' in c or 'J' in c or 'Q' in c or 'K' in c) else 11) for i, c in enumerate(self.Diler)])}")
                    time.sleep(2)
                    self.Player.clear(), self.Diler.clear()
                    break
        Player_list.clear()

for i in range(1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_0000):    
    BlackJack().Play()
