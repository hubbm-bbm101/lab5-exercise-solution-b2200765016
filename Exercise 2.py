status = False

while status == False:
    e_mail = input("Enter your e_mail: ")
    if "@" and "." in e_mail:
        status = True
        print("You entered your e-mail correctly")
    elif "." in e_mail :
        status = False
        print("You have to use . in your e-mail.")
    elif "@" in e_mail:
        status = False
        print("You have to use @ in your e-mail.")
    elif "@" and "." not in e_mail:
        status = False
        print("You have to use @ and . in your e mail.")