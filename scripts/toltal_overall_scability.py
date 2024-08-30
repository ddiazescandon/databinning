import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import sys
import string
rank_file_list = ['data/marine_short_co_samples_all_rank.csv',
                  'data/marine_short_single_samples_all_rank.csv',
                  'data/marine_short_multi_samples_all_rank.csv',
                  'data/marine_long_single_samples_all_rank.csv',
                  'data/marine_long_multi_samples_all_rank.csv',
                  'data/marine_hybrid_single_samples_all_rank.csv',
                  'data/marine_hybrid_multi_samples_all_rank.csv',
                  'data/cheese_short_co_samples_all_rank.csv',
                  'data/cheese_short_single_samples_all_rank.csv',
                  'data/cheese_short_multi_samples_all_rank.csv',
                  'data/cheese_long_single_samples_all_rank.csv',
                  'data/cheese_long_multi_samples_all_rank.csv',
                  'data/cheese_hybrid_single_samples_all_rank.csv',
                  'data/cheese_hybrid_multi_samples_all_rank.csv',
                  'data/human_short_co_samples_all_rank.csv',
                  'data/human_short_single_samples_all_rank.csv',
                  'data/human_short_multi_samples_all_rank.csv',
                  'data/human_long_single_samples_all_rank.csv',
                  'data/human_long_multi_samples_all_rank.csv',
                  'data/human_hybrid_single_samples_all_rank.csv',
                  'data/human_hybrid_multi_samples_all_rank.csv',
                  'data/water_short_co_samples_all_rank.csv',
                  'data/water_short_single_samples_all_rank.csv',
                  'data/water_short_multi_samples_all_rank.csv',
                  'data/water_long_single_samples_all_rank.csv',
                  'data/water_long_multi_samples_all_rank.csv',
                  'data/water_hybrid_single_samples_all_rank.csv',
                  'data/water_hybrid_multi_samples_all_rank.csv',
                  'data/human_3_short_co_samples_all_rank.csv',
                  'data/human_3_short_single_samples_all_rank.csv',
                  'data/human_3_short_multi_samples_all_rank.csv',
                  'data/human_3_long_single_samples_all_rank.csv',
                  'data/human_3_long_multi_samples_all_rank.csv',
                  'data/human_3_hybrid_single_samples_all_rank.csv',
                  'data/human_3_hybrid_multi_samples_all_rank.csv',
                  ]

#
fig, axes = plt.subplots(3, 7, figsize=(22, 12))
annot = list(string.ascii_lowercase)
axes[0, 0].text(-0.12, 1.1, annot[0], transform=axes[0, 0].transAxes, fontsize=18, fontweight='bold', va='top')
axes[1, 0].text(-0.12, 1.1, annot[1], transform=axes[1, 0].transAxes, fontsize=18, fontweight='bold', va='top')
axes[2, 0].text(-0.12, 1.1, annot[2], transform=axes[2, 0].transAxes, fontsize=18, fontweight='bold', va='top')
##
for i in range(7):
    data1 = pd.read_csv(rank_file_list[i], sep='\t', index_col=0,encoding='utf-8')
    data2 = pd.read_csv(rank_file_list[i + 7], sep='\t', index_col=0, encoding='utf-8')
    data3 = pd.read_csv(rank_file_list[i + 7*2], sep='\t', index_col=0, encoding='utf-8')
    data4 = pd.read_csv(rank_file_list[i + 7*3], sep='\t', index_col=0, encoding='utf-8')
    data5 = pd.read_csv(rank_file_list[i + 7*4], sep='\t', index_col=0, encoding='utf-8')
    if i == 0:
        #
        # new_data = [0] * len(data4.columns)
        # data4.loc['maxbin2.2.7'] = new_data
        # data4.loc['Metabinner'] = new_data
        # data4.loc['Comebin'] = new_data
        data = (data1 + data2 + data3 + data5)/4
        #
        # data.loc['maxbin2.2.7'] = new_data
        # data.loc['Metabinner'] = new_data
        # data.loc['Comebin'] = new_data
    else:
        data = (data1 + data2 + data3 + data4 + data5) / 5
    print(data.index)
    print(data)
    new_index=['concoct', 'maxbin2.2.7', 'metabat2.15', 'vamb', 'clmb','Metadecoder','binny','Metabinner','Semibin2','Comebin'][::-1]
    data = data.reindex(new_index)
    #
    data = data.rename(index={'concoct': 'CONCOCT', 'maxbin2.2.7':'MaxBin 2', \
    'metabat2.15':'MetaBAT 2', 'vamb':'VAMB', 'clmb':'CLMB', 'Metadecoder':'MetaDecoder',\
    'binny':'Binny', 'Metabinner':'MetaBinner', 'Semibin2':'SemiBin 2', 'Comebin':'COMEBin'})

    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)][:len(data.index)]
    cat_colors = sns.color_palette(cat_colors, desat=1)

    #
    axes[0, i].barh(data.index, data['overall_rank'], color=cat_colors, edgecolor='black')
    axes[0, i].tick_params(axis='y', labelsize=16)

##
data_time = pd.read_csv('data/time_new.txt', sep='\t', index_col=0, encoding='utf-8')
data_time = data_time[::-1]
print(data_time)
for i in range(7):
    # print(i)
    cur_data = data_time.iloc[:, i]
    # print(cur_data)
    # print(cur_data[cur_data  == 0].index)
    #
    # valid_rows = cur_data[cur_data != 0].index
    # cur_data = cur_data.loc[valid_rows]

    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)]
    cat_colors = sns.color_palette(cat_colors, desat=1)

    axes[1, i].barh(cur_data.index, cur_data, color=cat_colors, edgecolor='black')
    axes[1, i].tick_params(axis='y', labelsize=16)

#
data_time = pd.read_csv('data/mem_new.txt', sep='\t', index_col=0, encoding='utf-8')
data_time = data_time[::-1]
print(data_time)
for i in range(7):
    # print(i)
    cur_data = data_time.iloc[:, i]
    # print(cur_data)
    # print(cur_data[cur_data  == 0].index)
    #
    # valid_rows = cur_data[cur_data != 0].index
    # cur_data = cur_data.loc[valid_rows]

    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)]
    cat_colors = sns.color_palette(cat_colors, desat=1)

    axes[2, i].barh(cur_data.index, cur_data, color=cat_colors, edgecolor='black')
    axes[2, i].tick_params(axis='y', labelsize=16)


title_list = ['Short_co', 'Short_single', 'Short_multi', 'Long_single', 'Long_multi', 'Hybrid_single', 'Hybrid_multi']
for j in range(3):
    for i in range(7):
        if j==0:
            axes[j,i].set_xlim([0, 11])
            axes[j,i].set_xlabel('')
            #y title
            axes[j, i].set_title(title_list[i], fontsize=19)
        if i!=0:
            axes[j,i].set_yticks([])
        # x title
        if i == 0 :
            if j == 0:
                axes[j,i].set_ylabel("Overall ranking score", fontsize=19)
            elif j == 1:
                axes[j,i].set_ylabel("Time (minutes)", fontsize=19)
            elif j == 2:
                axes[j,i].set_ylabel("Memory (GB)", fontsize=19)
        #
        axes[j,i].spines['right'].set_visible(False)
        axes[j,i].spines['top'].set_visible(False)
        axes[j,i].spines['top'].set_visible(False)

plt.savefig("overall_scability_barplot.pdf", format="pdf")