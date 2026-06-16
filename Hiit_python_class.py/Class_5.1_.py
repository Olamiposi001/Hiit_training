product = "shoe"

if product == "shoe" or product == "bag":
    print("You will get a 10% discount on your purchase")

age = 18
if age >= 18:
    print("You are an adult")


age = 16
if age >= 18:
    print("You can vote")
else:
    print("You are not old enough to vote")
    
    
score = 75

if score >= 70:
    print("Excellent")
elif score >= 50:
    print("Passed")
else:
    print("Failed")

age = 20
has_id = True
if age >= 18 and has_id == True:
    print("Access granted")
    


age = 20
has_id = True
if age > 18:
    if has_id == True:
        print("Access granted")
    else:
        print("You need an ID")
else:
    print("You are undrage")



User_logged_in = True
cart_total = 750
payment_method = "credit card"
acceptable_payment_methods = ["credit card", "cash"]

# if user logged_in:
# and
# if user logged_in == True:
# are the same thing

# if not user_logged_in:
# and
# if user_logged_in == False:
# are the same thing

if User_logged_in:
    if cart_total > 0:
        if payment_method in acceptable_payment_methods :
            print("processing payment")
        else:
            print("Please get a Card or cash")
    else:
        print("Your cart is empty")
else:
    print("Please log in")