import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.stats import powerlaw, uniform, norm

FILEPATH = os.path.dirname(__file__)

def user_data(N, random_state=None):
    """Generate some user-level state data by randomly sampling from a csv containing city information.
    """
    # We randomly select cities from https://simplemaps.com/data/us-zips.
    loc_data = pd.read_csv(os.path.join(FILEPATH, 'uszips.csv'))

    locations = loc_data.sample(N, weights=loc_data.population, replace=True, random_state=random_state) \
        .reset_index()
    users = locations.rename({'index': 'id_user'}, axis=1)
    return users

def purchase_data(N):
    start = pd.to_datetime('2019-10-01')
    end = pd.to_datetime('2019-10-31')
    start_u = start.value//10**9
    end_u = end.value//10**9

    dates = pd.Series(pd.to_datetime(np.random.randint(start_u, end_u, N), unit='s'))

    # Generate user ids associated with these dates.
    event_ids = np.round(uniform.rvs(size=N)*N)

    # Purchase revenue for these events, following a fat tail distribution.
    revenue = 1/powerlaw.rvs(2.5, size=N)

    purchases = pd.DataFrame({
        'id_user': event_ids,
        'date': dates.dt.strftime('%Y-%m-%d'),
        'sale_value': revenue,
    })

    purchases['sale_value'] += dates.dt.dayofweek/35
    return purchases
