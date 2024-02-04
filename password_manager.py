from tkinter import *
from tkinter import messagebox
import random
import json

# -------------------------- SEARCH EXISTING WEBSITE -----------------------------#
def find_password():
    
    web = entry_w.get()
    
    try:
        with open("date.json","r") as filee:
        #reading old data
            data = json.load(filee) 
            
            if web in data:
                    
                gmail = data[web]["email"]
                passw = data[web]["password"]                

                messagebox.showinfo(web, f"Email: {gmail}\nPassword: {passw}")            
                
            else:
                
                messagebox.showinfo("Warning","No details for the website exists.")
                    
    except:
            
        messagebox.showinfo("Warning","No Data File Found")
            
        
                
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]    

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    
    password = ''.join(password_list)

    
    entry_p.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_w.get()
    user = entry_e.get()
    passe = entry_p.get()
    new_data = {
        web: {
            "email": user,
            "password": passe,
        }
    }
    
    if len(web) == 0 or len(user) == 0 or len(passe) == 0:
        
        messagebox.showinfo("Oops", "Please don't leave any of the fields empty")
        
    else:
        
        try:
                   
            with open("date.json","r") as filee:
                #reading old data
                data = json.load(filee) 
        
        except:
        
            with open("date.json","w") as filee:
                #saving update file
                json.dump(new_data, filee, indent=4)

        else:
            
            #updating oldd data with new data
            data.update(new_data)
            with open("date.json","w") as filee:
                #saving updated file
                json.dump(new_data, filee, indent=4)
        
        finally:
        
            entry_w.delete(0, END)
            entry_p.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

canvas = Canvas(width=200, height=200)
my_pass = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= my_pass)
canvas.grid(column= 1, row=0)


#Label
website = Label(text="Website:")
website.config(padx=0, pady=10)
website.grid(column= 0, row=1)

email = Label(text = "Email/Username:")
email.grid(column= 0, row=2)
email.config(padx=0, pady=10)

password = Label(text= "Password:")
password.grid(column=0, row=3)
password.config(padx=0, pady=10)


#Entries
entry_w = Entry(width=25)
entry_w.grid(column= 1, row= 1)
entry_w.focus()


entry_e = Entry(width=40)
entry_e.grid(column= 1, row= 2, columnspan= 2) 
entry_e.insert(0, "invernojoana@gmail.com")


entry_p = Entry(width= 25)
entry_p.grid(column= 1, row= 3)

#Buttons
button_add = Button(text="Add", width= 36, command= save)
button_add.grid(column= 1, row= 4, columnspan= 2)

generate = Button(text= "New Password", command= new)
generate.grid(column=2, row=3)

proc = Button(text= "Search", command=find_password)
proc.grid(column=2, row=1)






window.mainloop()
