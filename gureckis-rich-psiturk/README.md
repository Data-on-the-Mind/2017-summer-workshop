# psiTurk

by Todd Gureckis and Alex Rich

To be ready for the workshop please create a Amazon account (AWS) and an account on psiturk.org:

1. Up to date instructions for AWS: http://psiturk.readthedocs.io/en/latest/psiturk_org_setup.html
2. Up to date instructions for psiturk: http://psiturk.readthedocs.io/en/latest/psiturk_org_setup.html

## Accessing the workshop materials

### slides
The workshop slides are made using [remarkjs](https://remarkjs.com/) and are contained in this folder. To view them, navigate to the folder in a terminal and type `python -m SimpleHTTPServer 8000`. Then open a browser and enter `http://localhost:8000/index.html` in the address bar.

### psiTurk + jsPsych stroop example
The example experiment can be downloaded from the [psiTurk experiment exchange](http://psiturk.org/ee/) by typing the command `psiturk-install Vn8uJAA2RGCSJp6pAoFgTH` in a terminal. The `experiment_complete` folder contains the complete experiment. The `experiment_skeleton` folder contains the minimal functioning experiment. Navigate to `experiment_skeleton/static/js/` to find six javascript files that build the experiment up step by step, with comments.

## psiTurk documentation

In this workshop, we'll walk through the basics of creating and running an
online experiment using psiTurk. Complete documentation of psiTurk's functionality can be found [here](http://psiturk.readthedocs.io/en/latest/)

## psiTurk experiment exchange

One of the goals of psiTurk is to make behavioral experiments easily portable
and replicable. To facilitate this, the
psiTurk [Experiment Exchange](http://psiturk.org/ee/) allows researchers to
upload psiTurk-compatible experiments that can easily be downloaded and
replicated by other experimenters. In this workshop, we'll download and run a
simple experiment from the exchange.

## jsPsych

jsPsych is a javascript library that simplifies the process of creating
behavioral experiments in the browser. It provides plugins for a variety of
standard trial types (instructions, forced choice, likert scales, etc.), as well
as functions for trial sequencing and randomization. jsPsych is not required to
create high quality javascript experiments with psiTurk, we'll walk through a
simple example using the framework.

* [documentation for jsPsych](http://docs.jspsych.org/)
* [jsPsych on github](https://github.com/jspsych/jsPsych)

## Other useful libraries

A variety of javascript libraries can come in handy when creating interactive experiments. Here are a few:

* [jQuery](https://jquery.com/)
* [underscore](http://underscorejs.org/)
* [D3](https://d3js.org/)
* [Raphael](http://dmitrybaranovskiy.github.io/raphael/)
