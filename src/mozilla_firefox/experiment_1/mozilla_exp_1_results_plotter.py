# -*- coding: utf-8 -*-
"""
.. module:: mozilla_experiment_1_results_plotter
   :platform: Unix, Windows
   :synopsis: This module contains a class used to plot the results
              related to the first experiment of the thesis conducted
              on the bug reports of Mozilla Firefox. The experiment
              consists mainly of comparing several combinations of
              pre-processing techniques and selecting the best one.

.. moduleauthor:: Daniel Artchounin <daniel.artchounin@ericsson.com>


"""

import os
import inspect

current_dir = os.path.dirname(os.path.abspath( \
inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.insert(0,parent_dir)
grand_parent_dir = os.path.dirname(parent_dir)
os.sys.path.insert(0, grand_parent_dir)
from experiment_1.exp_1_results_plotter \
import Exp1ResultsPlotter

class MozillaExp1ResultsPlotter(Exp1ResultsPlotter):

    def __init__(self, cleaned_results_file_name):
        """Constructor"""
        self._current_dir = os.path.dirname(os.path.abspath( \
        inspect.getfile(inspect.currentframe())))
        super().__init__(cleaned_results_file_name)

    def plot_results(self):
        """This method plots the results in chart(s)"""
        self.plot_parameters = [
            {
                "key": "avg_accuracy",
                "x_lim_min": 0.1535,
                "x_lim_max": 0.17,
                "x_label": "Accuracy",
                "y_label": "Configurations",
                "title_font_size": 50,
                "labels_font_size": 45,
                "y_tick_labels_font_size": 40,
                "title": "Accuracy of the different pre-processing " \
                "configurations",
                "file_name" : "experiment_11.png",
                "debug_title": "Average Accuracy",
                "bars_labels_space": 0.0001,
            },
            {
                "key": "avg_mrr",
                "x_lim_min": 0.3285,
                "x_lim_max": 0.349,
                "x_label": "MRR",
                "y_label": "Configurations",
                "title_font_size": 50,
                "labels_font_size": 45,
                "y_tick_labels_font_size": 40,
                "title": "MRR of the different pre-processing " \
                "configurations",
                "file_name": "experiment_12.png",
                "debug_title": "Average MRR",
                "bars_labels_space": 0.0001,
            }
        ]
        super().plot_results()


def main():
    """The main function of the script"""
    cleaned_results_file_name = "cleaned_pre_processing_" + \
    "experiment_results.json"
    mozilla_exp_1_results_plotter = \
    MozillaExp1ResultsPlotter(cleaned_results_file_name)
    mozilla_exp_1_results_plotter.plot_results()

if __name__ == "__main__":
    main()