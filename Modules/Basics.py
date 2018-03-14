from __future__ import division
import numpy as np
import pandas
import math
import os
import types
import h5py
from six.moves import cPickle as pickle

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("white")

from ML_Tools.Plotting_And_Evaluation.Plotters import *
from ML_Tools.General.Misc_Functions import *
from ML_Tools.General.Ensemble_Functions import ensemblePredict

dirLoc = "../Data/"

def getTarget(sample):
    if 'quark' in sample:
        return 1
    else:
        return 0