# Python for Engineers: Case Studies from Calculator to Simulation

[![Check notebooks](https://github.com/ktwyw/python-for-engineers-case-studies/actions/workflows/check-notebooks.yml/badge.svg)](https://github.com/ktwyw/python-for-engineers-case-studies/actions/workflows/check-notebooks.yml)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/01_Python_as_an_Engineering_Calculator.ipynb)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Text and figures: CC BY 4.0](https://img.shields.io/badge/text%20%26%20figures-CC%20BY%204.0-lightgrey.svg)](DATA_LICENSE.md)

*Yanwei Wang*

A sequence of 23 Jupyter notebooks that teach Python through engineering problems. It starts with Python as a calculator for a water tank and ends with molecular-dynamics simulations and research-based flow models. Each notebook asks an engineering question, builds a program that answers it, and checks the answer against physics, a hand calculation or an exact result.

The notebooks are written for self-study by first-year engineering students. No programming experience is assumed at the start, and every line of code carries a comment.

## The learning path

The 17 **core** notebooks are meant to be read in order: each part uses what the parts before it taught. The **optional** notebooks add depth and can be read in any order once their prerequisites are done.

| # | Notebook | Python you learn | Engineering problem | Time* | Run |
|---|---|---|---|---|---|
| | **Part 1 · First programs** | | | | |
| 01 | [Python as an engineering calculator](notebooks/01_Python_as_an_Engineering_Calculator.ipynb) | arithmetic, variables, types, `math`, f-strings, round-off | pressure, volume and drain time of a tank | 30 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/01_Python_as_an_Engineering_Calculator.ipynb) |
| 02 | [Decisions, loops and functions](notebooks/02_Decisions_Loops_and_Functions.ipynb) | `if`, `for`, `while`, functions, `assert`, bisection | sizing a water pipe | 40 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/02_Decisions_Loops_and_Functions.ipynb) |
| | **Part 2 · Collections and data** | | | | |
| 03 | [From a data file to a result](notebooks/03_From_a_Data_File_to_a_Result.ipynb) | strings, lists, dictionaries, files, `csv` | cleaning a reactor temperature log | 45 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/03_From_a_Data_File_to_a_Result.ipynb) |
| 04 | [Statistics, algorithms and complexity](notebooks/04_Statistics_Algorithms_and_Complexity.ipynb) | sorting, searching, Big-O, recursion | summarising measurements | 75–90 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/04_Statistics_Algorithms_and_Complexity.ipynb) |
| 05 | [Transient heat conduction in a rod](notebooks/05_Transient_Heat_Conduction_in_a_Rod.ipynb) | **NumPy arrays** (introduced here), time stepping, stability | a rod warming up | 45 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/05_Transient_Heat_Conduction_in_a_Rod.ipynb) |
| 06 | [Drawing heart curves](notebooks/06_Drawing_Heart_Curves.ipynb) | array arithmetic, plotting with Matplotlib | curves for a plotter or laser cutter | 35 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/06_Drawing_Heart_Curves.ipynb) |
| 06b | [Heart curve gallery](notebooks/06b_Heart_Curve_Gallery_2D_3D_and_Animation.ipynb) *(optional)* | filled curves, 3D surfaces, animation | | 10 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/06b_Heart_Curve_Gallery_2D_3D_and_Animation.ipynb) |
| 07 | [Engineering design optimization](notebooks/07_Engineering_Design_Optimization.ipynb) | grid search, running best, constraints | the cheapest cylindrical tank | 35 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/07_Engineering_Design_Optimization.ipynb) |
| | **Part 3 · Getting it right** | | | | |
| 08 | [Find the bugs](notebooks/08_Find_the_Bugs.ipynb) | error messages, `assert`, tracing, unit tests, `raise` | a broken heat-conduction script | 45 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/08_Find_the_Bugs.ipynb) |
| 09 | [Reaction kinetics and parameter fitting](notebooks/09_Reaction_Kinetics_and_Parameter_Fitting.ipynb) | least squares, residuals, judging a fit | a rate constant from measurements | 40 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/09_Reaction_Kinetics_and_Parameter_Fitting.ipynb) |
| | **Part 4 · Objects** | | | | |
| 10 | [Classes for engineering components](notebooks/10_Classes_for_Engineering_Components.ipynb) | classes, methods, inheritance, composition | materials, stress–strain, a tie bar | 45 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/10_Classes_for_Engineering_Components.ipynb) |
| 11 | [Factory queues](notebooks/11_Factory_Queues_Discrete_Event_Simulation.ipynb) | dataclasses, heaps, event-driven simulation | when a waiting line keeps growing | 60 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/11_Factory_Queues_Discrete_Event_Simulation.ipynb) |
| | **Part 5 · Efficiency** | | | | |
| 12 | [Monte Carlo sampling and integration](notebooks/12_Monte_Carlo_Sampling_and_Integration.ipynb) | random numbers, sampling, error bars | integrals from random points | 55 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/12_Monte_Carlo_Sampling_and_Integration.ipynb) |
| 13 | [Molecular dynamics: introduction](notebooks/13_Molecular_Dynamics_Introduction.ipynb) | Newton's laws in code, reproducibility | 16 interacting particles | 35 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/13_Molecular_Dynamics_Introduction.ipynb) |
| 14 | [Molecular dynamics: efficient computing](notebooks/14_Molecular_Dynamics_Efficient_Computing.ipynb) | timing, profiling, vectorising, O(N²) | the same system, faster | 45–80 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/14_Molecular_Dynamics_Efficient_Computing.ipynb) |
| | **Part 6 · Engineering practice** | | | | |
| 15 | [The brachistochrone](notebooks/15_Brachistochrone_Fastest_Path.ipynb) | summing in loops, convergence, numerical evidence | the fastest track for a sliding bead | 55 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/15_Brachistochrone_Fastest_Path.ipynb) |
| 16 | [Hardy Cross pipe networks](notebooks/16_Hardy_Cross_Pipe_Networks.ipynb) | iteration to a tolerance, sign conventions | flows in a water network | 35 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/16_Hardy_Cross_Pipe_Networks.ipynb) |
| 17 | [Linear algebra for engineers](notebooks/17_Linear_Algebra_for_Engineers.ipynb) | vectors, matrices, `np.linalg` | forces and a temperature field | 55 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/17_Linear_Algebra_for_Engineers.ipynb) |
| | **Extensions** *(optional)* | | | | |
| 18 | [Statistics and complexity, extended](notebooks/18_Statistics_and_Complexity_Extended.ipynb) | more algorithms, numerical stability, a mini project | after 04 | 80 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/18_Statistics_and_Complexity_Extended.ipynb) |
| 19 | [Molecular dynamics in 3D](notebooks/19_Molecular_Dynamics_Advanced_3D.ipynb) | a longer simulation; pressure, structure | after 13 | 45 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/19_Molecular_Dynamics_Advanced_3D.ipynb) |
| 20 | [Polymer graphs and viscoelasticity](notebooks/20_Polymer_Graphs_and_Viscoelasticity.ipynb) | eigenvalues of graphs | after 17 | 45 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/20_Polymer_Graphs_and_Viscoelasticity.ipynb) |
| 21 | [Concrete pumping: a two-layer model](notebooks/21_Concrete_Pumping_Two_Layer_Model.ipynb) | a research-based flow model | after 05 | 50 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/21_Concrete_Pumping_Two_Layer_Model.ipynb) |
| 22 | [Polymer melt flow through a die](notebooks/22_Polymer_Melt_Pipe_Flow_Carreau_Yasuda.ipynb) | shear-thinning flow, root finding | after 21 | 55 min | [Colab](https://colab.research.google.com/github/ktwyw/python-for-engineers-case-studies/blob/main/notebooks/22_Polymer_Melt_Pipe_Flow_Carreau_Yasuda.ipynb) |

\*Time for the essential sections only. Allow about twice as long if you do the practice questions. The whole core path takes about 13 hours of reading, or about 25 hours with the practice.

The extensions use research-level science. You are **not** expected to follow every derivation: read them for the programming and the main result.

## How to run the notebooks

- **Google Colab (nothing to install):** click **Colab** next to a notebook in the table above, or the badge at the top of any notebook, then choose *Runtime → Run all*. To keep your changes, use *File → Save a copy in Drive*.
- **Your own computer:** install Python 3.10 or newer (for example with Anaconda). Then download this repository (*Code → Download ZIP*, or `git clone https://github.com/ktwyw/python-for-engineers-case-studies.git`), run `python -m pip install -r requirements.txt` once in its folder, open a notebook in JupyterLab and choose *Run → Run All Cells*.
- Every notebook is saved **with its outputs and figures**, so you can read it before running anything.
- Notebooks 01–04, 08 and 10 need only Python itself, plus Matplotlib for a few figures in 03, 04 and 10. From notebook 05 onwards most notebooks also use NumPy; notebook 22 also uses SciPy.
- The notebooks were tested with Python 3.10 (NumPy 1.26) and Python 3.13 (NumPy 2).

## How to study a notebook

1. **Read the Study guide** at the top. It says whether the notebook is core or optional, what you need first, which sections are essential, and what "understanding it" means: a short list of things you should be able to do without looking back.
2. Before you run a cell, **predict** what it will print or plot. Then run it and compare.
3. **Try each practice question** in the empty cell before you run the worked answers.
4. Experiment freely in a copy, so the original stays intact.
5. At the end, return to the Study guide's list. If you cannot do an item without looking back, reread that section.

**A note on comments.** Every line of code has a comment to help you read it. In your own programs, comment the *reasons* and the non-obvious steps instead.

## Checks

Every notebook is checked automatically each time the repository changes, on Python 3.10 and 3.12. You can run the same checks yourself from the repository folder:

| Command | What it checks |
|---|---|
| `python -m pip install -r requirements-dev.txt` | installs the packages the checks need (once) |
| `python tests/check_notebooks.py` | every line of code has a comment; every notebook has its title, series line and Study guide; no saved errors or local file paths |
| `python tests/run_notebooks.py` | every notebook runs from top to bottom without an error (about 2 minutes). Add a number, such as `python tests/run_notebooks.py 08`, to run one notebook |

Most notebooks also check their own results, with `assert` statements that compare the program against a hand calculation, a physical law or an exact solution. A notebook that runs to the end has passed those checks.

## Licence and citation

- **Code** (the code cells and the scripts in `tests/`): MIT, see [`LICENSE`](LICENSE).
- **Text, figures and generated data** (the explanations in the notebooks, their figures and the synthetic data sets they create): CC BY 4.0, see [`DATA_LICENSE.md`](DATA_LICENSE.md).

You are welcome to use and adapt the notebooks in your own teaching. Please cite the collection as given in [`CITATION.cff`](CITATION.cff); GitHub's *Cite this repository* button uses it.

## Contact

Yanwei Wang, Nazarbayev University: [yanwei.wang@nu.edu.kz](mailto:yanwei.wang@nu.edu.kz), ORCID [0000-0002-8488-9833](https://orcid.org/0000-0002-8488-9833).

Found a mistake or have a suggestion? Please open an [issue](https://github.com/ktwyw/python-for-engineers-case-studies/issues).
