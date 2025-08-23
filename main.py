import Lists_Task
import FileModule
#region : variable
WarningColor = "\033[91m" 
AtentionColor = "\033[93m"
resetColor = "\033[0m"

#endregion

#region : operation function:

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

#endregion

#region : menu
#----------------------------------------------------------------------------------

#region : inner menu                     
def edit_menu():
    '''
    This function is used in the internal menu section to edit tasks and lists such as updating, deleting, and adding tasks.
    
    Parametr(s):
    -----------
    None
    
    Return(s):
    ---------
    None
    '''
    while True:
        print("\nEditing .........................................\n")
        print("1.Add a new task\n2.Edit a task \n3.Delete a task \n4.View all tasks"
              "\n5.Delete List \n6.Update the List \n7.Back to main menu \n8.Exit")
        edit_choice = input("Enter your choice: ")
        
        if edit_choice == "1":
            print("----\nadd task(s) -------------------------\n ")
            print("for adding, do this steps :\n")
            FileModule.show_All_lists()
            
            Target_list= input("Which list do you want to add task(s)? ")
            try :
                todo_list_path = FileModule.getPath(Target_list)  
                FileModule.Add_Task(todo_list_path ,FileModule.getId(Target_list))
            except ValueError as erorr :
                print("Something is wrong with the input variable. Erorr : {erorr}")
            
        elif edit_choice == "2":
            print("----\nEdit a task -------------------------\n ")
            print("for edit, do this steps :\n")
            path_of_list = Show2Select()
            if path_of_list :
                ETask = input("Enter the Title of the task to edit: ")
                try :
                    task_path = FileModule.getPath(ETask)
                    FileModule.Edit_Task(path_of_list,ETask)
                except ValueError as er :
                    print("Something is wrong with the input variable. Erorr : {er}")
                    
                # if the task is found, you would update it here

                
        elif edit_choice == "3":
            print("----\nDelete a task -------------------------\n ")
            print("for delete, do this steps :\n")
            path_of_list = Show2Select()
            if path_of_list :
                deleteTask = input("Enter the Title of the task to delete: ")
                try :
                    FileModule.delete_Task(path_of_list,deleteTask)
                    print("The process was completed successfully.")
                except ValueError as erorr :
                    print("Something is wrong with the input variable. Erorr : {erorr}")
            
            
        elif edit_choice == "4":
            print("----\nView all tasks in list ----------------\n ")
            print("select the title of the lists : \n")
            FileModule.show_All_lists()
            
            Target_list = input("input the title: \n")
            try :
                
                path_of_list = FileModule.getPath(Target_list)
                FileModule.Show_List(path_of_list)
            except ValueError as erorr :
                print("Something is wrong with the input variable. Erorr : {erorr}")
          

        elif edit_choice == "5":
            print("----\nDelete a list -------------------------\n ")

            FileModule.show_All_lists()
            print("select the title of the lists : \n")
            try :
                Target_list = input("input the title: \n")
                path_of_list = FileModule.getPath(Target_list)
                confirm_delete = input("Do you want to delete it completely? (y/n) ")
                
            #-------------------------------
                tableListPath = FileModule.getPath_TableList()
            #-------------------------------
                if  confirm_delete.lower().strip() == 'y':
                    FileModule.delete_List(path_of_list,tableListPath) 
                    print("List deleted successfully")  
                else:
                    print("the process canceled")
            except ValueError as erorr :
                print("Something is wrong with the input variable. Erorr : {erorr}")
            
        elif edit_choice == "6":
            print("----\nUpdate the List -----------------------\n ")
            #TODO : implement update feature later
            
        elif edit_choice == "7":
            print("\nmain menu -----------------------------\n ")
            break
        elif edit_choice == "8":
            print("----\nexiting -------------------------------\n ")
            print("(T_T)\n ")
            exit()
            
        else:
            print("wrong input please try again later :)\n")
            print("Returning to the main menu")
            print("------------------------------------------------")
            break
#endregion            

#region :  main menu       

def main_menu():
    '''
    The main menu of the program, which contains the list, add list, and edit list.
    
    Parametr(s):
    -----------
    None
    
    Return(s):
    ----------
    None
    '''
    while True:

        print ("\nMenu :")
        print ("1.Create a new List\n2.Edit a List\n3.show the tasks \n4.Exit")
        main_choice = input("Enter your choice: ")
        
        if main_choice == "1":
            print("\nCreating new list ...............................\n ")
            #---- input the input_Title of the list
            List_Title = input("Enter the Title of the list: ")          
            #---- create a new list
            #---- add the list to the file
            (path,field, To_Do_List_ID) = FileModule.Create_New_list(List_Title)
            #---- for add tasks this is run in the function Create_New_list
            #---- if the user want to add tasks, this function will be called
            
        elif main_choice == "2":
            edit_menu()
            
        elif main_choice == "3":
            print("\nShowing : .................................\n ")
            FileModule.show_All_lists()
            try :
                Target_list= input("what list do you want to show?\n:")
                todo_list_path = FileModule.getPath(Target_list)    
                FileModule.Show_List(todo_list_path)
            except Exception :
                print(f"{WarningColor}Something is wrong with the input variable.{resetColor}")
            
            
        elif main_choice == "4":
            print("\nExiting from prograss .....................\n ")

            print("Khosh Galdin")
            break
        
        else :
            print(f"{AtentionColor}Unknow input .-.-.-.-.-.-.-.-.-.-.-.-.-..-.--.-.-.-.-.-\n ")

            print(f"wrong input please try again :){resetColor}")

#endregion        

#endregion            
                        
#region :   ---------- run the program 
print("\nwelcome to the ToDolist app")
if __name__ == "__main__":
    main_menu()
        
#endregion        