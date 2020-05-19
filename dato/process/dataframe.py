"""
pandas.DataFrame processing functions.
"""
import pandas as pd

from pipey import Pipeable, unpack_input, append_docstring
from .base import _make_pipeable_pandas


@Pipeable
def TopBy(data, column=None, N=10):
    if column is None:
        return data[data.isin(data.value_counts().head(N).index)]
    else:
        return data[data[column].isin(data[column].value_counts().head(N).index)]


@Pipeable
@append_docstring(pd.DataFrame.drop)
def Drop(df, *args, axis=1, **kwargs):
    """
    Implements `pd.DataFrame.drop()`, changing the default behavior to drop columns, not rows.

    :param *args:
        Any args accepted by `pd.DataFrame.drop`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.drop()`.

    """
    return df.drop(*args, axis=axis, **kwargs)


@Pipeable
@append_docstring(pd.DataFrame.fillna)
def FillNA(df, value=None, columns=None, **kwargs):
    """
    Implements `pd.DataFrame.fillna()`. If a scalar value is passed it is used to fill all missing values. Alternatively, an array-like 'value' can be given. It's expected that the array-like have the same length as 'self'.

    :param value: the value used to fill
    :type value: scalar, array-like
    :param columns: columns to apply fillna to
    :type columns: array-like
    :param **kwargs:
        Anything accepted by the `pd.DataFrame.fillna()` method.

    """
    df1 = df.copy()
    if columns is not None:
        for column in columns:
            df1[column] = df1[column].fillna(value=value, **kwargs)
    else:
        df1 = df1.fillna(value=value, **kwargs)
    return df1


@Pipeable
@append_docstring(pd.DataFrame.rename)
def Rename(df, *args, axis=1, **kwargs):
    """
    Implements `pd.DataFrame.rename()`, changing the default behavior to drop columns, not rows.

    """
    return df.drop(*args, axis=axis, **kwargs)


@Pipeable
def Select(df, *args):
    """
    Selects columns specified by args.

    :param *args: Column name.
    :type *args: tuple of strings.

    """
    if len(args) == 1:
        return df[args[0]]
    else:
        return df[list(args)]


