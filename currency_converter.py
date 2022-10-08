# Currency Converter Project via Python
"""
Project Structures:
1. Real-time Exchange rates.
2. Import required Libraries.
3. CurrencyConverter Class.
4. UI for CurrencyConverter.
5. perform() method.
6. RestrictNumberOnly() method.
7. Main Function.
"""

# 1. Real-time Exchange rates.
"ExchangeRate-API"

# 2. Import required Libraries.
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# 3. CurrencyConverter Class.
# 3.1 Constructor of class.
class RealTimeCurrencyConverter():  #CapWords for Class.
    def __init__(self,url):
        """
        requests.get(url) load the page in python program.
        .json() convert the page into the json file.
        """
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

# 3.2 Convert() method:
    def convert(self, from_currency, to_currency, amount):
        """
        From_currency: currency from which we want to convert.
        to _currency: target currency to convert.
        Amount: how much amount to convert.
        Lastly returns the converted amount.
        """
        initial_amount = amount 
        # First convert it into USD if it's not in USD,
        # since base currency is USD.
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
    
        # Limiting the precision to 4 d.p.
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

# 4. UI for CurrencyConverter.
class App(tk.Tk):
    def __init__(self, converter):
        """
        converter object use to convert currencies.
        This code will create a window frame.
        """
        tk.Tk.__init__(self)
        self.title("Currency Converter")
        self.currency_converter = converter
        self.geometry("500x200")
        self.resizable(0,0)

        # Label.
        self.intro_label = Label(self, text = ' Welcome to Real-time Currency Convertor ',  fg = 'black', relief = tk.RAISED, borderwidth = 6)
        self.intro_label.config(font = ('Arial 15 bold'))

        self.date_label = Label(self, text = f"1 Malaysian Ringgit equals = {self.currency_converter.convert('MYR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        self.date_label.config(font = ('Arial 12 bold'))

        self.intro_label.place(x = 42.5 , y = 5)
        self.date_label.place(x = 170/2+10, y= 50)

        # Entry box.
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        # restricNumberOnly function restrict user from entering invalid number
        # in amount_field.
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
        
        # Dropdown.
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("MYR") # Default value.
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # Default value.
        
        font = ("Arial 12 bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        
        # Placing.
        self.from_currency_dropdown.place(x = 30, y= 120)
        self.amount_field.place(x = 36, y = 150)
        self.to_currency_dropdown.place(x = 340, y= 120)
        # self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x = 346, y = 150)

        # Convert button.
        # command = self.perform means on click it will call perform().
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Arial 10 bold'))
        self.convert_button.place(x = 225, y = 135)

# 5. perform() method.
    def perform(self,):
        """
        perform() take user input & convert the amount into target currency
        and display it on the converted_amount entry box.
        """
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount= self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)  # Target result up to 2 d.p.
        
        self.converted_amount_field_label.config(text = str(converted_amount))

    # 6. RestrictNumberOnly() method.
    def restrictNumberOnly(self, action, string):
        regex = restrictNumberOnly.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

# 7. Main Function.
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
 
    App(converter)
    mainloop()