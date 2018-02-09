from matplotlib import pyplot as plt
import numpy as np
import csv
from net_incomes import *

MORTGAGE_PAYMENTS = 12.0 * np.array([75.0, 225.0, 375, 525, 700, 900, 1100, 1300,
                              1500, 1700, 1900, 2100, 2300, 2500, 2800, 3500, 4500, 6000])

def compute_mortgage_stress():
    net_incomes = calc_net_income()

    with open('income_mortgage.csv', 'rb') as abs_grid:
        abs_csv = csv.reader(abs_grid)
        mort_count = 0
        mortgage_stress = []
        for row in abs_csv:
            inc_count = 0
            for num_house in row:
                income = net_incomes[inc_count]
                mortgage = MORTGAGE_PAYMENTS[mort_count]
                if mortgage >= income:
                    ms = 1.0
                else:
                    ms = mortgage / income
                mortgage_stress += [ms] * int(num_house)
                inc_count += 1
            mort_count += 1
    return np.array(mortgage_stress)

mort_stress = compute_mortgage_stress()
plt.hist(mort_stress, bins=20, edgecolor='black')
plt.show()




