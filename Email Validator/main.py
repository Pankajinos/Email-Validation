def check_name(username):
    if( not len(username)):
        print("Invalid email")
        print("No username ")
        return 0
    if(username[0]=='.' or username[-1]=='.'):
        print("Invalid domain")
        print("Username can't start and end with dot")
        return 0

    for i in username:
        if(i.isalnum() or i=='.' or i=='_' or i=='+' or i=='-'):
            pass

        
        else:
            print("Invalid email")
            print(i,":","is alphabet, number or [. _ + -] ")
            return 0
    # checking for two consecutive dots
    temp=username[0]
    for i in range(1,len(username)):
        if(temp==username[i] and temp=='.'):
            print("Invalid Email")
            print("Two consecutive . are not allowed")
            return 0
        temp=username[i]
    return 1

def check_domain(domain):
    if( not len(domain)):
        print("Invalid email")
        print("No domain ")
        return 0
    if(domain[0]=='-' or domain[-1]=='-'):
        print("Invalid domain")
        print("Username can't start and end with -")
        return 0
    if(domain[0]=='.' or domain[-1]=='.'):
        print("Invalid domain")
        print("Username can't start and end with dot")
        return 0
    if(domain.count('.')!=1):
        print("Invalid domain")
        print("No . in domain")
        return 0
    for i in username:
        if(i.isalnum() or i=='-'):
            pass

        
        else:
            print("Invalid email")
            print(i,":","is alphabet, number or - ")
            return 0
        
        return 1


 
email=input("Enter email :")
if(email.count("@")==1):
    l=email.split("@")
    #splitting the domain and username
    username=l[0]
    domain=l[1]
    #checks for username 
    if(check_name(username) and check_domain(domain)):
        print("Valid Email")
    
else:
    print("Invalid domain")
    print("@ is not found or multiple @ are present")
print('')
    
            

        
                