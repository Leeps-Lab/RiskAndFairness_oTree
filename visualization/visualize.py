# visualizes a player's choices for a specific task over a range of rounds

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use('./elip12.mplstyle')

csv = 'test_test.csv'

df = pd.read_csv(csv,
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
# for now were doing it with all one color. later we will implement different colors for different probabilities
# also implement multiple graphs for each round of probability
# display: gray (default), color, coded
def plot_data(player_id, data, mode, display='color'):
    
    df = format_df(player_id, data)
    df = df[df['mode'] == mode]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect(aspect='equal')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.axis([0, 100, 0, 100])
    plt.xlabel('State A', color='#848484')
    plt.ylabel('State B', color='#848484')
    date, session = csv.split('_')[0], csv.split('_')[1].split('.')[0]
    plt.title(date.capitalize() + ' ' + session.capitalize() + ' ' + player_id.capitalize() + ' ' + mode.capitalize())

    if display not in ['gray', 'color', 'coded']:
        print("Invalid display argument, defaulting to gray.")
        display = 'gray'

    if display == 'gray':
        lines = ['#b2b2b2']
        dots = ['#eb860d']
    else:
        lines = ['#60d515', '#d22b10', '#1fa8e4', '#e0cc05', '#eb860d', '#b113ef']
        dots = ['#60d515', '#d22b10', '#1fa8e4', '#e0cc05', '#eb860d', '#b113ef']

    if mode == 'det_giv':
        for _, row in df.iterrows():
            ax.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']], color=lines[i % len(lines)], alpha=0.55, zorder=3, linewidth=.5)
            ax.scatter(row['me_a'], row['me_b'], color=dots[i % len(dots)], alpha=.8, zorder=4)
        plt.xlabel('You', color='#848484')
        plt.ylabel('Partner', color='#848484')

    elif mode == 'sec_ownrisk':
        for _, row in df.iterrows():
            ax.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']], color=lines[i % len(lines)], alpha=0.55, zorder=3, linewidth=.5)
            ax.scatter(row['me_a'], row['me_b'], color=dots[i % len(dots)], alpha=.8, zorder=4)
    
    elif mode in ['sec_1bl_1ch', 'sec_1bl_2ch', 'sec_2bl_1ch']:
        for i, row in df.iterrows():
            ax.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']], color=lines[i % len(lines)], alpha=0.55, zorder=3, linewidth=.5)
            if mode == 'sec_2bl_1ch':
                ax.plot([0, row['m'] / row['py']], [row['m'] / row['px'], 0], color=lines[i % len(lines)], alpha=0.55, zorder=3, linewidth=.5)
            ax.scatter(row['partner_a'], row['partner_b'], color=dots[i % len(dots)], marker='s', alpha=.7, zorder=4)
            ax.scatter(row['me_a'], row['me_b'], color=dots[i % len(dots)], alpha=.8, zorder=4)

    elif mode == 'sec_ownrisk_fixedother':
        for i, row in df.iterrows():
            ax.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']], color=lines[i % len(lines)], alpha=0.55, zorder=3, linewidth=.5)
            ax.scatter(row['me_a'], row['me_b'], color=dots[i % len(dots)], alpha=.8, zorder=4)

    elif mode == 'sec_otherrisk_ownfixed':
        for i, row in df.iterrows():
            ax.plot([row['m'] / row['px'], 0], [0, row['m'] / row['py']], color=lines[i % len(lines)], alpha=0.55, zorder=3, linewidth=.5)
            ax.scatter(row['partner_a'], row['partner_b'], color=dots[i % len(dots)], alpha=.8, zorder=4)

    # elif mode == 'probability':
    

    #plt.tight_layout()
    plt.show()

plot_data('LEEPS_1', df, 'sec_2bl_1ch', display='gray')


