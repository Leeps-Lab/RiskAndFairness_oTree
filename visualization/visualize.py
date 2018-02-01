# visualizes a player's choices for a specific task over a range of rounds

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use('./elip12.mplstyle')

df = pd.read_csv('data/2017-11-07_S2.csv',
    index_col='participant.id_in_session')

# pulls data for one player from the csv otree spits out,
# and reformats it to have rounds as rows and each round's data in the cols
def format_df(player_id, data):
    
    df1 = data.iloc[player_id, 24:]
    cols = [str(index) for index in df1[:][:16].index]
    df2 = pd.DataFrame(columns=cols)

    for i in range(0, df1.shape[0], 16):
        row_dict = {'round': i / 16 + 1}
        for j in range(16):
            row_dict[cols[j]] = [df1[i + j]]
        row_df = pd.DataFrame(row_dict)
        df2 = df2.append(row_df)
    
    df2['round'] = df2['round'].astype(int)
    df2.set_index('round', inplace=True)

    # for debugging
    # df2.to_csv('df2.csv')
    
    return df2


# pulls data from the config
# what is best way to do this:
#   each player has their own config file
#   I think the best way is to add player fields for [m, px, py] all, [a, b] fixedother/own, [ax, ay, bx, by] prob
#   The data we have now will be obselete then
def plot_background():
    pass

def plot_data(player_id, data, mode):
    
    df = format_df(player_id, data)
    df = df[df['RiskAndFairness_oTree.1.player.mode'] == mode]
    if mode == 'single_given':
        plt.scatter(df['RiskAndFairness_oTree.1.player.me_a'], df['RiskAndFairness_oTree.1.player.me_b'])
    plt.show()

plot_data(1, df, 'single_given')