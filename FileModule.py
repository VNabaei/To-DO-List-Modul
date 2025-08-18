import os
from datetime import datetime
import getpass
import csv

#region : the variables in FileModule.py
# -------------------------------------------------------------
file_status = ['created', 'edited', 'deleted'] # وضعیت فایل ها در دیتابیس
Status = ['Done', 'Todo', 'In Progress'] # وضعیت تسک ها در دیتابیس
field_Of_ToDoList = ["ID","Title","Descreaption","DeadLine","Status","Creat_at","Edited_by","Create_bY",'file_status'] 
#endregion

#region : the functions in FileModule.py
# -------------------------------------------------------------
#Folder Handeller :
def Add_List_in_Table_list(ToDoList_Folder,input_Title):
    fileTableList_path = os.path.join(ToDoList_Folder,"Table_list.csv") #ساخت مسیر فایل جدول لیست 
    with open(fileTableList_path, 'r', newline='', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))
        field_names = reader[0].keys() if reader else["id","Title","creator","time","file_status","path"]    # Get field Titles from the first table
        data = [
            {
                'id':datetime.today().strftime("%Y%m%d%H%M%S")
                ,'Title' : input_Title
                ,'creator' : Get_User()
                ,'time' : datetime.today()
                ,'file_status' : 'created'
                ,'path' : os.path.join(ToDoList_Folder,f"{input_Title}.csv") #برای برسی شناسه to do list  به این نیاز داریم
            }
        ]
        reader.extend(data)
    with open (fileTableList_path,"w",newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(reader)
        
        
# -------------------------------------------------------------
# FolderCreator :
def Foulder_of_ToDoList_Creator (ToDoList_Folder,input_Title):
        os.makedirs(ToDoList_Folder)
        fileTableList_path = os.path.join(ToDoList_Folder,"Table_list.csv") #ساخت مسیر فایل داده
        #ساخت جدول حاوی اطلاعات لیست ها
        fieds_of_table_list = ['id','Title','creator','time','file_status','path']
    
        data = [
            {
                'id':datetime.today().strftime("%Y%m%d%H%M%S")
                ,'Title' : input_Title
                ,'creator' : Get_User()
                ,'time' : datetime.today()
                # .strftime("%Y%m%d%H%M%S") به صورت شی زمان ذخیره بشه بهتره شاید
                ,'file_status' : 'created'
                ,'path' : os.path.join(ToDoList_Folder,f"{input_Title}.csv") #برای برسی شناسه to do list  به این نیاز داریم
            }
         ]
    
        with open(fileTableList_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieds_of_table_list)
            writer.writeheader()  
            writer.writerows(data)

#endregion    

#region : To Do List
# -------------------------------------------------------------
#region : To Do List file creator : 

def Create_New_list(input_Title :str):
    '''
    This function creates a file in csv format so that it can be loaded into the database.
    
    Parameters
    ---------- 
    input_Title : str
    The input_Title given to the toDOLIST
    
    Returns
    -------
    the path of File created
    
    '''
    
    # Creating folders for TDL files 
    current_dir = os.getcwd()
    ToDoList_File_name = "TodoLists app"
    ToDoList_Folder = os.path.join(current_dir,ToDoList_File_name)
    if not os.path.exists(ToDoList_Folder):
        Foulder_of_ToDoList_Creator (ToDoList_Folder,input_Title)
        # os.makedirs(ToDoList_Folder)
        # fileTableList_path = os.path.join(ToDoList_Folder,"Table_list.csv") #ساخت مسیر فایل داده
        # #ساخت جدول حاوی اطلاعات لیست ها
        # fieds_of_table_list = ['id','input_Title','creator','time','file_status']
    
        # data = [
        #     {
        #         'id':datetime.today().strftime("%Y%m%d%H%M%S")
        #         ,'Title' : input_Title
        #         ,'creator' : Get_User()
        #         ,'time' : datetime.today()
        #         # .strftime("%Y%m%d%H%M%S") به صورت شی زمان ذخیره بشه بهتره شاید
        #         ,'file_status' : 'created'
        #         ,'path' : os.path.join(ToDoList_Folder,f"{input_Title}.csv") #برای برسی شناسه to do list  به این نیاز داریم
        #     }
        #  ]
    
        # with open(fileTableList_path, 'w', newline='', encoding='utf-8') as file:
        #     writer = csv.DictWriter(file, field_names=fieds_of_table_list)
        #     writer.writeheader()  
        #     writer.writerows(data)
    else :
        Add_List_in_Table_list(ToDoList_Folder,input_Title)
        
    file_path = os.path.join(ToDoList_Folder,f"{input_Title}.csv") #ساخت مسیر فایل داده

    
    #برسی وجود داشتن از قبل یا نه
    if os.path.exists(file_path):
        #اگر موجود بود
        ans = input ("this list is exists now!\nDo you want replace it ?(y/n)") 
        if ans.upper() != 'y': #اگر نخواهد فایل جایگذین شود عملیات متوقف می شود
            return
        else : #اگر بخواهد جایگذین شود مسیر فایل قبلی حذف و مسیر جدید ساخته می شود
            delete_List(file_path)
            Create_New_list(input_Title) 
    else :#درصورتی که فایل وجود نداشت
        # TDList_File_Class = Lists_Task.To_Do_List(input_Title) Creat the TDLclass 
        with open(file_path,"w",newline='',encoding= 'utf-8') as f :
            writer = csv.DictWriter(f,field_Of_ToDoList)
            writer.writeheader() 
        
     
    # ---- If desired, the file will be completed.   
    # ---- the filed of colums table :

    
    #Add the tasks :
    ans =input("Do you want add tasks to this list (y/n)? : ")
    if ans.upper() == 'Y':
        tableListPath = os.path.join(ToDoList_Folder,"Table_list.csv")
        with open(tableListPath,'r',encoding='utf-8') as f :
            reader = list(csv.DictReader(f))
            for row in reader :
                if row.get("Title","") == input_Title:
                     ToDoList_id = row.get("id","")
       
        Add_Task(file_path,ToDoList_id)
    else:
        print("No tasks added to the list.")
        Null_ToDoList_creator(field_Of_ToDoList,file_path)
        
      
    # ---- File creation operation completed.
    print(f"List {input_Title} created successfully at {file_path}")
    return file_path , field_Of_ToDoList ,ToDoList_id 
#endregion        

#endregion

#region : Task
# -------------------------------------------------------------

#region : Tasks Creator      
def Add_Task (ToDoList_Path, ToDoList_Id = None ):
    '''
    This function, in the todolist file,creates a task and fills in the rows that are the tasks .
    
    Parameters
    ---------- 
    ToDoList_Path : path
    The path of todolist 
    
    field_Of_ToDoList : array
    the array of table fileds
    
    input_Title : str
    the input_Title of file e.g. : "first_file.csv"
    
    Returns
    -------
    the path of File created
    
    '''
     
    tasks = []
    while True :
        task_input_name =input("input the task, for break,input nothing! \n: ")
        if task_input_name == "":
            break
        else :
            task= {
                "ID" : ID_Generator(ToDoList_Path,ToDoList_Id) 
                ,"Title": task_input_name
                ,"Descreaption" : input("add Description : ")
                ,"DeadLine" : Deadline_Creator()
                ,"Status" : Status[1]  # 'Todo' as default
                ,"Creat_at" :datetime.today().date()
                ,"Edited_by" : Editor() 
                ,"Create_bY" : Get_User()     
                ,"file_status": file_status[0]  # 'created'        
             }
        
        tasks.append(task)
    #ذخیره سازی در فایل    
    # with open(ToDoList_Path, 'w', newline='', encoding='utf-8') as file:
    #     writer = csv.DictWriter(file, fieldnames=field_Of_ToDoList)
    #     writer.writeheader()  
    #     writer.writerows(tasks)
    with open(ToDoList_Path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_Of_ToDoList)
        if file.tell() == 0:  
            writer.writeheader()
        
        writer.writerows(tasks)

        
        
    print (f"task(s) saved in {ToDoList_Path} successfully")
 
 
# if no task to input :
def Null_ToDoList_creator(field_Of_ToDoList,ToDoList_Path):
    with open(ToDoList_Path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_Of_ToDoList)
        writer.writeheader()  
 #endregion  
#endregion      

#region : the operation Function :
#----------------------------------------------
#region : ---- for task 
def Show_the_task(file_path,Task):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tasks = [row for row in reader if (row.get("Statusfile", "").lower() != "delete") and (row.get("title", "").strip().lower() == Task.strip().lower())]
        for task in tasks:
            print(f"Title: {task.get('title', '')} |Descreaption: {task.get('Descreaption', '')} | Status: {task.get('Status', '')}DeadLine: {task.get('DeadLine', '')} | Created at: {task.get('Creat_at', '')}")

def Show_List_ALLTask(ToDoList_Path):
    '''
    Displays all tasks in full detail.
    
    Parametr(s) :
    -----------
    ToDoList_Path : path
    
    Return(s):
    ---------
    None
    
    '''
    
    if not os.path.exists(ToDoList_Path):
        print(f"{ToDoList_Path} does not exist.")
        return
    with open(ToDoList_Path, "r") as f:
        content = f.read()
        print(content)  
 
def delete_Task(file_path,Task):
    '''
    This function changes the file status in the given task to "deleted".
    
    Parametrs :
    ---------
    file_path : path
    the addres of TDL file
    
    Task : str
    The task we want to delete
    
    Returns :
    -------
    None
    '''
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            tasks = list(csv.DictReader(file))
            field_names = tasks[0].keys() if tasks else["ID","Title","Descreaption","DeadLine","Status","Creat_at","Edited_by","Create_bY",'file_status']    # Get field input_Titles from the first table

        task_found = False
        for task in tasks:
            if task['Title'].strip().lower() == Task.strip().lower():
                task['file_status'] = file_status[2]
                task_found = True
        if not task_found :
            print(f"{Task} not found")
            return
        with open(file_path, 'w' , encoding= 'utf-8', newline= '') as f :
            w = csv.DictWriter(f,fieldnames= field_names)
            w.writeheader()
            w.writerows(tasks)


def Edit_Task(file_path,Task):
    # تسک مدنظر را پیدا کرده و شاخصه های قابل تغییر را تغییر می دهد
    #و فایل را بازنویسی میکند.
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return   
    else:
        with open(file_path, 'r',newline='', encoding='utf-8') as file:
            tasks = list(csv.DictReader(file))
            field_names = tasks[0].keys() if tasks else["ID","Title","Descreaption","DeadLine","Status","Creat_at","Edited_by","Create_bY",'file_status']    # Get field input_Titles from the first table

        task_found = False
        for task in tasks:
            if task['Title'].strip().lower() == Task.strip().lower():
                Show_the_task(file_path,Task)
                quest = input('what the filed do you want chang? input number!!\n(1.Title 2.Descreaption 3.DeadLine 4.Status) ')
                match (quest):
                    case "1":
                        task['Title'] = input('enter the title\n:')
                    case "2":
                        task['Descreaption'] = input('enter the info\n:')
                    case "3" :
                        task['DeadLine'] = Deadline_Creator()
                    case "4": 
                        i= input('enter the status (1.Done, 2.Todo, 3.In Progress): ')
                        task['Status'] = Status[int(i)-1]
                    case __ :
                        print("the input is wrong")
                        return
                        
                task['file_status'] = file_status[1]
                task_found = True
        if not task_found :
            print(f"{Task} not found")
            return
        with open(file_path, 'w' ,encoding= 'utf-8', newline= '') as f :
            w = csv.DictWriter(f,fieldnames= field_names)
            w.writeheader()
            w.writerows(tasks)
#endregion    
     
   
#region : ---- for list
            
def Update_List():
    #فکر کنم این الان نیاز نباشه
    pass

def Edit_List ():
    #این هم الان اولویت نبست
    pass

def show_All_lists():
    '''
    This function displays the Table list values
    
    Parametr(s) :
    --------
    None
    
    Return(s) :
    --------
    None
    '''
    current_path = os.getcwd()
    foulder_path = os.path.join(current_path,"TodoLists app")
    fileTableList_path = os.path.join(foulder_path,"Table_list.csv")
     
        
    with open(fileTableList_path, "r", encoding="utf-8") as f:
        lists = list(csv.DictReader(f))
        active_lists = [lst for lst in lists if lst.get("file_status") != file_status[2]]
        if not active_lists:
            print("No active lists available.")
            return
        print("the title of active Lists : \n")
        for lst in active_lists:
            print(f" * {lst.get('Title',)}\n")    
    
    
def Show_List(ToDoList_Path):
    if not os.path.exists(ToDoList_Path):
        print(f"{ToDoList_Path} does not exist.")
        return

    with open(ToDoList_Path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tasks = [row for row in reader if row.get("file_status", "").lower() != file_status[2]]

    if not tasks:
        print("no active task was found")
        return

    print("Active tasks in list:")
    for task in tasks:
        print(f"Title: {task.get('Title', '')} |Descreaption: {task.get('Descreaption', '')} | Status: {task.get('Status', '')}| DeadLine: {task.get('DeadLine', '')} | Created at: {task.get('Creat_at', '')}")

def delete_List(file_path,tableListPath) :
    '''
    This function, given the given file address, deletes the file and also deletes its row from the list table.
    
    Parametr(s):
    -----------
    file_path : path
    the path of data file
    
    tableListPath :path
    the path of table list
    
    Return(s):
    ---------
    None
    '''
    
    if os.path.exists(file_path):
        os.remove(file_path)
        with open (tableListPath,'r',encoding='utf-8',newline='') as f:
            lists = list(csv.DictReader(f))
            field_names = lists[0].keys() if lists else ['id','Title','creator','time','file_status']
            rows = []
            for lst in lists :
                if lst.get("path") != file_path:
                    rows.append(lst)
        with open(tableListPath,'w',encoding='utf-8', newline='') as f:
            written = csv.DictWriter(f,fieldnames=field_names)
            written.writeheader()
            written.writerows(rows)
            
        print(f"{file_path} has been deleted successfully.")
    else:
        print(f"{file_path} does not exist.")    

def change_status_to_delete(file_path,list_Title):
    # NOTE : This function is currently unused.
    # DEPRECATED: Use logging instead of this function.
    '''
    this function chang the status of file (that have same Title to list Title) to deleted in table list
    
    Parametr(s):
    -----------
    file_path : path,
        the path of table list
    
    list_Title : str,
        the Title of deleted file
    
    Return(s):
    ---------
    None
    '''
    if os.path.exists(file_path):          
        with open(file_path, 'r', encoding='utf-8') as file:
            lists = list(csv.DictReader(file))
            field_names = lists[0].keys() if lists else ['id','Title','creator','time','file_status']
        list_found = False
        for lst in lists:
            if lst['Title'].strip().lower() == list_Title.strip().lower():
                lst['file_status'] = file_status[2]
                list_found = True
        if not list_found :
            print(f"{list_Title} not found")
            return
        with open(file_path, 'w' , encoding= 'utf-8', newline= '') as f :
            w = csv.DictWriter(f,fieldnames= field_names)
            w.writeheader()
            w.writerows(lists)
            
        print(f"{list_Title} has been deleted successfully.")
    else:
        print(f"{list_Title} does not exist.")   

#endregion    
 
#region : General function:
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
      
def ID_Generator(ToDoList_Path,ToDoList_ID) :
    '''
    This function get the last id and creat the next id 
    '''
    with open(ToDoList_Path, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

        if rows:
            last_row = rows[-1]
            id = last_row["ID"]
     
            # از فایل fileTDL در آخرین سطر، ستون Id  رو میخونیم و میریزیم توی اینجا
            x = int(id[43:]) # البته فقط برای این فرمت آی دی کار میکنه
            x += 1
            
            #-----------------
            # برای جدا کردن بخش شمارنده راه دیگه ای هم هست ولی فعلا استفاده نمیکنم 
            # match = re.search(r'(\d+)$', id)  # آخرین عدد رو می‌گیره
            # if match:
            #     x = int(match.group(1)) + 1
            # else:
            #     x = 1
            
        else :
            x = 0
    return f'TDL - {ToDoList_ID} - TSK - {datetime.today().strftime("%Y%m%d%H%M%S")}'+ f'{x:03d}'
    # ID format : TDL - {TDL_ID} - TSK - {YYYYMMDDHHMMSS} + {counter of tasks in this TDL file}
    # آی دی خیلی طولانی شد عذرخواهم

# Get Function :
#----------------------------------------------------------------------

def getPath(list_select):
    '''
    This function finds the address of the To Do List from the table list.
    
    Parametr(s) :
    -----------
    list_select : str
    the Title of to do list or task
    
    Return(s) :
    ---------
    path
    
    '''
    
    current_path = os.getcwd()
    foulder_path = os.path.join(current_path,"TodoLists app")
    fileTableList_path = os.path.join(foulder_path,"Table_list.csv")
    with open(fileTableList_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # هر ردیف رو به شکل دیکشنری میده
        for row in reader:
            if row.get('Title', '').strip().lower() == list_select.strip().lower():
                return row.get('path')
    return None 

def getId(list_Title: str, task_title: str = None):
    '''
    This function returns ID of either a ToDoList or a Task.
    
    Parameters
    ----------
    list_Title : str
        Title of the ToDoList
    task_title : str, optional
        Title of the task (if provided, returns Task ID instead of List ID)
    
    Returns
    -------
    str or None
        ID of the ToDoList or Task
    '''
    
    #the path of table list
    current_path = os.getcwd()
    folder_path = os.path.join(current_path, "TodoLists app")
    fileTableList_path = os.path.join(folder_path, "Table_list.csv")
    
    
    if not os.path.exists(fileTableList_path):
        return None
    
    # search in lists
    with open(fileTableList_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Title") == list_Title:
                list_id = row.get("id")
                list_path = row.get("path")
                
                # حالت فقط لیست
                if task_title is None:
                    return list_id
                
                # حالت تسک خاص
                if os.path.exists(list_path):
                    with open(list_path, "r", encoding="utf-8") as task_file:
                        task_reader = csv.DictReader(task_file)
                        for task in task_reader:
                            if task.get("Title", "").strip().lower() == task_title.strip().lower():
                                return task.get("ID")
                else:
                    
                    return None
    
    return None

def getPath_TableList():
    current_path = os.getcwd()
    foulder_path = os.path.join(current_path,"TodoLists app")
    fileTableList_path = os.path.join(foulder_path,"Table_list.csv")
    return fileTableList_path

#endregion

#endregion

#region : TODO
#TODO 1 :Logging and sending
#TODO 2 :List Upgrating in menu
#endregion