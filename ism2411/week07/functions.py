# Exercise 1

# Defining a function 
def calculate_tax(price, rate):
    return price * rate 

# Calling the function (calling is integral)
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
# print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}") # The danger is that it's not saved anywhere unlike the other taxes



# Exercise 2

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else: 
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")



# Exercise 3

def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"After gold discount: ${apply_discount(200, 'gold'):.2f}")
print(f"After tax: ${apply_discount(200, 'gold') + calculate_tax(apply_discount(200, 'gold'), 0.07):.2f}") # Since this makes the code very difficult to understand, I used ai to help me make this cleaner which I will attach as a comment down below
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


# AI disclosure: AI improved my understanding by helping me make my code more cleaner and readable for myself and others
# discounted = apply_discount(200, 'gold')
# tax = calculate_tax(discounted, 0.07)
# print(f"After tax: ${discounted + tax:.2f}")



# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")



# Exercise 5
# Bug 1 (line 10): missing colon after "for sale in sales". This is a SyntaxError. Fix: add ":".
# Bug 2 (line 6): "total = sale" overwrites instead of adding. Printed $90, not $715. Fix: "total += sale".
# Bug 3 (line 15): "i <= len(sales)" runs one index more, making it an IndexError. Fix: "i < len(sales)".



# Exercise 6

x = 100 # global x
def double_it():
    x = 999 # local x
    return x * 2

print(x) # 100
print(double_it()) # 1998
print(x) # The function ended so local x is gone and here x = 100
# # Scope is where a variable can be seen and used. A variable that is made inside a function is local, so it only exists while the function runs and doesn't change a variable with the same name outside it. A variable made outside any function is global and can be read from anywhere


# Answers to self assessment questions
# The first bug I spotted was the missing colon in line 10 and I found it from the traceback. The traceback for the IndexError then pointed me to the while loop. The print() statements helped me catch the total bug, since the output said $90 and I could see it wasn't adding up. I only used AI last, when I uploaded the error messages. I learned the most from reading tracebacks, then print statements, then AI. This tells me my instinct is to read the error first and check my own output before asking for help which I want to keep doing.
# apply_discount(price, tier) takes a price and a tier and returns the price after the tier's discount. A colleague could use it without reading the body as long as they know what the tiers are called.