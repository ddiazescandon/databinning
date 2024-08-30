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
        ax[i, j].text(-0.2, 1.07, annot[n], transform=ax[i, j].transAxes, fontsize=12, fontweight='bold', va='top')
        #
        # if i<2:
        #     axs[i, j].xaxis.set_visible(False)
        # else:
        #     axs[i, j].xaxis.set_tick_params(rotation=20)
        #
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        if i==1 and j==1 :
            ax[i, j].legend(loc='upper left', fontsize=8)
        #
        # if j==0:
        #     ax[i, j].set_title("Species", fontsize=15, pad=5)
        # elif j==1:
        #     ax[i, j].set_title("Strains", fontsize=15, pad=5)

        if i==0 and j==0:
            ax[i, j].set_ylabel('NC species (n)', fontsize=11, color='black')
        elif i==0 and j==1:
            ax[i, j].set_ylabel('NC strains (n)', fontsize=11, color='black')
        elif i==1 and j==0:
            ax[i, j].set_ylabel('HQ species (n)', fontsize=11, color='black')
        elif i==1 and j==1:
            ax[i, j].set_ylabel('HQ strains (n)', fontsize=11, color='black')

        ax[i, j].set_xticks(np.arange(3))
        ax[i, j].set_xticklabels(labels=['Short_read', 'Long_read', 'Hybrid'], minor=False, fontsize=12,
                           color='black')


    #
    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)][0:9]

    for k in range(4):
        i, j = k//2, k%2
        if i==0 and j== 0:
            ax[i, j].bar(0 - .2, 131, width=.2, color=cat_colors[0],
                   label='Short_co')
            ax[i, j].bar(0, 96, width=.2, color=cat_colors[1],
                   label='Short_single')
            ax[i, j].bar(0 + .2, 135, width=.2, color=cat_colors[2],
                   label='Short_multi')

            ax[i, j].bar(1 - .1, 70, width=.2, color=cat_colors[3],
                   label='Long_single')
            ax[i, j].bar(1 + .1, 86, width=.2, color=cat_colors[4],
                   label='Long_multi')

            ax[i, j].bar(2 - .1, 136, width=.2, color=cat_colors[5],
                   label='Hybrid_single')
            ax[i, j].bar(2 + .1, 157, width=.2, color=cat_colors[6],
                   label='Hybrid_multi')
        elif i==0 and j==1:
            ax[i, j].bar(0 - .2, 131, width=.2, color=cat_colors[0],
                   label='Short_co')
            ax[i, j].bar(0, 163, width=.2, color=cat_colors[1],
                   label='Short_single')
            ax[i, j].bar(0 + .2, 229, width=.2, color=cat_colors[2],
                   label='Short_multi')

            ax[i, j].bar(1 - .1, 70, width=.2, color=cat_colors[3],
                   label='Long_single')
            ax[i, j].bar(1 + .1, 87, width=.2, color=cat_colors[4],
                   label='Long_multi')

            ax[i, j].bar(2 - .1, 297, width=.2, color=cat_colors[5],
                   label='Hybrid_single')
            ax[i, j].bar(2 + .1, 374, width=.2, color=cat_colors[6],
                   label='Hybrid_multi')

        elif i==1 and j==0:
            ax[i, j].bar(0 - .2, 13, width=.2, color=cat_colors[0],
                   label='Short_co')
            ax[i, j].bar(0, 21, width=.2, color=cat_colors[1],
                   label='Short_single')
            ax[i, j].bar(0 + .2, 30, width=.2, color=cat_colors[2],
                   label='Short_multi')

            ax[i, j].bar(1- .1, 67, width=.2, color=cat_colors[3],
                   label='Long_single')
            ax[i, j].bar(1 + .1, 82, width=.2, color=cat_colors[4],
                   label='Long_multi')

            ax[i, j].bar(2 - .1, 109, width=.2, color=cat_colors[5],
                   label='Hybrid_single')
            ax[i, j].bar(2 + .1, 115, width=.2, color=cat_colors[6],
                   label='Hybrid_multi')

        elif i==1 and j==1:
            ax[i, j].bar(0 - .2, 13, width=.2, color=cat_colors[0],
                   label='Short_co')
            ax[i, j].bar(0, 28, width=.2, color=cat_colors[1],
                   label='Short_single')
            ax[i, j].bar(0 + .2, 48, width=.2, color=cat_colors[2],
                   label='Short_multi')

            ax[i, j].bar(1 - .1, 67, width=.2, color=cat_colors[3],
                   label='Long_single')
            ax[i, j].bar(1 + .1, 83, width=.2, color=cat_colors[4],
                   label='Long_multi')

            ax[i, j].bar(2 - .1, 208, width=.2, color=cat_colors[5],
                   label='Hybrid_single')
            ax[i, j].bar(2 + .1, 257, width=.2, color=cat_colors[6],
                   label='Hybrid_multi')




        format_axs(k, i, j)




def main():



    num_cols = 2
    num_rows = 2
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(8,6), sharex=True)
    go(axs, num_rows)
    #
    plt.subplots_adjust(wspace=0.3, hspace=0.15)
    sns.despine(fig)

    fig.savefig('./no_of_spe_str_checkm2.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()