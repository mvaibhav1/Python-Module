# name= input("PLease enter your Name :")

# print("Good Morning",name)

name=input("Please enter the Name :")
date = input("Enter Date in DD-MM-YYYY Format :")

letter= f'''
        Dear <|{name}|>,
        You are slected!
        <|{date}|>
'''
print(letter)