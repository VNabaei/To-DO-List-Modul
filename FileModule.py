import os
from datetime import datetime
import getpass
import csv
# import  Lists_Task  // با جدول کار می کنم نظرم عوض شد



# TDL file creator : 
def Create_New_list(name :str):
    '''
    This function creates a file in csv format so that it can be loaded into the database.
    
    Parameters
    ---------- 
    name : str
    The name given to the toDOLIST
    
    Returns
    -------
    the path of File created
    
    '''
    
    # Creating folders for TDL files 
    TDL_Folder = "TodoLists app"
    if not os.path.exists(TDL_Folder):
        os.makedirs(TDL_Folder)
        fileTL_path = os.path.join(TDL_Folder,"Table_list.csv") #ساخت مسیر فایل داده
        #ساخت جدول حاوی اطلاعات لیست ها
        fieds_of_table_list = ['id','name','creator','time','status_file']
    
        data = [
            {
                'id':datetime.today().__str__()
                ,'name' : name
                ,'creator' : Get_User()
                ,'time' : datetime.today().date().__str__()
                ,'status_file' : 'created'
            }
         ]
    
        with open(fileTL_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieds_of_table_list)
            writer.writeheader()  
            writer.writerows(data)
        
    
    file_path = os.path.join(TDL_Folder,f"{name}.csv") #ساخت مسیر فایل داده
    
    
    #برسی وجود داشتن از قبل یا نه
    if os.path.exists(file_path):
        #اگر موجود بود
        ans = input ("this list is exists now!\nDo you want replace it ?(y/n)") 
        if ans.upper() != 'y': #اگر نخواهد فایل جایگذین شود عملیات متوقف می شود
            return
        else : #اگر بخواهد جایگذین شود مسیر فایل قبلی حذف و مسیر جدید ساخته می شود
            delete_List(file_path)
            Create_New_list(name)
    else :#درصورتی که فایل وجود نداشت
        # TDList_File_Class = Lists_Task.To_Do_List(name) Creat the TDLclass 
        TDLfile = open(file_path,"w",encoding= 'utf-8')
        TDLfile.close()
      
    # ---- If desired, the file will be completed.   
    # ---- the filed of colums table :
    field_Of_TDL = ["ID","Title","Descreaption","DeadLine","Status","Creat_at","Edited_by","Create_bY",'file_status'] 
    
    input("Do you want add tasks to this list (y/n)? : ")
    if input().upper() == 'Y':
        Add_Task(file_path,field_Of_TDL,name)
    else:
        print("No tasks added to the list.")
        NulTDL_creator(field_Of_TDL,name)
        
      
    # ---- File creation operation completed.
    print(f"List {name} created successfully at {file_path}")
    return file_path , name
        
# Tasks Creator      
def Add_Task (FileTDS ,field_Of_TDL, name):
    '''
    This function, in the todolist file,creates a task and fills in the rows that are the tasks .
    
    Parameters
    ---------- 
    FileTDS : path
    The path of todolist 
    
    field_Of_TDL : array
    the array of table fileds
    
    name : str
    the name of file e.g. : "first_file.csv"
    
    Returns
    -------
    the path of File created
    
    '''
    
    tasks = []
    while True :
        task_name =input("input the task, for break,input nothing!")
        if task_name == "":
            break
        else :
            task= {
                "ID" : ID_Generator(FileTDS) 
                ,"Title": task_name
                ,"Descreaption" : input("add info")
                ,"DeadLine" : Deadline_Creator()
                ,"Status" : "Status"
                ,"Creat_at" :datetime.today().date()
                ,"Edited_by" : Editor() 
                ,"Create_bY" : Get_User()     
                ,"file_status": 'created'        
             }
        
        tasks.append(task)
    #ذخیره سازی در فایل    
    with open(f'{name}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_Of_TDL)
        writer.writeheader()  
        writer.writerows(tasks)
        
        
    print (f"task(s) saved in {FileTDS} successfully")
 
 
# if no task to input :
def NulTDL_creator(field_Of_TDL,name):
    with open(f'{name}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_Of_TDL)
        writer.writeheader()  
         

    
def Show_List(FileTDS):
    if not os.path.exists(FileTDS):
        print(f"{FileTDS} does not exist.")
        return
    with open(FileTDS, "r") as f:
        content = f.read()
        print(content)  


def delete_List(file_path) :
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted successfully.")
    else:
        print(f"{file_path} does not exist.")    
    

def delete_Task(Task):
    # Implement the logic to delete a specific task from the list
    with open(Task, "r") as f:
        line = f.readline()   
        if Task == line.split()  :  
            pass
            
    # with open(Task, "w") as f:
    #     for line in lines:
    #         if line.strip() != Task:    
    #             f.write(line)           
def Update_List():
    pass


def Edit_List ():
    pass

def Edit_Task():
    pass


# ---------------------------------------------------------------------
def Get_User():
    try:
        user = getpass.getuser()
        return user
    except Exception:
        return "Unknown"

def Editor():
    '''
    this function get user when the edit function called
    
    Parametrs:
    ---------
    null
    
    Returns:
    -------
    the user that editied the TDL/TSK
    '''
    return Get_User()

def Deadline_Creator():
    while True:
        ddline_input = input("inter the DDline (Year/month/day) e.g. : 2025/07/31  : ") # در اینجا یه برسی مقدار داده شده هم اجرا شود.
        if ddline_input :
            try:
                ddline_date = datetime.strptime(ddline_input, "%Y/%m/%d").date()
                if ddline_date < datetime.today().date():
                    print("DDline can not be in pass")
                    continue
                else:
                    return ddline_date
                    
            except ValueError:
                print("the format is wrong")
                print("Please enter the date in the format Y/M/D (e.g.: 2025/07/31)")
                continue
            break #exit the loop if date is valid
        else:
            ddline_date = datetime.today().date()
            print("DDline is set to today")
            return ddline_date
            break #exit the loop if no date is provided
      
def ID_Generator(FileTDS,TDL_ID) :
    '''
    This function get the last id and creat the next id 
    '''
    with open(FileTDS , 'r') as f :
        id = '' # از فایل fileTDL در آخرین سطر، ستون Id  رو میخونیم و میریزیم توی اینجا
    x = int(id[67:])
    return f'TDL - {TDL_ID} - TSK - {datetime.today().__str__()}'+ '{++x}'
       