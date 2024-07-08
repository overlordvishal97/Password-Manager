from tkinter import *
from tkinter import messagebox
from random import shuffle,randint,choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generating_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    passwords = "".join(password_list)
    #writes the created password to password input
    password_entry.insert(0,passwords)
    #copys the password to the clipboard
    pyperclip.copy(passwords)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """ Creates a text file with data you have entered into the input and clears the input"""
    web = website_entry.get()
    mail = email_entry.get()
    secret_pass = password_entry.get()

    #validation of the text
    if len(web) == 0 or len(secret_pass) == 0:
        messagebox.showinfo(title="Oops",message="Don't leave any fields empty!")
    else:
        # after validation this code is run
        is_ok = messagebox.askokcancel(title=web,message=f"Details are: \nEmail:{mail}"
                                                 f" \nPassword:{secret_pass} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{web} | {mail} | {secret_pass}\n")
            #clears the input
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
#create some space between the image and window
window.config(padx=50,pady=50)
#Title of the window
window.title("Password Manager")

#create window size
canvas = Canvas(width=200,height=200)
#read image
lock_img = PhotoImage(file="logo.png")
#add image to canvas
canvas.create_image(100,100,image=lock_img)
# canvas.grid(column=0,row=0)
canvas.grid(column = 1,row = 0)

#labels
website = Label(text="Website:")
email = Label(text="Email/Username:")
password = Label(text="Password:")
#assiging positions of labels in screens
website.grid(column = 0,row= 1)
email.grid(column = 0,row = 2)
password.grid(column = 0,row = 3)

#buttons
generate_password = Button(text="Generate Password",command=generating_password)
add = Button(text="Add",width=36,command=save)
#assinging buttons on the screen
generate_password.grid(column = 2,row = 3)
add.grid(column= 1,row = 4,columnspan= 2)

#input
website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0,"dwaramvishal@duck.com")
password_entry = Entry(width=21, show="*")
#assinging input on the screen
website_entry.grid(column=1,row=1,columnspan = 2)
email_entry.grid(column=1,row = 2,columnspan = 2)
password_entry.grid(column=1,row = 3)

window.mainloop()

