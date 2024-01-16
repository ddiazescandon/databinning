import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import string
import itertools
from collections import defaultdict
import seaborn as sns

pd.set_option('display.expand_frame_repr', False)

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', 99999999)
pd.set_option('display.expand_frame_repr', False)

DATASETS = ['Marine_MQ',  'Marine_NC', 'Marine_HQ',
            'Cheese_MQ', 'Cheese_NC', 'Cheese_HQ',
            'human_gut_MQ', 'human_gut_NC', 'human_gut_HQ']

DATASETS_L = {'Marine_MQ': 'Marine',
              'Cheese_MQ': 'Cheese',
              'human_gut_MQ': 'human_gut'}
def go(datasets, axs, num_rows):

    def format_axs(n, i, j, subset=None):
        annot = list(string.ascii_lowercase)
        axs[i, j].text(-0.2, 1.07, annot[n], transform=axs[i, j].transAxes, fontsize=12, fontweight='bold', va='top')
        #隐藏x轴
        # if i<2:
        #     axs[i, j].xaxis.set_visible(False)
        # else:
        #     axs[i, j].xaxis.set_tick_params(rotation=20)
        #最右边的黑线和上面的黑线去掉
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        if i==1 and j==1:
            axs[i, j].legend(loc='upper left', fontsize=8)
        #设置titile
        # if j==0:
        #     axs[i, j].set_title("Species", fontsize=15, pad=5)
        # elif j==1:
        #     axs[i, j].set_title("Strains", fontsize=15, pad=5)


        if i==0 and j==0:
            axs[i, j].set_ylabel('NC species (n)', fontsize=12, color='black')
        elif i==0 and j==1:
            axs[i, j].set_ylabel('NC strains (n)', fontsize=12, color='black')
        elif i==1 and j==0:
            axs[i, j].set_ylabel('HQ species (n)', fontsize=12, color='black')
        elif i==1 and j==1:
            axs[i, j].set_ylabel('HQ strains (n)', fontsize=12, color='black')


        if i==1:
            for ax in axs[1]:
                ax.set_xticks(np.arange(len(subset)))
                ax.set_xticklabels(labels=['Short_co vs single', 'Short_co vs multi', 'Short_single vs multi', 'Long_single vs multi', 'Hybrid_single vs multi'], rotation=20, minor=False, fontsize=10, color='black',ha='right')


    #设置颜色
    for i, subset in enumerate(datasets):
        print(subset, i)
        cur_ax = axs[i//2, i%2]
        color_list1 = ['#6495ED', '#6495ED', '#FA8072', '#DC143C', '#FFD700']
        color_list2 = ['#FA8072', '#3CB371', '#3CB371', '#FFC0CB', '#CD853F']
        label_list1 = ['Short_co only', None , 'Short_single only', 'Long_single only', 'Hybrid_single only']
        label_list2 = [None, 'Short_multi only', None, 'Long_multi only', 'Hybrid_multi only']


        for j, ind in enumerate(['Short_co_single', 'Short_co_multi', 'Short_single_multi', 'Long_single_multi', 'Hybrid_single_multi']):
            bar = cur_ax.bar(j-.15, subset.loc[ind, "Both"] + subset.loc[ind, 'previous only'], width=.296, color=color_list1[j], label=label_list1[j])
            bar = cur_ax.bar(j+.15, subset.loc[ind, "Both"] + subset.loc[ind,'before only'], width=.296, color=color_list2[j], label=label_list2[j])
            if j== 4:
                bar = cur_ax.bar(j, subset.loc[ind, "Both"], width=.6, color='#7570b3', label='both')
            else:
                bar = cur_ax.bar(j, subset.loc[ind, "Both"], width=.6, color='#7570b3', label=None)




        format_axs(i, i//2, i%2, subset)




def main():

    subset1 = pd.DataFrame(
        [(185-92-54, 92, 54), (216-80-85, 80, 85), (151-16-60, 16, 60), (102-7-32, 7, 32), (164-7-27, 7, 27)],
        index=['Short_co_single', 'Short_co_multi', 'Short_single_multi', 'Long_single_multi', 'Hybrid_single_multi'],
        columns=['Both', 'previous only', 'before only'])

    subset2 = pd.DataFrame(
        [(235-93-104, 93, 104), (314-83-183, 83, 183), (257-27-117, 27, 117), (104-7-34, 7, 34), (402-30-102, 30, 102)],
        index=['Short_co_single', 'Short_co_multi', 'Short_single_multi', 'Long_single_multi', 'Hybrid_single_multi'],
        columns=['Both', 'previous only', 'before only'])

    subset3 = pd.DataFrame(
        [(29-7-16, 7, 16), (37-7-24, 7, 24), (34-4-12, 4, 12), (101-8-34, 8 , 34), (126-11-17, 11, 17)],
        index=['Short_co_single', 'Short_co_multi', 'Short_single_multi', 'Long_single_multi', 'Hybrid_single_multi'],
        columns=['Both', 'previous only', 'before only'])

    subset4 = pd.DataFrame(
        [(37-7-24, 7, 24), (56-7-43, 7, 43), (56-8-27, 8, 27), (103-8-36, 8, 36), (279-24-70, 24, 70)],
        index=['Short_co_single', 'Short_co_multi', 'Short_single_multi', 'Long_single_multi', 'Hybrid_single_multi'],
        columns=['Both', 'previous only', 'before only'])


    DATASETS = [subset1, subset2, subset3, subset4]




    num_cols = 2
    num_rows = 2
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(8, 6), sharex=True)
    go(DATASETS, axs, num_rows)
    #每个子图之间的距离
    plt.subplots_adjust(wspace=0.3, hspace=0.25)
    sns.despine(fig)
    fig.tight_layout()
    fig.savefig('./dereplicate_overlap_checkm2.pdf', dpi=100, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()