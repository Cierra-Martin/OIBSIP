from tkinter import *
import pyperclip
import random
import string
from tkinter import messagebox

root=Tk()
root.title("Password Generator")
root.geometry("400x400")



# Functions
def generate_password():
    try:
        length= int(length_number.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length (an integer).")
        return
    characters= ""
    if lowercase.get():
        characters += string.ascii_lowercase
    if uppercase.get():
        characters += string.ascii_uppercase
    if numbers.get():
        characters += string.digits    
    if special_characters.get():
        characters += string.punctuation
    exclude_chars = exclude_var.get()
    characters = characters.translate(str.maketrans('', '', exclude_chars))  
    if not characters:
        messagebox.showwarning("Error","Password guidlines must be selected.")    
        return
    if length< 6:
        messagebox.showwarning("Password too short","To make a strong password it is recomended to be longer than 5 characters")
        return
    global password
    password= "".join(random.choice(characters)for i in range(length))
    Mylabel= Label(root,text= "Here is your new password " +password).grid(row=8,column=0,columnspan=2)
    



def copy():
    global password
    if password:
        pyperclip.copy(password)
        messagebox.showwarning("Password Copied","Your password has been saved")
    else: messagebox.showwarning("Please generate a password first","No password was found")



# entry boxes
lengthlbl= Label(root, text="How many letters:").grid(row=0, column=0, padx=5, pady=5)
length_number= Entry(root)
length_number.grid(row=1, column=0, padx=5, pady=5)
# Entry for excluding characters
exclude_label = Label(root, text="Exclude Characters:")
exclude_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
exclude_var = StringVar()
exclude_entry = Entry(root, textvariable=exclude_var)
exclude_entry.grid(row=1, column=2, padx=5, pady=5)


# Checkboxes for character sets
lowercase = BooleanVar()
lowercase_checkbox = Checkbutton(root, text="Lowercase", variable=lowercase)
lowercase_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky="w")
lowercase_checkbox.select() 

uppercase = BooleanVar()
uppercase_checkbox = Checkbutton(root, text="Uppercase", variable=uppercase)
uppercase_checkbox.grid(row=3, column=0, padx=5, pady=5, sticky="w")
uppercase_checkbox.select()  

numbers = BooleanVar()
digits_checkbox = Checkbutton(root, text="Numbers", variable= numbers)
digits_checkbox.grid(row=4, column=0, padx=5, pady=5, sticky="w")
digits_checkbox.select()  

special_characters = BooleanVar()
symbols_checkbox = Checkbutton(root, text="Special Characters", variable=special_characters)
symbols_checkbox.grid(row=5, column=0, padx=5, pady=5, sticky="w")


#Buttons
MyButton1= Button(root,text="Copy Password",command= copy)
MyButton1.grid(row=7, column=1, columnspan=2, padx=5, pady=10)
MyButton2= Button(root,text= "Generate Password", command= generate_password)
MyButton2.grid(row=6, column=1, columnspan=2, padx=5,pady=10)


root.mainloop()