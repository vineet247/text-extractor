from tkinter import filedialog
from tkinter import *
from tkinter.filedialog import askopenfilename
from app import extract_from_folder, extract_from_file
from tkinter import messagebox;

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global folder_name
    folder_name = ""
    folder_name = filedialog.askdirectory()
    #folder_path.set(folder_name)
    #print(folder_name)

def browse_button_file():
    global filename
    filename = ""
    filename = askopenfilename()
    #print(filename)

#def lang_text_file():
#    global textname
#    textname = askopenfilename()
    #print(textname)

def execute():
    global save_file_name
    global filename
    global folder_name
    global textname

    save_file_name = ""
    save_file_name = filedialog.askdirectory()

    if len(filename) == 0 and len(folder_name) == 0:
        messagebox.showinfo("Error", "No file or folder detected. Please select either a folder or a PDF file")

    if len(filename) > 0 and len(folder_name) > 0:
        messagebox.showinfo("Error", "Cannot select more than 1 file or folder. Please select either a folder or a PDF file")
        filename = ""
        folder_name = ""
        textname = ""

    else:

        if len(filename) > 0:
            #if len(textname) == 0:
            #    messagebox.showinfo("Error", "No language file detected. Please add a language file")
            #else:
            extract_from_file(filename, textname, save_file_name)
            messagebox.showinfo("Saved", "File Saved Successfully")
            filename = ""
            textname = ""

        if len(folder_name) > 0:
            #if len(textname) == 0:
            #    messagebox.showinfo("Error", "No language file detected. Please add a language file")
            #else:
            extract_from_folder(folder_name, textname, save_file_name)
            messagebox.showinfo("Saved", "File Saved Successfully")
            folder_name = ""
            textname = ""

root = Tk()
root.geometry("600x600")

folder_path = ""
filename = ""
textname = ""
folder_name = ""
save_file_name = ""

lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=5, column=2)
button2 = Button(text="For multiple PDF files, specify folder here", command=browse_button)
button2.place(relx=0.5, rely=0.3, anchor=CENTER)

lbl2 = Label(master=root,textvariable=filename)
lbl2.grid(row=2, column=2)
button3 = Button(text="Select single PDF file here", command=browse_button_file)
button3.place(relx=0.5, rely=0.4, anchor=CENTER)

lbl3 = Label(master=root,textvariable=textname)
lbl3.grid(row=3, column=2)
#button4 = Button(text="Enter language file here (.txt files)", command=lang_text_file)
#button4.place(relx=0.5, rely=0.5, anchor=CENTER)


button4 = Button(text="Execute and Save", command=execute)
button4.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()
