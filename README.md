# PYTHON--TOOLS
Python Fundamentals &amp; Security Research Tools
Day 1:
Today I practiced Python by creating small tools to understand how the language works and how it can be used for security-related tasks

First I learned about variables and how python stores data in memory (RAM).I used python built in id() concept to see memory location of a variable .I noticed that when the value of a variable changes is memory location is also changed.This help me understand how python  manage data internally in RAM

After that, I created a simple temperature conversion tool. The purpose of this tool was to convert temperature from Celsius to Fahrenheit using a basic mathematical formula. While doing this, I also learned how to take user input and how to handle errors using exception handling. If the user enters letters instead of numbers, the program shows an error message instead of crashing. This taught me how to make programs safer and more user-friendly.

Next, I built a password strength checker tool as part of my security learning. This tool uses Python's secrets library, which is designed for security-related random values. The tool does two main things:

It generates a strong and secure password automatically.

It checks the strength of a password entered by the user.

The password strength is measured using simple rules, such as:

Checking if the password is long enough

Checking if it contains numbers

Checking if it contains special characters

Based on these checks, the tool gives a strength score and tells the user whether the password is weak or acceptable. This helped me understand the difference between normal random values and secure random values, and why security-focused programs must use the correct tools.

Overall, today's practice helped me understand:

How variables work in memory

How to take user input safely

How to handle errors properly

How to think about basic security rules when building tools
