import pymysql

#connect databse here
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='amartya',
    db='projectsystem',
)
cur = conn.cursor()
#cur.execute("select @@version")
#cur.execute("SHOW TABLES")
#output = cur.fetchall()

#keep track of login 

def auth():
    
    print("\nPROJECT MANAGEMENT SYSTEM AUTHENTICATION :- ")
    
    print("\nEnter username :")
    username=input()
    
    print("\nPassword :")
    password=input()
    
    cur.execute("select * from user_password where Username='"+username+"' and Password='"+password+"'")
    output = cur.fetchall()
     
    if(len(output)!=0):
        return True
    
    return False   
       
def printQueries(i):
    print("--> Enter 1 to view all details")
    print("--> Enter 2 to search table")
    print("--> Enter 3 to execute custom queries")
    if(i==0):
        print("--> Enter any other key to go back to home.\n")

def printHome():
    print("\n ||----WELCOME TO PROJECT MANAGEMENT SYSTEM----|| \n")
    print("--> Enter 1 to view staff details (Enter into the staff table)")
    print("--> Enter 2 to view project details (Enter into the projects table)")
    print("--> Enter 3 to view all available roles (Enter into the roles table)")
    print("--> Enter any other key to terminate the program \n")
    
def printSearch():
    print("\n--> Enter 1 to search using ID")
    print("--> Enter 2 to search using name or description")
    print("--> Enter 3 to search using custom queries\n")

#TODO Create Update Delete functions
    

queryOption = 0   
#driver code

if(auth()):
    
    printHome()
    userchoice = int(input())
    
    while(userchoice<=3):


        #staff
        if(userchoice == 1):
            print("\nEntered into staff table !!\n")
            printQueries(1)
            print("--> Enter 4 to view staff degrees")
            print("--> Enter any other key to go back to home.\n")
            queryoption = int(input())
            
            if(queryoption ==1):
                cur.execute("select * from staff")
                output = cur.fetchall()

                print("\nOutput:\n")
                for row in output:
                    print(row)
            
            if(queryoption == 2):
                printSearch()
                searchoption = int(input())
                
                if(searchoption ==1):
                    print("\nEnter staff ID to search :")
                    staffID = int(input())
                    #write query
                    cur.execute("select * from staff where Staff_ID ="+str(staffID))
                    output = cur.fetchall()
                    
                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #TODO display for no output case
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue
                
                if(searchoption ==2):
                    print("\nEnter staff's first name to search:\n")
                    name =input()
                    #write query
                    cur.execute("select * from staff where First ='"+name+"'" )
                    output = cur.fetchall()

                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue

                if(searchoption ==3):
                    print("\nEnter custom query to execute:\n")
                    query = input()
                    #write query
                    cur.execute(query)
                    output = cur.fetchall()
 
                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue
            
            if(queryoption == 3):
                print("\nEnter custom query to perform on the staff table:\n")
                query = input()
                
                try:
                    cur.execute(query)
                    output = cur.fetchall()
                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                except:
                    print("\nError in query!!\n")
                finally:
                    printHome()
                    userchoice = int(input())
                    continue
            
            if(queryoption ==4):
                cur.execute("select * from staff_degrees")
                output = cur.fetchall()

                print("\nOutput:\n")
                for row in output:
                    print(row)
                        
            if(queryoption > 4): 
                printHome()
                userchoice = int(input())
                continue

        #role
        if(userchoice ==3):
            print("\nEntered into roles table !!\n")
            printQueries(0)
            queryOption = int(input())

            if(queryoption ==1):
                cur.execute("select * from roles")
                output = cur.fetchall()

                print("\nOutput:\n")
                for row in output:
                    print(row)

            if(queryoption == 2):
                printSearch()
                searchoption = int(input())
                
                if(searchoption ==1):
                    print("\nEnter role ID to search:\n")
                    RoleID = int(input())
                    #write query
                    cur.execute("select * from roles where Role_ID ="+str(RoleID))
                    output = cur.fetchall()
                    
                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #TODO display for no output case
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue
                
                if(searchoption ==2):
                    print("\nEnter roles description to search:\n")
                    desc =input()
                    #write query
                    cur.execute("select * from roles where Desription like '%"+name+"%'")
                    output = cur.fetchall()


                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue
            
            if(queryoption == 3):
                print("\nEnter custom query to perform on the roles table:\n")
                query = input()
                
                try:
                    cur.execute(query)
                    output = cur.fetchall()

                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                except:
                    print("\nError in query!!\n")
                finally:
                    printHome()
                    userchoice = int(input())
                    continue
            
            if(queryoption > 3):
                printHome()
                userchoice = int(input())
                continue


        #projects
        if(userchoice ==2):
            print("\nEntered into project table!!\n")
            
            printQueries(0)
            queryoption = int(input())

            if(queryoption ==1):
                cur.execute("select * from project")
                output = cur.fetchall()

                print("\nOutput:\n")
                for row in output:
                    print(row)
            
            if(queryoption == 2):
                printSearch()
                searchoption = int(input())
                
                if(searchoption ==1):
                    print("\nEnter project ID to search:\n")
                    projectID = int(input())
                    #write query
                    cur.execute("select * from project where project_id ="+str(projectID))
                    output = cur.fetchall()

                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #TODO display for no output case
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue
                
                if(searchoption ==2):
                    print("\nEnter project name to search:\n")
                    name =input()
                    #write query
                    cur.execute("select * from project where Project_Name like '%"+name+"%'")
                    output = cur.fetchall()

                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue

                if(searchoption ==3):
                    print("\nEnter custom query:\n")
                    query = input()
                    #write query
                    cur.execute(query)
                    output = cur.fetchall()
                    
                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                    #display results
                    #once this is done we go back to home
                    print("\nThank you for using our system !!\n")
                    printHome()
                    userchoice = int(input())
                    continue
            
            
            if(queryoption == 3):
                print("\nEnter custom query to perform on the projects table:\n")
                query = input()
                
                try:
                    cur.execute(query)
                    output = cur.fetchall()

                    print("\nOutput:\n")
                    for row in output:
                        print(row)
                except:
                    print("\nError in query!!\n")
                finally:
                    printHome()
                    userchoice = int(input())
                    continue
            
            
                      
            if(queryoption > 3):
                printHome()
                userchoice = int(input())
                continue
    

#auth dead
else:
    print("\nAuthentication error restart the application and try again !!\n")