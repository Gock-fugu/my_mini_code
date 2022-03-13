import tkinter as tk
 
 
def fahrenheit_to_celsius():
    """
    Конвертирует значение из градусов по Фаренгейту в градусы
    по Цельсию и выводит результат в ярлык lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
 
 
# Создание окна.
window = tk.Tk()
window.title("Конвертер температуры")
window.resizable(width=False, height=False)
 
# Создание рамки для ввода значения по Фаренгейту через виджет
# однострочного текстового поля вместе с ярлыком.
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
 
# Макет для рамки ввода температуры и ярлыка с символом Фаренгейта
# использует менеджер геометрии .grid().
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
 
# Создание кнопки-конвертера и ярлыка для вывода результата.
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
 
# Настройка макета через менеджер геометрии .grid().
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
 
# Запуск приложения.
window.mainloop()
