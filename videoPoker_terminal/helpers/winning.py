import random


def calculate_points(combination):
    multiplier = 0

    if combination.get("Pairs") == 1:
        multiplier = 1
    if combination.get("Pairs") == 2:
        multiplier = 2
    if combination.get("Brelan") == 1:
        multiplier = 3
    if combination.get("Quinte") == 1:
        multiplier = 4
    if combination.get("Flush") == 1:
        multiplier = 6
    if combination.get("Full") == 1:
        multiplier = 9
    if combination.get("Carre") == 1:
        multiplier = 25
    if combination.get("QuinteFlush") == 1:
        multiplier = 50
    if combination.get("RoyalFlush") == 1:
        multiplier = 250

    return multiplier
