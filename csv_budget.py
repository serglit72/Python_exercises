import csv
import os
category = []


def budget_calc(fl):
    with open(fl, 'r', encoding='utf8') as f:
        line = f.readlines()
        for each in line:
            if each not in line:
                category.append(each)

    return(category) 

print(budget_calc('All_Payment_Methods101219.csv'))

