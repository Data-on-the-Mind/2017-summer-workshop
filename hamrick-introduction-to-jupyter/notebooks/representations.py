import numpy as np
import pandas as pd
from sklearn import manifold
import matplotlib.pyplot as plt


def mds(similarities):
    """Computes nonmetric multidimensional scaling on the given
    distances, projecting the data into a 2D space.

    Parameters
    ----------
    distances : dataframe of shape (n, n)
        The distances between points (i.e., with zeros along the diagonal)

    Returns
    -------
    dataframe of shape (n, 2)

    """
    # parameters that are used by both of the MDS runs
    params = {
        'random_state': 23497,
        'eps': 1e-6,
        'max_iter': 500,
        'dissimilarity': "precomputed",
        'n_jobs': 1,
        'n_components': 2
    }

    # first fit the metric MDS, which we will use as initialization
    # for the nonmetric MDS algorithm
    mds = manifold.MDS(metric=True, n_init=1, **params)
    pos = mds.fit(1 - similarities).embedding_

    # now run the nonmetric MDS algorithm
    nmds = manifold.MDS(metric=False, n_init=1, **params)
    pos = nmds.fit_transform(1 - similarities, init=pos)
    
    df = pd.DataFrame(pos, index=similarities.index.copy(), columns=["x", "y"])
    df.index.name = "label"
    return df.reset_index()
