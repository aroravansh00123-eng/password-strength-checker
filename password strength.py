import re
def pass_strength(password):
    strength=0
    feedback=[]
    if len(password)>=8:
        strength+=1
    else:
        feedback.append('password should be atleast 8 characters long')
    if re.search(r'[a-z]',password):
        strength+=1
    else:
        feedback.append('add lower case letter example:a,e,i,o,u')
    if re.search(r'[A-Z]',password):
        strength+=1
    else:
        feedback.append('add upper case letter example: A,E,I,O,U')
    if re.search(r'[0-9]',password):
        strength+=1
    else:
        feedback.append('Add numbr to your password')
    if re.search(r'[`~!@#$%^&*()]',password):
        strength+=1
    else:
        feedback.append('add special charactor to your password example !,@,#,$,%,^,&,*,(,)')
    if strength ==5:
        print('STRONG PASSWORD')
    elif strength>3 and strength<5:
        print('MEDIUM PASSWORD')
        print('\n Suggestions:')
        for i in feedback:
            print('-',i)
print('here ypu need to enter your password to check strength of the password:')
password=input('enter your password:')
pass_strength(password)
