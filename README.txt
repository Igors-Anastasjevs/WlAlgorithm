Introduction
This repository is for implementation Weisfeiler-Lehman algorithm in 2 ways
for "Weisfeiler-Lehman Algorithm" Final Year Project(COMP3931) in University of Leeds
on 3rd year of Computing Science with Artifitial Inteligence course by Igors Anastasjevs (fy18ia).
These modules were created in order to compare performances of both variants of Weisfeiler-Lehman Algorithm[1,4]
with VF2, implemented in NetworkX[21].

WLalg.py has Weisfeiler-Lehman algorithm, described in D. Bieber's publication[1].
WLalgShevashidze.py has Weisfeiler-Lehman algorithm, described in N. Shevashidze's and co-authors' paper[4].
testWL.py has test cases for WLalg.py functions.
testWLShevashidze.py has test cases for WLalg.py functions.
savedata.py is a module with functions, which helps measure performances of algorithms of graph isomorphism determination, compatible with
NetworkX graphs.

Requirements
Before launching anything in this repository, I used some libraries, for example, NetworkX and mmh3.
"pip3 install -r requirements.txt" is required to be launched before launching my code.
Python 3.8 is recommended, as it was written on this version.

Unit testing
I used "unittest" module in order to create test cases.
Unit tests are launched by command "python -m unittest", being in "WLalgorithm" directory.

How to get results
In order to reproduce my results, type in command line "python main.py". Results will be seen in changed/created files
in "output" directory.
However, execution of these functions can take about a day long.