import tkinter
from tkinter import messagebox


def calculate():
    try:
        kg = int(weight_t.get())
        m = int(height_t.get()) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)

        if bmi < 18.5:
            messagebox.showinfo('Вывод ИМТ', f'ИМТ = {bmi} - У вас недостаточный вес')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('Вывод ИМТ', f'ИМТ = {bmi} - У вас нормальный вес')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('Вывод ИМТ', f'ИМТ = {bmi} - У вас избыточный вес')
        else:
            messagebox.showinfo('Вывод ИМТ', f'ИМТ = {bmi} - У вас ожирение')
    except:
        messagebox.showinfo('Вывод ИМТ', 'Поля необходимо заполнить корректно')
    return


root = tkinter.Tk()
root.title('Индекс массы тела')
root.geometry('400x150')
root['bg'] = 'lightblue'

label = tkinter.Label(text='Для расчёта индекса массы тела необходимо ввести ваш рост и вес')
label['bg'] = 'lightblue'
label.pack()

frame = tkinter.Frame(
    padx=10,
    pady=10,
)
frame['bg'] = 'lightblue'
frame.pack(expand=True)

height_l = tkinter.Label(
    frame,
    text="Введите свой рост (в см)",
)
height_l['bg'] = 'lightblue'
height_l.grid(row=3, column=1)

weight_l = tkinter.Label(
    frame,
    text="Введите свой вес (в кг)"
)
weight_l['bg'] = 'lightblue'
weight_l.grid(row=5, column=1)

height_t = tkinter.Entry(frame)
height_t.grid(row=3, column=2)

weight_t = tkinter.Entry(frame)
weight_t.grid(row=5, column=2)

cal_btn = tkinter.Button(
    frame,
    text="Рассчитать ИМТ"
)
cal_btn.grid(row=6, column=2, pady=5)

cal_btn = tkinter.Button(
    frame,
    text='Рассчитать ИМТ',
    command=calculate
)

cal_btn.grid(row=6, column=2)

root.mainloop()
