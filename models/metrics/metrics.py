import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import visualization_utils
SHOW_WEIGHTED = True # show weighted accuracy instead of unweighted accuracy
PLOT_CLIENTS = False
stat_file = 'stat_metrics.csv' # change to None if desired
sys_file = 'sys_metrics.csv' # change to None if desired

stat_metrics, sys_metrics = visualization_utils.load_data(stat_file, sys_file)

# Plots accuracy vs. round number.
if stat_metrics is not None:
    visualization_utils.plot_accuracy_vs_round_number(stat_metrics, True, plot_stds=False)