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

    def format_axs(i):
        annot = list(string.ascii_lowercase)
        ax[i].text(-0.2, 1.07, annot[i], transform=ax[i].transAxes, fontsize=12, fontweight='bold', va='top')
        #
        # if i<2:
        #     axs[i, j].xaxis.set_visible(False)
        # else:
        #     axs[i, j].xaxis.set_tick_params(rotation=20)
        #
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        if i==0 :
            ax[i].legend(loc='upper left', fontsize=6)
        #titile
        # if j==0:
        #     axs[i, j].set_title("Species", fontsize=15, pad=5)
        # elif j==1:
        #     axs[i, j].set_title("Strain", fontsize=15, pad=5)

        if i==0:
            ax[i].set_ylabel('Number of NC strains being host of ARGs', fontsize=11, color='black')
        elif i==1:
            ax[i].set_ylabel('Number of potential BGCs', fontsize=11, color='black')

        ax[i].set_xticks(np.arange(3))
        ax[i].set_xticklabels(labels=['Short-read', 'Long-read', 'Hybrid'], minor=False, fontsize=10,
                           color='black')


    #
    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)][0:9]

    for i in range(2):
        if i==0:
            ax[i].bar(0 - .2, 70, width=.2, color=cat_colors[0],
                   label='Short_co')
            ax[i].bar(0, 69, width=.2, color=cat_colors[1],
                   label='Short_single')
            ax[i].bar(0 + .2, 95, width=.2, color=cat_colors[2],
                   label='Short_multi')

            ax[i].bar(1 - .1, 55, width=.2, color=cat_colors[3],
                   label='Long_single')
            ax[i].bar(1 + .1, 75, width=.2, color=cat_colors[4],
                   label='Long_multi')

            ax[i].bar(2 - .1, 155, width=.2, color=cat_colors[5],
                   label='Hybrid_single')
            ax[i].bar(2 + .1, 193, width=.2, color=cat_colors[6],
                   label='Hybrid_multi')
        else:
            ax[i].bar(0 - .2, 513, width=.2, color=cat_colors[0],
                   label='Short_co')
            ax[i].bar(0, 419, width=.2, color=cat_colors[1],
                   label='Short_single')
            ax[i].bar(0 + .2, 673, width=.2, color=cat_colors[2],
                   label='Short_multi')

            ax[i].bar(1 - .1, 232, width=.2, color=cat_colors[3],
                   label='Long_single')
            ax[i].bar(1 + .1, 308, width=.2, color=cat_colors[4],
                   label='Long_multi')

            ax[i].bar(2 - .1, 935, width=.2, color=cat_colors[5],
                   label='Hybrid_single')
            ax[i].bar(2 + .1, 1177, width=.2, color=cat_colors[6],
                   label='Hybrid_multi')




        format_axs(i)




def main():



    num_cols = 2
    num_rows = 1
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 4))
    go(axs, num_rows)
    #
    plt.subplots_adjust(wspace=0.3, hspace=0.04)
    sns.despine(fig)

    fig.savefig('./bgc_and_arg_checkm2_comebin.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()