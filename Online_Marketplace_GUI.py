import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from functools import partial
from tkinter.ttk import *

df = pd.read_csv('/Users/zohaibzaheer/Desktop/PyStuff/Online_Marketplace/gorcery_list.csv')
products = np.array(df['Item'], dtype=str)
price = np.array(df['Price'], dtype=str)

window = Tk()
window.title("Online Marketplace")
window.geometry("720x350")
headinglbl = Label(window, text="Online Marketplace", font=('helvetica', '30'))
headinglbl.grid(column=1, row=0, pady=20, columnspan=3)

cart = []
quantity = []
totalbill = []


def itemclicked(i):  # what happens when an item is clicked ie adding to cart
    addtocart = tk.Toplevel(padx=25, pady=25)
    product = products[i]
    itemprice = int(price[i])
    itemprompt = ("You've picked ", product)
    promptlbl = Label(addtocart, text="".join(itemprompt))
    promptlbl.grid(column=0, row=0, padx=5, pady=5)
    nitemlbl = Label(addtocart, text="Choose quantity of items to add to cart")
    nitemlbl.grid(column=0, row=1)
    nitems = Spinbox(addtocart, from_=1, to=10, width=5, textvariable='1')
    nitems.grid(column=1, row=1)

    def cancelclicked():
        addtocart.destroy()

    def cartdoneclicked():  # addition to cart array, closing add to cart window
        number = nitems.get()
        if (len(nitems.get())) > 0:  # setting default value cuz spinbox doesn't allow under ttk
            number = nitems.get()
        else:
            number = "1"
        quantity.append(number)
        cart.append(product)
        finalprice = (int(itemprice) * int(number))
        totalbill.append(finalprice)
        addtocart.destroy()
        sucmsg = (number, " item(s) added to cart")
        tk.messagebox.showinfo("Successful", ("".join(sucmsg)))
        vcart = Button(window, text="View Cart", command=vcartclicked)
        vcart.grid(column=1, row=3, pady=5, ipadx=3, ipady=3)

    cartdonebtn = Button(addtocart, text="Done", command=cartdoneclicked)
    cartdonebtn.grid(column=0, row=2, pady=5, ipadx=2, ipady=2)
    cancelbtn = Button(addtocart, text="Cancel", command=cancelclicked)
    cancelbtn.grid(column=1, row=2, pady=5, ipadx=2, ipady=2)


def vcartclicked():  # printing the cart, multiple labels, row and column calculation
    viewcart = tk.Toplevel(padx=100, pady=100)

    for i in range(0, len(cart)):
        iheadlbl = Label(viewcart, text="Items")
        iheadlbl.grid(column=0, row=0, padx=2, pady=2)
        qheadlbl = Label(viewcart, text="Quantity")
        qheadlbl.grid(column=1, row=0, padx=2, pady=2)
        cheadlbl = Label(viewcart, text="Price")
        cheadlbl.grid(column=2, row=0, padx=2, pady=2)
        itemslbl = Label(viewcart, text=cart[i])
        itemslbl.grid(column=0, row=(i + 1), padx=2, pady=2)
        quantitylbl = Label(viewcart, text=quantity[i])
        quantitylbl.grid(column=1, row=(i + 1), padx=2, pady=2)
        costlbl = Label(viewcart, text=totalbill[i])
        costlbl.grid(column=2, row=(i + 1), padx=2, pady=2)
        global total
        total = sum(totalbill)
        theadlbl = Label(viewcart, text="Total")
        theadlbl.grid(column=0, row=(len(cart) + 1), padx=2, pady=4)
        total_lbl = Label(viewcart, text=("AED", total))
        total_lbl.grid(column=2, row=(len(cart) + 1), padx=2, pady=4)
        finalrow = (i + 3)

    def proceedclicked():
        confirm_msg = ("Proceed with payment of AED ", str(total))
        confirm = messagebox.askyesno("Confirmation", ("".join(confirm_msg)))
        if confirm == True:
            viewcart.destroy()
            bill = tk.Toplevel(padx=15, pady=25)
            confirmed_msg = ("Payment succesful. Total: AED ", str(total))
            confirmlbl = Label(bill, text=("".join(confirmed_msg)))
            confirmlbl.grid(column=0, row=0, pady=5)
            for i in range(0, len(cart)):  # printing cart again for final receipt
                iheadlbl = Label(bill, text="Items")
                iheadlbl.grid(column=0, row=2, padx=2, pady=5)
                qheadlbl = Label(bill, text="Quantity")
                qheadlbl.grid(column=1, row=2, padx=2, pady=5)
                cheadlbl = Label(bill, text="Price")
                cheadlbl.grid(column=2, row=2, padx=2, pady=5)
                itemslbl = Label(bill, text=cart[i])
                itemslbl.grid(column=0, row=(i + 3), padx=2, pady=2)
                quantitylbl = Label(bill, text=quantity[i])
                quantitylbl.grid(column=1, row=(i + 3), padx=2, pady=2)
                costlbl = Label(bill, text=totalbill[i])
                costlbl.grid(column=2, row=(i + 3), padx=2, pady=2)
                theadlbl = Label(bill, text="Total")
                theadlbl.grid(column=0, row=(len(cart) + 3), padx=2, pady=4)
                total_lbl = Label(bill, text=("AED", total))
                total_lbl.grid(column=2, row=(len(cart) + 3), padx=2, pady=4)
        elif confirm == False:
            viewcart.destroy()

    def cardclicked():  # card payment options
        account = Radiobutton(viewcart, text="Account", state='disabled')
        account.grid(column=2, row=(finalrow + 4), pady=4, padx=2)
        cprompt = Label(viewcart, text="Enter Card number")
        cprompt.grid(column=0, row=(finalrow + 5), pady=4)
        cardnumber = Entry(viewcart, width=45)
        cardnumber.grid(column=1, row=(finalrow + 5), columnspan=2, pady=4)
        dprompt = Label(viewcart, text="Enter expiry date")
        dprompt.grid(column=0, row=(finalrow + 6))
        date = Combobox(viewcart, values=(list(range(1, 13))), width=4)
        date.grid(column=1, row=(finalrow + 6))
        year = Combobox(viewcart, values=(list(range(20, 40))), width=4)
        year.grid(column=2, row=(finalrow + 6))
        sprompt = Label(viewcart, text="Enter security code")
        sprompt.grid(column=0, row=(finalrow + 7))
        security = Entry(viewcart, width=7)
        security.grid(column=1, row=(finalrow + 7), pady=2)
        proceed = Button(viewcart, text="Proceed", command=proceedclicked)
        proceed.grid(column=1, row=(finalrow + 8), pady=10, ipady=10)

    def accountclicked():
        card = Radiobutton(viewcart, text="Card", state='disabled')
        card.grid(column=1, row=(finalrow + 4), pady=4, padx=2)
        userprompt = Label(viewcart, text="Username:")
        userprompt.grid(column=0, row=(finalrow + 5), pady=4)
        username = Entry(viewcart, width=45)
        username.grid(column=1, row=(finalrow + 5), columnspan=2, pady=4)
        passprompt = Label(viewcart, text="Password:")
        passprompt.grid(column=0, row=(finalrow + 6))
        password = Entry(viewcart, width=45)
        password.grid(column=1, row=(finalrow + 6), columnspan=2, )
        proceed = Button(viewcart, text="Proceed", command=proceedclicked)
        proceed.grid(column=1, row=(finalrow + 8), pady=10, ipady=10)

    def contclicked():  # to close the cart view
        viewcart.destroy()

    def checkoutclicked():  # load payment options and address
        adheadlbl = Label(viewcart, text="SHIPPING ADDRESS")
        adheadlbl.grid(column=1, row=(finalrow + 1))
        stprompt = Label(viewcart, text="Street Name: ")
        stprompt.grid(column=0, row=(finalrow + 2), pady=4, padx=2)
        street = Entry(viewcart, width=45)
        street.grid(column=1, row=(finalrow + 2), pady=4, columnspan=2)
        ciprompt = Label(viewcart, text="City Name: ")
        ciprompt.grid(column=0, row=(finalrow + 3))
        city = Entry(viewcart, width=45)
        city.grid(column=1, row=(finalrow + 3), columnspan=2)
        global address
        address = (street.get() + ", " + city.get())
        p_prompt = Label(viewcart, text="How would you like to pay?")
        p_prompt.grid(column=0, row=(finalrow + 4), pady=4, padx=2)
        card = Radiobutton(viewcart, text="Card", command=cardclicked)
        card.grid(column=1, row=(finalrow + 4), pady=4, padx=2)
        account = Radiobutton(viewcart, text="Account", command=accountclicked)
        account.grid(column=2, row=(finalrow + 4), pady=4, padx=2)

    contbtn = Button(viewcart, text="Continue Shopping", command=contclicked)
    contbtn.grid(column=1, row=finalrow, padx=2, pady=4, ipadx=2, ipady=2)
    checkoutbtn = Button(viewcart, text="Go to Checkout", command=checkoutclicked)
    checkoutbtn.grid(column=2, row=finalrow, padx=2, pady=4, ipadx=2, ipady=2)


def itembuttons():
    aed = "AED"
    text = "Click to add to cart"
    nproducts = len(products)
    for i in range(0, (nproducts)):
        text1 = (products[i], "\n", aed, price[i], "\n", text)
        itembtn = Button(window, text=("".join(text1)), command=partial(itemclicked, i))
        if i < 5:
            itembtn.grid(column=i, row=1, padx=2, pady=2, ipadx=15, ipady=15)
        else:
            itembtn.grid(column=(i - 5), row=2, padx=2, pady=2, ipadx=15, ipady=15)


# -------------------------------------------------main()---------------------------------------------------

itembuttons()

window.mainloop()
