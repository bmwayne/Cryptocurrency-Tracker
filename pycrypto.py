from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My Portfolio App")
pycrypto.iconbitmap("favicon.ico")

def font_colour(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


def my_portfolio():
    api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=5747bb57-156c-4529-a987-ab3fa9ec709a")
    api = json.loads(api_requests.content)

    coins = [
        {
            "symbol":"BTC",
            "coins_owned":2,
            "price_per_coin":3200
        },
        {
            "symbol":"BCH",
            "coins_owned":100,
            "price_per_coin":2.05
        },
        {
            "symbol":"LTC",
            "coins_owned":75,
            "price_per_coin":25
        },
        {
            "symbol":"XMR",
            "coins_owned":10,
            "price_per_coin":40.05
        }
    ]

    total_pl = 0
    total_currentvalue = 0
    total_amountpaid = 0
    coin_row = 1

    for i in range(0,300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_price = coin["coins_owned"] * coin["price_per_coin"]
                current_valueofownedcoins = coin["coins_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coinsowned = pl_per_coin * coin["coins_owned"]
                total_pl = total_pl + total_pl_coinsowned
                total_currentvalue = total_currentvalue + current_valueofownedcoins
                total_amountpaid = total_amountpaid + total_price

                name = Label(pycrypto,text = api["data"][i]["name"], bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                name.grid(row = coin_row, column = 0, sticky = N+S+E+W)

                price = Label(pycrypto,text = "${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                price.grid(row = coin_row, column = 1, sticky = N+S+E+W)

                coinowned = Label(pycrypto,text = coin["coins_owned"], bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                coinowned.grid(row = coin_row, column = 2, sticky = N+S+E+W)

                totalpaid = Label(pycrypto,text = "${0:.2f}".format(total_price), bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                totalpaid.grid(row = coin_row, column = 3, sticky = N+S+E+W)

                currvalue = Label(pycrypto,text = "{0:.2f}".format(current_valueofownedcoins), bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                currvalue.grid(row = coin_row, column = 4, sticky = N+S+E+W)

                plpercoin = Label(pycrypto,text = "${0:.2f}".format(pl_per_coin), bg = "#F3F4F6", fg = font_colour(float("{0:.2f}".format(pl_per_coin))), font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                plpercoin.grid(row = coin_row, column = 5, sticky = N+S+E+W)

                totalplcoin = Label(pycrypto,text = "${0:.2f}".format(total_pl_coinsowned), bg = "#F3F4F6", fg = font_colour(float("{0:.2f}".format(total_pl_coinsowned))), font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
                totalplcoin.grid(row = coin_row, column = 6, sticky = N+S+E+W)

                coin_row = coin_row + 1

    totalpaid = Label(pycrypto,text = "${0:.2f}".format(total_amountpaid), bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
    totalpaid.grid(row = coin_row, column = 3, sticky = N+S+E+W)

    currvalue = Label(pycrypto,text = "{0:.2f}".format(total_currentvalue), bg = "#F3F4F6", fg = "black", font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
    currvalue.grid(row = coin_row, column = 4, sticky = N+S+E+W)

    totalplcoin = Label(pycrypto,text = "${0:.2f}".format(total_pl), bg = "#F3F4F6", fg = font_colour(float("{0:.2f}".format(total_pl))), font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
    totalplcoin.grid(row = coin_row, column = 6, sticky = N+S+E+W)

    api=""

    update = Button(pycrypto,text = "Update", bg = "#142E54", fg = "white",command = my_portfolio, font = "Lato 12 ", borderwidth = 2, relief = "groove", padx = "2", pady = "2")
    update.grid(row = coin_row + 1, column = 6, sticky = N+S+E+W)

name = Label(pycrypto,text = "Coin Name",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
name.grid(row = 0, column = 0, sticky = N+S+E+W)

price = Label(pycrypto,text = "Price",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
price.grid(row = 0, column = 1, sticky = N+S+E+W)

coinsowned = Label(pycrypto,text = "Coins Owned",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
coinsowned.grid(row = 0, column = 2, sticky = N+S+E+W)

totalprice = Label(pycrypto,text = "Total Amount Paid",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
totalprice.grid(row = 0, column = 3, sticky = N+S+E+W)

currvalue = Label(pycrypto,text = "Current Value",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
currvalue.grid(row = 0, column = 4, sticky = N+S+E+W)

plpercoin = Label(pycrypto,text = "P/L Per Coin",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
plpercoin.grid(row = 0, column = 5, sticky = N+S+E+W)

totalpl = Label(pycrypto,text = "Total P/L of Coins",bg = "#142E54", fg = "white", font = "Lato 12 bold", borderwidth = 2, relief = "groove", padx = "5", pady = "5")
totalpl.grid(row = 0, column = 6, sticky = N+S+E+W)

my_portfolio()
pycrypto.mainloop()
print("Program Completed")
