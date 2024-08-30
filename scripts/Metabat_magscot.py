import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import string
import itertools
from collections import defaultdict
import seaborn as sns


def go(ax, num_rows):

    def format_axs(n, i, j):
        annot = list(string.ascii_lowercase)
        ax[i, j].text(-0.25, 1.07, annot[n], transform=ax[i, j].transAxes, fontsize=9, fontweight='bold', va='top')
        ax[i, j].tick_params(axis='y', labelsize=6.5)
        #
        # if i<2:
        #     axs[i, j].xaxis.set_visible(False)
        # else:
        #     axs[i, j].xaxis.set_tick_params(rotation=20)
        #
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        if i==0 and j==0 :
            ax[i, j].legend(loc='upper left', fontsize=6)
        #
        if i==0 and j==0:
            ax[i, j].set_title("NC MAGs (n)", fontsize=11, pad=5)
        elif i==0 and j==1:
            ax[i, j].set_title("HQ MAGs (n)", fontsize=11, pad=5)
        #
        if i==0 and j==0:
            ax[i, j].set_ylabel('Marine', fontsize=10, color='black')
        elif i==1 and j==0:
            ax[i, j].set_ylabel('Cheese', fontsize=10, color='black')
        elif i==2 and j==0:
            ax[i, j].set_ylabel('Human gut I', fontsize=10, color='black')
        elif i==3 and j==0:
            ax[i, j].set_ylabel('Human gut II', fontsize=10, color='black')
        elif i==4 and j==0:
            ax[i, j].set_ylabel('Activated sludge', fontsize=10, color='black')
        # elif i==1 and j==0:
        #     ax[i, j].set_ylabel('No. of species after dereplicating HQ MAGs', fontsize=11, color='black')
        # elif i==1 and j==1:
        #     ax[i, j].set_ylabel('No. of strains after dereplicating HQ MAGs', fontsize=11, color='black')

        ax[i, j].set_xticks(np.arange(7))
        ax[i, j].set_xticklabels(labels=['Short_co', 'Short_single', 'Short_multi',  'Long_single', 'Long_multi', 'Hybrid_single', 'Hybrid_multi'], rotation=25, minor=False, fontsize=6, color='black',ha='right')


    #
    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)]

    for k in range(10):
        i, j = k//2, k%2
        #marine NC
        if i==0 and j==0:
            ax[i, j].bar(0 - .15, 85, width=.3, color=cat_colors[3] , label='MetaBAT 2')
            ax[i, j].bar(0 + .15, 131, width=.3, color=cat_colors[4] , label='MAGScoT')

            ax[i, j].bar(1 - .15, 164, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 335, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 312, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 513, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 89, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 208, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 273, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 310, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 444, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 634, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 607, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 767, width=.3, color=cat_colors[4] )
        #MARINE HQ
        elif i==0 and j==1:
            ax[i, j].bar(0 - .15, 6, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 13, width=.3, color=cat_colors[4])

            ax[i, j].bar(1 - .15, 37, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 64, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 44, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 115, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 76, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 187, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 256, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 282, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 316, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 447, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 435, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 552, width=.3, color=cat_colors[4] )
        #CHEESE NC
        elif i==1 and j==0:
            ax[i, j].bar(0 - .15, 28, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 29, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 62, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 115, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 70, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 135, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 88, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 116, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 93, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 114, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 84, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 126, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 78, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 142, width=.3, color=cat_colors[4] )
        #CHEESE HQ
        elif i==1 and j==1:
            ax[i, j].bar(0 - .15, 2, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 2, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 2, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 10, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 10, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 29, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 67, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 99, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 60, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 79, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 71, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 108, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 64, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 128, width=.3, color=cat_colors[4] )
        #HUMAN GUT I NC
        elif i==2 and j== 0:
            ax[i, j].bar(0 - .15, 31, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 71, width=.3, color=cat_colors[4])

            ax[i, j].bar(1 - .15, 32, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 135, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 37, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 132, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 65, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 101, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 72, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 94, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 46, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 137, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 42, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 132, width=.3, color=cat_colors[4] )
        #HUMAN GUT I HQ
        elif i==2 and j==1:
            ax[i, j].bar(0 - .15, 2, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 6, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 1, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 4, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 3, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 8, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 36, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 71, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 40, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 60, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 30, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 86, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 23, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 82, width=.3, color=cat_colors[4] )
        #HUMAN GUT II NC
        elif i==3 and j==0:
            ax[i, j].bar(0 - .15, 81, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 174, width=.3, color=cat_colors[4])

            ax[i, j].bar(1 - .15, 322, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 1033, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 703, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 1265, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 329, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 538, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 391, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 550, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 498, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 1145, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 784, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 1246, width=.3, color=cat_colors[4] )
        #HUMAN GUT II HQ
        elif i==3 and j==1:
            ax[i, j].bar(0 - .15, 5, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 10, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 10, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 49, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 29, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 142, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 193, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 418, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 256, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 402, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 309, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 707, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 486, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 779, width=.3, color=cat_colors[4] )
        #ACTIVATED SLUDGE NC
        elif i==4 and j==0:
            ax[i, j].bar(0 - .15, 0, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 0, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 254, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 389, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 354, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 481, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 456, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 531, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 513, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 569, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 590, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 764, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 504, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 801, width=.3, color=cat_colors[4] )
        #ACTIVATED SLUDGE HQ
        elif i==4 and j==1:
            ax[i, j].bar(0 - .15, 0, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 0, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 51, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 65, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 65, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 102, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 354, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 440, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 402, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 459, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 430, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 551, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 367, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 596, width=.3, color=cat_colors[4] )





        format_axs(k, i, j)




def main():



    num_cols = 2
    num_rows = 5
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(5, 10), sharex=True)
    go(axs, num_rows)
    #
    plt.subplots_adjust(wspace=0.3, hspace=0.15)
    sns.despine(fig)

    fig.savefig('./MAGScoT.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()