"""
Static plotting functions (e.g. matplotlib, seaborn).

"""
import functools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import FacetGrid

from pipey import Pipeable
from ..style import mpl_style_decorator, datolegend

line_kwargs = {
    'marker': 'o',
    'markersize': 3,
    'linewidth': 1,
    'linestyle': '-',
}


class DatoFacetGrid(FacetGrid):
    def _facet_plot(self, func, ax, plot_args, plot_kwargs):
        # Draw the plot
        func(*plot_args, **plot_kwargs)

        # Sort out the supporting information
        self._update_legend_data(ax)
        self._clean_axis(ax)


@Pipeable
@mpl_style_decorator
def Plot(data, x=None, y=None, *args, kind='line', row=None, col=None, hue=None, legend_out=True, **kwargs):

    # Parse flexible inputs.
    if type(data) == tuple:
        data = pd.DataFrame(data).T
        x = data.columns[0]
        y = data.columns[1]

    function_map = {
        'scatter': _scatter,
        'line': _line,
        'hist': _hist,
        'bar': _bar,
        'barh': _barh,
        'box': _boxplot,
    }
    plot_function = function_map[kind]

    # Deal with extra logic.
    if (row is not None) or (col is not None) or (hue is not None):
        g = DatoFacetGrid(data, row=row, col=col, hue=hue, legend_out=legend_out)
        if y is not None:
            g = g.map(plot_function, x, y, *args, **kwargs).add_legend()
        else:
            g = g.map(plot_function, x, *args, **kwargs).add_legend()
    else:
        if x is not None:
            if y is not None:
                g = plot_function(data[x], data[y], *args, **kwargs)
            else:
                g = plot_function(data[x], *args, **kwargs)
        else:
            g = plot_function(data, *args, **kwargs)
        datolegend(legend_out=legend_out)
    return g



def _scatter(x, y=None, *args, **kwargs):
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.5
    plt.scatter(x, y, *args, **kwargs)


def _hist(x, *args, **kwargs):
    return plt.hist(x, *args, **kwargs)


def _line(x, y=None, *args, **kwargs):
    if y is not None:
        return plt.plot(x, y, *args, **kwargs)
    else:
        return x.plot(*args, kind='line', **kwargs)


def _bar(x, height=None, *args, **kwargs):
    if height is not None:
        return plt.bar(x, height, *args, **kwargs)
    else:
        return x.plot(*args, kind='bar', **kwargs)


def _barh(y, width=None, *args, **kwargs):
    if width is not None:
        return plt.barh(x, width, *args, **kwargs)
    else:
        return y.plot(*args, kind='barh', **kwargs)


def _boxplot(x, *args, **kwargs):
    return x.plot(*args, kind='box', **kwargs)


@Pipeable
def Scatter(data, x=None, y=None, *args, **kwargs):
    return data >> Plot(x=x, y=y, kind='scatter', *args, **kwargs)


@Pipeable
def Hist(data, x=None, *args, **kwargs):
    return data >> Plot(x=x, kind='hist', *args, **kwargs)


@Pipeable
def Bar(data, x=None, height=None, *args, **kwargs):
    return data >> Plot(x=x, y=height, kind='bar', *args, **kwargs)


@Pipeable
def Barh(data, y=None, width=None, *args, **kwargs):
    return data >> Plot(x=y, y=width, kind='barh', *args, **kwargs)


@Pipeable
def Box(data, x=None, *args, **kwargs):
    return data >> Plot(x=x, kind='box', *args, **kwargs)
