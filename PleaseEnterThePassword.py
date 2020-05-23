password=input('Enter your password.')
if password=='abhi0607':
    print('You have access.')

else:
    print('Your password is incorrect. Retry again.')
    password=input('Enter your password.')
    if password=="abhi0607":
        print('You have access.')
    else: print('Wrong password. Your account is blocked. To unlock your account, answer your secret question.')
    question=input('Enter your mothers name. One attempt left.')
    if question=='Meenakshi PV':
        print('Your answer is correct. Your account has been unlocked.') 
    else: print('Your account remains blocked. If you wish to unlock it, contact your branch.')
    
    
        
    

