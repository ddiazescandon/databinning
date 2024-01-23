import pandas as pd
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import string
import itertools
from collections import defaultdict

pd.set_option('display.expand_frame_repr', False)

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', 99999999)
pd.set_option('display.expand_frame_repr', False)

DATASETS = ['human_co_mode',  'marine_co_mode', 'cheese_co_mode',
            'human_single_mode',  'marine_single_mode', 'cheese_single_mode',
            'human_multi_mode', 'marine_multi_mode', 'cheese_multi_mode']

DATASET_TO_PATH = {
                   'human_co_mode':'rank_data/human_co_mode.xlsx',
                   'marine_co_mode':'rank_data/marine_co_mode.xlsx',
                   'cheese_co_mode':'rank_data/cheese_co_mode.xlsx',
                   'human_single_mode':'rank_data/human_single_mode.xlsx',
                   'marine_single_mode':'rank_data/marine_single_mode.xlsx',
                   'cheese_single_mode':'rank_data/cheese_single_mode.xlsx',
                   'human_multi_mode':'rank_data/human_multi_mode.xlsx',
                   'marine_multi_mode':'rank_data/marine_multi_mode.xlsx',
                   'cheese_multi_mode':'rank_data/cheese_multi_mode.xlsx'}

DATASETS_L = {'marine_gsa': 'Marine GSA', 'marine_ma': 'Marine MA',
              'strain_gsa': 'Strain madness GSA', 'strain_ma': 'Strain madness MA',
              'plant_gsa': 'Plant-associated GSA', 'plant_ma': 'Plant-associated MA'}

def rank_list(lst):
    sorted_lst = sorted(lst, reverse=True)
    rank_lst = [sorted_lst.index(x) for x in lst]
    return rank_lst


