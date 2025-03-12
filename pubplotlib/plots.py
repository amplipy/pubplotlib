import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import os

from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FixedLocator, FixedFormatter
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

def PrettyMatplotlib(fig_font_scale=1.0, minor_tick_size=0.5, major_tick_size=1.0, num_minor_ticks=4, **kwargs):
    import matplotlib as mpl

    # Font sizes
    mpl.rcParams["axes.labelsize"] = fig_font_scale * 14
    mpl.rcParams["axes.titlesize"] = fig_font_scale * 16
    mpl.rcParams['font.family'] = 'Arial'
    mpl.rcParams['xtick.labelsize'] = fig_font_scale * 12
    mpl.rcParams['ytick.labelsize'] = fig_font_scale * 12
    mpl.rcParams["axes.labelpad"] = 0.7
    mpl.rcParams["legend.fontsize"] = fig_font_scale * 12  # Legend font size

    # Tick sizes
    mpl.rcParams['xtick.major.size'] = major_tick_size * 6
    mpl.rcParams['xtick.minor.size'] = minor_tick_size * 6
    mpl.rcParams['ytick.major.size'] = major_tick_size * 6
    mpl.rcParams['ytick.minor.size'] = minor_tick_size * 6

    # Number of minor ticks
    mpl.rcParams['xtick.minor.visible'] = True
    #just a comment
    mpl.rcParams['ytick.minor.visible'] = True
    mpl.rcParams['xtick.minor.top'] = True
    mpl.rcParams['ytick.minor.right'] = True
    mpl.rcParams['xtick.minor.bottom'] = True
    mpl.rcParams['ytick.minor.left'] = True
    mpl.rcParams['xtick.minor.width'] = minor_tick_size
    mpl.rcParams['ytick.minor.width'] = minor_tick_size
    mpl.rcParams['xtick.major.width'] = major_tick_size
    mpl.rcParams['ytick.major.width'] = major_tick_size

    # Apply additional customizations from kwargs
    for key, value in kwargs.items():
        mpl.rcParams[key] = value

_nred = lambda x: x/x[0]

def num_ticks(ax, xaxis=(4, 4), yaxis=(4, 4), log_scale=False):
    from matplotlib.ticker import AutoMinorLocator, MaxNLocator, LogLocator

    if log_scale:
        # Use LogLocator for log-scale axes
        #ax.xaxis.set_major_locator(LogLocator(base=10.0, numticks=major_ticks[0]))
        ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=yaxis[0]))
        #ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=minor_ticks[0]))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=yaxis[1]))
    else:
        # Use MaxNLocator and AutoMinorLocator for linear-scale axes
        ax.yaxis.set_major_locator(MaxNLocator(yaxis[0]))
        ax.yaxis.set_minor_locator(AutoMinorLocator(yaxis[1]))

    ax.xaxis.set_major_locator(MaxNLocator(xaxis[0]))
    ax.xaxis.set_minor_locator(AutoMinorLocator(xaxis[1]))
    # Example usage

def colorFader(c1, c2, mix=0):
    # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)


def plot_array(arr, **kwargs):
    
    import seaborn as sns

    params = {
        'alpha': 1.0,
        'ax': None,
        'x': np.arange(arr[0].shape[0]),
        'lw': 1.5,
        'linestyle': '-',
        'color': None,
        'cmap': 'viridis'
    }
    
    params.update(kwargs)

    if params['ax'] is None:
        f2, a2 = plt.subplots(1, 1)
    else:
        a2 = params['ax']
    
    if params['color'] is None:
        viridis = sns.color_palette(params['cmap'], as_cmap=True)
        colors = viridis(np.linspace(0.1, 1, len(arr)))
    else:
        colors = [params['color']] * len(arr)

    for _c, _arr in zip(colors, arr):
        a2.plot(params['x'], _arr, linewidth=params['lw'], color=_c, alpha=params['alpha'], linestyle=params['linestyle'])   

    if params['ax'] is None:
        return [f2, a2]