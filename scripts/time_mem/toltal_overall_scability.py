import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import sys
import string
from matplotlib.gridspec import GridSpec
from scipy.stats import rankdata
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
fig, axes = plt.subplots(3, 7, figsize=(22, 16))
annot = list(string.ascii_lowercase)
axes[0, 0].text(-0.12, 1.1, annot[0], transform=axes[0, 0].transAxes, fontsize=18, fontweight='bold', va='top')
axes[1, 0].text(-0.12, 1.1, annot[1], transform=axes[1, 0].transAxes, fontsize=18, fontweight='bold', va='top')
axes[2, 0].text(-0.12, 1.1, annot[2], transform=axes[2, 0].transAxes, fontsize=18, fontweight='bold', va='top')
#
for i in range(7):
    data1 = pd.read_csv(rank_file_list[i], sep='\t', index_col=0,encoding='utf-8')
    data2 = pd.read_csv(rank_file_list[i + 7], sep='\t', index_col=0, encoding='utf-8')
    data3 = pd.read_csv(rank_file_list[i + 7*2], sep='\t', index_col=0, encoding='utf-8')
    data4 = pd.read_csv(rank_file_list[i + 7*3], sep='\t', index_col=0, encoding='utf-8')
    data5 = pd.read_csv(rank_file_list[i + 7*4], sep='\t', index_col=0, encoding='utf-8')

    data = (data1 + data2 + data3 + data4 + data5) / 5
    #print(data.index)
    #print(data)
    new_index=['concoct', 'maxbin2.2.7', 'metabat2.15', 'vamb', 'clmb','Metadecoder','binny','Metabinner','Semibin2','Comebin'][::-1]
    data = data.reindex(new_index)
    #
    data = data.rename(index={'concoct': 'CONCOCT', 'maxbin2.2.7':'MaxBin 2', \
    'metabat2.15':'MetaBAT 2', 'vamb':'VAMB', 'clmb':'CLMB', 'Metadecoder':'MetaDecoder',\
    'binny':'Binny', 'Metabinner':'MetaBinner', 'Semibin2':'SemiBin 2', 'Comebin':'COMEBin'})

    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)][2:len(data.index)+2]
    cat_colors = sns.color_palette(cat_colors, desat=1)

    #
    axes[0, i].barh(data.index, data['overall_rank'], color=cat_colors, edgecolor='black')
    axes[0, i].tick_params(axis='y', labelsize=16)
    #
    for y, value in enumerate(rankdata(data['overall_rank'])):
        if value == 1:
            axes[0, i].text(
                data['overall_rank'][y] + 0.5,  #
                y,  #
                f'{int(value)}st',  #
                va='center',  #
                ha='left',  #
                fontsize=12  #
            )
        elif value == 2:
            axes[0, i].text(
                data['overall_rank'][y] + 0.5,  #
                y,  #
                f'{int(value)}nd',  #
                va='center',  #
                ha='left',  #
                fontsize=12  #
            )
        elif value==3:
            axes[0, i].text(
                data['overall_rank'][y] + 0.5,  #
                y,  #
                f'{int(value)}rd',  #
                va='center',  #
                ha='left',  #
                fontsize=12  #
            )
        else:
            axes[0, i].text(
                data['overall_rank'][y] + 0.5,  #
                y,  #
                f'{int(value)}th',  #
                va='center',  #
                ha='left',  #
                fontsize=12  #
            )

