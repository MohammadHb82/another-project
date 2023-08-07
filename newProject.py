print("hello bro your are in my website write know how i can serve you")
print("We are a company specialized in booking submarines for exploration trips")
print("You can choose the specifications you want shortly")
print("___>" *20)
submarines=[]
while True:
    submarine={}
    submarine["size of submarine"]=(input("How many people will this submarine accommodate?"))
    submarine["diving depth"]=int(input("How deep do you want to dive with this submarine?"))
    submarine["Manufacturing company"]=input("enter your Manufacturing company")
    submarine["Technical assistance"]=input("Would you like to take a technical assistant on a diving trip?")
    submarine["manufacturing year"]=input("enter your manufacturing year")
    submarines.append(submarine)
    if input("do you want to add another notfications")=="no":
        break
for i in range(len(submarines)):
    print("___>"*20)
    print(" Click on the submarine whose specifications you have chosen", i + 1)
    for sub in submarines[i]:
        print(sub,":",submarines[i][sub])

print("welcome  coustumer in my website")
print("you can chooze you propertize of your PC")
print("and you can add the model you want ,price,type,...etc")
print("___>"*20)