import re
def validate_email(email) :
    
    if re.match(r'^[a-zA-Z1-9\.\_]+@[1-9a-zA-Z]+\.[a-zA-Z]{3}$' , email ):
        return print('True')
    else :
        return print('False')

validate_email('saeed.matan@gmail.com')



def validate_number(number) :
   
    if re.match(r'^09[0-9]{9}$' , number ):
        return print('True')
    elif re.match(r'^\+989[0-9]{9}$' , number ) :
        return print('True')
    elif re.match(r'^00989[0-9]{9}$' , number ):
        return print('True')
    else :
        return print('False')

validate_number('09113106546')