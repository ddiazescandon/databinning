import sys
import argparse
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import numpy as np
import seaborn as sns
import math
from collections import defaultdict
import pandas as pd
import string

def radar_factory(num_vars, frame='circle'):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels, *args, **kwargs):
            self.set_thetagrids(np.degrees(theta), labels, *args, **kwargs)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

def create_colors_list():
    colors_list = []
    for color in plt.cm.tab10(np.linspace(0, 1, 10))[:-1]:
        colors_list.append(tuple(color))
    colors_list.append("black")
    for color in plt.cm.Set2(np.linspace(0, 1, 8)):
        colors_list.append(tuple(color))
    for color in plt.cm.Set3(np.linspace(0, 1, 12)):
        colors_list.append(tuple(color))
    return colors_list

def get_data():
    DATASET_TO_PATH = {
        "Human_gut_I_short_co" : "radar_data/human_short_co.xlsx",
        "Human_gut_I_short_single" : "radar_data/human_short_single.xlsx",
        "Human_gut_I_short_multi" : "radar_data/human_short_multi.xlsx",
        "Human_gut_I_long_single" : "radar_data/human_long_single.xlsx",
        "Human_gut_I_long_multi" : "radar_data/human_long_multi.xlsx",
        "Human_gut_I_hybrid_single" : "radar_data/human_hybrid_single.xlsx",
        "Human_gut_I_hybrid_multi" : "radar_data/human_hybrid_multi.xlsx",

        "Human_gut_II_short_co": "radar_data/human_30_short_co.xlsx",
        "Human_gut_II_short_single": "radar_data/human_30_short_single.xlsx",
        "Human_gut_II_short_multi": "radar_data/human_30_short_multi.xlsx",
        "Human_gut_II_long_single": "radar_data/human_30_long_single.xlsx",
        "Human_gut_II_long_multi": "radar_data/human_30_long_multi.xlsx",
        "Human_gut_II_hybrid_single": "radar_data/human_30_hybrid_single.xlsx",
        "Human_gut_II_hybrid_multi": "radar_data/human_30_hybrid_multi.xlsx",

        "Activated_sludge_short_co": "radar_data/activated_sludge_short_co.xlsx",
        "Activated_sludge_short_single": "radar_data/activated_sludge_short_single.xlsx",
        "Activated_sludge_short_multi": "radar_data/activated_sludge_short_multi.xlsx",
        "Activated_sludge_long_single": "radar_data/activated_sludge_long_single.xlsx",
        "Activated_sludge_long_multi": "radar_data/activated_sludge_long_multi.xlsx",
        "Activated_sludge_hybrid_single": "radar_data/activated_sludge_hybrid_single.xlsx",
        "Activated_sludge_hybrid_multi": "radar_data/activated_sludge_hybrid_multi.xlsx",

        "Cheese_short_co" : "radar_data/cheese_short_co.xlsx",
        "Cheese_short_single" : "radar_data/cheese_short_single.xlsx",
        "Cheese_short_multi" : "radar_data/cheese_short_multi.xlsx",
        "Cheese_long_single" : "radar_data/cheese_long_single.xlsx",
        "Cheese_long_multi" : "radar_data/cheese_long_multi.xlsx",
        "Cheese_hybrid_single" : "radar_data/cheese_hybrid_single.xlsx",
        "Cheese_hybrid_multi" : "radar_data/cheese_hybrid_multi.xlsx",

        "Marine_short_co" : "radar_data/marine_short_co.xlsx",
        "Marine_short_single" : "radar_data/marine_short_single.xlsx",
        "Marine_short_multi" : "radar_data/marine_short_multi.xlsx",
        "Marine_long_single" : "radar_data/marine_long_single.xlsx",
        "Marine_long_multi" : "radar_data/marine_long_multi.xlsx",
        "Marine_hybrid_single" : "radar_data/marine_hybrid_single.xlsx",
        "Marine_hybrid_multi" : "radar_data/marine_hybrid_multi.xlsx",
    }

    d_comb = defaultdict(list)
    modes= ["short_co", "short_single", "short_multi", "long_single", "long_multi", "hybrid_single", "hybrid_multi"]
    combs = ["Marine_MQ", "Marine_NC", "Marine_HQ", "Cheese_MQ", "Cheese_NC", "Cheese_HQ", "Human_gut_I_MQ", "Human_gut_I_NC", "Human_gut_I_HQ", "Human_gut_II_MQ", "Human_gut_II_NC", "Human_gut_II_HQ", "Activated_sludge_MQ", "Activated_sludge_NC", "Activated_sludge_HQ"]
    #
    for comb in combs:
        cur_dataname, cur_q = comb[: comb.rfind("_")], comb[comb.rfind("_") + 1 :]
        DAS_list = []
        MAG_list = []
        Metawrap_list = []
        #
        for mode in modes:
            cur_data = pd.read_excel(DATASET_TO_PATH[cur_dataname + '_' + mode], index_col=0, header=0)
            DAS_list.append(cur_data.loc["DAS_tool"][cur_q])
            MAG_list.append(cur_data.loc["MAGScoT"][cur_q])
            Metawrap_list.append(cur_data.loc["Metawrap"][cur_q])
        #
        d_comb[comb].append(DAS_list)
        d_comb[comb].append(MAG_list)
        d_comb[comb].append(Metawrap_list)
    # for key, value in d_comb.items():
    #     print(key)
    #     print(value)
    return modes, combs, d_comb





if __name__ == '__main__':
    theta = radar_factory(7, frame='polygon')
    colors = [sns.color_palette('colorblind')[x] for x in [1, 2, 4]]

    fig, axes = plt.subplots(figsize=(14, 26), nrows=5, ncols=3, subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.1, hspace=0.5, top=0.87, bottom=0.45,left=0.3, right=0.87)

    modes, combs, d_comb = get_data()
    print(d_comb)

    #
    annot = list(string.ascii_lowercase)
    i=0
    for ax, comb in zip(axes.flat, combs):
        it = 1
        for d, color in zip(d_comb[comb], colors):
            print(d)
            print(color)
            ax.plot(theta, d, color=color, linewidth=1.5, dashes=(it, 2))
            it += 1

        labels = ["DAStool", "MAGScoT", "MetaWRAP"]
        ax.set_title(comb, size=10, position=(0.5, 1.15), horizontalalignment='center', verticalalignment='center')
        ax.set_varlabels(["Short_co", "Short_single", "Short_multi", "Long_single", "Long_multi", "Hybrid_single", "Hybrid_multi"], fontsize=8)
        ax.text(-0.1, 1.05, annot[i], transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')
        i+=1
        ax = axes[0, 0]

        ax.legend(labels, loc=(2.5 - 0.5 * len(labels), 1.25), labelspacing=1, fontsize=12, ncol=len(labels), frameon=False)


    plt.savefig("./radar.pdf", dpi=300, format='pdf', bbox_inches='tight')