#
data_time = pd.read_csv('time_new.txt', sep='\t', index_col=0, encoding='utf-8')
data_time = data_time[::-1]
std_time = pd.read_csv('time_std.txt', sep='\t', index_col=0, encoding='utf-8')
std_time = std_time[::-1]
data_all_time = pd.read_csv('time_all.txt', sep='\t', index_col=0, encoding='utf-8')
data_all_time = data_all_time[::-1]
#print(data_time)
for i in range(7):
    # print(i)
    cur_data = data_time.iloc[:, i]
    cur_all_data = data_all_time.iloc[:, i].tolist()
    if i>0:
        for z, item in enumerate(cur_all_data):
            cur_items = item.split(',')
            cur_all_data[z] = list(map(int, cur_items))

    cur_std = std_time.iloc[:, i]
    # print(cur_data)
    # print(cur_data[cur_data  == 0].index)
    #
    # valid_rows = cur_data[cur_data != 0].index
    # cur_data = cur_data.loc[valid_rows]

    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)]
    cat_colors = sns.color_palette(cat_colors, desat=1)
    if i==0:
        axes[1, i].barh(cur_data.index, cur_data, color=cat_colors, edgecolor='black')
        axes[1, i].tick_params(axis='y', labelsize=16)
    else:
        axes[1, i].barh(cur_data.index, cur_data, color=cat_colors, edgecolor='black', xerr=cur_std, error_kw={'linewidth': 2, 'capsize': 7})
        print(cur_data.index)
        for j in range(len(cur_data.index)):
            axes[1, i].scatter(cur_all_data[j], [list(cur_data.index)[j]]*len(cur_all_data[j]), color='black', zorder=5, label='Data points',s=5, alpha=0.7)
        axes[1, i].tick_params(axis='y', labelsize=16)
    #
    cur_max_data = max(cur_data)
    for y, value in enumerate(cur_data):
        if value==0:
            axes[1, i].text(
                cur_max_data*0.02,  #
                y,  #
                f'nan',  #
                va='center',  #
                ha='left',  #
                fontsize=14  #
            )



#
data_time = pd.read_csv('mem_new.txt', sep='\t', index_col=0, encoding='utf-8')
data_time = data_time[::-1]
data_std = pd.read_csv('mem_std.txt', sep='\t', index_col=0, encoding='utf-8')
data_std = data_std[::-1]
data_all_time = pd.read_csv('mem_all.txt', sep='\t', index_col=0, encoding='utf-8')
data_all_time = data_all_time[::-1]

#print(data_time)
for i in range(7):
    # print(i)
    cur_data = data_time.iloc[:, i]
    cur_all_data = data_all_time.iloc[:, i].tolist()
    if i>0:
        for z, item in enumerate(cur_all_data):
            cur_items = item.split(',')
            cur_all_data[z] = list(map(float, cur_items))
    cur_std = data_std.iloc[:, i]
    # print(cur_data)
    # print(cur_data[cur_data  == 0].index)
    #
    # valid_rows = cur_data[cur_data != 0].index
    # cur_data = cur_data.loc[valid_rows]

    pastels = matplotlib.cm.get_cmap('Set3')
    cat_colors = [pastels(x) for x in np.linspace(0, 1, 12)]
    cat_colors = sns.color_palette(cat_colors, desat=1)
    if i== 0:
        axes[2, i].barh(cur_data.index, cur_data, color=cat_colors, edgecolor='black')
        axes[2, i].tick_params(axis='y', labelsize=16)
    else:
        axes[2, i].barh(cur_data.index, cur_data, color=cat_colors, edgecolor='black', xerr=cur_std, error_kw={'linewidth': 2, 'capsize': 7})
        print(cur_data.index)
        for j in range(len(cur_data.index)):
            axes[2, i].scatter(cur_all_data[j], [list(cur_data.index)[j]]*len(cur_all_data[j]), color='black', zorder=5, label='Data points',s=6, alpha=0.7)
        axes[2, i].tick_params(axis='y', labelsize=16)
    #
    cur_max_data = max(cur_data)
    for y, value in enumerate(cur_data):
        if value ==0:
            axes[2, i].text(
                cur_max_data*0.02,  #
                y,  #
                f'nan',  #
                va='center',  #
                ha='left',  #
                fontsize=14  #
            )



title_list = ['Short_co', 'Short_single', 'Short_multi', 'Long_single', 'Long_multi', 'Hybrid_single', 'Hybrid_multi']
for j in range(3):
    for i in range(7):
        if j==0:
            axes[j,i].set_xlim([0, 11])
            axes[j,i].set_xlabel('')
            #y title
            axes[j, i].set_title(title_list[i], fontsize=21)
        if i!=0:
            axes[j,i].set_yticks([])
        # x title
        if i == 3 :
            if j == 0:
                axes[j,i].set_xlabel("Overall ranking score", fontsize=21)
            elif j == 1:
                axes[j,i].set_xlabel("Time (minutes)", fontsize=21)
            elif j == 2:
                axes[j,i].set_xlabel("Memory (GB)", fontsize=21)
        #
        axes[j,i].spines['right'].set_visible(False)
        axes[j,i].spines['top'].set_visible(False)
        axes[j,i].spines['top'].set_visible(False)

plt.savefig("overall_scability_barplot_final.pdf", format="pdf")