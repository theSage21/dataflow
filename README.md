DataFlow
========

Tries to expose sk-learn via a dataflow diagram


Documentation
-------------

- There are three main types of blocks
    - **Source blocks** create something out of nothing. These are the blocks which read datasets and create estimators
    - **D2D** Data to data blocks transform data in some way.
    - **DE** Data and Estimator blocks take in a dataset and an estimator and return a transformed dataset and estimator. These are typically training blocks.
- All blocks can be connected in a data flow diagram. 
