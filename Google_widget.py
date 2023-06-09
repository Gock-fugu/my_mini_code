import customtkinter as tk
import tkinter, webbrowser, keyboard, sys, os
tk.set_appearance_mode("dark")  # Modes: system (default), light, dark

app = tk.CTk()  # Вікно програми
app_width = app.winfo_screenwidth() - 200
app_height = app.winfo_screenheight() - 95
app.geometry('200x55+{}+{}'.format(app_width, app_height))  # Розмір і розташування вікна програми
app.overrideredirect(1)
app.attributes('-alpha', 0.7)  # прозорість вікна
f = open("Chrome-links.txt", "r+", encoding="utf-8")

def Open_and_Save_Links(): #відкриває запит і зберігає його в текстовому документі
    webbrowser.open(f"https://www.google.com/search?q={str(entry.get())}") if entry.get()!='' else None
    f = open("Chrome-links.txt", "a+", encoding="utf-8")
    f.write(f"\n{entry.get()}")

def Clean_link(): # Видалення ссилокм з списку і файла 
        selected = link_box.curselection()
        for index in selected[::-1]:
            link_box.delete(index)
        with open("Chrome-links.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("Chrome-links.txt", "w", encoding="utf-8") as f:
            for i, line in enumerate(lines):
                if i not in selected:
                    f.write(line)

entry=tk.CTkEntry(master=app, width=155)
entry.pack()#Поле для введеня

scrollbar = tkinter.Scrollbar(app, orient='vertical')
scrollbar.place(x=180, y=30, height=21)
link_box=tkinter.Listbox(app, yscrollcommand=scrollbar.set, width=25, height=1, bg='grey')
LINK=[i for i in set(f) if i!='']
for link in LINK:
    link_box.insert(tk.END, link)

link_box.pack()
scrollbar.config(command=link_box.yview)

Search_Button = tk.CTkButton(master=app, text="🔍", command=Open_and_Save_Links, width=20, height=5, border_width=1, corner_radius=8)
Search_Button.place(x=1, y=3)#Кнопка пошуку

Clean_link_Button=tk.CTkButton(master=app, text="🗑️", command=Clean_link, width=20, height=5, border_width=1, corner_radius=8, fg_color='grey', hover_color='grey')
Clean_link_Button.place(x=178, y=2)

KILL_Button = tk.CTkButton(master=app, command=app.destroy, width=2, height=2, text="kill", fg_color='red', hover_color='red')
KILL_Button.place(x=1, y=30)#кнопка виходу з програми

def search(): #підтягує запит з списку
    link_box.delete(0, tk.END)
    query = entry.get().lower()
    filtered_items = [item for item in LINK if query in item.lower()]
    for item in filtered_items:
        link_box.insert(tk.END, item)

def COPY(event): #переносить запит з списка в поле для ввода
    entry.delete(0, tkinter.END)
    entry.insert(0, link_box.get(link_box.curselection()))

def reboot(): #перезапуск програми
    python = sys.executable
    os.execl(python, python, * sys.argv)

link_box.bind('<Button-1>', COPY)
keyboard.add_hotkey('ctrl+alt', lambda: reboot())
keyboard.add_hotkey('Enter', lambda: Open_and_Save_Links())
entry.bind('<KeyRelease>', lambda event: search())

app.mainloop()