#!/usr/bin/env python3.8

def fizzbuzz(n):
    for i in range(n+1):
        fizz = 'Fizz' if i%3 == 0 else ''
        buzz = 'Buzz' if i%5 == 0 else ''
        print(f'{fizz}{buzz}' or i)

if __name__ == '__main__':
    n = int(input("Enter a number: "))

    fizzbuzz(n)