import os
from datetime import datetime

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
    ddline_input = input("inter the DDline exp: (7/31/2025)")
    if ddline_input :
        try:
            ddline_date = datetime.strptime(ddline_input, "%Y-%m-%d").date()
            if ddline_date < datetime.today().date():
                print("DDline can not be in pass")
                return
        except ValueError:
            print("the format is wrong")
            return
        
        
        
def Add_Task (FileTDS,DDLine,taskName):
    tasks = []
    while True :
        task = input("input the task, for break,input nothing!")
        if task == "":
            break
        tasks.append(task)
    with open(FileTDS,"w") as f :
        f.write(f"DeadLine : {DDLine}\n")
        f.write("Task :\n")
        for t in tasks :
            f.write(f" {t} \n")
    print (f"task(s) saved in {FileTDS} successfully")