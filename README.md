Assignment 2
Question 9: Rounds of the Josephus Problem
Amarnoor Kaur, Nicholas Retel, Vibhu Dikshit
COMP 359 – AB1 – Design & Analysis of Algorithms
Dr. Russell Campbell
October 18th, 2024

Introduction
Our group chose the task of implementing a visualization of the Josephus problem for an input size of 100. The Josephus problem is a mathematical puzzle inspired by Jewish soldier and historian Josephus Flavius (Shúilleabháin et al., 2019, p. 6). In the Josephus problem, people are formed in a circle, and each member is sequentially eliminated until one final member remains. Given an input size of 100 participants, our goal was to find and visualize the one final remaining participant who was not eliminated. With this goal, a solution was created in Python by using:

The Josephus formula, a method for calculating the final surviving participant based on the largest power of 2 ≤ n the number of participants
Binary rotation, which shifts the leftmost bit of the binary representation of the number of participants, converting to decimal to show the final survivor in the circle
By implementing both methods, the correct solution was provided successfully, enabling us to accurately visualize the elimination process and identify the last remaining person in a group of 100 participants.

Problem Solving
The challenge of the Josephus problem is to determine which position the last remaining participant will be in a circle of 100 people. To find the last remaining participant, we implemented two different methods in python, the Josephus formula and binary rotation.

josephus_formula Method:
Finds the position of the last participant who is not eliminated in the circle by using bitwise operations to identify the largest power of 2 ≤ n the total number of participants, then calculates the remaining participants and applies a formula to determine the safe position.

The Josephus formula is as follows:
w: position of the final participant who has not been eliminated
n: total number of participants in the circle
m: exponent of the largest power of 2 ≤ n

w = 2 (n – 2m) + 1
(Regan, 2009)

Pseudocode of josephus_formula Method
max_power_of_two = largest power of 2 ≤ to n
leftover_participants = n – max_power_of_two
return 2 * leftover_participants + 1

binary_rotation Method
Converts the number of participants, n, into a binary string, rotates the bits, and then converts the string back to decimal form to determine the position of the last participant.

Pseudocode of josephus_formula Method
binary_str = binary representation of n removing ‘0b’ prefix
rotated_binary_str = rotated leftmost bit of the binary string
return decimal form of rotated binary string

Implementation
The following are the implementation of the two methods in python for finding the solution to the Josephus problem with an input size of 100 participants.

def josephus_formula(n):
# Using bit-shifting to find the largest power of 2 <= n
max_power_of_two = 1 << (n.bit_length() - 1) # Largest power of two <= n
# One-liner to find the safe position
l = n - max_power_of_two # Leftover people after filling the circle
# Josephus formula: safe spot after adjustments
return 2 * l + 1

def binary_rotation(n):
# Convert n to its binary form (removing '0b' prefix)
binary_str = bin(n)[2:]
# Rotate the leftmost bit to the end (bit rotation)
rotated_binary_str = binary_str[1:] + binary_str[0]
# Convert rotated binary string back to a decimal number
return int(rotated_binary_str

References
Regan, R. (2009, July 24). Powers of two in the Josephus problem - exploring binary. Exploring Binary. https://www.exploringbinary.com/powers-of-two-in-the-josephus-problem/
Shúilleabháin, A. N., Cronin, A., Beirne, P., & Lewanowski-Breen, E. (Eds.). (2019). MATHS SPARKS VOL III. University College Dublin. https://www.ucd.ie/mathstat/t4media/SPARKS_FINALVol3.pdf
