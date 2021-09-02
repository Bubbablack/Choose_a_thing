import random 




choices = []
i= ""
while i != "N" :
    item = input("Enter your items here  type N when your done  ")
    if item == "N":
        i = item
    elif item.endswith("."): 
        choices = [item]
    else:    
        choices.append(item)
    

 
print(random.choice(choices))