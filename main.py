import Lists_Task
import FileModule

def Show2Select():
        print("select the title of the lists : \n")
        FileModule.show_All_lists()
        List_select = input("input the title: \n")
        List_path = FileModule.getPath(List_select)
        FileModule.Show_List(List_path)
        return List_path
            
    
    
def main():
    print ("menu :")
    print ("1.Create a new List\n2.Edit a List\n3.show the tasks \n4.Exit")
    choiceL1 = input("Enter your choice: ")
    if choiceL1 == "1":
        #---- input the input_name of the list
        List_Title = input("Enter the name of the list: ")          
        #---- create a new list
        # To_Do_List = Lists_Task.To_Do_List(List_Title)
        #---- add the list to the file
        (path,field, To_Do_List_ID) = FileModule.Create_New_list(List_Title)
        #---- for add tasks this is run in the function Create_New_list
        #---- if the user want to add tasks, this function will be called
        

        
    elif choiceL1 == "2":
        print("1. Add a new task\n2.Edit a task \n3.Delete a task \n4.View all tasks \n5.Delete List \n6.Update the List \n7.back to main menu \n8.Exit")
        choiceL2 = input("Enter your choise : ")
        if choiceL2 == "1":
            List_select= input("what list do you want to add task(s)?")
            ToDoList_Path = FileModule.getPath(List_select)  
            # خب اینجا این مشکل رو داریم که باید مقادیر رو از خود جدول استخراج کنیم 
            FileModule.Add_Task(ToDoList_Path ,field,FileModule.getId(List_select))
            # input_nameTask = input("Enter the name of the task: ")
            # Here you would typically add the task to a list or database
                
        elif choiceL2 == "2":
            print("Edit a task -------------------------\n ")
            print("for edit, do this steps :\n")
            List_path = Show2Select()
            
            ETask = input("Enter the name of the task to edit: ")
            # if the task is found, you would update it here
            task_path = FileModule.getPath(ETask)
            FileModule.Edit_Task(List_path,ETask)
                
        elif choiceL2 == "3":
            deleteTask = input("Enter the input_name of the task to delete: ")
            task_path = FileModule.getPath(deleteTask)
            FileModule.delete_Task(task_path,deleteTask)
            
        elif choiceL2 == "4":
            print("select the title of the lists : \n")
            FileModule.show_All_lists()
            List_select = input("input the title: \n")
            List_path = FileModule.getId(List_select)
            FileModule.Show_List(List_path)

        elif choiceL2 == "5":
                    
            print("Delete List")
        elif choiceL2 == "6":
            print("Update the List")
        elif choiceL2 == "7":
            main()
        elif choiceL2 == "8":
            exit()
        else:
            print("wrong input please try again later :)")
            
    elif choiceL1 == "3" :
        # کار میکنه ولی زشته ....
        FileModule.show_All_lists()
        List_select= input("what list do you want to show?")
        ToDoList_Path = FileModule.getPath(List_select)    
        FileModule.Show_List_ALLTask(ToDoList_Path) 
            
    elif choiceL1 == "4":
        print("Khosh Galdin")
    else :
        print("wrong input please try again later :)")
        
        
        
        
#   ---------- run the program 
print("welcome to the ToDolist app")
if __name__ == "__main__":
    main()