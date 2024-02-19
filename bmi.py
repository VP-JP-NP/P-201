from tkinter import *
window=Tk()

# add widgets here


window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_simpleinterest():
    principle = int(principle_entry.get())
    rate = int(rate_entry.get())
    time = int(time_entry.get())
    sinterest = (principle*rate*time)/100
    sinterest = round(sinterest, 1)
    name = username.get()
    result_label.destroy()

    output_message = Label(result_frame, text = sinterest, bg = "lightcyan", font = ("Calibri", 12), width = 42)
    output_message.place(x = 20, y = 40)
    output_message.pack()



app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principle_label=Label(window, text="Principle", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principle_label.place(x=20, y=140)

principle_entry=Entry(window, text="", bd=2, width=15)
principle_entry.place(x=150, y=142)

rate_label=Label(window, text="Rate", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=187)

time_label=Label(window, text="Time", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=220)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=220)

calculate_button = Button(window, text="CALCULATE", fg="black", bg="cyan", bd=4, command=calculate_simpleinterest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()
