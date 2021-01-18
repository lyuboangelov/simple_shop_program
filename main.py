from tkinter import *
from actions import add_product, new_product
import yaml

from accounts_check import account_check


def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()


def login(username, password):
    with open('accounts.yml', 'r') as accounts:
        accounts_list = yaml.full_load(accounts)
        login = account_check(username, password, accounts_list)
    if login:
        logged_in(tk)
    else:
        Label(tk, text="Wrong credentials!").grid(row=6, column=0)


def log_view(tk):
    clear_view(tk)
    Label(tk, text="Enter Credentials", bg='yellow').grid(row=0, column=0, padx=350, pady=10)
    Label(tk, text="Username", bg='yellow').grid(row=1, column=0, padx=350, pady=10)
    username = Entry(tk)
    username.grid(row=2, column=0, padx=350, pady=10)
    Label(tk, text="Password", bg='yellow').grid(row=3, column=0, padx=350, pady=10)
    password = Entry(tk, show="*")
    password.grid(row=4, column=0, padx=350, pady=10)
    Button(tk, text="Login", bg='red', command=lambda: login(username.get(), password.get())).grid(row=5, column=0,
                                                                                                   padx=350, pady=10)


def logged_in(tk):
    clear_view(tk)
    Button(tk, text="Add product", bg='yellow', command=lambda: rend_add_product(tk)).grid(row=0, column=0, padx=350,
                                                                                           pady=20)
    Button(tk, text="Sell Product", bg='yellow', command=lambda: rend_sell_product(tk)).grid(row=1, column=0, padx=350,
                                                                                             pady=20)
    Button(tk, text="Show inventory", bg='yellow', command=lambda: rend_sell_product(tk)).grid(row=3, column=0, padx=350,
                                                                                              pady=20)
    Button(tk, text="Remove Product", bg='yellow', command=lambda: rend_remove_product(tk)).grid(row=2, column=0, padx=350,
                                                                                              pady=20)
    Button(tk, text="Quit", bg='yellow', command=lambda: log_view(tk)).grid(row=4, column=0, padx=350, pady=20)


# def rend_new_product(tk):
#     Label(tk, text="This product is new add:", bg='yellow').grid(row=6, column=0, padx=350, pady=10)
#     Label(tk, text="Barcode", bg='yellow').grid(row=7, column=0, padx=350, pady=10)
#     barcode = Entry(tk)
#     barcode.grid(row=8, column=0)
#     Label(tk, text="Code", bg='yellow').grid(row=9, column=0, padx=350, pady=10)
#     code = Entry(tk)
#     code.grid(row=10, column=0)
#     Label(tk, text="Price", bg='yellow').grid(row=11, column=0, padx=350, pady=10)
#     price = Entry(tk)
#     price.grid(row=12, column=0, padx=350, pady=10)




def rend_add_product(tk):
    clear_view(tk)
    Label(tk, text="ADD PRODUCT", bg='yellow').grid(row=0, column=0, padx=350, pady=10)
    Label(tk, text="Product", bg='yellow').grid(row=1, column=0, padx=350, pady=10)
    product = Entry(tk)
    product.grid(row=2, column=0, padx=350, pady=10)
    Label(tk, text="Quantity", bg='yellow').grid(row=3, column=0, padx=350, pady=10)
    quantity = Entry(tk)
    quantity.grid(row=4, column=0, padx=350, pady=10)
    prod = product.get()
    quant = quantity.get()
    Button(tk, text="ADD", bg='red', command=lambda: add_product(prod, quant)).grid(row=5, column=0,
                                                                                   padx=350, pady=10)

    Label(tk, text="This product is new add:", bg='yellow').grid(row=6, column=0, padx=350, pady=10)
    Label(tk, text="Barcode", bg='yellow').grid(row=7, column=0, padx=350, pady=10)
    barcode = Entry(tk)
    barcode.grid(row=8, column=0)
    Label(tk, text="Code", bg='yellow').grid(row=9, column=0, padx=350, pady=10)
    code = Entry(tk)
    code.grid(row=10, column=0)
    Label(tk, text="Price", bg='yellow').grid(row=11, column=0, padx=350, pady=10)
    price = Entry(tk)
    price.grid(row=12, column=0, padx=350, pady=10)
    bar = barcode.get()
    cod = code.get()
    pri = price.get()
    Button(tk, text="ADD", bg='red', command=lambda: new_product(prod, quant, bar, cod, pri)).grid(row=14, column=0,
                                                                                    padx=350, pady=10)


def rend_sell_product(tk):
    clear_view(tk)


def rend_remove_product(tk):
    clear_view(tk)


def rend_show_incentory(tk):
    clear_view(tk)


tk = Tk()
tk.geometry("800x600")
tk.title('Shop program')
tk.config(bg="gray")
log_view(tk)

tk.mainloop()
