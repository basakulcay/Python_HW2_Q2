#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 08:57:50 2021

@author: basakulcay
"""

def determine_grade():
    total=0
    count = len(open('scores.txt').readlines())
    print('Score\tGrade')
    print('--------------')
    infile = open('scores.txt', 'r')
    for line in infile:
        
        grade=line.rstrip('\n')
        total=total+int(grade)
        
        if int(grade) >= 90:
            print(grade, "\t\tAA")
        elif int(grade) >= 85:
            print(grade, "\t\tBA")
        elif int(grade) >= 80:
            print(grade, "\t\tBB")
        elif int(grade) >= 75:
            print(grade, "\t\tCB")
        elif int(grade) >= 70:
            print(grade, "\t\tCC")
        elif int(grade) >= 65:
            print(grade, "\t\tDC")
        elif int(grade) >= 60:
            print(grade, "\t\tDD")
        else:
            print(grade, "\t\tFF")
            
    #print('The total score is',total)
    #print(count)
    print('The score average of the scores:',total/count)

determine_grade()
