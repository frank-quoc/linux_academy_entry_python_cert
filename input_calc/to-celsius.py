#!/usr/bin/env python

# Python implementation goes here

fahrenheight = float(input("What temp (in Fahrenheight) would you like converted to Celsius? "))
celsius = (fahrenheight - 32) * 5 / 9

print(fahrenheight, "F is", round(celsius, 2), "C")