import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("USER PROFILE")
window.geometry("300x650")

frame1 = tk.Frame(bg = "Pink")
frame1.pack()

header = tk.Label(frame1,text = "----User Form----" , bg = "pink")
header.pack(fill = "x")

# Name -

frame2 = tk.Frame(bg = "Pink")
frame2.pack(fill = "x")

label1 = tk.Label(frame2,text = "Enter Your Name" , bg = "pink")
label1.pack(pady = 20)
name = ttk.Entry(frame2)
name.focus()
name.pack()

# gender

frame3 = tk.Frame(bg = "Pink")
frame3.pack(fill = "x")

label2 = tk.Label(frame3,text = "Gender" , bg = "pink")
label2.pack(pady = 20)

Gender_storage = tk.StringVar()

gender_1 = ttk.Radiobutton(frame3,text = "Male" , value = "Male" , variable = Gender_storage)
gender_2 = ttk.Radiobutton(frame3,text = "Female" , value = "Female" , variable = Gender_storage)
gender_1.pack(side = "left" , padx = 70)
gender_2.pack(side = "left")

# course --

frame4 = tk.Frame(bg = "Pink")
frame4.pack(fill = "x")

label3 = tk.Label(frame4,text = "Select course" , bg = "pink")
label3.pack(pady = 20)

course_storage = tk.StringVar()

course = ttk.Combobox(frame4,values = ("Python" , "Java" , "C++" , "R" , "Html" , "DSA") , textvariable = course_storage)
course["state"] = "readonly"
course.pack()

# Experience ----

frame5 = tk.Frame(bg = "Pink")
frame5.pack(fill = "x")

label4  = tk.Label(frame5,text = "Experience " , bg = "pink")
label4.pack(pady = 20)

experience_store = tk.StringVar()

experience = ttk.Combobox(frame5,values = ("Beginner" , "Intermediate" , "Advanced")  , textvariable = experience_store )
experience["state"] = "readonly"
experience.pack()

# terms

frame6 = tk.Frame(bg = "Pink")
frame6.pack()

condition_storage = tk.IntVar()

conditions = tk.Checkbutton(frame6,text = "Agree Terms & Conditions" , variable = condition_storage , bg = "pink")
conditions.pack(pady = 30)

# def

def submit():

    if name.get() == "" :

        result.config(text = "Enter Your Name")

    elif Gender_storage.get() == "":

        result.config( text = "Enter Your Gender")

    elif course_storage.get() == "":

        result.config(text = "Select Your Course")

    elif experience_store.get() == "" :

        result.config(text = "Select Your Experience")

    elif condition_storage.get() == 0 :

        result.config(text = "Accept Terms & Conditions")

    else :

        result.config(text = f"NAME - {name.get().upper()} \nGENDER - {Gender_storage.get()} "
                             f"\nCOURSE - {course_storage.get()} \nExperience - {experience_store.get()}")

# reset

def reset():

    name.delete(0,tk.END)

    Gender_storage.set("")

    course_storage.set("")

    experience_store.set("")

    condition_storage.set(0)




# Button

button = tk.Button(text = "Submit" , command = submit ,bg = "Pink")
button.pack(pady = 20)

#button2

reset_button = tk.Button(text = "Reset" , command  = reset , bg = "Pink")
reset_button.pack(pady = 20)

result = tk.Label(text = "" , bg = "Pink")
result.pack()

window.config(bg = "Pink")
window.mainloop()


