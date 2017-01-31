template_dir = 'templates'
static_dir = '/home/arjoonn/dev/dataflow/static'

source_box_class = 'BoxSource'
dd_box_class = 'BoxDD'
de_box_class = 'BoxDE'
sink_box_class = 'BoxSink'

code_imports = '''
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split

#########################################################
'''

program_table = dict(addreadcsv=['Read csv', source_box_class,
    'data = pd.read_csv("data.csv")'],
        addrfclassifier=['RandomForest Classifier', source_box_class,
            'est = RandomForestClassifier(n_jobs=-1)'],
        addscore=['Add Score', de_box_class,
        '''X, Y = data.drop("target", axis=1), data.target
'p = est.predict(X)
'score = roc_auc_score(Y, p)'''],
        addtrainclassifier=['Train Classifier', de_box_class,
        '''X, Y = data.drop("target", axis=1), data.target
est.fit(X, Y)'''],
        addtraintestsplit=['TrainTestSplit', dd_box_class,
        '''X, Y = data.drop("target", axis=1), data.target
x_tr, x_ts, y_tr, y_ts = train_test_split(X, Y, 0.25)
train = x_tr["target"] = y_tr
test = x_ts["target"] = y_ts'''],
        addprint=['Print', sink_box_class, 'print(inp)']
        )
