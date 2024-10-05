import tkinter as tk

kalk=tk.Tk()
kalk.geometry("300x377")
kalk.title("KALKULATOR")
kalk.resizable(True,False)

vpis=tk.Entry(kalk,font=("Calibri",20), width=30, justify="center")
vpis.grid(columnspan=4,sticky="NSEW")

def zapis(pisi):
    vpis.insert(tk.END,pisi)
    
    

def brisaje():
    vpis.delete(0,tk.END)

def izracun():
    zapis1=vpis.get() 
    try:
        rezultat=str(eval(zapis1))
        vpis.delete(0,tk.END)
        vpis.insert(tk.END,rezultat)
    except : 
         vpis.delete(0,tk.END)
         
kalk.grid_columnconfigure(0,weight=1)  
kalk.grid_columnconfigure(1,weight=1)  
kalk.grid_columnconfigure(2,weight=1)  
kalk.grid_columnconfigure(3,weight=1)  
kalk.grid_columnconfigure(4,weight=1)  



gumb1= tk.Button(kalk, text="1",background="lightgreen" , height=4,width=7,command=lambda:zapis("1"))
gumb1.grid(row=1,column=0,sticky="NSEW")

gumb2= tk.Button(kalk, text="2",background="lightgreen" , height=4,width=7,command=lambda:zapis("2"))
gumb2.grid(row=1,column=1,sticky="NSEW")

gumb3= tk.Button(kalk, text="3",background="lightgreen" , height=4,width=7,command=lambda:zapis("3"))
gumb3.grid(row=1,column=2,sticky="NSEW")

gumb4= tk.Button(kalk, text="4",background="lightgreen" , height=4,width=7,command=lambda:zapis("4"))
gumb4.grid(row=2,column=0,sticky="NSEW")

gumb5= tk.Button(kalk, text="5",background="lightgreen" ,height=4,width=7,command=lambda:zapis("5"))
gumb5.grid(row=2,column=1,sticky="NSEW")

gumb6= tk.Button(kalk, text="6",background="lightgreen" ,height=4,width=7,command=lambda:zapis("6"))
gumb6.grid(row=2,column=2,sticky="NSEW")

gumb7= tk.Button(kalk, text="7",background="lightgreen" ,height=4,width=7,command=lambda:zapis("7"))
gumb7.grid(row=3,column=0,sticky="NSEW")

gumb8= tk.Button(kalk, text="8",background="lightgreen" ,height=4,width=7,command=lambda:zapis("8"))
gumb8.grid(row=3,column=1,sticky="NSEW")

gumb9= tk.Button(kalk, text="9",background="lightgreen" ,height=4,width=7,command=lambda:zapis("9"))
gumb9.grid(row=3,column=2,sticky="NSEW")

gumb0= tk.Button(kalk, text=".",background="lightgreen" ,height=4,width=7,command=lambda:zapis("."))
gumb0.grid(row=4,column=0,sticky="NSEW")

gumb_pika= tk.Button(kalk, text="0",background="lightgreen" ,height=4,width=7,command=lambda:zapis("0"))
gumb_pika.grid(row=4,column=1,sticky="NSEW")

gumbenako= tk.Button(kalk, text="=",height=4,width=7,bg="gold3",command=izracun)
gumbenako.grid(row=4,column=2,sticky="NSEW")

gumb_plus= tk.Button(kalk, text="+",height=4,width=7,bg="lightblue",command=lambda:zapis("+"))
gumb_plus.grid(row=1,column=3,sticky="NSEW")

gumb_minus= tk.Button(kalk, text="-",height=4,width=7,bg="lightblue",command=lambda:zapis("-"))
gumb_minus.grid(row=2,column=3,sticky="NSEW")

gumb_deljeno= tk.Button(kalk, text="/",height=4,width=7,bg="lightblue",command=lambda:zapis("/"))
gumb_deljeno.grid(row=3,column=3,sticky="NSEW")

gumb_krat= tk.Button(kalk, text="*",height=4,width=7,bg="lightblue",command=lambda:zapis("*"))
gumb_krat.grid(row=4,column=3,sticky="NSEW")

gumb_brisanje= tk.Button(kalk, text="C",height=3,width=10,bg="red",command=brisaje)
gumb_brisanje.grid(row=5,columnspan=4,sticky="NSEW")

kalk.mainloop()




     

      

