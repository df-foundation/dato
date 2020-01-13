"""
Static plotting functions (e.g. matplotlib, seaborn).

"""
import functools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import FacetGrid

from ..base import Pipeable
from ..style import mpl_style_decorator

line_kwargs = {
    'marker': 'o',
    'markersize': 3,
    'linewidth': 1,
    'linestyle': '-',
}


class DatoFacetGrid(FacetGrid):
    def _facet_plot(self, func, ax, plot_args, plot_kwargs):
        # Draw the plot
        plot_args >> func(**plot_kwargs)

        # Sort out the supporting information
        self._update_legend_data(ax)
        self._clean_axis(ax)


@Pipeable
@mpl_style_decorator
def Plot(data, kind='line', x=None, y=None, row=None, col=None, hue=None, **kwargs):

    function_map = {
        'scatter': Scatter,
        'line': Line,
        'hist': Hist,
        'bar': Bar,
        'barh': Barh,
        'box': Boxplot,
    }
    plot_function = function_map[kind]

    # Deal with extra logic.
    if (row is not None) or (col is not None) or (hue is not None):
        g = DatoFacetGrid(data, row=row, col=col, hue=hue, **kwargs)
        g = g.map(plot_function, x, y, **kwargs)
    else:
        if (x is not None):
            g = data >> plot_function(x=x, y=y, **kwargs)
        else:
            g = data >> plot_function(**kwargs)
    return g


def allow_multiple_plot_methods(func):
    def wrapper(data, *args, **kwargs):
        # Check data type.
        # If series, plot is automatic.
        if type(data) == pd.Series:
            return func(data, *args, **kwargs)
        # If x or y are specified, then assume dataframe.
        elif 'x' in kwargs:
            x = data[kwargs.pop('x')]
            if 'y' in kwargs:
                y = data[kwargs.pop('y')]
            else:
                y = None

            if y is not None:
                return func(x, y, *args, **kwargs)
            else:
                return func(x, *args, **kwargs)
        elif type(data) in (tuple, list):
            return func(*data, *args, **kwargs)
        else:
            return func(data, *args, **kwargs)
    return wrapper


@Pipeable
@mpl_style_decorator
@allow_multiple_plot_methods
def Line(*args, **kwargs):
    return plt.plot(*args, **kwargs)


@Pipeable
@mpl_style_decorator
@allow_multiple_plot_methods
def Scatter(*args, **kwargs):
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.5
    return plt.scatter(*args, **kwargs)


@Pipeable
@mpl_style_decorator
def Bar(*args, **kwargs):
    return plt.bar(*args, **kwargs)


@Pipeable
@mpl_style_decorator
def Barh(*args, **kwargs):
    return plt.bar(*args, **kwargs)


@Pipeable
@mpl_style_decorator
def Boxplot(df, *args, **kwargs):
    return df.boxplot(*args, **kwargs)


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



