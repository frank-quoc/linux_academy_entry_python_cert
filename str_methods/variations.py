#!/usr/bin/env python

# Python implementation here

msg = input("Enter a message: ")

print("Lowercase:", msg.lower())
print("Uppercase:", msg.upper())
print("Capitalized:", msg.capitalize())
print("Title Case:", msg.title())

words = msg.split()
print("Words:", words)

sorted_words = sorted(words)
print("Alphabetic First Word:",  sorted_words[0])
print("Alphabetic Last Word:",  sorted_words[-1])