from tkinter import *
from tkinter import ttk
from random import randint

window = Tk()
window.title('Конвертер систем счисления')
window.geometry('332x149')
window.resizable(width=False, height=False)

converter = LabelFrame(window, text='Переводчик', font=('Consolas', 10))
calculator = LabelFrame(window, text='Калькулятор', font=('Consolas', 10))
converter.grid()
calculator.grid()

def to_dec(base, number):
    count = 0
    result = 0
    index = 0

    BASE_32 = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'G': 16,
        'H': 17,
        'I': 18,
        'J': 19,
        'K': 20,
        'L': 21,
        'M': 22,
        'N': 23,
        'O': 24,
        'P': 25,
        'Q': 26,
        'R': 27,
        'S': 28,
        'T': 29,
        'U': 30,
        'V': 31,
        'W': 32,
        'X': 33,
        'Y': 34,
        'Z': 35
    }

    number = [item for item in str(number)][::-1]
    for item in number:
        number[index] = BASE_32[item]
        index += 1

    for item in number:
        result += item * base ** count
        count += 1

    return result

def from_dec(base, number):
    result = ''
    
    BASE_32 = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'G',
        17: 'H',
        18: 'I',
        19: 'J',
        20: 'K',
        21: 'L',
        22: 'M',
        23: 'N',
        24: 'O',
        25: 'P',
        26: 'Q',
        27: 'R',
        28: 'S',
        29: 'T',
        30: 'U',
        31: 'V',
        32: 'W',
        33: 'X',
        34: 'Y',
        35: 'Z'
    }

    number = int(number)
    while number >= base:
        result += BASE_32[number % base]
        number = number // base
    result += BASE_32[number]

    result = ''.join([item for item in result][::-1])

    return result

choice = ttk.Combobox(converter, values=['BIN', 'OCT', 'DEC', 'HEX'], width=3, font=('Consolas', 10))
choice.grid(row=0, column=0)
choice.current(randint(0, 3))

source = Entry(converter, font=('Consolas', 10), width=23)
source.grid(row=0, column=1, padx=(2, 2))

main_lbl = Label(converter, text='- Результат конвертации -', font=('Consolas', 10))
main_lbl.grid(row=1, columnspan=3)

bin_lbl = Label(converter, text='BIN:', font=('Consolas', 10))
bin_lbl.grid(row=2, column=0)
bin_etr = Entry(converter, width=38, font=('Consolas', 10))
bin_etr.grid(row=2, column=1, columnspan=2)

oct_lbl = Label(converter, text='OCT:', font=('Consolas', 10))
oct_lbl.grid(row=3, column=0)
oct_etr = Entry(converter, width=38, font=('Consolas', 10))
oct_etr.grid(row=3, column=1, columnspan=2)

dec_lbl = Label(converter, text='DEC:', font=('Consolas', 10))
dec_lbl.grid(row=4, column=0)
dec_etr = Entry(converter, width=38, font=('Consolas', 10))
dec_etr.grid(row=4, column=1, columnspan=2)

hex_lbl = Label(converter, text='HEX:', font=('Consolas', 10))
hex_lbl.grid(row=5, column=0)
hex_etr = Entry(converter, width=38, font=('Consolas', 10))
hex_etr.grid(row=5, column=1, columnspan=2)

def convert():
    global to_dec
    global from_dec

    if choice.get() == 'BIN':
        bin_etr.delete(0, 'end')
        oct_etr.delete(0, 'end')
        dec_etr.delete(0, 'end')
        hex_etr.delete(0, 'end')

        bin_etr.insert(0, source.get())
        oct_etr.insert(0, from_dec(8, to_dec(2, source.get())))
        dec_etr.insert(0, to_dec(2, source.get()))
        hex_etr.insert(0, from_dec(16, to_dec(2, source.get())))

        main_lbl.configure(text='- Результат конвертации -', fg='#000000')

    elif choice.get() == 'OCT':
        bin_etr.delete(0, 'end')
        oct_etr.delete(0, 'end')
        dec_etr.delete(0, 'end')
        hex_etr.delete(0, 'end')

        bin_etr.insert(0, from_dec(2, to_dec(8, source.get())))
        oct_etr.insert(0, source.get())
        dec_etr.insert(0, to_dec(8, source.get()))
        hex_etr.insert(0, from_dec(16, to_dec(8, source.get())))

        main_lbl.configure(text='- Результат конвертации -', fg='#000000')
        
    elif choice.get() == 'DEC':
        bin_etr.delete(0, 'end')
        oct_etr.delete(0, 'end')
        dec_etr.delete(0, 'end')
        hex_etr.delete(0, 'end')

        bin_etr.insert(0, from_dec(2, source.get()))
        oct_etr.insert(0, from_dec(8, source.get()))
        dec_etr.insert(0, source.get())
        hex_etr.insert(0, from_dec(16, source.get()))

        main_lbl.configure(text='- Результат конвертации -', fg='#000000')
        
    elif choice.get() == 'HEX':
        bin_etr.delete(0, 'end')
        oct_etr.delete(0, 'end')
        dec_etr.delete(0, 'end')
        hex_etr.delete(0, 'end')

        bin_etr.insert(0, from_dec(2, to_dec(16, source.get())))
        oct_etr.insert(0, from_dec(8, to_dec(16, source.get())))
        dec_etr.insert(0, to_dec(16, source.get()))
        hex_etr.insert(0, source.get())

        main_lbl.configure(text='- Результат конвертации -', fg='#000000')
        
    else:
        choice.current(randint(0, 3))
        main_lbl.configure(text='- Выберите верную исходную систему -', fg='#FF0000')

convert = Button(converter, text='Преобразовать', command=convert, width=15, font=('Consolas', 10))
convert.grid(row=0, column=2, padx=(0, 1))

window.mainloop()