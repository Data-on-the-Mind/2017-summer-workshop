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

Additionally, part of the tutorial covers converting the notebook to other
formats. This requries `pandoc` to be installed:
http://pandoc.org/installing.html

## Outline

This tutorial will be broken down into two sections: *basics* and *advanced
usage*. In the basics section of the tutorial, we will cover the following
topics:

1. **Introduction to the Jupyter Notebook** -- in this notebook, we will go
   through basic usage of the notebook (editing and executing cells, restarting
   the kernel, adding new cells, etc.)
2. **Markdown and LaTeX Cheatsheet** -- this notebook introduces the basis of
   using Markdown (a language for formatting text) and LaTeX equations (a
   language for rendering mathematical equations). While we won't go through the
   whole notebook in detail during the workshop, it is provided as a reference
   for you afterwards and to encourage you to document your notebooks with rich
   text and math.
3. **Manipulating and Plotting Data in the Notebook** -- in this notebook, I
   will give a very brief introduction to Pandas and Matplotlib, and demonstrate
   how to create simple plots in the notebook.
4. **Using Matplotlib Interactively** -- this notebook is really more of an
   extension of the previous notebook, and introduces an alternate way of
   creating plots in the notebook. In the interactive mode, plots can be
   modified on the fly and interactively inspected.

In the advanced section of the tutorial we will cover:
