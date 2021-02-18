from database_operation import *
import sys
while(True):
    print('**************************contact book*******************************')
    print('1) new contact')
    print('2) view contact')
    print('3) delete contact')
    print('4) exit')
    print(' enter your choice to continue:')
    choice=int(input())
    if choice==4:
        sys.exit(0)
    elif choice==1:
        print('enter the name')
        name=input()
        print('enter the number')
        num=int(input())
        print('enter address')
        address=input()
        write_to_database(name,num,address)
        print("saved successfully")
    elif choice==2:
        print('enter the name')
        name=input()
        result=fetch_by_name(name)
        if result==[]:
            print("no record found")
        else:
            print(f" the number of {name} is {result[0][1]} ")
    else:
        print('enter a number to delete')
        num=int(input())
        delete_from_base(num)
        print('deletion success')








