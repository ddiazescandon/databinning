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

DATASETS = ['Marine_MQ',  'Marine_NC', 'Marine_HQ',
            'Cheese_MQ', 'Cheese_NC', 'Cheese_HQ',
            'human_gut_3_MQ', 'human_gut_3_NC', 'human_gut_3_HQ',
            'human_gut_MQ', 'human_gut_NC', 'human_gut_HQ',
            'waster_water_MQ', 'waster_water_NC', 'waster_water_HQ']

DATASET_TO_PATH = {'Marine_MQ':'heatmap_data/Marine_MQ.xlsx',
                   'Marine_NC':'heatmap_data/Marine_NC.xlsx',
                   'Marine_HQ':'heatmap_data/Marine_HQ.xlsx',
                   'Cheese_MQ':'heatmap_data/Cheese_MQ.xlsx',
                   'Cheese_NC':'heatmap_data/Cheese_NC.xlsx',
                   'Cheese_HQ':'heatmap_data/Cheese_HQ.xlsx',
                   'human_gut_3_MQ': 'heatmap_data/Human_gut_3_MQ.xlsx',
                   'human_gut_3_NC': 'heatmap_data/Human_gut_3_NC.xlsx',
                   'human_gut_3_HQ': 'heatmap_data/Human_gut_3_HQ.xlsx',
                   'human_gut_MQ':'heatmap_data/Human_gut_MQ.xlsx',
                   'human_gut_NC':'heatmap_data/Human_gut_NC.xlsx',
                   'human_gut_HQ':'heatmap_data/Human_gut_HQ.xlsx',
                   'waster_water_MQ':'heatmap_data/Waster_water_MQ.xlsx',
                   'waster_water_NC':'heatmap_data/Waster_water_NC.xlsx',
                   'waster_water_HQ':'heatmap_data/Waster_water_HQ.xlsx'}

DATASETS_L = {'Marine_MQ': 'Marine',
              'Cheese_MQ': 'Cheese',
              'human_gut_3_MQ' : 'Human gut I',
              'human_gut_MQ': 'Human gut II',
              'waster_water_MQ': 'Activated sludge'}


def go(datasets, axs, num_rows):

    def format_axs(n, i, j, dataset=None):
        annot = list(string.ascii_lowercase)
        axs[i, j].text(-0.1, 1.08, annot[n], transform=axs[i, j].transAxes, fontsize=12, fontweight='bold', va='top')
        #
        if i<2:
            axs[i, j].xaxis.set_visible(False)
        else:
            axs[i, j].set_xticklabels(labels=['Short_co', 'Short_single', 'Short_multi',  'Long_single', 'Long_multi', 'Hybrid_single', 'Hybrid_multi'], rotation=25, minor=False, fontsize=11, color='black',ha='right')
        axs[i, j].yaxis.set_tick_params(labelsize=13)
        #
        # axs[i, j].spines['right'].set_visible(False)
        # axs[i, j].spines['top'].set_visible(False)
        #
        if i==0 and j==0:
            axs[i, j].set_title("MQ MAGs (n)", fontsize=15, pad=5)
        elif i==0 and j==1:
            axs[i, j].set_title("NC MAGs (n)", fontsize=15, pad=5)
        elif i==0 and j==2:
            axs[i, j].set_title("HQ MAGs (n)", fontsize=15, pad=5)

        if i==0 and j==0:
            axs[i, j].set_ylabel(DATASETS_L[dataset], fontsize=15)
        elif i==1 and j==0:
            axs[i, j].set_ylabel(DATASETS_L[dataset], fontsize=15)
        elif i==2 and j==0:
            axs[i, j].set_ylabel(DATASETS_L[dataset], fontsize=15)
        elif i==3 and j==0:
            axs[i, j].set_ylabel(DATASETS_L[dataset], fontsize=15)
        elif i==4 and j==0:
            axs[i, j].set_ylabel(DATASETS_L[dataset], fontsize=15)


    #

    for i, dataset in enumerate(datasets):
        print(dataset, i)
        data = pd.read_excel(DATASET_TO_PATH[dataset], index_col=0, header=0)
        mean_values = data.median().round().astype(int)
        data.loc['Median'] = mean_values
        #
        column_name_mapping = {
            'mNGS_co': 'Short_co',
            'mNGS_sing': 'Short_single',
            'mNGS_mul': 'Short_multi',
            'HiFi_sing': 'Long_single',
            'HiFi_mul': 'Long_multi',
            'hybrid_sing': 'Hybrid_single',
            'hybrid_mul': 'Hybrid_multi',
        }
        #
        data.rename(columns=column_name_mapping, inplace=True)
        if 'waster_water' in dataset:
            true_matrix = np.full(data.shape, True)
            true_matrix[0, 0], true_matrix[1, 0], true_matrix[7, 0], true_matrix[9, 0] = False, False, False, False
            print(data)
            print(true_matrix)
            annot_data = np.where(true_matrix, data, np.nan)
            sns.heatmap(data, annot=annot_data, linewidth=1, linecolor='w', cmap="OrRd", fmt='.0f',
                        ax=axs[i // 3, i % 3], cbar_kws={"shrink": 0.8}, annot_kws={'fontsize': 9.5})
        #print(data)
        else:
            sns.heatmap(data, annot=True, linewidth=1, linecolor='w',
                    cmap="OrRd", fmt='d', ax=axs[i // 3, i % 3], cbar_kws={"shrink": 0.8}, annot_kws={'fontsize':9.5})
        #axs[i // 3, i % 3].set_aspect('auto')

        format_axs(i, i//3, i%3, dataset)



def main():

    num_cols = 3
    num_rows = 5
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(17, 14), sharex=True)
    go(DATASETS, axs, num_rows)
    #
    plt.subplots_adjust(wspace=0.3, hspace=0.04)

    fig.tight_layout()
    fig.savefig('./5_3_heatmap.pdf', dpi=300, format='pdf', bbox_inches='tight')
    plt.close()

    print('done')


if __name__ == "__main__":
    main()