"""Q1:
Write a Python program that takes a sentence from the user and prints:
Number of characters
Number of words
Number of vowels"""

"""sentence = input("Send the sentence : ")
no_of_characters = len(sentence)
words = sentence.split()
no_of_words = len(words)
vowels = "aeiouAEIOU"
no_of_vowels = 0
for ch in sentence:
    if ch in vowels:
        no_of_vowels += 1
print("Number of characters : ",no_of_characters)
print("Number of words : ",no_of_words)
print("Number of vowels : ",no_of_vowels)"""


"""Q2:
Count Even and Odd Numbers
Take a list of numbers as input (comma-separated).
Count how many are even and how many are odd.
Print results.
Example Input:
10, 21, 4, 7, 8"""

"""nums = input("Enter the numbers : ")
numbers = nums.split(",")
even_count = 0
odd_count = 0
for n in numbers:
    n = int(n.strip())
    if n%2==0:
        even_count += 1
    elif n%2 !=0:
        odd_count += 1
print("Even counts : ",even_count)
print("Odd counts : ",odd_count)"""


"""Q3:
Given a CSV file Products.csv with columns:
Write a Python program to:
a) Read the CSV
b) Print each row in a clean format
c) Total number of rows
d) Total number of products priced above 500
e) Average price of all products
f) List all products belonging to a specific category (user input)
g) Total quantity of all items in stock"""

import pandas as pd
df = pd.read_csv("D:\products.csv")
for row in df.iterrows():
    print(row)
row_count = len(df.index)
print("Total row count : ", row_count)
price_above_500 = df[df["price"]>500]
print("Product above 500 are : ", price_above_500)
average_price= df["price"].mean()
print("Average price : ", average_price)
category = input("Enter the category to filter the product : ")
filtered_product = df[df["category"].str.lower()==category.lower()]
print("Product in category{category}: ")
if filtered_product.empty:
    print("No product found.....")
else:
    print(filtered_product)
total_quantity = df["quantity"].sum()
print("Total quantity of all products : ", total_quantity)