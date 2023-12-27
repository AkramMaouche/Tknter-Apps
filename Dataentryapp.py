import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
import openpyxl 
import os 



window  =  tk.Tk()
window.title('Data Entry')

## frame 
frame = tk.Frame(window,)

##### user information Layout  
user_info = tk.LabelFrame(frame,text='User Information')
user_info.grid(row=0,column=0,sticky='news',pady=5,padx=10)

### First name label and entry 
first_name =  tk.Label(user_info, text='Fisrt Name')
first_name.grid(row=0,column=0)
first_name_entry = tk.Entry(user_info)
first_name_entry.grid(row=1,column=0)

#Last name label and entry 
last_name = tk.Label(user_info,text='Last name')
last_name.grid(row=0,column=1)
last_name_entry = tk.Entry(user_info)
last_name_entry.grid(row=1,column=1)

#tiltle label
title = tk.Label(user_info,text='Title')
title.grid(row=0,column=2)
title_entry = ttk.Combobox(user_info,values=['Mr.','Ms.'])
title_entry.grid(row = 1, column=2)

#age label and entry  
age = tk.Label(user_info,text='Age')
age.grid(row =2 , column=0)
age_entry =  tk.Spinbox(user_info,from_=18, to=66 )
age_entry.grid(row=3,column=0 ) 

#nationalities 
NATIONALITIES_list = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']

nationality =tk .Label(user_info,text='Nationality')
nationality.grid(row=2,column=1)
nationality_entry = ttk.Combobox(user_info,values=NATIONALITIES_list)
nationality_entry.grid(row=3,column=1)

for widget in user_info.winfo_children():
    widget.grid(padx=5,pady=5)
##### user information Layout  

register  =  tk.LabelFrame(frame) 
register.grid(row=1,column=0,sticky='news',pady=5,padx=10)

#regester stuts
regestration_stutus =  tk.Label(register,text='Registration Status')
regestration_stutus.grid(row=0,column=0) 

register_var = tk.StringVar(window,'Not Registered')
regestration_stutus_entry =  tk.Checkbutton(register,text='Currently registered',
                                            variable = register_var,
                                            onvalue='Registered',offvalue='Not Registered')

regestration_stutus_entry.grid(row=1,column=0)

#Courses 
courses =  tk.Label(register,text='#Completed Courses')
courses.grid(row=0,column=1)
courses_entry = tk.Spinbox(register,from_=0, to =20)
courses_entry.grid(row=1,column=1)

#semsters 
semester =  tk.Label(register,text='#Semesters')
semester.grid(row=0,column=2)
semester_entry = tk.Spinbox(register,from_=0,to=10)
semester_entry.grid(row=1,column=2)

for widget in register.winfo_children(): 
    widget.grid(padx=7,pady=5)


terms = tk.LabelFrame(frame,text='Terms & Conditions')
terms.grid(row=2,column=0,sticky='news',pady=5,padx=10)

terms_var = tk.StringVar(terms,'not Accepted')
terms_conditions = tk.Checkbutton(terms,text='I accept the Terms and Conditions',variable=terms_var,onvalue='Accept the terms',offvalue='not Accepted')
terms_conditions.grid(row=0,column=0)



def enter_data_func():
    register_check = register_var.get()
    terms_check = terms_var.get()
    First_name = first_name_entry.get()
    Last_name = last_name_entry.get()
    Title = title_entry.get()
    Age = age_entry.get()
    Nationality = nationality_entry.get()
    Courses = courses_entry.get()
    Semster = semester_entry.get()
    


    if terms_check == 'Accept the terms':
        if first_name_entry.get() and last_name_entry.get():
            # print('First Name:',first_name_entry.get(),'   ','Last Name:',last_name_entry.get())
            # print('Title:',title_entry.get(),'Age:','   ',age_entry.get(),'   ','Nationality:',nationality_entry.get())
            # print('Courses:',courses_entry.get(),'Semester:','   ',semester_entry.get(),'Registration Status:',register_check)
            # print("---------------------------------------------------------")

            filepath = 'D:\Siplast App\data.xlsx'
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active 
                heading = ['First Name', 'Last Name','Title','Age','Nationality','Courses','Semsters','Registration Status'] 
                sheet.append(heading)
                workbook.save(filepath)

            workbook = openpyxl.load_workbook(filepath) 
            sheet = workbook.active 
            sheet.append([First_name,Last_name,Title,Age,Nationality,Courses,Semster,register_check])
            workbook.save(filepath)    

            messagebox.showinfo(title='approved',message='the informations are saved ')         

        
        else:
             messagebox.showwarning(title='Wearning',message='You must enter the name ')      

     
    else:
      messagebox.showwarning(title='Wearning',message='You must Accept The Terms ')    






enter_data = tk.Button(frame,text='Enter Data',command=enter_data_func)
enter_data.grid(row=3,column=0,sticky='news',pady=10,padx=10)














frame.pack()

window.mainloop()
