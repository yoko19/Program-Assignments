from tkinter import NE
food_prices={"Chicken":1.59, "Beef":1.99, "Cheese":1.00, "Milk":2.50}

Chicken_price = food_prices ["Chicken"]
Beef_price = food_prices ["Beef"]
Cheese_price = food_prices ["Cheese"]
Milk_price = food_prices ["Milk"]

print(food_prices)
print(Chicken_price)

soccer_players={"Messi":30, "Neymar":10, "Ronaldo":7, "Mbappe":7} 
Messi_jersey = soccer_players["Messi"]   #step v
Neymar_jersey = soccer_players["Neymar"]
Ronaldo_jersey = soccer_players["Ronaldo"]
Mbappe_jersey = soccer_players["Mbappe"]
print (Messi_jersey, Neymar_jersey, Ronaldo_jersey, Mbappe_jersey)
print( Messi_jersey) 
 
Shoe_Dictionary = {"Jordan": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
Shoe_Dictionary["SB Dunk"] -= 2 #step 6
Shoe_Dictionary["Yeezy"] += 1

Shoe_Dictionary["Jordan"] += 7
Shoe_Dictionary["Yeezy"] += 7
Shoe_Dictionary["Foamposite"] += 7
Shoe_Dictionary["Air Max"] += 7
Shoe_Dictionary["SB Dunk"] += 7

Shoe_Dictionary["Jordan"] -= 2
Shoe_Dictionary["Yeezy"] -= 2
Shoe_Dictionary["Foamposite"] -= 2
Shoe_Dictionary["Air Max"] -= 2
Shoe_Dictionary["SB Dunk"] -= 2

Messi_jersey["Messi"] = 30 #changing value of a dictionary 
Neymar_jersey["Neymar"] = 10 #step 8
Ronaldo_jersey["Ronaldo"] = 7
Mbappe_jersey["Mbappe"] = 7

del Messi_jersey["Messi"]
del Neymar_jersey["Neymar"]

print(Messi_jersey)