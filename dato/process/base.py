"""
Base pandas/dask functionality. `pd.FUNCTIONS`.
"""
import pandas as pd

from pipey import Pipeable, unpack_input, append_docstring


def _make_pipeable_pandas(func_name, parent_class=pd, is_property=False):

    # Check if a property.
    if isinstance(getattr(parent_class, func_name), property) or is_property:
        @Pipeable
        def pipeable_function(obj):
            return getattr(obj, func_name)

    else:
        if parent_class == pd:
            func = getattr(pd, func_name)

            @Pipeable
            @append_docstring(func)
            def pipeable_function(*args, **kwargs):
                """Makes a pipeable version of the following pandas method:"""
                return func(*args, **kwargs)

        elif parent_class == pd.DataFrame:
            @Pipeable
            @append_docstring(getattr(pd.DataFrame, func_name))
            def pipeable_function(df, *args, **kwargs):
                """Makes a pipeable version of the following pandas dataframe method:"""
                return getattr(df, func_name)(*args, **kwargs)

        elif parent_class == pd.core.groupby.generic.DataFrameGroupBy:
            @Pipeable
            @append_docstring(getattr(pd.core.groupby.generic.DataFrameGroupBy, func_name))
            def pipeable_function(gb, column=None, **kwargs):
                """Makes a pipeable version of the pandas dataframe method.

                :param column: columns over which to perform the aggregation
                :param type: string or array-like

                """
                if column is not None:
                    aggregation = getattr(gb, func_name)(**kwargs)[column]
                else:
                    aggregation = getattr(gb, func_name)(**kwargs)
                return aggregation


    return pipeable_function


@Pipeable
@append_docstring(pd.to_datetime)
def ToDatetime(df, *args, **kwargs):
    """
    Implements `pd.to_datetime()`.

    :param *args:
        Any args accepted by `pd.to_datetime()`.
    :param **kwargs:
        Any kwargs accepted by `pd.to_datetime()`.

    """
    if not args:
        df = pd.to_datetime(df)
    else:
        for column in args:
            df[column] = pd.to_datetime(df[column], **kwargs)
    return df


ReadCsv = _make_pipeable_pandas('read_csv')
Api = _make_pipeable_pandas('api')
Array = _make_pipeable_pandas('array')
Arrays = _make_pipeable_pandas('arrays')
BdateRange = _make_pipeable_pandas('bdate_range')
Compat = _make_pipeable_pandas('compat')
Concat = _make_pipeable_pandas('concat')
Crosstab = _make_pipeable_pandas('crosstab')
Cut = _make_pipeable_pandas('cut')
DateRange = _make_pipeable_pandas('date_range')
Errors = _make_pipeable_pandas('errors')
Eval = _make_pipeable_pandas('eval')
Factorize = _make_pipeable_pandas('factorize')
GetDummies = _make_pipeable_pandas('get_dummies')
InferFreq = _make_pipeable_pandas('infer_freq')
IntervalRange = _make_pipeable_pandas('interval_range')
Isna = _make_pipeable_pandas('isna')
Isnull = _make_pipeable_pandas('isnull')
Lreshape = _make_pipeable_pandas('lreshape')
Melt = _make_pipeable_pandas('melt')
Merge = unpack_input(_make_pipeable_pandas('merge'))
MergeAsof = unpack_input(_make_pipeable_pandas('merge_asof'))
MergeOrdered = unpack_input(_make_pipeable_pandas('merge_ordered'))
Notna = _make_pipeable_pandas('notna')
Notnull = _make_pipeable_pandas('notnull')
PeriodRange = _make_pipeable_pandas('period_range')
Pivot = _make_pipeable_pandas('pivot')
PivotTable = _make_pipeable_pandas('pivot_table')
Qcut = _make_pipeable_pandas('qcut')
ReadClipboard = _make_pipeable_pandas('read_clipboard')
ReadCsv = _make_pipeable_pandas('read_csv')
ReadExcel = _make_pipeable_pandas('read_excel')
ReadFeather = _make_pipeable_pandas('read_feather')
ReadFwf = _make_pipeable_pandas('read_fwf')
ReadGbq = _make_pipeable_pandas('read_gbq')
ReadHdf = _make_pipeable_pandas('read_hdf')
ReadHtml = _make_pipeable_pandas('read_html')
ReadJson = _make_pipeable_pandas('read_json')
ReadParquet = _make_pipeable_pandas('read_parquet')
ReadPickle = _make_pipeable_pandas('read_pickle')
ReadSas = _make_pipeable_pandas('read_sas')
ReadSpss = _make_pipeable_pandas('read_spss')
ReadSql = _make_pipeable_pandas('read_sql')
ReadSqlQuery = _make_pipeable_pandas('read_sql_query')
ReadSqlTable = _make_pipeable_pandas('read_sql_table')
ReadStata = _make_pipeable_pandas('read_stata')
ReadTable = _make_pipeable_pandas('read_table')
TimedeltaRange = _make_pipeable_pandas('timedelta_range')
# ToDatetime = _make_pipeable_pandas('to_datetime')
ToNumeric = _make_pipeable_pandas('to_numeric')
ToPickle = _make_pipeable_pandas('to_pickle')
ToTimedelta = _make_pipeable_pandas('to_timedelta')
Unique = _make_pipeable_pandas('unique')
ValueCounts = _make_pipeable_pandas('value_counts')
WideToLong = _make_pipeable_pandas('wide_to_long')

