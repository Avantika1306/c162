from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
import os
from tkinter import filedialog
import webbrowser
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("Notepad")
label_file=Label(root,text="file name")
label_file.place(relx=0.28,rely=0.03)
input_filename=Entry(root)
input_filename.place(relx=0.45,rely=0.03)
name=""
def openfile():
    global name
    textarea.delete(1.0,END)
    input_filename.delete(0,END)
    html_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("html Files","*.html"),))
    name=os.path.basename(html_file)
    formated_name=name.split(".")[0]
    input_filename.insert(END,formated_name)
    root.title(formated_name)
    html_file=open(name,"r")
    paragraph=html_file.read()
    textarea.insert(END,paragraph)
    html_file.close()

def savefile():
    filename=input_filename.get()
    file=open(filename+ ".html","w")
    data=textarea.get(1.0,END)
    file.write(data)
    input_filename.delete(0,END)
    textarea.delete(1.0,END)
    messagebox.showinfo("update","succsess")
     

def run_html():
    global name 
    webbrowser.open(name)

        

button_open=Button(root,text="open",command=openfile)
button_open.place(relx=0.05,rely=0.03,anchor=CENTER)
button_save=Button(root,text="save",command=savefile)
button_save.place(relx=0.11,rely=0.03,anchor=CENTER)
button_close=Button(root,text="run",command=run_html)
button_close.place(relx=0.17,rely=0.03,anchor=CENTER)
textarea=Text(root,height=35,width=80)
textarea.place(relx=0.5,rely=0.55,anchor=CENTER)
root.mainloop()