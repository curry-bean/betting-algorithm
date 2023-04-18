import pandas as pd
import math

# Load data from CSV file
data = pd.read_csv('data.csv')
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