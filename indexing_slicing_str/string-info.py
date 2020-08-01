#!/usr/bin/env python 

msg = input("Enter a message: ")

print("First character:", msg[0])
print("Last character:", msg[-1])
print("Middle character:", msg[int(len(msg) / 2)])
print("Even index characters:", msg[0::2])
print("Odd index characters:", msg[1::2])
print("Reversed message:", msg[::-1])