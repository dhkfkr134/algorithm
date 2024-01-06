#문제 그대로 짰음.
import sys
angle = list(map(int, sys.stdin.readlines()))
if angle[0]+angle[1]+angle[2] != 180:
    print("Error")
else:
    if angle[0] == angle[1] == angle[2]:
        print("Equilateral")
    elif angle[0] == angle[1] or angle[0] == angle[2] or angle[1] == angle[2]:
        print("Isosceles")
    else:
        print("Scalene")