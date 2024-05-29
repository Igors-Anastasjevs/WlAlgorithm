Introduction

This repository is for implementation Weisfeiler-Lehman algorithm in 2 ways
for "Weisfeiler-Lehman Algorithm" Final Year Project(COMP3931) in University of Leeds
on 3rd year of Computing Science with Artifitial Inteligence course by Igors Anastasjevs (fy18ia).
These modules were created in order to compare performances of both variants of Weisfeiler-Lehman Algorithm[1,2]
with VF2, implemented in NetworkX[3].

WLalg.py has Weisfeiler-Lehman algorithm, described in D. Bieber's publication[1].
WLalgShevashidze.py has Weisfeiler-Lehman algorithm, described in N. Shevashidze's and co-authors' paper[2].
testWL.py has test cases for WLalg.py functions.
testWLShevashidze.py has test cases for WLalgShevashidze.py functions.
savedata.py is a module with functions, which helps measure performances of algorithms of graph isomorphism determination, compatible with
NetworkX graphs.

Requirements

Before launching anything in this repository, I used some libraries, for example, NetworkX and mmh3.
"pip3 install -r requirements.txt" is required to be launched before launching my code.
Python 3.8 is recommended, as it was written on this version.

Unit Testing

I used "unittest" module in order to create test cases.
Unit tests are launched by command "python -m unittest", being in "WLalgorithm" directory.

How to Get Results

In order to reproduce my results, type in command line "python main.py". Results will be seen in changed/created files
in "output" directory.
However, execution of these functions can take about a day long.

1.	Bieber, D., The Weisfeiler-Lehman Isomorphism Test, [Online], 2019. [Assessed October 2021]
Available from: https://davidbieber.com/post/2019-05-10-weisfeiler-lehman-isomorphism-test/
2.  Shervashidze, N., Schweitzer, P., van Leeuwen, E. J., Mehlhorn, K., Borgwardt, K. M., Bach, F., ed.
 Weisfeiler-Lehman Graph Kernels, Journal of Machine Learning Research, 2011, 12, article no: 2539-2561
3.  21.	NetworkX. is_isomorphic. [no date]. [Accessed July 2022] Available from:
  https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.isomorphism.is_isomorphic.html#networkx.algorithms.isomorphism.is_isomorphic
