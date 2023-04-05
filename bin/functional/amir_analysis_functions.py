#!/usr/bin/python3

def join_summary(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    print("In first       : ", len(s1))
    print("In second      : ", len(s2))
    print("Intersection   : ", len(s1 & s2))
    print("Only in first  : ", len(s1 - s2))
    print("Only in second : ", len(s2 - s1))