#Data base Tutorial
import sqlite3

conn = sqlite3.connect('Coins_player.db')# Підключення до бази даних (якщо база даних не існує, вона буде автоматично створена)
cursor=conn.cursor()#Курсор для керування базою даних
cursor.execute('''CREATE TABLE IF NOT EXISTS Coins(name TEXT, price INTEGER)''') #execute метод для прописування SQL запитів. А в даному випадку створення таблиці.

#cursor.execute("INSERT INTO Coins (name, price) VALUES (?, ?)", ('Mortal', 500))#Додавання елементів в таблицю
#cursor.execute("DELETE FROM Coins") #Видалення елементів таблиці
#cursor.execute("SELECT * FROM Coins")#Виведення результатів з таблиці.
#conn.commit()#збереження змін


def check_element_exists():
    
    # Введіть назву вашої таблиці, стовпчика і список елементів для перевірки
    elements = ['element1', 'element2', 'element3']

    # Перевірка наявності елементів зі списку
    placeholders = ', '.join(['?'] * len(elements))
    query = f"SELECT * FROM Coins WHERE name IN ({placeholders})"
    cursor.execute(query, elements)
    rows = cursor.fetchall()

    element_exists = len(rows) > 0

    cursor.close()
    conn.close()

    return element_exists

#print(cursor.fetchall())


#conn.close() #Закриття підключення
