# Exercise 1:
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
for sale in sales:
    total += sale   # update
print(f"Total: ${total}")


# Exercise 2:
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0      
count = 0
for sale in sales:
    total += sale   # update
    count += 1
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")


# Exercise 3:
sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale  
print(f"Largest Sale: ${current_max}")


# Exercise 4:
sales = [120, 80, 250, 175, 90, 410, 60, 215]
count = 0
total = 0

for sale in sales: # Loop through sales and accumulate only those over $100
    if sale > 100:
        count += 1
        total += sale
print(f"Sales over $100: {count}")
print(f"Total of those sales: ${total}")


# Exercise 5:
sales = [120, 80, 250, 175, 90, 410, 60, 215]

for sale in sales:
    if sale > 400: # Check for the outlier first to stop the loop
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    
    if sale <= 100: # Skip sales that are $100 or less
        continue

    print(f"${sale}")


# Exercise 6:
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0  # index

while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total sales: ${total}")

# In production, I would use the `for` loop version. The `for` loop is shorter, more readable, and less error-prone because Python handles indexing and iteration automatically without requiring manual index management (i += 1).


# Exercise 7:
sales = [120, 80, 250, 175, 90, 410, 60, 215]

for sale in sales:
    if sale >= 200:
        discount_rate = 0.10
        discount_str = "10%"
    elif sale >= 100:
        discount_rate = 0.05
        discount_str = "5%"
    else:
        discount_rate = 0.0
        discount_str = "0%"

    discounted_price = sale * (1 - discount_rate)
    print(f"${sale} -> {discount_str} discount -> ${discounted_price:.2f}")


# Answers to Self-assessment questions:
#1 The accumulator pattern is a way to keep running totals or counts as you go through a list. First, you initialize a variable like total = 0 to create a clean starting point (clean slate) before counting. Then you loop through the list and update the total with total += sale on each step. Lastly, you print or use the result after the loop finishes so you can see the total sum.
#2 The while loop required extra code because you have to set up an index variable and increase it manually. A for loop is shorter, easy to read and less risky because Python automatically moves to the next item. A while loop gives you more direct control over the index position but it risks creating an infinite loop if you forget to increment the index variable.
#3 You can use a loop to summarize a list of store sales figures. The list would store individual customer purchase amounts from a shift. The loop would accumulate the sum of all purchases into a single running total. At the end, the program would print the total revenue generated for that day.