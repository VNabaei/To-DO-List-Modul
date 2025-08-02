import Lists_Task
import FileModule


    
    
def main():
    print ("menu :")
    print ("1.Create a new List\n2.Edit a List\n3.Exit")
    choiceL1 = input("Enter your choice: ")
    if choiceL1 == "1":
        #---- input the name of the list
        List_Title = input("Enter the name of the list: ")          
        #---- create a new list
        To_Do_List = Lists_Task.To_Do_List(List_Title)
        #---- add the list to the file
        FileModule.Create_New_list(To_Do_List)
        #---- for add tasks this is run in the function Create_New_list
        #---- if the user want to add tasks, this function will be called
        

        pass
    elif choiceL1 == "2":
        print("1. Add a new task\n2.Edit a task \n3.Delete a task \n4.View all tasks \n5.Delete List \n6.Update the List \n7.back to main menu \n8.Exit")
        choiceL2 = input("Enter your choise : ")
        if choiceL2 == "1":
            nameTask = input("Enter the name of the task: ")
            # Here you would typically add the task to a list or database
                
        elif choiceL2 == "2":
            print("Edit a task")
            ETask = input("Enter the name of the task to edit: ")
            # if the task is found, you would update it here
                
        elif choiceL2 == "3":
            deleteTask = input("Enter the name of the task to delete: ")
            print("Delete a task")
        elif choiceL2 == "4":
                
            print("View all tasks")
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
    elif choiceL1 == "3":
        print("Khosh Galdin")
    else :
        print("wrong input please try again later :)")
        
        
        
        
#   ---------- run the program 
print("welcome to the ToDolist app")
if __name__ == "__main__":
    main()