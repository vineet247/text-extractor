import pdfbox
import re
import os
from datetime import date
import docx2txt as dx


p = pdfbox.PDFBox()
today = date.today()

#if single file is given
def extract_from_file(file_name, text_file, save_file_name):
    flag = 0
    check_words = ["ERISA", "Employee Retirement Income Security Act of 1974","Employee Retirement Income Security Act"]
    s_path, s_file = os.path.split(file_name)

    #extract words from language file and store in list
    #content = dx.process(text_file)
    #lang_words = content.split()


    #extract text from PDF file and store in list
    object = p.extract_text(file_name)

    #open text file in which text is stored
    base_file, ext = os.path.splitext(file_name)
    ext = ext.replace('.','')
    new_file = base_file + '.txt'


    file = open(new_file, "r", encoding = "utf8")
    reader = file.read()
    pdf_words = reader.split()

    if check_words[0] in pdf_words or check_words[1] in pdf_words or check_words[2] in pdf_words:
        flag = 1
    else:
        flag = 0

    #print("it exists")
    if flag == 1:
        save_file = open(save_file_name + '\\' + str(today) + "ERISA-eligible" + ".txt" , "a")
        save_file.write(s_file + "-" + "ERISA" + "-" + "eligible" + '\n')
        save_file.close()
    else:
        #print("it doesnt")
        save_file = open(save_file_name + '\\' + str(today)+ "ERISA-not-eligible" + ".txt" , "a")
        save_file.write(s_file + "-" + "ERISA" + "-" + "not eligible" + '\n')
        save_file.close()

    file.close()

    os.remove(new_file)

#if folder is given
def extract_from_folder(file_path, text_file, save_file_name):
    check_words = ["ERISA", "Employee Retirement Income Security Act of 1974","Employee Retirement Income Security Act"]
    os.chdir(file_path)
    path = os.listdir(file_path)

    #with open(text_file) as f:
    #    content = f.readlines()

    #content = [x.strip() for x in content]

    for f_file in path:
        #print(f_file)
        if ".pdf" in f_file:
            object = p.extract_text(file_path + '\\' + f_file)

            #open text file in which text is stored
            base_file, ext = os.path.splitext(f_file)
            ext = ext.replace('.','')
            new_file = base_file + '.txt'

            file = open(new_file, "r", encoding="utf8")

            if check_words[0] in file.read() or check_words[1] in file.read() or check_words[2] in file.read() :
                #print("it exists")
                save_file = open(save_file_name + '\\' + str(today)+ "ERISA-eligible" + ".txt", "a")
                save_file.write(f_file + "-" + "ERISA" + "-" + "eligible" + '\n')
                save_file.close()

            else:
                #print("it doesnt")
                save_file = open(save_file_name + '\\' + str(today)+"ERISA-not-eligible"+".txt" , "a")
                save_file.write(f_file + "-" + "ERISA" + "-" + "not eligible" + '\n')
                save_file.close()
            file.close()

            os.remove(new_file)




#extract_from_file(r"C:\Users\vinee\OneDrive\Desktop\ML\assignments\assignment1\part1.pdf", r"C:\Users\vinee\OneDrive\Desktop\ML\assignments\assignment1\text.txt")
#extract_from_folder(r"C:\Users\vinee\OneDrive\Desktop\ML\assignments\assignment1", r"C:\Users\vinee\OneDrive\Desktop\ML\assignments\assignment1\text.txt")
