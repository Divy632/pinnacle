import tkinter as tk
import math

def calculate():
    try:
        result = eval(entry.get())  # Evaluates the expression in the entry
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0,tk.END)

def cut():
    current_expr = entry.get() 
    entry.delete(len(current_expr) - 1, tk.END)

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

#MAIN PROGRAM

root=tk.Tk()
root.title("MY BASIC CALCULATOR")
entry=tk.Entry(root,width=20,font=("Times New Roman",24),borderwidth=4,justify="right",relief="solid")
entry.grid(row=0,column=0,columnspan=4)
buttons=[("7",1,0),("8",1,1),("9",1,2),("/",1,3),
         ("6",2,0),("5",2,1),("4",2,2),("-",2,3),
         ("1",3,0),("2",3,1),("3",3,2),("*",3,3),
         ("0",4,0),(".",4,1),("+",4,2),("=",4,3),]
for (text,row,col) in buttons:
    if(text=="="):
        button=tk.Button(root,text=text,width=5, height=2,font=("Arial",15),command=calculate)
    else:
        button=tk.Button(root,text=text,width=5,height=2,font=("Arial",15),command=lambda value=text: click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", width=5, font=("Arial",15),height=2,command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
cut_button=tk.Button(root,text="<-", width=5, height=2,font=("Arial",15),command=cut)
cut_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()



