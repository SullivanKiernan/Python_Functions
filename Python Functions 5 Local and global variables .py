
x = 25
def greet ():
    message = "a"
    
def send_email ():
    message = "b"
     
#these are examples of local variables. They onlt exist within their set def; this means that you can set "message" 
# to multiple different meqaning/values bacause they reset once the next def is used. 
#global variables are the variables set outside the def functions, they are the ones that are typically used. in this example
# x would be the globabl variable, and in each def function, unless otherwise stated, x will be equal to 25.