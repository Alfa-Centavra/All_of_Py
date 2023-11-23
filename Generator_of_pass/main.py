import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import customtkinter as ctk

import passw


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('460x370')
        self.title('Генератор пароля')
        self.resizable(False, False)

        self.pass_frame = ctk.CTkFrame(master=self, fg_color='transparent')
        self.pass_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky='nsew')

        self.pass_entry = ctk.CTkEntry(master=self.pass_frame, width=300)
        self.pass_entry.grid(row=0, column=0, padx=(0, 20), pady=(20, 20))

        self.btn_gen = ctk.CTkButton(master=self.pass_frame, text='Generate', width=100,
                                     command=self.pass_set)
        self.btn_gen.grid(row=0, column=1)

        self.set_frame = ctk.CTkFrame(master=self)
        self.set_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

        self.pass_lenght_sld = ctk.CTkSlider(master=self.set_frame,
                                             from_=0, to=50, number_of_steps=50,
                                             command=self.sld_event)
        self.pass_lenght_sld.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky='ew')
        self.pass_lenght_entry = ctk.CTkEntry(master=self.set_frame, width=50)
        self.pass_lenght_entry.grid(row=1, column=3, padx=(20, 10), sticky='we')

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = ctk.CTkCheckBox(master=self.set_frame, text='0-9', variable=self.cb_digits_var,
                                         onvalue=digits, offvalue='')
        self.cb_digits.grid(row=2, column=0, padx=5, pady=10)

        self.cb_uppercase_var = tkinter.StringVar()
        self.cb_uppercase = ctk.CTkCheckBox(master=self.set_frame, text='A-Z', variable=self.cb_uppercase_var,
                                            onvalue=ascii_uppercase, offvalue='')
        self.cb_uppercase.grid(row=2, column=1, padx=5, pady=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = ctk.CTkCheckBox(master=self.set_frame, text='a-z', variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue='')
        self.cb_lower.grid(row=2, column=2, padx=5, pady=10)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = ctk.CTkCheckBox(master=self.set_frame, text='!@#$', variable=self.cb_symbol_var,
                                         onvalue=punctuation, offvalue='')
        self.cb_symbol.grid(row=2, column=3)

        self.pass_lenght_sld.set(12)
        self.pass_lenght_entry.insert(0, 12)

    def sld_event(self, value):
        self.pass_lenght_entry.delete(0, 'end')
        self.pass_lenght_entry.insert(0, int(value))

    def get_char(self):
        chars = ''.join(self.cb_digits_var.get() + self.cb_uppercase_var.get() +
                        self.cb_lower_var.get() + self.cb_symbol_var.get())
        return chars

    def pass_set(self):
        self.pass_entry.delete(0, 'end')
        self.pass_entry.insert(0, passw.create_pass(length=int(self.pass_lenght_sld.get()),
                                                    characters=self.get_char()))

    def get_characters(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
