import tkinter as tk 
from tkinter import messagebox as mb 
def login(): 
    username = 'siplast'
    pasword = '12345'

    if username_entry.get().lower() ==  username  and password_entry.get() ==  pasword:
        print(f'Welcome {username.upper()}')
    else : 
        print(f'Login failed, Try again  ')
        mb.showinfo(title="Invalid Login",message='Username or Password is invalid , Try again! ')




window  = tk.Tk() 
window.configure(bg='#042326')
window.geometry('800x600')

window.title('LogIn') 
frame = tk.Frame(bg ='#042326' )

title_lable =  tk.Label(frame,text ='Log In', font=('Arial','30'),fg='#00E3CC',bg='#042326') 
username_label = tk.Label(frame,text = "Username",font=('Arial','16'),fg='#ffffff',bg='#042326')
username_entry = tk.Entry(frame) 
password_label = tk.Label(frame,text = "Password",font=('Arial','16'),fg='#ffffff',bg='#042326' )
password_entry = tk.Entry(frame,show='*') 
Login_bt = tk.Button(frame, text='Login', font=('Arial','16'), bg='#107361',fg = '#ffffff',command=login   )



title_lable.grid(row=0,column=0,columnspan=2,sticky='news',pady=40)
username_label.grid(row =1, column =0)
username_entry.grid(row =1, column =1,pady=15)
password_label.grid(row= 2 ,column=0,pady =15)
password_entry.grid(row=2,  column = 1)
Login_bt.grid(row=3,column=0, columnspan=3,pady= 20)


frame.pack()

window.mainloop()