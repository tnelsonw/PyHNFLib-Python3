# PyHNFLib
A hypergame normal form (HNF) library written in Python3. This is forked from https://github.com/cngutierr/PyHNFLib which was originally written in Python version 2. There are a few TODO items left. They are all related to the test_DesertStorm unit test in src/tests/test_gambit.py. That is the only test that failed to pass unit tests in the Python2 to Python3 conversion. The issues are most likely related to subgames. 

If using this library and not using subgames, then you will have no issues. This library has great plots to track hypergame expected utility (HEU). 

To make a new hypergame, make a new yaml file in the config directory. Use previous yaml files as examples for creating your own. 
