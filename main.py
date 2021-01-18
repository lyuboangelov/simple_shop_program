from tkinter import *
from mysql_func import *
from actions import *

def clear_view(tk):
        for s in tk.grid_slaves():
            s.destroy()

def login(username, password):
    accounts_list = get_users()
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
    username.grid(row=2, column=1, padx=350, pady=10)
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
    Button(tk, text="Show inventory", bg='yellow', command=lambda: rend_show_incentory(tk)).grid(row=3, column=0, padx=350,
                                                                                              pady=20)
    Button(tk, text="Remove Product", bg='yellow', command=lambda: rend_remove_product(tk)).grid(row=2, column=0, padx=350,
                                                                                              pady=20)
    Button(tk, text="Quit", bg='yellow', command=lambda: log_view(tk)).grid(row=4, column=0, padx=350, pady=20)

def rend_add_product(tk):
    clear_view(tk)
    Label(tk, text="ADD PRODUCT", bg='yellow').grid(row=0, column=0, padx=350, pady=10)
    Label(tk, text="Product", bg='yellow').grid(row=1, column=0, padx=350, pady=10)
    product = Entry(tk)
    product.grid(row=2, column=0, padx=350, pady=10)
    Label(tk, text="Quantity", bg='yellow').grid(row=3, column=0, padx=350, pady=10)
    quantity = Entry(tk)
    quantity.grid(row=4, column=0, padx=350, pady=10)       
    Label(tk, text="Barcode", bg='yellow').grid(row=7, column=0, padx=350, pady=10)
    barcode = Entry(tk)
    barcode.grid(row=8, column=0)    
    Label(tk, text="Price", bg='yellow').grid(row=9, column=0, padx=350, pady=10)
    price = Entry(tk)
    price.grid(row=10, column=0, padx=350, pady=10)    
    Button(tk, text="ADD", bg='red', command=lambda: add_product(product.get(), quantity.get(), barcode.get(), price.get())).grid(row=11, column=0, padx=350, pady=10)
    Button(tk, text="Back", bg='yellow', command=lambda: logged_in(tk)).grid(row=12, column=0, padx=350, pady=20)

def rend_sell_product(tk):
    clear_view(tk)

def rend_remove_product(tk):
    clear_view(tk)
    Label(tk, text="Remove product", bg='yellow').grid(row=0, column=0, padx=350, pady=10)
    Label(tk, text="Product", bg='yellow').grid(row=0, column=1, padx=350, pady=10)
    product = Entry(tk)
    product.grid(row=2, column=0, padx=350, pady=10)
    Button(tk, text="Remove", bg='red', command=lambda: remove_product(product.get())).grid(row=5, column=0,
                                                                                                   padx=350, pady=10)
    Button(tk, text="Back", bg='yellow', command=lambda: logged_in(tk)).grid(row=6, column=0, padx=350, pady=20)                                                                                               

def rend_show_incentory(tk):
    clear_view(tk)
    Button(tk, text="Back", bg='yellow', command=lambda: logged_in(tk)).grid(row=0, column=0, padx=350, pady=20)
    class Table: 
        
        def __init__(self,root):             
             
            for i in range(total_rows): 
                for j in range(total_columns):                    
                    self.e = Entry(root, width=10, fg='blue', 
                                font=('Arial',16,'bold'))                     
                    self.e.grid(row=i, column=j) 
                    self.e.insert(END, lst[i][j])     
    
    lst = get_products()    
    total_rows = len(lst) 
    total_columns = len(lst[0])      
    root = Tk() 
    t = Table(root) 
    root.mainloop()
    
tk = Tk()
tk.geometry("800x600")
tk.title('Shop program')
tk.config(bg="gray")
log_view(tk)
tk.mainloop()