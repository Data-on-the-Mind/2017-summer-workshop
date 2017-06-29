"""Computationally reproducible experiments."""

import dallinger

experiment = dallinger.experiments.Griduniverse()

data = experiment.collect(
    app_id=u"3b9c2aeb-0eb7-4432-803e-bc437e17b3bb",
)

print(data.networks.df)
