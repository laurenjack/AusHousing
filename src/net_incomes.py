import numpy as np

POS_INF = 1000000000000
FIRST_BRACKET = 18200.0
BRACKETS = np.array([37000, 87000, 180000])
RATES = np.array([0.19, 0.325, 0.37])
FINAL_RATE = 0.45
FULL_TAX = np.array([BRACKETS[0] - FIRST_BRACKET, BRACKETS[1]- BRACKETS[0], BRACKETS[2] - BRACKETS[1]]) * RATES

ANNUAL_INCOMES = np.array([0, 0, 3400, 11700, 18200, 23400, 29900, 37700, 46800, 58500, 71500, 84500, 97500,
                   117000, 143000, 169000, 195000, 221000, 247000, 286000, 364000])

def calc_net_income():
    tax_sums = np.zeros(ANNUAL_INCOMES.shape)
    running_balance = np.copy(ANNUAL_INCOMES) - FIRST_BRACKET
    last_bracket = FIRST_BRACKET
    for i in xrange(BRACKETS.shape[0]):
        bracket = BRACKETS[i]
        bracket_size = bracket - last_bracket
        ft = FULL_TAX[i]
        rate = RATES[i]
        new_balance = running_balance - bracket_size
        in_this_bracket = np.where(np.greater(running_balance, 0.0), running_balance*rate, 0.0)
        tax_at_b = np.where(np.greater(new_balance, 0.0), ft, in_this_bracket)
        tax_sums += tax_at_b
        running_balance = new_balance
        last_bracket = bracket
    last_bracket_tax = np.where(np.greater(running_balance, 0), running_balance * FINAL_RATE, 0.0)
    tax_sums += last_bracket_tax
    return ANNUAL_INCOMES - tax_sums







