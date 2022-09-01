import pymysql
import pandas as pd
from datetime import datetime
from datetime import timedelta
from datetime import date

mydb=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="library_management_system")
c=mydb.cursor()




# list=[['the pilgrims progress ','john bunyan', '1678'],['seven days','miss lana','1998'],["verity","arif","2012"],['pokemon','danish','2002']]

# res=[]
# borrowed=[]
# renew_book=[]
# librarian=['aliyan','ahmer','zeshan','mohsin','zain']
# reserve=[]
# customers=['shahroz','jahanzaib','hunzala','huzaifa','hammad','nehal']





class library:
    def __init__(self):
        self.name_cus='None'
        self.name_admin='None'  
    
    def add(self):
        while True:
             print(" WELCOME TO ADMIN ADD BOOK SECTION ")
            ##   print(" WELCOME TO ADMIN LOGIN AREA ")
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                break
             book_name=input('ENTER BOOK NAME: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()
             pub_date=input('ENTER PUBLISHED DATE IN FORMAT [ YYYY/MM/DD ]: ').lower()
             c.execute('select count(*) from books')
             if book_name=='' or author_name=='' or pub_date=='':
                 print('PLZ FILL ALL THE INPUT BOXES ')
             else:
                 
              
                 res=c.fetchall()
                 res=str(res)
                 op=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 if op==():
                    op='BK-'+str(0)
                 else:
                    op='BK-'+str(op)
                        

                 
                 c.execute(''' insert into books values(%s,%s,%s,%s) ''',(op,book_name,author_name,pub_date))
                 mydb.commit()
                 print('YOU HAVE SUCCESSFULLY ADDED A NEW BOOK IN LIBRARY')

    def remove(self):
        while True:
             print(" WELCOME TO ADMIN REMOVE BOOK SECTION ")
            
            ##   print(" WELCOME TO ADMIN LOGIN AREA ")
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                break

            ###
             book_name=input('ENTER BOOK NAME: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()
             
             if book_name=='' or author_name=='':
                  print('PLZ FILL ALL THE INPUT BOXES ')
                  
             else:
                 c.execute(''' select count(*) from books
where book_name=%s and author_name=%s and book_id in(select book_id from borrowed_books)
''',(book_name,author_name))
                 res=c.fetchall()
                 res=str(res)
                 res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 res=int(res)

                 if res>0:
                     print("THE BOOK IS BORROWED BY OUR VALUABLE CUSTOMER SO WE CANT REMOVE BOOK AT THIS MOMENT !")
##                     c.execute(''' delete from books where book_name=%s and author_name=%s ''',(book_name,author_name))
##                     mydb.commit()
##                     print('YOU HAVE SUCCESSFULLY REMOVE A BOOK FROM LIBRARY ')                 

                 else:
                     c.execute(''' select count(*) from books
where book_name=%s and author_name=%s
''',(book_name,author_name))
                     
                     res1=c.fetchall()
                     res1=str(res1)
                     res1=res1.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                     res1=int(res1)
                     if res1>0:
                     
                         c.execute(''' delete from books where book_name=%s and author_name=%s ''',(book_name,author_name))
                         mydb.commit()
                         print('YOU HAVE SUCCESSFULLY REMOVE A BOOK FROM LIBRARY ')
                     else:
                         print('WE DONOT HAVE THAT BOOK IN OUR LIBRARY')
                 
             
                    
             
             
                
                
    def edit(self):
        while True:
             print(" WELCOME TO ADMIN EDIT BOOK SECTION ")
         ##      print(" WELCOME TO ADMIN LOGIN AREA ")
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                    break
             book_name=input('ENTER BOOK NAME: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()
             #pub_date=input('ENTER PUBLISHED DATE IN FORMAT [ DD/MM/YYYY ]: ').lower()
             if book_name=='' or author_name=='':
                  print('PLZ FILL ALL THE INPUT BOXES ')
             else:
               #  c.execute(''' select count(*) from books where book_name=%s and author_name=%s ''',(book_name,author_name))
                 c.execute(''' select count(*) from books
where book_name=%s and author_name=%s and book_id in(select book_id from borrowed_books)
''',(book_name,author_name))
                 res=c.fetchall()
                 res=str(res)
                 res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 res=int(res)

                 if res>0:
                     print("THE BOOK IS BORROWED BY OUR VALUABLE CUSTOMER SO WE CANT UPDATE BOOK AT THIS MOMENT !")

                     

                 else:
                     c.execute(''' select count(*) from books
where book_name=%s and author_name=%s
''',(book_name,author_name))
                     
                     res1=c.fetchall()
                     res1=str(res1)
                     res1=res1.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                     res1=int(res1)
                     if res1>0:
                         
                         new_book_name=input('ENTER NEW BOOK NAME: ').lower()
                         new_author_name=input('ENTER NEW AUTHOR NAME: ').lower()
                         new_pub_date=input('ENTER PUBLISHED DATE IN FORMAT [ DD/MM/YYYY ]: ').lower()
                         
                         c.execute(''' update books set book_name=%s,author_name=%s,published_date=%s
where book_name=%s and author_name=%s ''',(new_book_name,new_author_name,new_pub_date,book_name,author_name))
                         
                         mydb.commit()
                         print('YOU HAVE SUCCESSFULLY UPDATED A BOOK FROM LIBRARY ')
                         print('[',book_name,author_name,']',' => ','[',new_book_name,new_author_name,new_pub_date,']')
                     
                     else:
                         print('WE DONOT HAVE THAT BOOK IN OUR LIBRARY')
                 
                    
    def cancel_ad_mem(self):
        while(True):
            print(" WELCOME TO ADMIN CANCEL MEMBERSHIP SECTION ")
            ##   print(" WELCOME TO ADMIN LOGIN AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            ad_name=input('ENTER YOUR NAME: ')
            ad_pass=input('ENTER YOUR PASSWORD: ')
            if ad_name=='' or ad_pass=='':
                print('PLZ FILL ALL INPUT BOXES! ')
            else:
                c.execute(''' select count(*) from person p, admin a where a.id=p.id and p.user_name=%s and p.user_password=%s ''',(ad_name,ad_pass))
                res=c.fetchall()
                res=str(res)
                res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                res=int(res)
                if res >0:
                    c.execute(''' delete from person where user_name=%s and user_password=%s ''',(ad_name,ad_pass))
                    mydb.commit()
                    print(ad_name,'YOUR MEMBERSHIP HAS BEEN SUCCESFULLY CANCELED! ')
                    break
                


                else:
                    print('THERE IS NO ACCOUNT WITH THIS USERNAME OR PASSWORD')
    def show_borrowed(self):
        while(True):
            print(" WELCOME TO ADMIN BORROWED BOOK SECTION ")
         
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            c.execute(''' select p.user_name,bk.book_name,bk.author_name,br.borrowed_date,br.end_date from
person p , books bk , borrowed_books br where p.id=br.cus_id and bk.book_id=br.book_id
''')
            output=c.fetchall()
            df=pd.DataFrame(output,  columns=['user_name','book_name','author_date','borrowed_date','end_date'])
            print(df)
            
    def show_reserved(self):
          
        while(True):
            print(" WELCOME TO ADMIN RESERVED BOOK SECTION ")
            
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            c.execute(''' select p.user_name,bk.book_name,bk.author_name,br.reserved_date from
person p , books bk , reserved_books br where p.id=br.cus_id and bk.book_id=br.book_id
''')
            output=c.fetchall()
            df=pd.DataFrame(output, columns=['book_name','author_name','reserved_date'])
            print(df)
            
        
           
                
    ## customer staff    
    def cancel_cus_mem(self):
        while(True):
            print(" WELCOME TO CUSTOMER CANCEL MEMBERSHIP SECTION ")
            ##print(" WELCOME TO ADMIN LOGIN AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            cu_name=input('ENTER YOUR NAME: ')
            cu_pass=input('ENTER YOUR PASSWORD: ')
            if ad_name=='' or ad_pass=='':
                print('PLZ FILL ALL INPUT BOXES! ')
            else:
                c.execute(''' select count(*) from person p, customer c where c.id=p.id and p.user_name=%s and p.user_password=%s ''',(ad_name,ad_pass))
                res=c.fetchall()
                res=str(res)
                res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                res=int(res)
                if res >0:
                    c.execute(''' delete from person where user_name=%s and user_password=%s ''',(cu_name,cu_pass))
                    mydb.commit()
                    print(cu_name,'YOUR MEMBERSHIP HAS BEEN SUCCESFULLY CANCELED! ')
                    break
                


                else:
                    print('THERE IS NO ACCOUNT WITH THIS USERNAME OR PASSWORD')        
                            
                
            
        
                    
                    

    def search(self):
        while True:
             print(" WELCOME TO SEARCH BOOK SECTION ")
       #  print(" WELCOME TO ADMIN LOGIN AREA ")
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                    break
             book_name=input('ENTER BOOK NAME: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()            
             if book_name=='' or author_name=='':
                  print('PLZ FILL ALL THE INPUT BOXES ')
             else:
                 c.execute(''' select count(*) from books where book_name=%s and author_name=%s ''',(book_name,author_name))
                 res=c.fetchall()
                 res=str(res)
                 res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 res=int(res)

                 if res>0:
                     c.execute(''' select book_name,author_name,published_date from books where book_name=%s and author_name=%s ''',(book_name,author_name))
                     output=c.fetchall()
                     df=pd.DataFrame(output, columns=['book_name','author_name','published_date'])
                     print(df)

                 else:
                     print('WE DONOT HAVE THAT BOOK IN OUR LIBRARY')
                 
                 
    def show_collection(self):
        while True:
            print(" WELCOME TO ADMIN BOOK COLLECTION SECTION ")
          ##  print(" WELCOME TO ADMIN LOGIN AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            c.execute(''' select book_name,author_name,published_date from books''')
            output=c.fetchall()
            df=pd.DataFrame(output, columns=['book_name','author_name','published_date'])
            print(df)


    def reserve(self):
        while True:
             
             print(" WELCOME TO RESERVE BOOK SECTION ")
          ##  print(" WELCOME TO ADMIN LOGIN AREA ")
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                break
             book_name=input('ENTER BOOK NAME: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()
             if book_name=='' or author_name=='':
                 print('PLZ FILL ALL INPUT BOXES')
             else:             
                 #1
                 c.execute('''select count(*) from books
    where book_name=%s and author_name=%s and book_id in (select book_id from reserved_books)''',(book_name,author_name))
                 
                 res=c.fetchall()
                 res=str(res)
                 res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 res=int(res)

                 #2
                 c.execute('''SELECT count(*) from books
    where book_name=%s and author_name=%s and book_id not in (select book_id from reserved_books)and book_id not in(select book_id from borrowed_books)''',(book_name,author_name))
                 res5=c.fetchall()
                 res5=str(res5)
                 res5=res5.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 res5=int(res5)
                 
                 
                 if res>0:
                     print("THE BOOK IS ALREADY RESERVED BY OUR VALUABLE CUSTOMER SO YOU CANNOT RESERVED THE BOOK AT THE MOMENT !")

                 elif res5>0:
                      print("THE BOOK ALREADY AVAILABLE YOU CAN BORROW IT !")
                 else:
                     c.execute(''' select count(*) from books
    where book_name=%s and author_name=%s
    ''',(book_name,author_name))
                     
                     res1=c.fetchall()
                     res1=str(res1)
                     res1=res1.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                     res1=int(res1)
                     if res1>0:
                         #for book id
                         c.execute('''select book_id from books where book_name=%s and author_name=%s''',(book_name,author_name))
                         res2=c.fetchall()
                         res2=str(res2)
                         res2=res2.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                        
                         #for customer id
                         c.execute('''select id from person where user_name=%s''',(self.name_cus))
                         res3=c.fetchall()
                         res3=str(res3)
                         res3=res3.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")

                     
                         c.execute(''' insert into reserved_books(book_id,cus_id) values(%s,%s) ''',(res2,res3))
                         mydb.commit()
                         print('YOU HAVE SUCCESSFULLY RESERVED A BOOK FROM LIBRARY ')
                     else:
                         print('WE DONOT HAVE THAT BOOK IN OUR LIBRARY')
                     

    def borrow(self):
        while True:
           
             print(" WELCOME TO BORROW BOOK SECTION ")
          ##  print(" WELCOME TO ADMIN LOGIN AREA ")
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                break
            # taking input
             book_name=input('ENTER BOOK NAME: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()
             if book_name=='' or author_name=='':
                 print('PLZ FILL ALL INPUT BOXES')
             else:

                 
                 c.execute('''select count(*) from books
    where book_name=%s and author_name=%s and (book_id in (select book_id from borrowed_books) or book_id in (select book_id from reserved_books))''',(book_name,author_name))
                 
                 res=c.fetchall()
                 res=str(res)
                 res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                 res=int(res)

                 if res>0:
                     print("THE BOOK IS BORROWED OR RESERVED BY OUR VALUABLE CUSTOMER SO YOU CANNOT BORROWED THE BOOK AT THE MOMENT !")
    ##                     c.execute(''' delete from books where book_name=%s and author_name=%s ''',(book_name,author_name))
    ##                     mydb.commit()
    ##                     print('YOU HAVE SUCCESSFULLY REMOVE A BOOK FROM LIBRARY ')                 

                 else:
                     c.execute(''' select count(*) from books
    where book_name=%s and author_name=%s
    ''',(book_name,author_name))
                     
                     res1=c.fetchall()
                     res1=str(res1)
                     res1=res1.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                     res1=int(res1)
                     if res1>0:
                         #for book id
                         c.execute('''select book_id from books where book_name=%s and author_name=%s''',(book_name,author_name))
                         res2=c.fetchall()
                         res2=str(res2)
                         res2=res2.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                        
                         #for customer id
                         c.execute('''select id from person where user_name=%s''',(self.name_cus))
                         res3=c.fetchall()
                         res3=str(res3)
                         res3=res3.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")

                         # for taking end date
                         # taking input as the current date
                         # today() method is supported by date 
                         # class in datetime module
                         Begindatestring = date.today()
                          
                         # print begin date
    ##                     print("Beginning date")
                         #print(Begindatestring)
                          
                        # calculating end date by adding 4 days
                         end_date = Begindatestring + timedelta(days=4)
                          
                         # printing end date
    ##                     print("Ending date")
    ##                     print(Enddate)

                         
                         
                     
                         c.execute(''' insert into borrowed_books(book_id,cus_id,end_date) values(%s,%s,%s) ''',(res2,res3,end_date))
                         mydb.commit()
                         print('YOU HAVE SUCCESSFULLY BORROWED A BOOK FROM LIBRARY ')
                     else:
                         print('WE DONOT HAVE THAT BOOK IN OUR LIBRARY')
            
    def renew(self):
        while True:
             print(" WELCOME TO RENEW BOOK SECTION ")
         
             inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
             if inp=="back":
                break
            # taking input
             # FOR CUST_ID
             c.execute('''select id from person where user_name=%s''',(self.name_cus))
             res3=c.fetchall()
             res3=str(res3)
             res3=res3.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
             #
             book_name=input('ENTER BOOK NAME YOU WANT TO RENEW: ').lower()
             author_name=input('ENTER AUTHOR NAME: ').lower()
            
             

                         
             if book_name=='' or author_name=='':
                 print('PLZ FILL ALL INPUT BOXES')
             else:
                 b=c.execute('''select end_date from borrowed_books
        where book_id in (select book_id from books  where book_name=%s and author_name=%s) and  cus_id=%s''',(book_name,author_name,res3))
                 if b:
                     res4=c.fetchall()
                 
                     res4=str(res4)
                     res4=res4.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                     print(res4,type(res4))
                   
                     a=datetime.strptime(res4,"%Y-%m-%d").date()
                                
                     end_date = a + timedelta(days=24)
                     result=c.execute('''select count(*) from books bk,borrowed_books bb
            where bk.book_id=bb.book_id and bk.book_name=%s and bk.author_name=%s and bb.cus_id=%s''',(book_name,author_name,res3))
                     if result:
                             c.execute('''update borrowed_books set end_date=%s where book_id in(select book_id from books)''',(end_date))
                             mydb.commit()
                             print("BOOK IS SUCCESSFULLY RENEWED")
                     else:
                             print("THE BOOK IS NOT RENEWD")
                 else:
                     print("THE BOOK IS NOT IN OUR LIBRARY")

    def returnn(self):
        while True:
            print(" WELCOME TO RETURN BOOK SECTION SECTION ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break

            #for cut_id
            c.execute('''select id from person where user_name=%s''',(self.name_cus))
            res3=c.fetchall()
            res3=str(res3)
            res3=res3.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")

            
            
            book_name=input('ENTER BOOK NAME YOU WANT TO RETURN: ').lower()
            author_name=input('ENTER AUTHOR NAME: ').lower()
            if book_name=='' or author_name=='':
                print('PLZ FILL ALL INPUT BOXES')
            else:
                b=c.execute('''delete from borrowed_books where 
         book_id in (select book_id from books  where book_name=%s and author_name=%s) and  cus_id=%s''',(book_name,author_name,res3))
                if b:
                     mydb.commit()
                     print("YOU HAVE SUCCESSFULLY RETURNED THE BOOK")
                else:
                    print("THE BOOK IS NOT IN OUR LIBRARY")
                
            
        
                 
         
    def see_review(self):
        while True:
            print(" WELCOME TO ADMIN REVIEW SECTION ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            
            c.execute('''select p.user_name,r.customer_rating,r.customer_review,r.Date_Time
    from review_table r left outer join  person p
    on p.id=r.customer_id''')
        
            result=c.fetchall()
            df=pd.DataFrame(result, columns=['user_name','customer_rating','customer_review','Date_Time'])
            print(df)
            

    def give_review(self):
        while(True):
            print(" WELCOME TO REVIEW AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            
            rating=input('GIVE US RATING FROM 1-9: ')
            review=input('GIVE US YOUR FEEDBACK: ').lower()
            
            if rating=='' or review=='':
                print("PLZ FILL ALL INPUT BOXES !")
            else:
              
                name=self.name_cus
               
                
                c.execute('select id from customer where id=(select id from person where user_name=%s)',(name))
                
            
                res=c.fetchall()
                res=str(res)
                res=res.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
                
                
                
                c.execute('insert into review_table(customer_id,customer_rating,customer_review) values(%s,%s,%s)',(res,rating,review))
                mydb.commit()
                print('YOUR REVIEW HAS BEEN RECIEVED !')
                break
            
        
        
        

        
    def admin_signup(self):
        t=True
        while(t):
            print(" WELCOME TO ADMIN SIGNUP AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            c.execute('''SELECT count(*) from person''')
            op=c.fetchall()
            op=str(op)
            op=op.strip("(").strip(")").strip(",").strip(")").strip(",")
            if op==():
                op='AD-'+str(0)
            else:
                op='AD-'+str(op)
                
        ## for admin
            c.execute('''SELECT count(*) from admin''')
            ad=c.fetchall()
            ad=str(ad)
            ad=ad.strip("(").strip(")").strip(",").strip(")").strip(",")
            if ad==():
                ad='ADMIN-'+str(0)
            else:
                ad='ADMIN-'+str(ad)                    
      ##
                
            name=input('Enter your name : ')
            passw=input('Enter passwords: ')

            c.execute('select count(user_name) from person where user_name=%s',(name))
            invalid=c.fetchall()

            #####
            inv=str(invalid)
            inv=inv.strip("(").strip(")").strip(",").strip(")").strip(",")
            inv=int(inv)
            
        




            #####
            #VALIDATION
            if inv>0:
                print('User name already occupied plz select different user name !')
            elif name==''or passw=='':
                print('PLZ FILL ALL THE INPUT BOXES ! ')
            else:
            
                c.execute('''insert into person values (%s, %s, %s)''', (op,name,passw)) 
                c.execute('''insert into admin values(%s,%s)''', (op,ad))
                mydb.commit()
                
                print(name.upper(),'YOUR ACCOUNT HAS BEEN CREATED')
                t=False
            
            
        
    def admin_login(self):
        t=True
        while(t):

            print(" WELCOME TO ADMIN LOGIN AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            
            name=input('Enter your name : ')
            passw=input('Enter password: ')
            result=c.execute('select *  from person p,admin a where p.user_name = %s AND p.user_password= %s AND p.id=a.id limit 1',(name,passw))
            if result==True:

                while(True):
                    print('''              ENGINNER ABDUL KALAM LIBRARY 
                
    1) ADD BOOK 
    2)REMOVE BOOK
    3)EDIT BOOK
    4)RESERVED BOOKS
    5)BORROWED BOOKS
    6)SEE REVIEWS
    7)CANCEL MEMBERSHIP
    8) EXIT
    ''') 
                    try:

                        n=int(input('enter your choice: '))

                        if n==1:
                            l.add()
                        elif n==2:
                            l.remove()
                        elif n==3:
                            l.edit()
                        elif n==4:
                            l.show_reserved()
                        elif n==5:
                            l.show_borrowed()

                        elif n==6:
                            l.see_review()
                        elif n ==7:
                            l.cancel_ad_mem()
                        elif n==8:
                            print('Thanks you for visiting our library :) !')
                            t=False
                            break
                        else:
                            print("WRONG INPUT !")

                    except:
                        print('PLZ INPUT INTEGER VALUE')
            else:
                print('WRONG USER NAME OR PASSWORD')





            
    def customer_signup(self):
        t=True
        while(t):
            print(" WELCOME TO CUSTOMER SIGNUP AREA ")
            try:
                inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
                if inp=="back":
                    break
                
                c.execute('''SELECT count(*) from person''')
                op=c.fetchall()
                op=str(op)
                op=op.strip("(").strip(")").strip(",").strip(")").strip(",")
                if op==():
                    op='CUS-'+str(0)
                else:
                    op='CUS-'+str(op)

                name=input('Enter your name : ')
                passw=input('Enter passwords: ')

                c.execute('select count(user_name) from person where user_name=%s',(name))
                invalid=c.fetchall()

                #####
                inv=str(invalid)
                inv=inv.strip("(").strip(")").strip(",").strip(")").strip(",")
                inv=int(inv)
                
                
        




                #####
                #VALIDATION
                if inv>0:
                    print('User name already occupied plz select different user name !')
                elif name==''or passw=='':
                    print('PLZ FILL ALL THE INPUT BOXES ! ')
                else:
                    
                    c.execute('''insert into person values (%s, %s, %s)''', (op,name,passw)) 
                    c.execute('''insert into customer(id) values(%s)''', (op))
                    mydb.commit()
                    
                    print(name.upper(),'YOUR ACCOUNT HAS BEEN CREATED')
                    t=False
            except:
                print('PLZ INPUT INTEGER VALUE ! ')
            
    def customer_login(self):
        t1=True
        while(t1):
            print(" WELCOME TO CUSTOMER LOGIN AREA ")
            inp=input(" PRESS ENTER TO CONTINUE OR WRITE BACK TO GO BACK IN OPTIONS: ").lower()
            if inp=="back":
                break
            self.name_cus=input('Enter your name : ')
            passw=input('Enter password: ')
            result=c.execute('select *  from person p,customer c where p.user_name = %s AND p.user_password= %s AND c.id=p.id limit 1',(self.name_cus,passw))
            if result==True:

                while(True):
                    print('''              ENGINNER ABDUL KALAM LIBRARY 
                
    1)SEARCH BOOK
    2)RESERVE BOOK
    3)BORROW BOOK
    4)RENEW BOOK
    5)RETURN BOOK
    6)CANCEL MEMBERSHIP
    7)COLLECTION OF BOOKS
    8)GIVE REVIEW
    9) EXIT
    ''')
                    try:

                        n=int(input('enter your choice: '))

                        if n==1:
                            l.search()
                        elif n==2:
                            l.reserve()
                        elif n==3:
                            l.borrow()
                        elif n==4:
                            l.renew()
                        elif n==5:
                            l.returnn()

                        elif n==6:
                            l.cancel_cus_mem()
                        elif n ==7:
                            l.show_collection()
                        elif n ==8:
                            l.give_review()                    
                        elif n==9:
                            print('Thanks you for visiting our library :) !')
                            t1=False
                            break
                        else:
                            print("WRONG INPUT !")
                          

                    except:
                        print('PLZ INPUT INTEGER VALUE')
            else:
                print('WRONG USERNAME OR PASSWORD')





        
        
        


       
        
    
        
                  
                      


while True:
    

    l=library()
    print(''' WELCOME TO  ENGINNER ABDUL KALAM LIBRARY
    1) Customer Portal
    2) Admin Portal
    3) Exit''')
    n=int(input('enter your choice: '))
    if n==1:
        while True:
            print('''WELCOME TO STUDENT PORTAL
            1) LOGIN AREA
            2) SIGNUP AREA
            3) BACK''')
            n1=int(input('enter your choice: '))
            if n1==1:
                l.customer_login()
                   
                    
            elif n1==2:
                l.customer_signup()

            elif n1==3:
                break

            else:
                print("WRONG INPUT !")
            
    elif n==2:
        while True:
            print('''WELCOME TO ADMIN PORTAL
            1) LOGIN AREA
            2) SIGNUP AREA
            3) BACK''')        
            n3=int(input('enter your choice: '))
            if n3==1:
                l.admin_login()
                   
                    
            elif n3==2:
                l.admin_signup()
                
            elif n3==3:
                break

            else:
                print("WRONG INPUT !")
    elif n==3:
        print('Thankyou for visiting our library :)')
    else:
        print('WRONG INPUT !')
            
    
#     name=input('enter your name: ')
#     if name.lower() in customers or name in librarian:
#         print('''              ENGINNER ABDUL KALAM LIBRARY 
# 1) ADD BOOK 
# 2)REMOVE BOOK
# 3)EDIT BOOK
# 4)SEARCH BOOK
# 5)RESERVE BOOK
# 6)BORROW BOOK
# 7)RENEW BOOK
# 8)RETURN BOOK
# 9)CANCEL MEMBERSHIP
# 10)COLLECTION OF BOOKS
# 11) EXIT
# ''')
#         while(True):
#             try:
            
#                 n=int(input('enter your choice: '))
#                 if n==1:
#                     l.add()
#                 elif n==2:
#                     l.remove()
#                 elif n==3:
#                     l.edit()
#                 elif n==4:
#                     l.search(res)
#                 elif n==5:
#                     l.reserve()
#                 elif n==6:
#                     l.borrow()
#                 elif n==7:
#                     l.renew()
#                 elif n==8:
#                     l.returnn()

#                 elif n==9:
#                     l.cancel_membership()
#                 elif n ==10:
#                     l.show_collection()
#                 elif n==11:
#                     print('Thanks you for visiting our library :) !')
#                     break
                        
#             except:
#                 print('PLZ INPUT INTEGER VALUE')
#     elif name.lower() not in customers:
        
#         print()
#         print('you have to purchase our member ship in order to avail our services')
#         print()
    
#         inp=input('Do you want to purchase our member ship if yes than type yes/YES: ') 
       
        
#         if inp=='yes' or inp=='YES':
#             l.register_account()
#         else:
#             print('Thankyou for visiting our library :)')

        
    



        
        
