import re
def validate_email() :
    a = input('Enter your mail address : ')
    if re.match(r'[a-zA-Z1-9/./_]+@+[1-9a-zA-Z/./]+[a-zA-Z]{3}$' , a ):
        return print('true')
    else :
        return print('false')

validate_email()