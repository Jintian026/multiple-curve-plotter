import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

def multiple_curves_plot(title, datas, labels, xticks, yticks, xlabel, ylabel):
    x = []
    y = []
    line_styles = ['-', '--', '-.', (0, (8, 5, 1, 5, 1, 5)), ':']
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    markers = ['^', 's', 'x', 'o', 'D']
    if len(datas) > 5:
        raise ValueError("Supports up to 5 datasets only.")
    for data in datas:
        x.append(data[0])
        y.append(data[1])
    plt.figure(figsize=(5, 3), dpi=300)
    for i in range(len(datas)):
        plt.plot(
            x[i], y[i],
            linestyle=line_styles[i],
            color=colors[i],
            marker=markers[i],
            label=labels[i],
            markersize=5
        )
    if xticks is not None:
        xtick_vals = np.arange(xticks['min'], xticks['max'] + xticks['interval'], xticks['interval'])
        xtick_labels = [f"{val}{xticks.get('suffix','')}" for val in xtick_vals]
        plt.xticks(xtick_vals, xtick_labels, fontsize=9)
        plt.xlim(xticks['min'], xticks['max'])
    if yticks is not None:
        ytick_vals = np.arange(yticks['min'], yticks['max'] + yticks['interval'], yticks['interval'])
        ytick_labels = [f"{val}{yticks.get('suffix','')}" for val in ytick_vals]
        plt.yticks(ytick_vals, ytick_labels, fontsize=9)
        plt.ylim(yticks['min'], yticks['max'])
    if xticks is not None and xticks.get('style', 'linear') == 'log':
        plt.xscale('log')
    if yticks is not None and yticks.get('style', 'linear') == 'log':
        plt.yscale('log')
    if 'round' in xticks:
        plt.gca().xaxis.set_major_formatter(FormatStrFormatter(xticks['round']))
    if 'round' in yticks:
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter(yticks['round']))
    plt.title(title, fontsize=9, fontweight="bold")
    plt.xlabel(xlabel, fontsize=9, fontweight="bold")
    plt.ylabel(ylabel, fontsize=9, fontweight="bold")
    plt.grid(True)
    plt.legend(fontsize=9)
    plt.tight_layout()
    plt.show()


def multiple_curves_plot_2y(title, datas_y1, datas_y2, labels, xticks, yticks1, yticks2, xlabel, ylabel1, ylabel2):
    line_styles = ['-', '--', '-.', (0, (8, 5, 1, 5, 1, 5)), ':']
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    markers = ['^', 's', 'x', 'o', 'D']
    fig, ax1 = plt.subplots(figsize=(5, 3), dpi=300)
    for i, data in enumerate(datas_y1):
        ax1.plot(
            data[0], data[1],
            linestyle=line_styles[i % len(line_styles)],
            color=colors[i % len(colors)],
            marker=markers[i % len(markers)],
            label=labels[i],
            markersize=5,
            zorder=3
        )
    if xticks is not None:
        xtick_vals = np.arange(xticks['min'], xticks['max'] + xticks['interval'], xticks['interval'])
        xtick_labels = [f"{val}{xticks.get('suffix','')}" for val in xtick_vals]
        ax1.set_xticks(xtick_vals)
        ax1.set_xticklabels(xtick_labels, fontsize=9)
        ax1.set_xlim(xticks['min'], xticks['max'])
        if xticks.get('style','linear') == 'log':
            ax1.set_xscale('log')
    ax1.set_xlabel(xlabel, fontsize=9, fontweight="bold")
    ax1.set_ylabel(ylabel1, fontsize=9, fontweight="bold")
    if yticks1 is not None:
        ytick_vals = np.arange(yticks1['min'], yticks1['max'] + yticks1['interval'], yticks1['interval'])
        ytick_labels = [f"{val}{yticks1.get('suffix','')}" for val in ytick_vals]
        ax1.set_yticks(ytick_vals)
        ax1.set_yticklabels(ytick_labels, fontsize=9)
        ax1.set_ylim(yticks1['min'], yticks1['max'])
        if yticks1.get('style','linear') == 'log':
            ax1.set_yscale('log')
    ax1.set_axisbelow(True)
    ax1.grid(True, which='major', axis='x', linestyle='-', alpha=0.6)
    ax1.grid(True, which='major', axis='y', linestyle='-', alpha=0.3)
    ax2 = ax1.twinx()
    for j, data in enumerate(datas_y2):
        ax2.plot(
            data[0], data[1],
            linestyle=line_styles[(j + len(datas_y1)) % len(line_styles)],
            color=colors[(j + len(datas_y1)) % len(colors)],
            marker=markers[j % len(markers)],
            label=labels[len(datas_y1) + j],
            markersize=5,
            zorder=4
        )
    ax2.set_ylabel(ylabel2, fontsize=9, fontweight="bold")
    if yticks2 is not None:
        ytick_vals = np.arange(yticks2['min'], yticks2['max'] + yticks2['interval'], yticks2['interval'])
        ytick_labels = [f"{val}{yticks2.get('suffix','')}" for val in ytick_vals]
        ax2.set_yticks(ytick_vals)
        ax2.set_yticklabels(ytick_labels, fontsize=9)
        ax2.set_ylim(yticks2['min'], yticks2['max'])
        if yticks2.get('style','linear') == 'log':
            ax2.set_yscale('log')
    ax2.patch.set_visible(False)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='best')
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter(xticks['round']))
    if 'round' in yticks1:
        ax1.yaxis.set_major_formatter(FormatStrFormatter(yticks1['round']))
    if 'round' in yticks2:
        ax2.yaxis.set_major_formatter(FormatStrFormatter(yticks2['round']))
    plt.title(title, fontsize=9, fontweight="bold")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    data1 = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8]]
    data2 = [[1, 2, 3, 4, 5], [6, 5, 4, 3, 2]]
    data3 = [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]]
    data4 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]

    # 单 y 轴
    multiple_curves_plot(
        title='Single Y-axis Example',
        datas=[data1, data2],
        labels=['Data 1', 'Data 2'],
        xticks={'min':0, 'max':6, 'interval':1, 'suffix':'', 'style':'linear', 'round':"%.2f"},
        yticks={'min':2, 'max':9, 'interval':1, 'suffix':'', 'style':'linear', 'round':"%.2f"},
        xlabel='X Label',
        ylabel='Y Label'
    )

    # 双 y 轴
    multiple_curves_plot_2y(
        title='Dual Y-axis Example',
        datas_y1=[data1, data2],
        datas_y2=[data3, data4],
        labels=['Left 1', 'Left 2', 'Right 1', 'Right 2'],
        xticks={'min':0, 'max':6, 'interval':1, 'suffix':'', 'style':'linear', 'round':"%.2f"},
        yticks1={'min':2, 'max':9, 'interval':1, 'suffix':'', 'style':'linear', 'round':"%.2f"},
        yticks2={'min':2, 'max':9, 'interval':1, 'suffix':'', 'style':'linear', 'round':"%.2f"},
        xlabel='X Label',
        ylabel1='Left Y',
        ylabel2='Right Y'
    )
