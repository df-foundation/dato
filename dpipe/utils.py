from dateutil.parser import parse
import inspect
import matplotlib as mpl
import numpy as np

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def series_is_date(series):
    """
    Check if the column has date-like strings, by checking dates for the most common values.

    :param series: pd.Series with the values to be evaluated.
    """
    date_checks = []
    for val in series.value_counts().head().index:
        date_check = is_date(val)
        date_checks.append(date_check)
    if all(date_checks):
        series_is_date = True
    else:
        series_is_date = False

    return series_is_date

