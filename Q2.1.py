#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:46:55 2021

@author: basakulcay
"""

def main():
    
    outfile=open('scores.txt','w')
    score=int(input('Enter the scores (-1 to stop):'))
    
    while score !=-1:
        outfile.write(str(score)+ '\n')
        score=int(input('Enter the scores (-1 to stop):'))
        
    outfile.close()
    print('Data is written')
    
main()
