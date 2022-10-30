import json
with open("login.json",'r') as f:
    data = json.load(f)
username = input("Enter the username")
password = input("Enter the password")
info = {
    "Login_username" : username,
    "Login_password" : password,       
}
if input("Enter \"yes\" if above detail is your account details : ") == "yes":
    for row in data:
        for i in range(len(data)):
            if username.lower() == row["Login_username"] and password.lower() == row["Login_password"]:
                print("welcome to python course") 
                break
elif input("if you new for Python Course then Enter \"yes\"") == "yes":
         if input("Enter \"yes\" if you want to add above username & password") == "yes":
             with open("login.json","r") as f:
                 data = json.load(f)
             data.append(info)
             with open("login.json","w") as f:
                 json.dump(data, f,indent=4)
             print(data)
             print("Successfully added ")
             
         elif input("If you want to new account \"CREATE NEW\"").lower() == "create new":
             username1 = input("Enter the username")
             password1 = input("Enter the password")
             info1 = {
                 "Login_username" : username1,
                 "Login_password" : password1,       
             }
             with open("login.json","r") as f:
                 data = json.load(f)
             data.append(info1)
             with open("login.json","w") as f:
                 json.dump(data, f,indent=4)
             print("Sccessfully added")
             # print(data)
             print("Welcome to python course")
         else:
             print("Thank you for visiting")
else:
    print("Thank you for visiting")