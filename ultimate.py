import numpy as np
import pandas as pd
import math

# Load data from CSV file
data = pd.read_csv('data.csv')

def big():
        # Calculate Kelly Criterion for each bet
    def kelly_criterion(win_prob, odds):
        """
        Calculates the Kelly Criterion for a given win probability and odds.

        Args:
        win_prob (float): Win probability of the bet
        odds (float): Odds of the bet

        Returns:
        float: Kelly Criterion bet size
        """
        if odds == 0:
            return 0
        else:
            kelly_fraction = (win_prob * (odds + 1) - 1) / odds
            return kelly_fraction

    bet_sizes = []
    for index, row in data.iterrows():
        win_prob = row['1']
        odds = row['R1']
        bet_size = kelly_criterion(win_prob, odds)
        bet_sizes.append(bet_size)

    # Add bet sizes to the dataframe
    data['Kelly_Bet_Size'] = bet_sizes

    # Display the updated dataframe
    print(data)

def small():
    # Data provided
    data = np.array([
        [1.9, 3, 2.9, 1.6, 1.75],
        [1.55, 3.3, 4, 1.7, 1.65],
        [2, 3, 2.7, 1.8, 1.55],
        [1.9, 3, 2.9, 1.75, 1.6],
        [1.65, 3.2, 3.6, 1.7, 1.65],
        [2, 2.8, 2.9, 1.3, 2.3],
        [2, 2.8, 2.9, 1.35, 2.15],
        [1.65, 3.1, 3.75, 1.5, 1.85],
        [2.9, 2.8, 2, 1.3, 2.3]
    ])

    # Calculate the probability of winning (p) and losing (q)
    p = 1 / data.shape[1]  # Assuming equally likely outcomes
    q = 1 - p

    # Loop through each row (betting option)
    for i in range(data.shape[0]):
        odds = data[i, :].astype(float)  # Extract odds for the current betting option
        b = np.where(odds > 1, odds, 1/odds)  # Convert odds to decimal format
        f_star = (b * p - q) / b  # Calculate optimal bet size using Kelly Criterion
        max_f_star = np.max(f_star)  # Find the maximum bet size
        print("Optimal bet size for betting option", i+1, ":", max_f_star)

print("")
el=int(input("I have two algorithms for betting.\n Pick one: \n1. Big \n2. Small. \n"))
if el == 1:
    big()
else:
    small()
