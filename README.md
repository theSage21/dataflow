DataFlow
========

I used to love working on [Blender's](https://www.blender.org) node editor in
my college days. That love was invoked again once I encountered Microsoft's
MLStudio. I liked it for the simple fact that I did not have to type a lot.
That is where dataflow originates from.

Dataflow provides nodes/boxes/operators which represent processing units. These
are connected via links/data paths/lines to show dependency. There are four
main kinds of boxes (Source, Sink, DataData, DataEstimator). These are named so
because Dataflow tries to expose as much of the sk-learn api as possible via a
dataflow diagram.

In the future dataflow may not remain limited to Python.


Get Started
-----------

Here's a session from start to finish.

```bash
virtualenv -p python3 env
source env/bin/activate
pip install git+https://github.com/theSage21/dataflow.git@master


Trivia
-------------

- There are three main types of blocks
    - **Source blocks** create something out of nothing. These are the blocks which read datasets and create estimators
    - **D2D** Data to data blocks transform data in some way.
    - **DE** Data and Estimator blocks take in a dataset and an estimator and return a transformed dataset and estimator. These are typically training blocks.
    - **Sink** Data sinks are things like `print` blocks which create no outputs.
- All blocks can be connected in a data flow diagram. 
- Controls:


To use dataflow, run `dataflow` and navigate to `127.0.0.1:8080` in your browser. The data blocks can be added and connected by hand.

Once the command is issued to make a file, it is generated in `static/scripts/`

![Main page screenshot](screenshots/main.png)

## This flowchart generates the following code

```python
# Generated on
# 2017-01-31 16:58:56.740630
# via DataFlow: https://github.com/theSage21/dataflow


import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split

#########################################################


def TrainClassifier0(est=None, data=None):
    X, Y = data.drop("target", axis=1), data.target
    est.fit(X, Y)
    
    return est
    

def ReadCsv2():
    data = pd.read_csv("data.csv")
    return data
    

def RandomForestClassifier3():
    est = RandomForestClassifier(n_jobs=-1)
    return est
    

def TrTsSplit4(data=None):
    X, Y = data.drop("target", axis=1), data.target
    x_tr, x_ts, y_tr, y_ts = train_test_split(X, Y, 0.25)
    train = x_tr["target"] = y_tr
    test = x_ts["target"] = y_ts
    
    return train, test
    

def Print5(inp=None):
    print(inp)
    return 
    

def Score1(est=None, data=None):
    X, Y = data.drop("target", axis=1), data.target
    p = est.predict_proba(X)[:, 0]
    score = roc_auc_score(Y, p)
    
    return score
    

#########################
#MAIN
#########################
# Parts within steps can be run in parallel


# Step --------------------------<[1]>-

var2 = RandomForestClassifier3()
var0 = ReadCsv2()

# Step --------------------------<[2]>-

var1, var4 = TrTsSplit4(var0)

# Step --------------------------<[3]>-

var3 = TrainClassifier0(var2, var1)

# Step --------------------------<[4]>-

var5 = Score1(var3, var4)

# Step --------------------------<[5]>-

Print5(var5)
```
