"""
Matplotlib plotting functions.
"""
import matplotlib.pyplot as plt
import numpy as np

from .base import Pipeable, unpack_input
from .style import mpl_style, mpl_style_decorator, show_grid

line_kwargs = {
    'marker': 'o',
    'markersize': 3,
    'linewidth': 1,
    'linestyle': '-',
}

@Pipeable
@mpl_style_decorator
def Plot(*args, **kwargs):

    if not kwargs:
        kwargs = line_kwargs

    handle = plt.plot(*args, **kwargs)

    # Autoformat dates.
    fig = plt.gcf()
    fig.autofmt_xdate()

    return handle


@unpack_input
@Pipeable
@mpl_style_decorator
def Scatter(*args, **kwargs):

    if not kwargs:
        kwargs['alpha'] = 0.5

    return plt.scatter(*args, **kwargs)


@Pipeable
@mpl_style_decorator
def LogLogHist(a, bins=10, range=None, normed=None, weights=None, density=None, **kwargs):
    """A log-log histogram.
    """

    # If there are no plot kwargs, use default style.
    if not kwargs:
        kwargs.update(line_kwargs)

    y, x = np.histogram(a, bins=bins, range=range, normed=normed, weights=weights, density=density)
    handle = plt.plot((x[1:] + x[:-1])/2, y, **kwargs)
    plt.xscale('log')
    plt.yscale('log')

    return handle


@Pipeable
@mpl_style_decorator
def Hist(*args, **kwargs):
    handle = plt.hist(*args, **kwargs)
    return handle

