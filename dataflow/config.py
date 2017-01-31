template_dir = 'templates'
static_dir = '/home/arjoonn/dev/dataflow/static'

source_box_class = 'BoxSource'

code_imports = '''
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split

#########################################################
'''
