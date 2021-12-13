from functions import ticker_to_sec
import pyperclip

# asks users to provide input parameters
form_type= input("Form type to search [e.g., S-1, 10-K]: ")
datea= input("search after the date [yyyymmdd format]: ")
dateb= input("search before the date [yyyymmdd format]: ")

# initialize ticker with dummy
ticker="dummy"

# stop if ticker includes nothing
while ticker!="":

    # get ticker
    ticker= input("Type ticker: ")

    # get url
    url= ticker_to_sec(ticker) + f"&type={form_type}" + f"&dateb={dateb}" + f"&datea={datea}"

    # print url
    print(url)

    # save in clipboard
    try:
        pyperclip.copy(url)
    except:
        None
