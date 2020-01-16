from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings


rc = {
    'style': 'dato_light',
}


FONT_DICT = {'family': 'Helvetica',
            'size': 8}


STYLES = {
    'default': {},
    'dato_dark': {
        'axes.edgecolor': '#4A5151',
        'axes.labelcolor': '#9CA7A8',
        'bg': '#222626',
        'font': FONT_DICT,
        'cycler': ["#FFC045", '#E01A4F', "#0A91AB", "#EB8258", "#995D81", "#F9F7F3", "#B5E2FA", "#EDDEA4", ],
        'grid.color': '#383B3F',
        'legend.textcolor': 'white',
        'plotbg': '#222626',
        'tick.color': '#9CA7A8',
        'text.color': 'white',
    },
    'dato_light': {
        'axes.edgecolor': 'black',
        'axes.labelcolor': 'black',
        'cycler': ["#463b75", "#e01a4f", "#6c969d", "#0c090d", "#A7D49B",],
        'bg': (1, 1, 1, 0),
        'font': FONT_DICT,
        'grid.color': '#F5F4F8',
        'legend.textcolor': 'black',
        'plotbg': 'white',
        'tick.color': 'black',
        'text.color': 'black',
    },
}


def _check_list_empty(list_obj):
    try:
        return all(map(_check_list_empty, list_obj))
    except:
        return False


def use(style_name=None, dato_only=False):
    if style_name is None:
        style = STYLES[rc['style']]
    else:
        # Set global style.
        rc['style'] = style_name

        style = STYLES[style_name]

    if not dato_only and rc['style'] != 'default':
        color_cycler = style['cycler']

        mpl.rc('axes', prop_cycle=(cycler('color', color_cycler)))

        mpl.rcParams['figure.facecolor'] = style['bg']
        mpl.rcParams['axes.facecolor'] = style['plotbg']
        mpl.rcParams['xtick.color'] = style['tick.color']
        mpl.rcParams['ytick.color'] = style['tick.color']
        mpl.rcParams['axes.labelcolor'] = style['axes.labelcolor']
        mpl.rcParams['axes.edgecolor'] = style['axes.edgecolor']
        mpl.rcParams['text.color'] = style['text.color']

        mpl.rcParams['figure.figsize'] = [4.86, 3]
        mpl.rcParams['figure.dpi'] = 130
        mpl.rcParams['axes.axisbelow'] = True
        mpl.rc('font', **style['font'])

        mpl.rcParams['axes.grid'] = True
        mpl.rcParams['grid.color'] = style['grid.color']
        mpl.rcParams['grid.linestyle'] = ':'


def datolegend(legend_out=True, **kwargs):
    if rc['style'] != 'default':
        style = STYLES[rc['style']]

        legend_dict = {
            'prop': style['font'],
            'frameon': False,
            'framealpha': 0,
        }
        if legend_out:
            legend_dict.update({
                'loc': 'center left',
                'bbox_to_anchor': (1, 0.5),
            })
        legend_dict.update(kwargs)

        handles = plt.gca().get_legend_handles_labels()
        if not _check_list_empty(handles):
            leg = plt.legend(**legend_dict)
            for h, t in zip(leg.legendHandles, leg.get_texts()):
                t.set_color(style['legend.textcolor'])


def mpl_style_decorator(func):
    def wrapper(*args, **kwargs):
        # Temporarility suppress warnings.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            # Save current styling.
            original_mpl_params = dict(mpl.rcParams)

            # Use custom styling.
            if rc['style'] != 'default':
                use(rc['style'])

            func_return_value = func(*args, **kwargs)

            # Handle legends.
            # datolegend()

            # Deal with datetimes.
            fig = plt.gcf()
            fig.autofmt_xdate()

            # Set bounds on plot to tight.
            # ax = plt.gca()
            # ax.autoscale(enable=True, axis='x', tight=True)

            # Set style back to original style.
            mpl.rcParams.update(original_mpl_params)

        return func_return_value
    return wrapper

