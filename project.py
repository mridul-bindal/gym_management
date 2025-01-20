import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="BlackPearl",db="fitness")
curr=conn.cursor()
print("success")

def main1():
        print('*-'*15,'WELCOME','*-'*15)
        print('\n','\t'*3,'   Enter Action to Perform:')
        print('\t'*3,'1. Check List of Members','\n','\t'*3,'2. Add New Member','\n','\t'*3,'3. Find Member','\n','\t'*3,'4. Update Member Information')
        a=int(input('\t                Enter Choice:'))
        if a==1:
                check_list()
        elif a==2:
                q="SELECT * FROM MEMBER ORDER BY GYM_ID DESC LIMIT 1;"
                curr.execute(q)
                print("Last Record ID =>",curr.fetchone())
                id2=input("Enter GYM ID:")
                name=input("Enter Name:")
                age=int(input("Enter Age:"))
                mem=(input("Membership:"))
                day=(input("Days Fixed:"))
                add_new(id2,name,age,mem,day)
        elif a==3:
                i=input("ID or Name =>")
                ip=input("Search =>")
                if i in ('ID','id','Id'):
                        find1(ip)
                else:
                        find2(ip)
        elif a==4:
                id1=input('Enter ID Number Of MEMBER:')
                print("Records=>","\n1. Membership","\n2. Age.")
                rec=int(input("Enter Record to Update(Sr no.):"))
                if rec==1:
                        change_membership(id1)
                elif rec==2:
                        change_age(id1)
               

def check_list():
        q="SELECT * FROM MEMBER;"
        curr.execute(q)
        print(curr.fetchall())
        ent=input("Continue?(Y/N):")
        if ent=="Y":
                main1()
def add_new(id2,name,age,mem,day):
        q="INSERT INTO MEMBER(GYM_ID,NAME,AGE,MEMBERSHIP,DAYS_FIXED) VALUES('{}','{}',{},'{}','{}');".format(id2,name,age,mem,day)
        curr.execute(q)
        conn.commit()
        print("Successfully Updated")
        ent=input("Continue?(Yes/No):")
        if ent=="Y":
                main1()
def find1(ip):
        q="SELECT GYM_ID, NAME, AGE, MEMBERSHIP,DAYS_FIXED FROM MEMBER WHERE GYM_ID='%s';" % ip
        curr.execute(q)
        print(curr.fetchone())
        ent=input("Continue?(Y/N):")
        if ent=="Y":
                main1()
def find2(ip):
        q="SELECT GYM_ID, NAME, AGE, MEMBERSHIP, DAYS_FIXED FROM MEMBER WHERE NAME='%s';" % ip
        curr.execute(q)
        print(curr.fetchone())
        ent=input("Continue?(Y/N):")
        if ent=="Y":
                main1()
def change_membership(id1):
        q1="SELECT GYM_ID, NAME FROM MEMBER WHERE GYM_ID ='%s';" % id1
        curr.execute(q1)
        print("Saved Record =>",curr.fetchone())
        change=input('Enter Membership(Monthly/Yearly):')
        q="UPDATE MEMBER SET MEMBERSHIP='%s' WHERE GYM_ID='%s';" % (change,id1)
        curr.execute(q)
        conn.commit()
        print('Successfully Updated')
        ent=input("Continue?(Y/N):")
        if ent=="Y":
                main1()

def change_age(id1):
        q1="SELECT GYM_ID, NAME, AGE FROM MEMBER WHERE GYM_ID='%s';" % id1
        curr.execute(q1)
        print("Saved Record =>",curr.fetchone())
        change=int(input('Enter AGE.:'))
        q="UPDATE MEMBER SET AGE='%s' WHERE GYM_ID='%s';" % (change,id1)
        curr.execute(q)
        conn.commit()
        print('Successfully Updated')
        ent=input("Continue?(Y/N):")
        if ent=="Y":
                main1()


main1()
print('*-'*15,"Thank You",'*-'*14)
print('Logging Out...............')
