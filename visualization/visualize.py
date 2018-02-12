# visualizes a player's choices for a specific task over a range of rounds

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use('./elip12.mplstyle')

df = pd.read_csv('test3.csv',
    index_col='participant.label')

# pulls data for one player from the csv otree spits out,
# and reformats it to have rounds as rows and each round's data in the cols
def format_df(player_id, data):
    
    df1 = data.loc[player_id, 'RiskAndFairness_oTree.1.player.id_in_group':]

    # there are 29 variables that ger recorded per round
    cols = [str(index).split('.')[-1] for index in df1[:][:29].index]
    df2 = pd.DataFrame(columns=cols)
    i = 0
    for i in range(0, df1.shape[0], 29):
        row_dict = {'round': i / 29 + 1}
        for j in range(29):
            row_dict[cols[j]] = [df1[i + j]]
        row_df = pd.DataFrame(row_dict)
        df2 = df2.append(row_df)
    
    df2['round'] = df2['round'].astype(int)
    df2.set_index('round', inplace=True)
    
    return df2

# plots the choices a given player made for a given mode
def plot_data(player_id, data, mode):
    
    df = format_df(player_id, data)
    df = df[df['mode'] == mode]
    print(df)
    if mode == 'det_giv':
        plt.scatter(df['me_a'], df['me_b'])
        for _, row in df.iterrows():
            plt.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']])
        plt.xlabel('You', color='#848484')
        plt.ylabel('Partner', color='#848484')

    elif mode == 'sec_ownrisk':
        plt.scatter(df['me_a'], df['me_b'])
        for _, row in df.iterrows():
            plt.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']])
        plt.xlabel('State A', color='#848484')
        plt.ylabel('State B', color='#848484')
    
    # elif mode == 'sec_1bl_1ch':

    # elif mode == 'sec_1bl_2ch':

    # elif mode == 'sec_2bl_1ch':

    # elif mode == 'sec_ownrisk':

    # elif mode == 'sec_ownrisk_fixedother':

    # elif mode == 'sec_otherrisk_ownfixed':

    # elif mode == 'probability':
    

    #plt.tight_layout()
    plt.title(player_id + ' ' + mode + ' choices')
    plt.show()

plot_data('LEEPS_1', df, 'det_giv')


