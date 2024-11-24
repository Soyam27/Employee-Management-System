#INTRODUCTION:Employee management system
#Developer option(will be used to create/delete databases and tables):
#Below module takes user/passwd as inputs and establishes connection with respective MYSQL server

def connection():
    global connector   #It will allow variable connector to be accessed form any corner of the soure code
    
    print("\nPlease connect to MYSQL user(To continue Y(YES)/N(NO)):\n")
    connecting_var = input("Choose(Y/N):")
    
    #When condition is yes:
    
    if connecting_var in "Yy":
        user= input("Username:")
        passwd= input("Password:")
        import mysql.connector as con
        data_config={"host":"localhost",
                     "user":user,
                     "passwd":passwd}
        print('-'*80)
        
        #here the connector tries to connect with server
        
        try:
            connector = con.connect(**data_config)
            if connector.is_connected():
                print("Connection successful!")
                
        #if user/passwd is incorrect,exepct with generate a redirection:
                
        except:
            print("error in user/password please re-enter:")
            print('-'*80)
            connection()
    #When condition is no:

    elif connecting_var in "Nn":
       print("THANK YOU")
       ex=input("press enter:")
       if ex=="":
            exit()
        #else is just to prevent misleading inputs
       else:
            connection()

    #in case connecting_var got misleading entry, else will again call the module

    else:
        connection()

#this connection just calls the module from mains:
        
connection()

#here we introduce our cursor used in further modules

cur= connector.cursor()

#first module is to create data base if not any present or usable

def createDB(a):
    query="create database if not exists {}".format(a)
    cur.execute(query)
    connector.commit()
    if cur.rowcount>0:
        print("Data base",a,"is successfully created..")
    devmenu()

#second module is to create tables(which has predefined schemea)
    #namely they are:1.department 2.employee 3.leaves
    #board discription:1. employee table has its department_id refrenced to department table's department_id.
    #2.leaves table has its employee_id refrenced to employee table's employee_id.


def createTB(table_):
    if table_=="1":
        query="""create table if not exists Department(Department_id int primary key,
                 Department_name varchar(255),
                 Manager_id int)
                 """
    elif table_=="2":
             query="""create table if not exists employee(Employee_id int primary key,
                first_name varchar(255),
                last_name varchar(255),
                Email varchar(255),
                Contact_number varchar(255),
                Department_id int,
                Position Varchar(255),
                Salary Decimal(10,2),
                Hire_date date)
                """
        
                 
    elif table_=="3":
        query="""create table if not exists Leaves(
                 Employee_id int,
                 Leave_id int primary key,
                 Leave_type varchar(255),
                 Leave_from date,
                 Leave_to date,
                 Reason varchar(255),
                 Status varchar(255),
                 foreign key (Employee_id) references employee(Employee_id)
                 on delete cascade
                 on update cascade)
                 """
    cur.execute(query)
    connector.commit()
    if table_=="1":
        print("Department table is craeted")
    elif table_=="2":
        print("Employee table is craeted")
    elif table_=="3":
        print("Leaves table is craeted")
        
    devmenu()

#Developers option: this is to execute different actson Databases and tables:
    #1.create/delete database
    #2.create/delete table

def devmenu():
    print("--------------------------Welcome to developers option---------------------------")
    print("DEVELOPERS MENU:")
    print("1.Create database\n2.Create table(1.department 2.employee 3.leave)\n3.Delete table\n4.Delete database\n5.Use database\n6.main menu\n7.Exit")
    print("-"*80)
    devq = input("Select operation:")
    print("Operation selected",devq)
    
    #devq-1: is for createion of database
    
    if devq=="1":
        DBname=input("enter database name:")
        createDB(DBname)
        print('-'*80)

    #devq-2: is for creation of tables
    
    elif devq=="2":
        try:
            type_tab=input("enter table you want to create(1-->2-->3):")
            createTB(type_tab)
        except Exception as e:
            print('-'*80)
            print("Issue arises:",e)
            devmenu()
        print('-'*80)

    #devq-3: is for deletion of tables

    elif devq=="3":
        tab = input("enter table name:")
        try:
            query="drop table {}".format(tab)
            cur.execute(query)
            connector.commit()
            print("table",tab,"deleted")
            devmenu()
        except Exception as e:
            print("Issue arises:",e)
            devmenu()
        print('-'*80)

    #devq-4: if for deletion of databases

    elif devq=="4":
        dab = input("enter database name:")
        try:
            query="drop database {}".format(dab)
            cur.execute(query)
            connector.commit()
            print("database",dab,"deleted")
            devmenu()
        except Exception as e:
            print("Issue arrises:",e)
            devmenu()
        print('-'*80)

    #devq-5: selects the database needs to be in use
    
    elif devq=="5":
        try:
            dbn = input("enter database:")
            query = "use {}".format(dbn)
            cur.execute(query)
            connector.commit()
            print("database changed to",dbn)
            devmenu()
        except Exception as e:
            print("Issue arises:",e)
            devmenu()
        print('-'*80)

    #This option dev1-6 directs us to main menu
    
    elif devq=="6":
        print('-'*80)
        Mains()

    #devq-7: exits form program

    elif devq=="7":
        print("THANK YOU")
        ex=input("press enter:")
        if ex=="":
            exit()

    #devq-8: wrong enrty prevention
    
    else:
        devmenu()


