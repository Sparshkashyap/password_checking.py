

# password checking with the help of re->regex ->regular exception

import re

a="Flyall123@"

if((len(a)<6 or len(a)>10 )):
    print("Not Vailed")
    
else:
    if (not re.search(r"[a-z]",a)):
        print("Not Vailed")
        
    if(not re.search(r"[A-Z]",a)):
        print("Not Vailed")
        
    if(not re.search(r"[0-9]",a)):
        print("Not Vailed")
        
    if(not re.search(r"[#$@]",a)):
        print("Not Vailed")
        
    else:
        print("Vailed password")