def go(datasets, axs, num_rows):

    def format_axs(n, i, j, dataset=None):
        if n==0 or n==3 or n==6:
            annot = list(string.ascii_lowercase)
            axs[i, j].text(-1.2, 1.2, annot[n//3], transform=axs[i, j].transAxes, fontsize=8, fontweight='bold', va='top')
        #legend
        if i==0 and j==0:
            axs[i, j].legend(bbox_to_anchor=(-0.3, 1.25, 7.1, 1.25), loc=3,   #bbox_to_anchor设置了legend的位置（左边x轴位置，y高度，右边x轴位置，y高度）
                       ncol=3, mode="expand", borderaxespad=0., fontsize=6)
        else:
            axs[i, j].legend_.remove()
        #
        if i==0 and j<=2:
            print(i,j)
            axs[i, j].set_xlim([0, 30])
            axs[i, j].set_xticks([0,10,20,30])
            axs[i, j].set_xticklabels(['0','10','20','30'], fontsize=6)
        elif 1<=i<=2 and j<=2:
            axs[i, j].set_xlim([0, 80])
            axs[i, j].set_xticks([0,20,40,60,80])
            axs[i, j].set_xticklabels(['0','20','40','60','80'], fontsize=6)
        elif j==3:
            axs[i, j].set_xlim([0, 10])
            axs[i, j].set_xticks([0,2,4,6,8,10])
            axs[i, j].set_xticklabels(['0','2','4','6','8','10'], fontsize=6)

        axs[i, j].tick_params(axis='y', length=0, labelsize=6)
        #
        axs[i, j].spines['right'].set_visible(False)
        axs[i, j].spines['top'].set_visible(False)
        #titile
        if j==3:
            if i==0:
                axs[i, j].set_title('co_mode', fontsize=8, pad=5)
            if i==1:
                axs[i, j].set_title('single_mode', fontsize=8, pad=5)
            if i==2:
                axs[i, j].set_title('multi_mode', fontsize=8, pad=5)
        else:
            axs[i, j].set_title(dataset, fontsize=7, pad=5)
        #
        # if j == 2 and dataset:
        #     axs[i, j].set_title(DATASETS_L[dataset], fontsize=11, pad=3)  # x=-0.5
        #     axs[i, j].set_ylabel('')
        # elif j == 0:
        #     axs[i, j].set_ylabel(string.ascii_lowercase[i], rotation='0', weight='bold', fontsize=12)
        #     axs[i, j].yaxis.set_label_coords(-1.1, 0.95)
        #     # axs[i, j].yaxis.set_label_coords(-0.8, 0.95)
        # else:
        #     axs[i, j].set_ylabel('')

        #
        # if j > 0:
        #     axs[i, j].set_yticklabels('')
        #
        if i == 2 and j<=2:
            axs[i, j].set_xlabel(xlabel, fontsize=8)
        if i == 2 and j ==3:
            axs[i, j].set_xlabel('Avg of ranks', fontsize=8)
        axs[i, j].grid(which='major', linestyle=':', linewidth='0.5', axis='x')

    #
    pastels = matplotlib.cm.get_cmap('Set3')

    co_sum_list = [0] * 10
    single_sum_list = [0] * 10
    multi_sum_list = [0] * 10
    for i, dataset in enumerate(datasets):
        print(dataset, i)
        data = pd.read_excel(DATASET_TO_PATH[dataset], index_col=0, header=0)
        data = data.rename(index={'VAMB_2000': 'VAMB', 'CLMB_2000': 'CLMB', 'MaxBin': 'MaxBin 2',
                                  'MetaBAT': 'MetaBAT 2', 'Metabinner': 'MetaBinner', 'SemiBin2':'SemiBin 2',
                                  })
        #print(data)

        y_tool = data.index.tolist()

        if i//3==1:
            mNGS_sing_MQ_list = rank_list(data['mNGS_sing_MQ'].tolist())
            mNGS_sing_NC_list = rank_list(data['mNGS_sing_NC'].tolist())
            mNGS_sing_HQ_list = rank_list(data['mNGS_sing_HQ'].tolist())
            Hifi_sing_MQ_list = rank_list(data['Hifi_sing_MQ'].tolist())
            Hifi_sing_NC_list = rank_list(data['Hifi_sing_NC'].tolist())
            Hifi_sing_HQ_list = rank_list(data['Hifi_sing_HQ'].tolist())
            hybrid_sing_MQ_list = rank_list(data['hybrid_sing_MQ'].tolist())
            hybrid_sing_NC_list = rank_list(data['hybrid_sing_NC'].tolist())
            hybrid_sing_HQ_list = rank_list(data['hybrid_sing_HQ'].tolist())

            cur_list = [sum(items) for items in zip(mNGS_sing_MQ_list, mNGS_sing_NC_list, mNGS_sing_HQ_list,
                                                  Hifi_sing_MQ_list, Hifi_sing_NC_list, Hifi_sing_HQ_list,
                                                  hybrid_sing_MQ_list, hybrid_sing_NC_list, hybrid_sing_HQ_list)]
            single_sum_list = [sum(items) for items in zip(cur_list, single_sum_list)]

        elif i//3==2:
            mNGS_sing_MQ_list = rank_list(data['mNGS_multi_MQ'].tolist())
            mNGS_sing_NC_list = rank_list(data['mNGS_multi_NC'].tolist())
            mNGS_sing_HQ_list = rank_list(data['mNGS_multi_HQ'].tolist())
            Hifi_sing_MQ_list = rank_list(data['Hifi_multi_MQ'].tolist())
            Hifi_sing_NC_list = rank_list(data['Hifi_multi_NC'].tolist())
            Hifi_sing_HQ_list = rank_list(data['Hifi_multi_HQ'].tolist())
            hybrid_sing_MQ_list = rank_list(data['hybrid_multi_MQ'].tolist())
            hybrid_sing_NC_list = rank_list(data['hybrid_multi_NC'].tolist())
            hybrid_sing_HQ_list = rank_list(data['hybrid_multi_HQ'].tolist())

            cur_list = [sum(items) for items in zip(mNGS_sing_MQ_list, mNGS_sing_NC_list, mNGS_sing_HQ_list,
                                                    Hifi_sing_MQ_list, Hifi_sing_NC_list, Hifi_sing_HQ_list,
                                                    hybrid_sing_MQ_list, hybrid_sing_NC_list, hybrid_sing_HQ_list)]

            multi_sum_list = [sum(items) for items in zip(cur_list, multi_sum_list)]

        elif i//3==0:
            mNGS_sing_MQ_list = rank_list(data['mNGS_co_MQ'].tolist())
            mNGS_sing_NC_list = rank_list(data['mNGS_co_NC'].tolist())
            mNGS_sing_HQ_list = rank_list(data['mNGS_co_HQ'].tolist())

            cur_list = [sum(items) for items in zip(mNGS_sing_MQ_list, mNGS_sing_NC_list, mNGS_sing_HQ_list)]
            co_sum_list = [sum(items) for items in zip(cur_list, co_sum_list)]


        if i//3==1 or i//3==2:
            df = pd.DataFrame({'#Short_MQ_MAGS': mNGS_sing_MQ_list,
                               '#Short_NC_MAGS': mNGS_sing_NC_list,
                               '#Short_HQ_MAGS':mNGS_sing_HQ_list,
                               '#Long_MQ_MAGS':Hifi_sing_MQ_list,
                               '#Long_NC_MAGS':Hifi_sing_NC_list,
                               '#Long_HQ_MAGS':Hifi_sing_HQ_list,
                               '#Hybrid_MQ_MAGS':hybrid_sing_MQ_list,
                               '#Hybrid_NC_MAGS':hybrid_sing_NC_list,
                               '#Hybrid_HQ_MAGS':hybrid_sing_HQ_list},
                               index = y_tool
                              )
        elif i//3==0:
            df = pd.DataFrame({'#Short_MQ_MAGS': mNGS_sing_MQ_list,
                               '#Short_NC_MAGS': mNGS_sing_NC_list,
                               '#Short_HQ_MAGS': mNGS_sing_HQ_list,
                               '#Long_MQ_MAGS': [0] * len(mNGS_sing_HQ_list),
                               '#Long_NC_MAGS': [0] * len(mNGS_sing_HQ_list),
                               '#Long_HQ_MAGS': [0] * len(mNGS_sing_HQ_list),
                               '#Hybrid_MQ_MAGS': [0] * len(mNGS_sing_HQ_list),
                               '#Hybrid_NC_MAGS': [0] * len(mNGS_sing_HQ_list),
                               '#Hybrid_HQ_MAGS': [0] * len(mNGS_sing_HQ_list)
                               },
                              index=y_tool
                              )

        #
        cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)][:9]
        cat_colors = sns.color_palette(cat_colors, desat=.75)

        df.plot.barh(stacked=True, ax=axs[i // 3, i % 3],
                     color=cat_colors, figsize=(5,5))

        # for patch, color in zip(axs[(i - 1) // 2, (i - 1) % 2].patches, cat_colors):
        #     patch.set_facecolor(color)
        #     patch.set_edgecolor('black')
        xlabel = "Sum of ranks"
        format_axs(i, i//3, i%3, dataset)


    print(y_tool)
    print([item/9 for item in co_sum_list])
    print([item/27 for item in single_sum_list])
    print([item/27 for item in multi_sum_list])
    df = pd.DataFrame([item/9 for item in co_sum_list],
                      index=y_tool)

    df.plot.barh(stacked=True, ax=axs[0, 3],
                 color='black', figsize=(5, 5),alpha=0.5)

    format_axs(11, 0, 3, dataset)

    df = pd.DataFrame([item/27 for item in single_sum_list],
                      index=y_tool)
    df.plot.barh(stacked=True, ax=axs[1, 3],
                 color='black', figsize=(5, 5),alpha=0.5)
    format_axs(11, 1, 3, dataset)

    df = pd.DataFrame([item/27 for item in multi_sum_list],
                      index=y_tool)
    df.plot.barh(stacked=True, ax=axs[2, 3],
                 color='black', figsize=(5, 5),alpha=0.5)
    format_axs(11, 2, 3, dataset)




def main():

    num_cols = 4
    num_rows = 3
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(8, 11))
    go(DATASETS, axs, num_rows)
    #
    plt.subplots_adjust(wspace=1.2, hspace=0.45)
    fig.savefig('./rank_avg_checkm2.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()