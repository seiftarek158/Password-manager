from tkinter import *
from tkinter import messagebox
from  random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def searchPass():
    try:
        with open('passwords.json','r') as file:
            data =json.load(file)
            
            website=website_field.get("1.0",END)[:-1]
            if website in data:
                password=data[website]["password"]
                email=data[website]["email"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                warning=messagebox.showwarning(title="Warning",message=f"There is no password stored for {website} website")


    except FileNotFoundError:
        warning=messagebox.showwarning(title="Warning",message="No file found")
    

    


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePass():
    #delete any old password
    passwordField.delete("1.0",END)

    #generate new password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_list+=[choice(letters) for _ in range(randint(8, 10))]
    password_list+=[choice(symbols) for _ in range(randint(5, 6))]
    password_list+=[choice(numbers) for _ in range(randint(3, 5))]

    shuffle(password_list)
    password = ''.join(password_list)
    passwordField.insert(END,password)

    #copy the password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePass():
    website=website_field.get("1.0",END)
    email=emailField.get("1.0",END)
    password=passwordField.get("1.0",END)
    new_data={
        website[:-1]: {
        "email": email[:-1],
        "password": password[:-1]
    }}
    if len(website)==1 or len(password)==1:
        warning=messagebox.showwarning(title="Warning",message="You left one or more fields empty!")
    else:
        
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}Password: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open('passwords.json','r') as file:
                
                        #read old data
                        data =json.load(file)
                        #update the data
                        data.update(new_data)
                    
            except FileNotFoundError:
                data=new_data
            finally:

                with open('passwords.json','w') as file:
                    #insert the new data
                    json.dump(data,file,indent=4)
                    
                website_field.delete("1.0",END)
                passwordField.delete("1.0",END)
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


c=Canvas(width=200,height=200 )


logoimg= PhotoImage(file="logo.png")

c.create_image(60,100, image=logoimg)
c.grid(row=0, column=1)

website_label=Label(window,text="Website:")
website_label.grid(row=1,column=0)
 
website_field=Text(window,height=1 ,width=20)
website_field.grid(row=1,column=1,sticky='w')
website_field.focus()

emailLabel=Label(window,text="Email/Username: ")
emailLabel.grid(row=2,column=0)
 
emailField=Text(window,height=1 ,width=40)
emailField.insert(END,"johndoe157@gmail.com")
emailField.grid(row=2,column=1)

passwordLabel=Label(window,text="Password:")
passwordLabel.grid(row=3,column=0)
 
passwordField=Text(window,height=1 ,width=20)
passwordField.grid(row=3,column=1,sticky="w")

generate_button= Button(window, text= "Generate Password", command=generatePass ,height=1,width=20)
generate_button.grid(row=3, column=1,sticky="e")

add_button= Button(window, text= "Add", command=savePass ,height=1,width=45)
add_button.grid(row=4, column=1)

search_button= Button(window, text= "Search", command=searchPass ,height=1,width=20)
search_button.grid(row=1, column=1,sticky="e")

window.mainloop()

