from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import random

root=Tk()
root.title("Jobs ")
root.geometry("900x500")
root.configure(bg="white")

image=ImageTk.PhotoImage(Image.open("new-job.jpg"))
place_image=Label(root)
place_image["image"]=image
place_image.place(relx=0.7,rely=0.5,anchor=CENTER)

label=Label(root,text="Job Assigning Application",font=("Inter",20,"bold"),bg="white")
label.place(relx=0.01,rely=0.09,anchor=W)

label_doctor=Label(root,text="Doctor : ",bg="white")
label_doctor.place(relx=0.04,rely=0.25,anchor=CENTER)

label_IT=Label(root,text="IT professional: ",bg="white")
label_IT.place(relx=0.06,rely=0.45,anchor=CENTER)

label_chemical_engi=Label(root,text="Chemical Engineer : ",bg="white")
label_chemical_engi.place(relx=0.07,rely=0.65,anchor=CENTER)


entry_doctor=Entry(root)
entry_doctor.place(relx=0.25,rely=0.25,anchor=CENTER)

entry_IT=Entry(root)
entry_IT.place(relx=0.25,rely=0.45,anchor=CENTER)

entry_chemical_engi=Entry(root)
entry_chemical_engi.place(relx=0.25,rely=0.65,anchor=CENTER)

label_selected_doc=Label(root,font=("Inter",12,"bold"),fg="white")
label_selected_doc.place(relx=0.01,rely=0.32,anchor=W)

label_selected_IT=Label(root,font=("Inter",12,"bold"),fg="white")
label_selected_IT.place(relx=0.01,rely=0.52,anchor=W)

label_selected_chem_engi=Label(root,font=("Inter",12,"bold"),fg="white")
label_selected_chem_engi.place(relx=0.01,rely=0.72,anchor=W)




class parent():
    def __init__(self):
        print("This is Partent Class")
        
        
   
    def doctor(doctor_name):
        hospital_list=["Apex","Apollo","City Care","Galaxy"]
        random_hospital=random.randint(0,3)
        label_selected_doc['text']=doctor_name+" has been alotted to "+hospital_list[random_hospital]
        
    
    def softwareEngineer(it_professional_name):
        IT_company_list=["Tata Consultancy service","Infosys","HCL Technologies","ATOS"]
        random_IT_company=random.randint(0,3)
        label_selected_IT['text']=it_professional_name+" has been alotted to "+IT_company_list[random_IT_company]
        
        
    
    def chemicalEngineer(chemical_engineer_name):
        company_list=["Ineos","BASF","Tata Chemicals Ltd","DuPant"]
        random_company=random.randint(0,3)
        label_selected_chem_engi['text']=chemical_engineer_name +" has been alotted to "+ company_list[random_company]

        
        
        
        
        


class child1(parent):
    def __init__(self):
        print("This is Child1 Class")
        
        
    def getDoctor(self):
        name=entry_doctor.get()
        parent.doctor(name)
       
        
       
        
       
class child2(parent):
    def __init__(self):
        print("This is Child2 Class")
        
        
    def getIT(self):
        name=entry_IT.get()
        parent.softwareEngineer(name) 
        
        
        
        
        
        
class child3(parent):
   def __init__(self):
        print("This is Child3 Class")
        
        
   def getchemicalEngineer(self):
        name=entry_chemical_engi.get()
        parent.chemicalEngineer(name)         
        
        
obj1=child1()
obj2=child2()
obj3=child3()

btn_doctor=Button(root,text="Show the hospital alotted",command=obj1.getDoctor,bg="white",relief=FLAT)
btn_doctor.place(relx=0.1,rely=0.18,anchor=CENTER)
btn_IT=Button(root,text="Show the It company alotted",command=obj2.getIT,bg="white",relief=FLAT)
btn_IT.place(relx=0.11,rely=0.38,anchor=CENTER)
btn_engi=Button(root,text="Show the chemical company alotted",command=obj3.getchemicalEngineer,bg="white",relief=FLAT)
btn_engi.place(relx=0.13,rely=0.58,anchor=CENTER)


root.mainloop()