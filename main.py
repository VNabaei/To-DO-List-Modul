import Lists_Task
import FileModule

def Show2Select():
        '''
        To show list Titles while adding or editing tasks
        
        Parametr(s):
        -----------
        None
        
        Return(s):
        ---------
        path_of_list :str
            String containing the path value of the desired list. 
        '''
        print("select the title of the lists : \n")
        FileModule.show_All_lists()
        Target_list = input("input the title: \n")
        try :
            path_of_list = FileModule.getPath(Target_list)
            FileModule.Show_List(path_of_list)
            return path_of_list
        except Exception as error:
            print(f" Error : list not found.\n detail:({error})")
            return None
            
    
    
def main():
    print ("menu :")
    print ("1.Create a new List\n2.Edit a List\n3.show the tasks \n4.Exit")
    choiceL1 = input("Enter your choice: ")
    if choiceL1 == "1":
        print("Creating new list ...............................\n ")
        #---- input the input_Title of the list
        List_Title = input("Enter the Title of the list: ")          
        #---- create a new list
        # To_Do_List = Lists_Task.To_Do_List(List_Title)
        #---- add the list to the file
        (path,field, To_Do_List_ID) = FileModule.Create_New_list(List_Title)
        #---- for add tasks this is run in the function Create_New_list
        #---- if the user want to add tasks, this function will be called
        return True

        
    elif choiceL1 == "2":
        print("Editing .........................................\n ")

        print("1.Add a new task\n2.Edit a task \n3.Delete a task \n4.View all tasks \n5.Delete List \n6.Update the List \n7.back to main menu \n8.Exit")
        choiceL2 = input("Enter your choise : ")
        if choiceL2 == "1":
            print("add task(s) -------------------------\n ")
            print("for adding, do this steps :\n")
            FileModule.show_All_lists()
            
            Target_list= input("what list do you want to add task(s)? ")
            ToDopath_of_list = FileModule.getPath(Target_list)  
            # خب اینجا این مشکل رو داریم که باید مقادیر رو از خود جدول استخراج کنیم 
            FileModule.Add_Task(ToDopath_of_list ,FileModule.getId(Target_list))
            # input_TitleTask = input("Enter the Title of the task: ")
            # Here you would typically add the task to a list or database
            return True
                
        elif choiceL2 == "2":
            print("Edit a task -------------------------\n ")
            print("for edit, do this steps :\n")
            path_of_list = Show2Select()
            
            ETask = input("Enter the Title of the task to edit: ")
            # if the task is found, you would update it here
            task_path = FileModule.getPath(ETask)
            FileModule.Edit_Task(path_of_list,ETask)
            return True
                
        elif choiceL2 == "3":
            print("delete a task -------------------------\n ")
            print("for delete, do this steps :\n")
            path_of_list = Show2Select()
            
            deleteTask = input("Enter the Title of the task to delete: ")
            FileModule.delete_Task(path_of_list,deleteTask)
            print("The process was completed successfully.")
            return True
            
        elif choiceL2 == "4":
            print("view all tasks in list ----------------\n ")
            print("select the title of the lists : \n")
            FileModule.show_All_lists()
            Target_list = input("input the title: \n")
            path_of_list = FileModule.getPath(Target_list)
            FileModule.Show_List(path_of_list)
            return True

        elif choiceL2 == "5":
            print("delete a list -------------------------\n ")

            FileModule.show_All_lists()
            print("select the title of the lists : \n")
            Target_list = input("input the title: \n")
            path_of_list = FileModule.getPath(Target_list)
            
            answer = input("Do you want to delete it completely? (y/n) ")
            #-------------------------------
            tableListPath = FileModule.getPath_TableList()
            #-------------------------------
            if  answer.lower().strip() == 'y':
                FileModule.delete_List(path_of_list,tableListPath) 
                # FileModule.change_status_to_delete(tableListPath,Target_list) 
                # در اینجا باید وضعیت تسک در جلدول اصلی، به پاک ده تغییر کند
                # FileModule.change_status_to_delete(tableListPath,Target_list)    
            else:
                print("the prosess canceled")
            return True
            
        elif choiceL2 == "6":
            print("Update the List -----------------------\n ")
            return True
            
        elif choiceL2 == "7":
            print("main menu -----------------------------\n ")
            return True
        elif choiceL2 == "8":
            print("exiting -------------------------------\n ")
            print("(T_T)\n ")
            return False
        else:
            print("wrong input please try again later :)")
            return True
            
    elif choiceL1 == "3" :
        print("Showing : .................................\n ")
        # کار میکنه ولی زشته ....
        FileModule.show_All_lists()
        Target_list= input("what list do you want to show?\n:")
        ToDopath_of_list = FileModule.getPath(Target_list)    
        # FileModule.Show_List_ALLTask(ToDopath_of_list) #show all atribiut
        # print("\n")
        FileModule.Show_List(ToDopath_of_list)
        return True
            
    elif choiceL1 == "4":
        print("Exiting from prograss .....................\n ")

        print("Khosh Galdin")
        return False
    else :
        print("Unknow .-.-.-.-.-.-.-.-.-.-.-.-.-..-.--.-.-.-.-.-\n ")

        print("wrong input please try again later :)")
        return True
        
def edit_menu():
    ""
        
        
#   ---------- run the program 
print("welcome to the ToDolist app")
if __name__ == "__main__":
    running = True
    while running:
        running = main()
        
        