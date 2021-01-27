AbhinavList=['Python', 'C++', 'JavaScript', 'HTML', 'CSS']
print ('Hi. Your list is ',AbhinavList)
question=input('Which programming language do you wish to remove?')
if question=='Python':
    AbhinavList.remove('Python')
    print ('OK. Python has been removed.')
    print ('Your new list is ',AbhinavList)
    for q in question:
        while question=='Python':
            question=input('Which programming language do you wish to remove? If you wish to stop, enter STOP. Or, do you want a copy of the List in your mail? If so, enter Mail')
if question=='C++':
    AbhinavList.remove('C++')
    print ('OK. C++ has been removed.')
    print ('Your new list is ',AbhinavList)
    for q in question:
        while question=='C++':
            question=input('Which programming language do you wish to remove? If you wish to stop, enter STOP. Or, do you want a copy of the List in your mail? If so, enter Mail')            
if question=='JavaScript':
    AbhinavList.remove('JavaScript')
    print ('OK. JavaScript has been removed.')
    print ('Your new list is ',AbhinavList)
    for q in question:
        while question=='JavaScript':
            question=input('Which programming language do you wish to remove? If you wish to stop, enter STOP. Or, do you want a copy of the List in your mail? If so, enter Mail')
if question=='HTML':
    AbhinavList.remove('HTML')
    print ('OK. HTML has been removed.')
    print ('Your new list is ',AbhinavList)
    for q in question:
        while question=='HTML':
            question=input('Which programming language do you wish to remove? If you wish to stop, enter STOP. Or, do you want a copy of the List in your mail? If so, enter Mail')
if question=='CSS':
    AbhinavList.remove('CSS')
    print ('OK. CSS has been removed.')
    print ('Your new list is ',AbhinavList)
    for q in question:
        while question=='CSS':
            question=input('Which programming language do you wish to remove? If you wish to stop, enter STOP. Or, do you want a copy of the List in your mail? If so, enter Mail')
if question=='Stop':
    exit()
if question=='Mail':
    recipient=input('Enter your Mail ID.')
    subject='Your List'
    body=AbhinavList
    import webbrowser
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body)
else:
    for q in question:
        question=input('You have entered an invalid option. Which programming language do you wish to remove? If you wish to stop, enter STOP. Or, do you want a copy of the List in your mail? If so, enter Mail')

    

 