import pyperclip
import pyshorteners
import webbrowser
from tkinter import *

root = Tk()
root.title("URL Shortener")
root.configure(bg="#49A")

url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

def openurl():
    url_short = url_address.get()
    webbrowser.open(url_short)

# Header
header_label = Label(root, text="My URL Shortener", font=("Arial", 24, "bold"), fg="#333", bg="#49A")
header_label.pack(pady=20)

# Input section
input_frame = Frame(root, bg="#EDEDED")
input_frame.pack(pady=10)

input_label = Label(input_frame, text="Enter your link:", font=("Arial", 14), fg="#333", bg="#EDEDED")
input_label.pack(pady=5)

url_entry = Entry(input_frame, textvariable=url, font=("Arial", 12), width=40)
url_entry.pack(pady=5)

generate_button = Button(input_frame, text="Generate Short URL", command=urlshortener, bg="#49A", fg="white", font=("Arial", 12, "bold"))
generate_button.pack(pady=10)

# Result section
result_frame = Frame(root, bg="#EDEDED")
result_frame.pack(pady=10)

result_label = Label(result_frame, text="Shortened URL:", font=("Arial", 14), fg="#333", bg="#EDEDED")
result_label.pack(pady=5)

short_url_entry = Entry(result_frame, textvariable=url_address, font=("Arial", 12), width=40, state='readonly')
short_url_entry.pack(pady=5)

copy_button = Button(result_frame, text="Copy URL", command=copyurl, bg="#49A", fg="white", font=("Arial", 12, "bold"))
copy_button.pack(pady=10)

open_button = Button(result_frame, text="Open URL", command=openurl, bg="#49A", fg="white", font=("Arial", 12, "bold"))
open_button.pack(pady=10)

# Footer
footer_label = Label(root, text="Developed by PRASHANT KUMAR", font=("Arial", 10), fg="#555", bg="#49A")
footer_label.pack(pady=10)

root.mainloop()