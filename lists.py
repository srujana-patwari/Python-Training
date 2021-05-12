vegetables=['Tomato','Cabbage','Potato','Cucumber','Carrot']
print(vegetables)
fruits=['Mango','Banana','Apple']
#vegetables.append(fruits)
vegetables_fruits=[]
vegetables_fruits.append(vegetables)
vegetables_fruits.append(fruits)
print(vegetables_fruits)

vegetables.pop(0)
vegetables.pop(3)
print(vegetables_fruits)