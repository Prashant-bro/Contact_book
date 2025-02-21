import tkinter as tk
from tkinter import messagebox
import mysql.connector as m

# Connect to MySQL database
db = m.connect(host="localhost", user="root", passwd="CODER", database="ContactBook", charset="latin1")
k = db.cursor()

# Initialize main window
win = tk.Tk()
win.geometry("500x500") 
win.title("Contact book")
win.configure(bg="sky blue")
l1 = tk.Label(win, text="Contact Book", font=("Arial", 25, "bold"), bg="sky blue")
l1.pack(pady=20)

# Search Section
l2 = tk.Label(win, text="Enter Name:", font=("Arial", 15), bg="sky blue")
l2.pack(pady=5)

e1 = tk.Entry(win, font=("Arial", 15), width=30)  
e1.pack(pady=5)

# Search Button
def ser():
    l = e1.get()
    query = f"SELECT * FROM contacts WHERE name LIKE '{l}%'"
    k.execute(query)
    o = k.fetchall()
    r_str = "\n".join([str(row) for row in o]) if o else "No results found"
    l3.config(text=r_str)

b1 = tk.Button(win, text="SEARCH", font=("Arial", 15), command=ser, bg="lightgray")
b1.pack(pady=10)

# Search Result Label
l3 = tk.Label(win, text="RESULT", font=("Arial", 15, "bold"), bg="sky blue")
l3.pack(pady=10)

# Display all contacts
k.execute("SELECT name, phone FROM contacts;")
o = k.fetchall()
r_str1 = "\n".join([str(row) for row in o]) if o else "No contacts available"

l4 = tk.Label(win, text=r_str1, font=("Arial", 12), bg="blue", justify="left")
l4.pack(pady=10)

# Function for adding new contact
def mni():
    mn_win = tk.Toplevel()
    mn_win.geometry("400x400")
    mn_win.title("Add Contact")
    mn_win.configure(bg="lightblue")

    tk.Label(mn_win, text="NAME:", font=("Arial", 15), bg="lightblue").pack(pady=5)
    p1 = tk.Entry(mn_win, font=("Arial", 15), width=25)
    p1.pack(pady=5)

    tk.Label(mn_win, text="PHONE NO:", font=("Arial", 15), bg="lightblue").pack(pady=5)
    p2 = tk.Entry(mn_win, font=("Arial", 15), width=25)
    p2.pack(pady=5)

    tk.Label(mn_win, text="EMAIL:", font=("Arial", 15), bg="lightblue").pack(pady=5)
    p3 = tk.Entry(mn_win, font=("Arial", 15), width=25)
    p3.pack(pady=5)

    tk.Label(mn_win, text="ADDRESS:", font=("Arial", 15), bg="lightblue").pack(pady=5)
    p4 = tk.Entry(mn_win, font=("Arial", 15), width=25)
    p4.pack(pady=5)

    def info():
        name, phone, email, address = p1.get(), p2.get(), p3.get(), p4.get()
        if name and phone:
            k.execute("INSERT INTO contacts (name, phone, email, address) VALUES (%s,%s,%s,%s)",
                      (name, phone, email, address))
            db.commit()
            messagebox.showinfo("Success", "Contact Added Successfully!")
        else:
            messagebox.showwarning("Error", "Name and Phone are required!")

    tk.Button(mn_win, text="SUBMIT", font=("Arial", 15), command=info, bg="green", fg="white").pack(pady=10)

    def cle_en():
        p1.delete(0, tk.END)
        p2.delete(0, tk.END)
        p3.delete(0, tk.END)
        p4.delete(0, tk.END)

    tk.Button(mn_win, text="CLEAR", font=("Arial", 15), command=cle_en, bg="orange").pack(pady=5)
    tk.Button(mn_win, text="DONE", font=("Arial", 15), command=mn_win.destroy, bg="red", fg="white").pack(pady=5)

# Add Contact Button
tk.Button(win, text="ADD CONTACT", font=("Arial", 15), command=mni, bg="blue", fg="white").pack(pady=10)

# Function to Update Contact
def mni_win():
    up_win = tk.Toplevel()
    up_win.geometry("400x300")
    up_win.title("Update Contact")
    up_win.configure(bg="lightblue")

    tk.Label(up_win, text="Enter Name to Update:", font=("Arial", 15), bg="lightblue").pack(pady=5)
    p12 = tk.Entry(up_win, font=("Arial", 15), width=25)
    p12.pack(pady=5)

    tk.Label(up_win, text="New Phone:", font=("Arial", 15), bg="lightblue").pack(pady=5)
    p13 = tk.Entry(up_win, font=("Arial", 15), width=25)
    p13.pack(pady=5)

    def ap_up():
        name, phone = p12.get(), p13.get()
        if name and phone:
            k.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
            db.commit()
            messagebox.showinfo("Updated", "Contact Updated Successfully!")
        else:
            messagebox.showwarning("Error", "Both fields are required!")

    tk.Button(up_win, text="UPDATE", font=("Arial", 15), command=ap_up, bg="green", fg="white").pack(pady=10)
    tk.Button(up_win, text="CLOSE", font=("Arial", 15), command=up_win.destroy, bg="red", fg="white").pack(pady=5)

# Update Contact Button
tk.Button(win, text="UPDATE CONTACT", font=("Arial", 15), command=mni_win, bg="purple", fg="white").pack(pady=5)



#Delete button
def del_1():
    del_win=tk.Toplevel()
    del_win.geometry("400x400")
    del_win.title("Delete Box")

    tk.Label(del_win,text="Enter the name to delete",font=("Arial",15)).pack()
    e4 = tk.Entry(del_win, font=("Arial", 15))
    e4.pack(pady=10)


    def del_2():
        name = e4.get()
        name=str(name)
        if name:
            k.execute("DELETE FROM contacts WHERE name = %s", (name,))
            db.commit()
            messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully!")
            del_win.destroy()
        else:
            messagebox.showwarning("Error", "Please enter a name to delete!")
    b12=tk.Button(del_win,text="DELETE",font=("Arial",20),command=del_2).pack(pady=10)

    del_win.mainloop()
de12=tk.Button(text="DELETE",font=("Arial",15),command=del_1).pack(pady=12)
# Run Mainloop
win.mainloop()
