# Objective
# Today, we are building on our knowledge of arrays by adding another dimension.
# Check out the Tutorial tab for learning materials and an instructional video.
#
# Context
# Given a
# 2D Array,
#
# :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# We define an hourglass in
# to be a subset of values with indices falling in this pattern in
#
# 's graphical representation:
#
# a b c
#   d
# e f g
#
# There are
# hourglasses in
#
# , and an hourglass sum is the sum of an hourglass' values.
#
# Task
# Calculate the hourglass sum for every hourglass in
#
# , then print the maximum hourglass sum.
#
# Example
#
# In the array shown above, the maximum hourglass sum is
#
# for the hourglass in the top left corner.
#
# Input Format
#
# There are
# lines of input, where each line contains space-separated integers that describe the 2D Array
#
# .
#
# Constraints
#
# Output Format
#
# Print the maximum hourglass sum in
#
# .
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#
# Sample Output
#
# 19
#
# Explanation
#
# contains the following hourglasses:
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0
#
# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0
#
# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
#
# The hourglass with the maximum sum (19) is:
#
# 2 4 4
#   2
# 1 2 4


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    matrix = []
    maxSum = None

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for row in range(len(arr) - 2):
        for element in range(len(arr[row]) - 2):
            first_three_list = [arr[row][element], arr[row][element + 1], arr[row][element + 2]]
            second_three_list = [arr[row + 1][element + 1]]
            third_three_list = [arr[row + 2][element], arr[row + 2][element + 1], arr[row + 2][element + 2]]
            final_list = first_three_list + second_three_list + third_three_list
            if maxSum is None:
                maxSum = sum(final_list)
            else:
                if sum(final_list) > maxSum:
                    maxSum = sum(final_list)

    print(maxSum)
