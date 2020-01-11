from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings


rc = {
    'style': 'dato_light',
}


STYLES = {
    'dato_dark': {
        'cycler': ["#FFC045", '#E01A4F', "#0A91AB", "#EB8258", "#995D81", "#F9F7F3", "#B5E2FA", "#EDDEA4", ],
        'grid': '#383B3F',
        'ticks': '#9CA7A8',
        'labels': '#9CA7A8',
        'title': 'white',
        'bg': '#222626',
        'plotbg': '#222626',
        'edge': '#4A5151',
    },
    'dato_light': {
        'cycler': ["#463b75", "#e01a4f", "#6c969d", "#0c090d", "#A7D49B",],
        'grid': '#F5F4F8',
        'bg': (1, 1, 1, 0),
        'title': 'black',
        'plotbg': 'white',
        'ticks': 'black',
        'edge': 'black',
        'labels': 'black',
    },
}


def use(style_name=None, dato_only=False):
    if style_name is None:
        style = STYLES[rc['style']]
    else:
        # Set global style.
        rc['style'] = style_name

        style = STYLES[style_name]

    if not dato_only:
        grid_color = style['grid']

        color_cycler = style['cycler']

        mpl.rc('axes', prop_cycle=(cycler('color', color_cycler)))

        mpl.rcParams['figure.facecolor'] = style['bg']
        mpl.rcParams['axes.facecolor'] = style['plotbg']
        mpl.rcParams['xtick.color'] = style['ticks']
        mpl.rcParams['ytick.color'] = style['ticks']
        mpl.rcParams['axes.labelcolor'] = style['labels']
        mpl.rcParams['axes.edgecolor'] = style['edge']
        mpl.rcParams['text.color'] = style['title']

        mpl.rcParams['figure.figsize'] = [4.86, 3]
        mpl.rcParams['figure.dpi'] = 130
        mpl.rcParams['axes.axisbelow'] = True
        font = {'family' : 'Helvetica',
                'size'   : 8}
        mpl.rc('font', **font)

        mpl.rcParams['axes.grid'] = True
        mpl.rcParams['grid.color'] = grid_color
        mpl.rcParams['grid.linestyle'] = ':'


def mpl_style_decorator(func):
    def wrapper(*args, **kwargs):
        # Temporarility suppress warnings.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            # Save current styling.
            original_mpl_params = dict(mpl.rcParams)

            # Use custom styling.
            use(rc['style'])

            func_return_value = func(*args, **kwargs)

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

