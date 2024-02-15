# greeting
print("good day welcome to our resturant...")
print("how much is your total purchase?")


purchase_cost = float(input("$ "))
tip = 0.03 * purchase_cost
print(f"we'll charge you 3% of what you bought which is {tip}")
total_cost = tip + purchase_cost
print("are you making a joint payment")
print("a. single payment")
print("b. joint payment")
response =input("")
if response == "a": 
    print(f"your total is {total_cost}")
elif response == "b":
    print("how many of you are paying")
    number = int(input())
    payment = total_cost / number
    print(f"you are all to pay ${payment} each")
else:
    print("invalid request")

    
print("are you paying with ")
print("a. cash")
print("b. bank")

response2 = input("")
if response2 == "a" or "cash":
    print("how much cash are you paying with ")
    cash = float(input ("$"))
    change = cash - total_cost
    if cash < total_cost:
        print(" alaye get the fuck out joor")
    elif cash >= total_cost:
        print(f" your change is ${change}")
        
if change == 0: 
    print(" you dont have any balance with us")


elif response2 == "b" or "bank":
    print("ok that's fine")



    




