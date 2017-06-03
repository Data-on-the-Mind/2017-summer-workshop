# Using Jupyter notebooks for interactive analyses and reproducible science

The Jupyter notebook is a widely used tool for performing reproducible,
interactive data analysis. As a "digital lab notebook", Jupyter weaves together
code, prose, images, and more, allowing users to iterate on analyses and view
the results all within a single document. This tutorial will give a hands-on
overview of some of the notebook's capabilities using Python, including how the
notebook integrates with Python packages such as matplotlib, pandas, and
statsmodels. Additionally, this tutorial will cover more advanced uses,
including "widgets" for interactively exploring data, conversions to other
formats such as HTML, using the notebook with R, and reproducibility.

## Learning Objectives

After completing this tutorial, you should come away with:

* A working knowledge of how to use the Jupyter notebook
* An u

## Setup

This tutorial requires Python 3 and R to be installed, along with the Python
packages listed in the `requirements.txt` file, which you can install with:

```
pip install -r requirements.txt
```

You will also need to enable the IPython widgets extension with:

```
jupyter nbextension enable --py --sys-prefix widgetsnbextension
```
