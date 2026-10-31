# Starter Code from Lab 5

total = float(input("Enter cart total: $"))


# Exercise 1:
# Add your if/elif/else here               # python counts largest to smallest 
# elif only runs if the one directly above it runs, second one only runs if the one above it fails
if total >= 500:
    discount = 0.15
elif total>= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0


final = total * (1-discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final Price: ${final:.2f}")



# Exercise 2:
if final > 1000: # strictly greater than.
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(status)



# Exercise 3:

region = "South" # S is capitalized

if region == "South":
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")
else: extra_discount = 0

final_discount = discount + extra_discount
final = total * (1 - (discount + extra_discount))
print(f"Final Discount: {final_discount*100:.0f}%")
print(f"Final Price: ${final:.2f}")



# Exercise 4:
# Nested version — rewrite this
# if region == "South":
#     if total > 100:
#         if customer_type == "wholesale":
#             extra_discount = 0.03

customer_type = "wholesale" # flat structure (rewritten version)
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03
# the flat structure is way easier because it is readable and more easy to edit



# Exercise 5:
amount = 15000
if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")



# Exercise 6:

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False # bool

vip_upgrade = True
if total_spent_this_year > 2000 or orders_this_year > 10 and not has_outstanding_balance:
    vip_upgrade =  True
else:
    vip_upgrade = False
print(f"VIP Upgrade: {vip_upgrade}")


print("-"*50)


# Answers to Self-Reflection Questions:
#1 It starts from the first level of the condition where the amount is greater than equal to 500 and corresponds with 15% discount.It stops at the first elif since it now fulfills the condition and the discount received is 10%.
#2 The first if statement ensures both conditions are filled at the same time. Two separate if statements would be independent of each other. They will not produce the same result because the second one acts as two different functions and does so consecutively and independently.
#3 I have experienced this when I shop online. The discount offered to me varies depending on the amount of stuff in my cart.