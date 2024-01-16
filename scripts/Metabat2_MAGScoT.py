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
        #隐藏x轴
        # if i<2:
        #     axs[i, j].xaxis.set_visible(False)
        # else:
        #     axs[i, j].xaxis.set_tick_params(rotation=20)
        #最右边的黑线和上面的黑线去掉
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        if i==1 and j==0 :
            ax[i, j].legend(loc='upper left', fontsize=6)
        #设置titile
        if i==0 and j==0:
            ax[i, j].set_title("Human gut", fontsize=11, pad=5)
        elif i==0 and j==1:
            ax[i, j].set_title("Cheese", fontsize=11, pad=5)
        elif i==0 and j==2:
            ax[i, j].set_title("Marine", fontsize=11, pad=5)
        #
        if i==0 and j==0:
            ax[i, j].set_ylabel('NC MAGs (n)', fontsize=10, color='black')
        elif i==1 and j==0:
            ax[i, j].set_ylabel('HQ MAGs (n)', fontsize=10, color='black')
        # elif i==1 and j==0:
        #     ax[i, j].set_ylabel('No. of species after dereplicating HQ MAGs', fontsize=11, color='black')
        # elif i==1 and j==1:
        #     ax[i, j].set_ylabel('No. of strains after dereplicating HQ MAGs', fontsize=11, color='black')

        ax[i, j].set_xticks(np.arange(7))
        ax[i, j].set_xticklabels(labels=['Short_co', 'Short_single', 'Short_multi',  'Long_single', 'Long_multi', 'Hybrid_single', 'Hybrid_multi'], rotation=25, minor=False, fontsize=6, color='black',ha='right')


    #设置颜色
    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)]

    for k in range(6):
        i, j = k//3, k%3
        if i==0 and j== 0:
            ax[i, j].bar(0 - .15, 31, width=.3, color=cat_colors[3])
            ax[i, j].bar(0 + .15, 67, width=.3, color=cat_colors[4])

            ax[i, j].bar(1 - .15, 31, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 130, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 36, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 125, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 65, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 101, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 72, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 96, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 41, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 129, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 47, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 142, width=.3, color=cat_colors[4] )
        elif i==0 and j==1:
            ax[i, j].bar(0 - .15, 20, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 25, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 64, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 104, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 83, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 130, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 88, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 116, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 93, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 115, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 74, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 125, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 70, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 140, width=.3, color=cat_colors[4] )
        elif i==0 and j==2:
            ax[i, j].bar(0 - .15, 85, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 131, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 164, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 314, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 312, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 513, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 89, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 208, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 273, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 349, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 444, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 634, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 607, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 767, width=.3, color=cat_colors[4] )
        elif i==1 and j==0:
            ax[i, j].bar(0 - .15, 2, width=.3, color=cat_colors[3], label='MetaBAT 2' )
            ax[i, j].bar(0 + .15, 4, width=.3, color=cat_colors[4] , label='MAGScoT')

            ax[i, j].bar(1 - .15, 1, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 7, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 3, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 11, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 36, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 71, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 40, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 65, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 23, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 82, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 29, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 94, width=.3, color=cat_colors[4] )
        elif i==1 and j==1:
            ax[i, j].bar(0 - .15, 2, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 2, width=.3, color=cat_colors[4] )

            ax[i, j].bar(1 - .15, 1, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 11, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 9, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 20, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 67, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 99, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 60, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 81, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 63, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 111, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 57, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 123, width=.3, color=cat_colors[4] )
        elif i==1 and j==2:
            ax[i, j].bar(0 - .15, 6, width=.3, color=cat_colors[3] )
            ax[i, j].bar(0 + .15, 13, width=.3, color=cat_colors[4])

            ax[i, j].bar(1 - .15, 37, width=.3, color=cat_colors[3] )
            ax[i, j].bar(1 + .15, 63, width=.3, color=cat_colors[4] )

            ax[i, j].bar(2 - .15, 44, width=.3, color=cat_colors[3] )
            ax[i, j].bar(2 + .15, 115, width=.3, color=cat_colors[4] )

            ax[i, j].bar(3 - .15, 76, width=.3, color=cat_colors[3] )
            ax[i, j].bar(3 + .15, 187, width=.3, color=cat_colors[4] )

            ax[i, j].bar(4 - .15, 256, width=.3, color=cat_colors[3] )
            ax[i, j].bar(4 + .15, 326, width=.3, color=cat_colors[4] )

            ax[i, j].bar(5 - .15, 316, width=.3, color=cat_colors[3] )
            ax[i, j].bar(5 + .15, 447, width=.3, color=cat_colors[4] )

            ax[i, j].bar(6 - .15, 435, width=.3, color=cat_colors[3] )
            ax[i, j].bar(6 + .15, 552, width=.3, color=cat_colors[4] )




        format_axs(k, i, j)




def main():



    num_cols = 3
    num_rows = 2
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(8, 4), sharex=True)
    go(axs, num_rows)
    #每个子图之间的距离
    plt.subplots_adjust(wspace=0.3, hspace=0.15)
    sns.despine(fig)

    fig.savefig('./MAGScoT.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()