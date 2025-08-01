import os
from datetime import datetime
import getpass


#creat the tdl folder if not exist:
TDL_Folder = "TodoLists app"
if not os.path.exists(TDL_Folder):
    os.makedirs(TDL_Folder)

def Create_New_list(name = str):
    
    file_path = os.path.join(TDL_Folder,f"{name}.txt")
    if os.path.exists(file_path):
        ans = input ("this list is exists now!\nDo you want replace it ?(y/n)")
        if ans.upper() != 'y':
            return
        else :
            delete_List(file_path)
            Create_New_list(name)
    ddline_input = input("inter the DDline exp: (7/31/2025)") # در اینجا یه برسی مقدار داده شده هم اجرا شود.
    if ddline_input :
        try:
            ddline_date = datetime.strptime(ddline_input, "%Y-%m-%d").date()
            if ddline_date < datetime.today().date():
                print("DDline can not be in pass")
                return
        except ValueError:
            print("the format is wrong")
            return
    Add_Task(file_path,ddline_date)    
        
        
def Add_Task (FileTDS,DDLine):
    tasks = []
    while True :
        task = input("input the task, for break,input nothing!")
        if task == "":
            break
        tasks.append(task)
    with open(FileTDS,"w") as f :
        f.write(f"Title : {DDLine}\n") # از نوع لیست کلاس بساز
        f.write(f"DeadLine : {DDLine}\n")
        f.write(f"DeadLine : {DDLine}\n")
        f.write(f"DeadLine : {DDLine}\n")
        f.write(f"DeadLine : {DDLine}\n")
        
        f.write(f"DeadLine : {DDLine}\n")
        f.write(f"ceator : {Get_User}\n")
        f.write("Task :\n")
        for t in tasks :
            f.write(f" {t} \n")
    print (f"task(s) saved in {FileTDS} successfully")
    
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
