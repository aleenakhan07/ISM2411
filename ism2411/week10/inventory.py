# Exercise 1: Build a list

print("---Exercise 1: Build a List---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index practice

print("---Exercise 2: Index Practice---")
print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hardcoded)

# Exercise 3: 

print("---Exercise 3: List Slicing---")

print(inventory[:3]) # grabs the first 3 items
print(inventory[-2:]) # grabs the last 2 items
print(inventory[::2]) # skips 1

# Exercise 4

print("---Exercise 4: List Methods---")
inventory.append("envelope") # .append adds an item to the end of the list

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

# Exercise 5:

print("---Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060) # New York City Coordinates

# coords[0] = 99 this will raise a type error because tuples are immutable
try:
    coords[0] = 99 
except TypeError as error:
    print(f"TypeError Caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

# Exercise 6:

print("---Exercise 6: List Average Sales---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total Sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average Sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sale: {min(sales)}")


# Exercise 7:

print("---Exercise 7: Accumulator Pattern---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount # the 2 here rounds to 2 dp

print(price)
print(discounted)


# Exercise 8: 

print("---Exercise 8: Filter---")
sales= [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales: # never use remove when looping over a list
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")


## Reflection

#1 Python lists can hold different types of data at the same timeand change size automatically without any setup. Shortcuts like list comprehensionsalso make sorting through data much quicker than writing long loops.

#2 Looking at monthly sales report or item lists across hundreds of different files manually in Excel takes too long and leads to mistakes. Using a python list with a loop lets you put all the information together instantly.