#MAIN MENU:main menu starts from here i.e. now we can add/delete/update/read records
def Mains():

    print("----------------------WELCOME TO EMPLOYEE MANAGEMENT SYSTEM---------------------")

    #As soon as connection establishes, program directs towards main menu so using a DB is must
    #From here Main menu section starts 

    while True:
        print("1.Insert Record\n2.View Record\n3.Update Record\n4.Search Record\n5.Delete Record\n6.Developer option\n7.Exit")
        print("-"*80)
        opt = input("Enter operation:")
        print("Operation choosed",opt)
        c = 0
        print("-"*80)
            
        #first operation is insertion
            
        if opt=="1":
            try:
                freq = int(input("Numbers of records:"))
            except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
            tab_use = input("Enter table:")
            for i in range(freq):
                if tab_use.lower() == "employee":
                    
                    try:
                        inp1= int(input("enter employee_id:"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
            
                    inp2= input("enter first_name:")
                    inp3= input("enter last_name:")
                    inp4= input("enter email:")
                    inp5= input("enter contact number:")
                        
                    try:
                        inp6= int(input("enter department id:"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                    inp7= input("enter position:")
                        
                    try:
                        inp8= float(input("enter salary"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                    inp9= input("enter hire date(yyyy-mm-dd):")
                    query = "insert into employee values({},'{}','{}','{}','{}',{},'{}',{},'{}')".format(inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9)

                    try:
                        cur.execute(query)
                        connector.commit()
                        print("Record has been enterd")
                        print('-'*80)
                        c=c+1
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                elif tab_use.lower() == "department":
                    
                    try:
                        inp1= int(input("enter department_id:"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                    inp2= input("enter department_name:")
                        
                    try:
                        inp3= int(input("enter manager_id:"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                    query = "insert into department values({},'{}',{})".format(inp1,inp2,inp3)
                    cur.execute(query)
                    connector.commit()
                    print("Record has been enterd")
                    print('-'*80)
                    c=c+1
                elif tab_use.lower() == "leaves":
                    
                    try:
                        inp1= int(input("enter employee_id:"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()

                    try:
                        inp2= int(input("enter leave_id"))
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                    inp3= input("enter leave type:")
                    inp4= input("enter leave from(yyyy-mm-dd):")
                    inp5= input("enter leave to(yyyy-mm-dd):")
                    inp6= input("enter reason of leave:")
                    inp7= input("enter status:")
                    query = "insert into leaves values({},{},'{}','{}','{}','{}','{}')".format(inp1,inp2,inp3,inp4,inp5,inp6,inp7)
                    try:
                        cur.execute(query)
                        connector.commit()
                        print("Record has been enterd")
                        print('-'*80)
                        c=c+1
                    except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()

            if c==0:
                print("Table not existing")
            print("-"*80)

        #Second operation is reading
        
        elif opt=="2":
            tab_use=input("enter table:")
            try:
                if tab_use=="employee":
                    query="select * from employee"
                    cur.execute(query)
                    for i in cur.fetchall():
                        print(i)
                elif tab_use=="department":
                    query="select * from department"
                    cur.execute(query)
                    for i in cur.fetchall():
                        print(i)
                elif tab_use=="leaves":
                    query="select * from leaves"
                    cur.execute(query)
                    for i in cur.fetchall():
                        print(i)
                else:
                    print("Table not existing..")
            except Eception as e:
                print("Issue arises:",e)
            print("-"*80)

        #third operation is updating
        
        elif opt=="3":
            tab_use = input("enter table:")

            
            if tab_use=="employee":
                
                try:
                    empid = int(input("enter employee id to be updated:"))
                except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                val_tobeup = input("what you want to update:")
                val_tobeset = input("enter the new value for the column"+val_tobeup+":")
                
                try:
                    val_tobeset = int(val_tobeset)
                except:
                    pass
                
                try:
                    query= "update employee set {}='{}' where employee_id={}".format(val_tobeup,val_tobeset,empid)
                    cur.execute(query)
                    connector.commit()
                    print("updated successfully..")
                except Exception as e:
                    print("Issue arises",e)

                    
            elif tab_use=="department":
                
                try:
                    deptid = int(input("enter department id to be updated:"))
                except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                val_tobeup = input("what you want to update:")
                val_tobeset = input("enter the new value for the column"+val_tobeup+":")
                try:
                    val_tobeset = int(val_tobeset)
                except:
                    pass
                
                try:
                    query= "update department set {}='{}' where department_id={}".format(val_tobeup,val_tobeset,deptid)
                    cur.execute(query)
                    connector.commit()
                    print("updated successfully..")
                except Exception as e:
                    print("Issue arises",e)

                    
                    
            elif tab_use=="leaves":
                
                try:
                    empid = int(input("enter employee id to be updated:"))
                except Exception as e:
                        print("Issue arises",e)
                        print("Redirecting to developer option")
                        devmenu()
                        
                val_tobeup = input("column you want to update:")
                val_tobeset = input("enter the new value for the column"+val_tobeup+":")
                try:
                    val_tobeset = int(val_tobeset)
                except:
                    pass
                
                try:
                    query= "update leaves set {}='{}' where employee_id={}".format(val_tobeup,val_tobeset,empid)
                    cur.execute(query)
                    connector.commit()
                    print("updated successfully..")
                except Exception as e:
                    print("Issue arises",e)
                    
            else:
                print("Table not existing..")
            print("-"*80)

        #fourth operation is searching
        
        elif opt=="4":
            tab_use = input("enter table:")

            
            if tab_use=="employee":
                
                try:
                    empid=int(input("enter employee id to searched:"))
                    query="select * from employee where employee_id={}".format(empid)
                    cur.execute(query)
                    print(cur.fetchall())
                except Exception as e:
                    print("Issue arises:",e)
                    
                    
            elif tab_use=="department":
                
                try:
                    deptid=int(input("enter department id to searched:"))
                    query="select * from department where department_id={}".format(deptid)
                    cur.execute(query)
                    print(cur.fetchall())
                except Exception as e:
                    print("Issue arises:",e)
                    
                    
            elif tab_use=="leaves":
                
                try:
                    empid=int(input("enter employee id to searched:"))
                    query="select * from leaves where employee_id={}".format(empid)
                    cur.execute(query)
                    print(cur.fetchall())
                except Exception as e:
                    print("Issue arises:",e)
            else:
                print("Table not existing..")
                
            print("-"*80)

        #fifth operation is record deletion by ids
        
        elif opt=="5":
            tab_use = input("enter table:")
            if tab_use=="employee":
                
                try:
                    empid=int(input("enter employee id to deleted:"))
                    query="delete from employee where employee_id={}".format(empid)
                    cur.execute(query)
                    connector.commit()
                    print("Record deleted successfully..")
                except Exception as e:
                    print("Issue arises:",e)
                    
            elif tab_use=="department":
                try:
                    deptid=int(input("enter department id to deleted:"))
                    query="delete from department where department_id={}".format(deptid)
                    cur.execute(query)
                    connector.commit()
                    print("Record deleted successfully..")
                except Exception as e:
                    print("Issue arises:",e)
                    
            elif tab_use=="leaves":
                try:
                    empid=int(input("enter employee id to deleted:"))
                    query="delete from leaves where employee_id={}".format(empid)
                    cur.execute(query)
                    connector.commit()
                    print("Record deleted successfully..")
                except Exception as e:
                    print("Issue arises:",e)
            else:
                print("Table not existing..")
            print("-"*80)

        #sixth operation is to open developers option
            
        elif opt=="6":
            devmenu()

        #seventh operation is to exit program
        
        elif opt=="7":
            print("THANK YOU")
            ex=input("Press enter to exit:")
            if ex=="":
                exit()

conq=input("Do you have data base?(Press Y/N):")
if conq in "Yy":
    try:
            dbn = input("enter database:")
            query = "use {}".format(dbn)
            cur.execute(query)
            connector.commit()
            print("database changed to",dbn)
            print("-"*80)

        #if any problem with DB arises, except will redirect us to developers option
            
    except Exception as e:
            print("Issue arises:",e)
            print("Redirecting to developers area:")
            devmenu()
else:
    devmenu()

        
Mains()
        
    
    

    

