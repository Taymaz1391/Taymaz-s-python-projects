from tkinter import *


root = Tk()
root.resizable(0 , 0)
root.title("ماشين حساب عمو")

def plus ():
    try : 
        e1=float (en1.get())
        e2=float (en2.get())
        ans = e1 + e2
        L.config(text ='Answer : '+str(ans))
    except :
        L.config(text= "invalid")
	
def minus ():
    try :
    	e1=float (en1.get())
    	e2=float (en2.get())
    	ans = e1 - e2
    	L.config(text ='Answer : '+str(ans))
    except :
        L.config(text= "invalid")		
	
def multiple():
    try :
        e1=float (en1.get())
        e2=float (en2.get())
        ans = e1 * e2
        L.config(text ='Answer : '+str(ans))
    except :
        L.config(text= "invalid")	
def divide ():
    try :	
        e1=float (en1.get())
        e2=float (en2.get())
        if e2 == 0 :
                L.config (text ="Can't divide by zero " )
        else :
                ans = e1/e2
                L.config(text ='Answer : '+str(ans))
    except :
                L.config(text= "invalid")	
def quotient():
        try :	
                e1=float (en1.get())
                e2=float (en2.get())
                if e2 == 0 :
                        L.config (text ="Can't divide by zero " )
                else :
                        ans = e1//e2
                        L.config(text ='Answer : '+str(ans))
        except :
                L.config(text= "invalid")	
def remainder():
    try:
        e1=float (en1.get())
        e2=float (en2.get())
        if e2 == 0 :
                L.config (text ="Can't divide by zero " )
        else :
            ans = e1%e2
            L.config(text ='Answer : '+str(ans))
    except :
                 L.config(text= "invalid")	
def color():
		root.config(bg="#415a77")
		LB.config(bg="#778da9")
		btn1.config(bg="#ffb703")
		btn2.config(bg="#ffb703")
		btn3.config(bg="#ffb703")
		btn4.config(bg="#ffb703")
		btn5.config(bg="#ffb703")
		btn6.config(bg="#ffb703")
		L.config(bg="#415a77")
		btn_color.config(bg="#CFAB8D")
def dark_color():
		root.config(bg="#03071e")
		LB.config(bg="#03071e" , fg = "white")
		btn1.config(bg="#6a040f" , fg = "white")
		btn2.config(bg="#6a040f" , fg = "white")
		btn3.config(bg="#6a040f" , fg = "white")
		btn4.config(bg="#6a040f" , fg = "white")
		btn5.config(bg="#6a040f" , fg = "white")
		btn6.config(bg="#6a040f" , fg = "white")
		L.config(bg="#03071e" , fg = "white")
		dark_btn.config(bg = "#6a040f")
		btn_color.config(bg="#6a040f" , fg = "white")


root.config(bg = "#fee440")
LB = Label (root, text = 'Enter numbers : ' , bg = "#fee440" , font = ("Gabriola") )
LB.pack(ipadx=100)
en1 = Entry (root, width =30 , font = ("impact"))
en1.pack(pady=20)
en2 = Entry (root, width =30 , font = ("impact"))
en2.pack(pady=20)
btn1 =Button (root, text ='+', width=5 , command=plus , bg = "#f15bb5", font = ("impact") )
btn1.pack()
btn2 =Button (root, text ='-', width=5, command=minus , bg = "#f15bb5", font = ("impact"))
btn2.pack()
btn3 =Button (root, text ='*', width=5, command=multiple, bg = "#f15bb5", font = ("impact"))
btn3.pack()
btn4 =Button (root, text ='/', width=5, command=divide, bg = "#f15bb5", font = ("impact"))
btn4.pack()
btn5 =Button (root, text ='//', width=5, command=quotient , bg = "#f15bb5", font = ("impact"))
btn5.pack()
btn6 =Button (root, text ='%', width=5, command=remainder , bg = "#f15bb5", font = ("impact"))
btn6.pack()
L = Label (root, text=''  , bg = "#fee440", font = ("impact"))
L.pack(pady=20)
btn_color = Button (root, text ="Change Theme", command =color, font = ("impact"))
btn_color.pack()
dark_btn = Button (root , text = "dark them" , bg = "#03071e" , fg="white" , command = dark_color, font = ("impact"))
dark_btn.pack()
root.mainloop()
