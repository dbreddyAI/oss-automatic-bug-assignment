# -*- coding: utf-8 -*-
"""
.. module:: eclipse_experiment_2_results_plotter
   :platform: Unix, Windows
   :synopsis: This module contains a class used to plot the results 
              related to the second experiment of the thesis conducted
              on the bug reports of Eclipse JDT. The experiment 
              consists mainly of comparing several feature extraction
              techniques and selecting the best one.

.. moduleauthor:: Daniel Artchounin <daniel.artchounin@ericsson.com>


"""

import os
import inspect

current_dir = os.path.dirname(os.path.abspath( \
inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.insert(0, parent_dir)
grand_parent_dir = os.path.dirname(parent_dir)
os.sys.path.insert(0, grand_parent_dir)
from experiment_2.exp_2_results_plotter \
import Exp2ResultsPlotter

class EclipseExp2ResultsPlotter(Exp2ResultsPlotter):

    def __init__(self, cleaned_results_file_name):
        """Constructor"""
        self._current_dir = os.path.dirname(os.path.abspath( \
        inspect.getfile(inspect.currentframe())))
        super().__init__(cleaned_results_file_name)
        
    def plot_results(self):
        """This method plots the results in chart(s)"""
        self.plot_parameters = [
            {
                "key": "not_combined_avg_accuracy",
                "x_lim_min": 0.08,
                "x_lim_max": 0.299,
                "x_label": "Accuracy",
                "y_label": "Configurations",
                "title_font_size": 45,
                "labels_font_size": 40, 
                "y_tick_labels_font_size": 35,
                "title": "Accuracy of the different feature " + \
                "extraction techniques (without combination of " + \
                "features)",
                "file_name" : "experiment_21.png",
                "debug_title": "Average Accuracy (Without Combination)",
                "combined": False,
                "bars_labels_space": 0.0015
            },
            {
                "key": "combined_avg_accuracy",
                "x_lim_min": 0.20,
                "x_lim_max": 0.289,
                "x_label": "Accuracy",
                "y_label": "Configurations",
                "title_font_size": 45,
                "labels_font_size": 40, 
                "y_tick_labels_font_size": 35,
                "title": "Accuracy of the different feature " + \
                "extraction techniques (with combination of " + \
                "features)",
                "file_name": "experiment_22.png",
                "debug_title": "Average Accuracy (With Combination)",
                "combined": True,
                "bars_labels_space": 0.0005
            },
            {
                "key": "not_combined_avg_mrr",
                "x_lim_min": 0.23,
                "x_lim_max": 0.45,
                "x_label": "MRR",
                "y_label": "Configurations",
                "title_font_size": 45,
                "labels_font_size": 40, 
                "y_tick_labels_font_size": 35,
                "title": "MRR of the different feature " + \
                "extraction techniques (without combination of " + \
                "features)",
                "file_name" : "experiment_23.png",
                "debug_title": "Average MRR (Without Combination)",
                "combined": False,
                "bars_labels_space": 0.0015
            },
            {
                "key": "combined_avg_mrr",
                "x_lim_min": 0.3625,
                "x_lim_max": 0.439,
                "x_label": "MRR",
                "y_label": "Configurations",
                "title_font_size": 45,
                "labels_font_size": 40, 
                "y_tick_labels_font_size": 35,
                "title": "MRR of the different feature " + \
                "extraction techniques (with combination of " + \
                "features)",
                "file_name": "experiment_24.png",
                "debug_title": "Average MRR (With Combination)",
                "combined": True,
                "bars_labels_space": 0.0005
            }   
        ]
        super().plot_results()

def main():
    """The main function of the script"""
    cleaned_results_file_name = "cleaned_tr_representation_" + \
    "experiment_results.json"
    eclipse_exp_2_results_plotter = \
    EclipseExp2ResultsPlotter(cleaned_results_file_name)
    eclipse_exp_2_results_plotter.plot_results()

if __name__ == "__main__":
    main()