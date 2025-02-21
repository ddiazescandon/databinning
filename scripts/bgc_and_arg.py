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

    def format_axs(i, j):
        annot = list(string.ascii_lowercase)
        n=i*2+j
        ax[i, j].text(-0.2, 1.07, annot[n], transform=ax[i, j].transAxes, fontsize=12, fontweight='bold', va='top')
        #
        # if i<2:
        #     axs[i, j].xaxis.set_visible(False)
        # else:
        #     axs[i, j].xaxis.set_tick_params(rotation=20)
        #
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        if i==0 and j==0:
            ax[i, j].legend(loc='upper left', fontsize=10)
        #
        # if j==0:
        #     axs[i, j].set_title("Species", fontsize=15, pad=5)
        # elif j==1:
        #     axs[i, j].set_title("Strain", fontsize=15, pad=5)

        if i==0 and j==0:
            ax[i, j].set_ylabel('Number of ARG hosts', fontsize=11, color='black')
        elif i==0 and j==1:
            ax[i, j].set_ylabel('Number of ARG hosts with multi-resistance features', fontsize=11, color='black')
        elif i==1 and j==0:
            ax[i, j].set_ylabel('Number of potential BGCs', fontsize=11, color='black')
        elif i==1 and j==1:
            ax[i, j].set_ylabel('Number of potential novel BGCs', fontsize=11, color='black')

        ax[i, j].set_xticks(np.arange(3))
        ax[i, j].set_xticklabels(labels=['Short-read', 'Long-read', 'Hybrid'], minor=False, fontsize=12,
                           color='black')


    #
    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)][0:9]

    for i in range(2):
        for j in range(2):
            if i==0 and j==0:
                ax[i, j].bar(0 - .2, 63, width=.2, color=cat_colors[0],
                       label='Short_co')
                ax[i, j].bar(0, 73, width=.2, color=cat_colors[1],
                       label='Short_single')
                ax[i, j].bar(0 + .2, 95, width=.2, color=cat_colors[2],
                       label='Short_multi')
    
                ax[i, j].bar(1 - .1, 55, width=.2, color=cat_colors[3],
                       label='Long_single')
                ax[i, j].bar(1 + .1, 67, width=.2, color=cat_colors[4],
                       label='Long_multi')
    
                ax[i, j].bar(2 - .1, 155, width=.2, color=cat_colors[5],
                       label='Hybrid_single')
                ax[i, j].bar(2 + .1, 193, width=.2, color=cat_colors[6],
                       label='Hybrid_multi')
            if i == 0 and j == 1:
                ax[i, j].bar(0 - .2, 5, width=.2, color=cat_colors[0],
                             label='Short_co')
                ax[i, j].bar(0, 6, width=.2, color=cat_colors[1],
                             label='Short_single')
                ax[i, j].bar(0 + .2, 7, width=.2, color=cat_colors[2],
                             label='Short_multi')

                ax[i, j].bar(1 - .1, 11, width=.2, color=cat_colors[3],
                             label='Long_single')
                ax[i, j].bar(1 + .1, 13, width=.2, color=cat_colors[4],
                             label='Long_multi')

                ax[i, j].bar(2 - .1, 14, width=.2, color=cat_colors[5],
                             label='Hybrid_single')
                ax[i, j].bar(2 + .1, 20, width=.2, color=cat_colors[6],
                             label='Hybrid_multi')
            elif i==1 and j==0:
                ax[i, j].bar(0 - .2, 316, width=.2, color=cat_colors[0],
                       label='Short_co')
                ax[i, j].bar(0, 288, width=.2, color=cat_colors[1],
                       label='Short_single')
                ax[i, j].bar(0 + .2, 444, width=.2, color=cat_colors[2],
                       label='Short_multi')
    
                ax[i, j].bar(1 - .1, 162, width=.2, color=cat_colors[3],
                       label='Long_single')
                ax[i, j].bar(1 + .1, 201, width=.2, color=cat_colors[4],
                       label='Long_multi')
    
                ax[i, j].bar(2 - .1, 638, width=.2, color=cat_colors[5],
                       label='Hybrid_single')
                ax[i, j].bar(2 + .1, 803, width=.2, color=cat_colors[6],
                       label='Hybrid_multi')

            elif i == 1 and j == 1:
                ax[i, j].bar(0 - .2, 212, width=.2, color=cat_colors[0],
                             label='Short_co')
                ax[i, j].bar(0, 183, width=.2, color=cat_colors[1],
                             label='Short_single')
                ax[i, j].bar(0 + .2, 249, width=.2, color=cat_colors[2],
                             label='Short_multi')

                ax[i, j].bar(1 - .1, 122, width=.2, color=cat_colors[3],
                             label='Long_single')
                ax[i, j].bar(1 + .1, 156, width=.2, color=cat_colors[4],
                             label='Long_multi')

                ax[i, j].bar(2 - .1, 529, width=.2, color=cat_colors[5],
                             label='Hybrid_single')
                ax[i, j].bar(2 + .1, 646, width=.2, color=cat_colors[6],
                             label='Hybrid_multi')




            format_axs(i, j)




def main():



    num_cols = 2
    num_rows = 2
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 10))
    go(axs, num_rows)
    #
    plt.subplots_adjust(wspace=0.3, hspace=0.1)
    sns.despine(fig)

    fig.savefig('./4_bgc_and_arg.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()