T = _make_pipeable_pandas('T', parent_class=pd.DataFrame, is_property=True)
Abs = _make_pipeable_pandas('abs', parent_class=pd.DataFrame)
Add = _make_pipeable_pandas('add', parent_class=pd.DataFrame)
AddPrefix = _make_pipeable_pandas('add_prefix', parent_class=pd.DataFrame)
AddSuffix = _make_pipeable_pandas('add_suffix', parent_class=pd.DataFrame)
Agg = _make_pipeable_pandas('agg', parent_class=pd.DataFrame)
Aggregate = _make_pipeable_pandas('aggregate', parent_class=pd.DataFrame)
Align = _make_pipeable_pandas('align', parent_class=pd.DataFrame)
All = _make_pipeable_pandas('all', parent_class=pd.DataFrame)
Any = _make_pipeable_pandas('any', parent_class=pd.DataFrame)
Append = _make_pipeable_pandas('append', parent_class=pd.DataFrame)
Apply = _make_pipeable_pandas('apply', parent_class=pd.DataFrame)
Applymap = _make_pipeable_pandas('applymap', parent_class=pd.DataFrame)
Asfreq = _make_pipeable_pandas('asfreq', parent_class=pd.DataFrame)
Asof = _make_pipeable_pandas('asof', parent_class=pd.DataFrame)
Assign = _make_pipeable_pandas('assign', parent_class=pd.DataFrame)
Astype = _make_pipeable_pandas('astype', parent_class=pd.DataFrame)
At = _make_pipeable_pandas('at', parent_class=pd.DataFrame, is_property=True)
AtTime = _make_pipeable_pandas('at_time', parent_class=pd.DataFrame)
Axes = _make_pipeable_pandas('axes', parent_class=pd.DataFrame, is_property=True)
BetweenTime = _make_pipeable_pandas('between_time', parent_class=pd.DataFrame)
Bfill = _make_pipeable_pandas('bfill', parent_class=pd.DataFrame)
Bool = _make_pipeable_pandas('bool', parent_class=pd.DataFrame)
# Boxplot = _make_pipeable_pandas('boxplot', parent_class=pd.DataFrame)
Clip = _make_pipeable_pandas('clip', parent_class=pd.DataFrame)
Columns = _make_pipeable_pandas('columns', parent_class=pd.DataFrame, is_property=True)
Combine = _make_pipeable_pandas('combine', parent_class=pd.DataFrame)
CombineFirst = _make_pipeable_pandas('combine_first', parent_class=pd.DataFrame)
Copy = _make_pipeable_pandas('copy', parent_class=pd.DataFrame)
Corr = _make_pipeable_pandas('corr', parent_class=pd.DataFrame)
Corrwith = _make_pipeable_pandas('corrwith', parent_class=pd.DataFrame)
Count = _make_pipeable_pandas('count', parent_class=pd.DataFrame)
Cov = _make_pipeable_pandas('cov', parent_class=pd.DataFrame)
Cummax = _make_pipeable_pandas('cummax', parent_class=pd.DataFrame)
Cummin = _make_pipeable_pandas('cummin', parent_class=pd.DataFrame)
Cumprod = _make_pipeable_pandas('cumprod', parent_class=pd.DataFrame)
Cumsum = _make_pipeable_pandas('cumsum', parent_class=pd.DataFrame)
Describe = _make_pipeable_pandas('describe', parent_class=pd.DataFrame)
Diff = _make_pipeable_pandas('diff', parent_class=pd.DataFrame)
Div = _make_pipeable_pandas('div', parent_class=pd.DataFrame)
Divide = _make_pipeable_pandas('divide', parent_class=pd.DataFrame)
Dot = _make_pipeable_pandas('dot', parent_class=pd.DataFrame)
# Drop = _make_pipeable_pandas('drop', parent_class=pd.DataFrame)
DropDuplicates = _make_pipeable_pandas('drop_duplicates', parent_class=pd.DataFrame)
DropLevel = _make_pipeable_pandas('droplevel', parent_class=pd.DataFrame)
DropNA = _make_pipeable_pandas('dropna', parent_class=pd.DataFrame)
Dtypes = _make_pipeable_pandas('dtypes', parent_class=pd.DataFrame, is_property=True)
Duplicated = _make_pipeable_pandas('duplicated', parent_class=pd.DataFrame)
Empty = _make_pipeable_pandas('empty', parent_class=pd.DataFrame, is_property=True)
Eq = _make_pipeable_pandas('eq', parent_class=pd.DataFrame)
Equals = _make_pipeable_pandas('equals', parent_class=pd.DataFrame)
Eval = _make_pipeable_pandas('eval', parent_class=pd.DataFrame)
Ewm = _make_pipeable_pandas('ewm', parent_class=pd.DataFrame)
Expanding = _make_pipeable_pandas('expanding', parent_class=pd.DataFrame)
Explode = _make_pipeable_pandas('explode', parent_class=pd.DataFrame)
Ffill = _make_pipeable_pandas('ffill', parent_class=pd.DataFrame)
#Fillna = _make_pipeable_pandas('fillna', parent_class=pd.DataFrame)
Filter = _make_pipeable_pandas('filter', parent_class=pd.DataFrame)
First = _make_pipeable_pandas('first', parent_class=pd.DataFrame)
FirstValidIndex = _make_pipeable_pandas('first_valid_index', parent_class=pd.DataFrame)
Floordiv = _make_pipeable_pandas('floordiv', parent_class=pd.DataFrame)
FromDict = _make_pipeable_pandas('from_dict', parent_class=pd.DataFrame)
FromRecords = _make_pipeable_pandas('from_records', parent_class=pd.DataFrame)
Ge = _make_pipeable_pandas('ge', parent_class=pd.DataFrame)
Get = _make_pipeable_pandas('get', parent_class=pd.DataFrame)
GroupBy = _make_pipeable_pandas('groupby', parent_class=pd.DataFrame)
Gt = _make_pipeable_pandas('gt', parent_class=pd.DataFrame)
Head = _make_pipeable_pandas('head', parent_class=pd.DataFrame)
# Hist = _make_pipeable_pandas('hist', parent_class=pd.DataFrame)
Iat = _make_pipeable_pandas('iat', parent_class=pd.DataFrame, is_property=True)
Idxmax = _make_pipeable_pandas('idxmax', parent_class=pd.DataFrame)
Idxmin = _make_pipeable_pandas('idxmin', parent_class=pd.DataFrame)
Iloc = _make_pipeable_pandas('iloc', parent_class=pd.DataFrame, is_property=True)
Index = _make_pipeable_pandas('index', parent_class=pd.DataFrame, is_property=True)
Infer_objects = _make_pipeable_pandas('infer_objects', parent_class=pd.DataFrame)
Info = _make_pipeable_pandas('info', parent_class=pd.DataFrame)
Insert = _make_pipeable_pandas('insert', parent_class=pd.DataFrame)
Interpolate = _make_pipeable_pandas('interpolate', parent_class=pd.DataFrame)
Isin = _make_pipeable_pandas('isin', parent_class=pd.DataFrame)
Isna = _make_pipeable_pandas('isna', parent_class=pd.DataFrame)
Isnull = _make_pipeable_pandas('isnull', parent_class=pd.DataFrame)
Items = _make_pipeable_pandas('items', parent_class=pd.DataFrame)
Iteritems = _make_pipeable_pandas('iteritems', parent_class=pd.DataFrame)
Iterrows = _make_pipeable_pandas('iterrows', parent_class=pd.DataFrame)
Itertuples = _make_pipeable_pandas('itertuples', parent_class=pd.DataFrame)
Join = _make_pipeable_pandas('join', parent_class=pd.DataFrame)
Keys = _make_pipeable_pandas('keys', parent_class=pd.DataFrame)
Kurt = _make_pipeable_pandas('kurt', parent_class=pd.DataFrame)
Kurtosis = _make_pipeable_pandas('kurtosis', parent_class=pd.DataFrame)
Last = _make_pipeable_pandas('last', parent_class=pd.DataFrame)
LastValidIndex = _make_pipeable_pandas('last_valid_index', parent_class=pd.DataFrame)
Le = _make_pipeable_pandas('le', parent_class=pd.DataFrame)
Loc = _make_pipeable_pandas('loc', parent_class=pd.DataFrame, is_property=True)
Lookup = _make_pipeable_pandas('lookup', parent_class=pd.DataFrame)
Lt = _make_pipeable_pandas('lt', parent_class=pd.DataFrame)
Mad = _make_pipeable_pandas('mad', parent_class=pd.DataFrame)
Mask = _make_pipeable_pandas('mask', parent_class=pd.DataFrame)
Max = _make_pipeable_pandas('max', parent_class=pd.DataFrame)
Mean = _make_pipeable_pandas('mean', parent_class=pd.DataFrame)
Median = _make_pipeable_pandas('median', parent_class=pd.DataFrame)
Melt = _make_pipeable_pandas('melt', parent_class=pd.DataFrame)
Memory_usage = _make_pipeable_pandas('memory_usage', parent_class=pd.DataFrame)
# Merge = _make_pipeable_pandas('merge', parent_class=pd.DataFrame)
Min = _make_pipeable_pandas('min', parent_class=pd.DataFrame)
Mod = _make_pipeable_pandas('mod', parent_class=pd.DataFrame)
Mode = _make_pipeable_pandas('mode', parent_class=pd.DataFrame)
Mul = _make_pipeable_pandas('mul', parent_class=pd.DataFrame)
Mutate = _make_pipeable_pandas('eval', parent_class=pd.DataFrame)
Multiply = _make_pipeable_pandas('multiply', parent_class=pd.DataFrame)
Ndim = _make_pipeable_pandas('ndim', parent_class=pd.DataFrame, is_property=True)
Ne = _make_pipeable_pandas('ne', parent_class=pd.DataFrame)
Nlargest = _make_pipeable_pandas('nlargest', parent_class=pd.DataFrame)
Notna = _make_pipeable_pandas('notna', parent_class=pd.DataFrame)
Notnull = _make_pipeable_pandas('notnull', parent_class=pd.DataFrame)
Nsmallest = _make_pipeable_pandas('nsmallest', parent_class=pd.DataFrame)
Nunique = _make_pipeable_pandas('nunique', parent_class=pd.DataFrame)
PctChange = _make_pipeable_pandas('pct_change', parent_class=pd.DataFrame)
Pipe = _make_pipeable_pandas('pipe', parent_class=pd.DataFrame)
Pivot = _make_pipeable_pandas('pivot', parent_class=pd.DataFrame)
PivotTable = _make_pipeable_pandas('pivot_table', parent_class=pd.DataFrame)
Pop = _make_pipeable_pandas('pop', parent_class=pd.DataFrame)
Pow = _make_pipeable_pandas('pow', parent_class=pd.DataFrame)
Prod = _make_pipeable_pandas('prod', parent_class=pd.DataFrame)
Product = _make_pipeable_pandas('product', parent_class=pd.DataFrame)
Quantile = _make_pipeable_pandas('quantile', parent_class=pd.DataFrame)
Query = _make_pipeable_pandas('query', parent_class=pd.DataFrame)
Radd = _make_pipeable_pandas('radd', parent_class=pd.DataFrame)
Rank = _make_pipeable_pandas('rank', parent_class=pd.DataFrame)
Rdiv = _make_pipeable_pandas('rdiv', parent_class=pd.DataFrame)
Reindex = _make_pipeable_pandas('reindex', parent_class=pd.DataFrame)
ReindexLike = _make_pipeable_pandas('reindex_like', parent_class=pd.DataFrame)
Rename = _make_pipeable_pandas('rename', parent_class=pd.DataFrame)
RenameAxis = _make_pipeable_pandas('rename_axis', parent_class=pd.DataFrame)
ReorderLevels = _make_pipeable_pandas('reorder_levels', parent_class=pd.DataFrame)
Replace = _make_pipeable_pandas('replace', parent_class=pd.DataFrame)
Resample = _make_pipeable_pandas('resample', parent_class=pd.DataFrame)
ResetIndex = _make_pipeable_pandas('reset_index', parent_class=pd.DataFrame)
Rfloordiv = _make_pipeable_pandas('rfloordiv', parent_class=pd.DataFrame)
Rmod = _make_pipeable_pandas('rmod', parent_class=pd.DataFrame)
Rmul = _make_pipeable_pandas('rmul', parent_class=pd.DataFrame)
Rolling = _make_pipeable_pandas('rolling', parent_class=pd.DataFrame)
Round = _make_pipeable_pandas('round', parent_class=pd.DataFrame)
Rpow = _make_pipeable_pandas('rpow', parent_class=pd.DataFrame)
Rsub = _make_pipeable_pandas('rsub', parent_class=pd.DataFrame)
Rtruediv = _make_pipeable_pandas('rtruediv', parent_class=pd.DataFrame)
Sample = _make_pipeable_pandas('sample', parent_class=pd.DataFrame)
Select_dtypes = _make_pipeable_pandas('select_dtypes', parent_class=pd.DataFrame)
Sem = _make_pipeable_pandas('sem', parent_class=pd.DataFrame)
SetAxis = _make_pipeable_pandas('set_axis', parent_class=pd.DataFrame)
SetIndex = _make_pipeable_pandas('set_index', parent_class=pd.DataFrame)
Shape = _make_pipeable_pandas('shape', parent_class=pd.DataFrame)
Shift = _make_pipeable_pandas('shift', parent_class=pd.DataFrame)
Size = _make_pipeable_pandas('size', parent_class=pd.DataFrame)
Skew = _make_pipeable_pandas('skew', parent_class=pd.DataFrame)
Slice_shift = _make_pipeable_pandas('slice_shift', parent_class=pd.DataFrame)
SortIndex = _make_pipeable_pandas('sort_index', parent_class=pd.DataFrame)
SortValues = _make_pipeable_pandas('sort_values', parent_class=pd.DataFrame)
Sparse = _make_pipeable_pandas('sparse', parent_class=pd.DataFrame)
Squeeze = _make_pipeable_pandas('squeeze', parent_class=pd.DataFrame)
Stack = _make_pipeable_pandas('stack', parent_class=pd.DataFrame)
Std = _make_pipeable_pandas('std', parent_class=pd.DataFrame)
Sub = _make_pipeable_pandas('sub', parent_class=pd.DataFrame)
Subtract = _make_pipeable_pandas('subtract', parent_class=pd.DataFrame)
Sum = _make_pipeable_pandas('sum', parent_class=pd.DataFrame)
Swapaxes = _make_pipeable_pandas('swapaxes', parent_class=pd.DataFrame)
Swaplevel = _make_pipeable_pandas('swaplevel', parent_class=pd.DataFrame)
Tail = _make_pipeable_pandas('tail', parent_class=pd.DataFrame)
Take = _make_pipeable_pandas('take', parent_class=pd.DataFrame)
ToClipboard = _make_pipeable_pandas('to_clipboard', parent_class=pd.DataFrame)
ToCsv = _make_pipeable_pandas('to_csv', parent_class=pd.DataFrame)
ToDict = _make_pipeable_pandas('to_dict', parent_class=pd.DataFrame)
ToExcel = _make_pipeable_pandas('to_excel', parent_class=pd.DataFrame)
ToFeather = _make_pipeable_pandas('to_feather', parent_class=pd.DataFrame)
ToGbq = _make_pipeable_pandas('to_gbq', parent_class=pd.DataFrame)
ToHdf = _make_pipeable_pandas('to_hdf', parent_class=pd.DataFrame)
ToHtml = _make_pipeable_pandas('to_html', parent_class=pd.DataFrame)
ToJson = _make_pipeable_pandas('to_json', parent_class=pd.DataFrame)
ToLatex = _make_pipeable_pandas('to_latex', parent_class=pd.DataFrame)
ToNumpy = _make_pipeable_pandas('to_numpy', parent_class=pd.DataFrame)
ToMarkdown = _make_pipeable_pandas('to_markdown', parent_class=pd.DataFrame)
ToParquet = _make_pipeable_pandas('to_parquet', parent_class=pd.DataFrame)
ToPeriod = _make_pipeable_pandas('to_period', parent_class=pd.DataFrame)
ToPickle = _make_pipeable_pandas('to_pickle', parent_class=pd.DataFrame)
ToRecords = _make_pipeable_pandas('to_records', parent_class=pd.DataFrame)
ToSql = _make_pipeable_pandas('to_sql', parent_class=pd.DataFrame)
ToStata = _make_pipeable_pandas('to_stata', parent_class=pd.DataFrame)
ToString = _make_pipeable_pandas('to_string', parent_class=pd.DataFrame)
ToTimestamp = _make_pipeable_pandas('to_timestamp', parent_class=pd.DataFrame)
Toxarray = _make_pipeable_pandas('to_xarray', parent_class=pd.DataFrame)
Transform = _make_pipeable_pandas('transform', parent_class=pd.DataFrame)
Transpose = _make_pipeable_pandas('transpose', parent_class=pd.DataFrame)
Truediv = _make_pipeable_pandas('truediv', parent_class=pd.DataFrame)
Truncate = _make_pipeable_pandas('truncate', parent_class=pd.DataFrame)
Tshift = _make_pipeable_pandas('tshift', parent_class=pd.DataFrame)
TzConvert = _make_pipeable_pandas('tz_convert', parent_class=pd.DataFrame)
TzLocalize = _make_pipeable_pandas('tz_localize', parent_class=pd.DataFrame)
Unstack = _make_pipeable_pandas('unstack', parent_class=pd.DataFrame)
Update = _make_pipeable_pandas('update', parent_class=pd.DataFrame)
Values = _make_pipeable_pandas('values', parent_class=pd.DataFrame)
Var = _make_pipeable_pandas('var', parent_class=pd.DataFrame)
Where = _make_pipeable_pandas('where', parent_class=pd.DataFrame)
Xs = _make_pipeable_pandas('xs', parent_class=pd.DataFrame)

