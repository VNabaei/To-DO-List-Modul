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
    while True:
        ddline_input = input("inter the DDline (Year/month/day) e.g. : 2025/07/31  : ") # در اینجا یه برسی مقدار داده شده هم اجرا شود.
        if ddline_input :
            try:
                ddline_date = datetime.strptime(ddline_input, "%Y/%m/%d").date()
                if ddline_date < datetime.today().date():
                    print("DDline can not be in pass")
                    continue
            except ValueError:
                print("the format is wrong")
                print("Please enter the date in the format Y/M/D (e.g.: 2025/07/31)")
                continue
            break #exit the loop if date is valid
        else:
            ddline_date = datetime.today().date()
            print("DDline is set to today")
            break #exit the loop if no date is provided
            
    input("Do you want add tasks to this list (y/n)? : ")
    if input().upper() == 'Y':
        Add_Task(file_path)
    else:
        print("No tasks added to the list.")
    print(f"List {name} created successfully at {file_path}")
    return file_path
        
        
def Add_Task (FileTDS):
    
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
