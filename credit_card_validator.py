# Python credit card validator program

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step3
for x in card_number[::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step4
total = sum_odd_digits + sum_even_digits

# Step5
if total % 10 == 0:
    print("Valid")
else:
    print("INVALID")
