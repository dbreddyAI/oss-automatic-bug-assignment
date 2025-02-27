# -*- coding: utf-8 -*-
"""
.. module:: mozilla_pre_processing_experiment
   :platform: Unix, Windows
   :synopsis: This module contains a class used to conduct the first
              experiment of the thesis on the bug reports of Mozilla
              Firefox. The experiment consists mainly of comparing
              several combinations of pre-processing techniques and
              selecting the best one.

.. moduleauthor:: Daniel Artchounin <daniel.artchounin@ericsson.com>


"""

import os
import inspect
import logging

current_dir = os.path.dirname(os.path.abspath( \
inspect.getfile(inspect.currentframe())))
os.sys.path.insert(0, current_dir)
from mozilla_data_pre_processer import MozillaDataPreProcesser
parent_dir = os.path.dirname(current_dir)
grand_parent_dir = os.path.dirname(parent_dir)
os.sys.path.insert(0, grand_parent_dir)
from experiment_1.exp_1_launcher \
import Exp1Launcher

class MozillaExp1Launcher(Exp1Launcher):

    def __init__(self, data_file, developers_dict_file, \
    developers_list_file, clean_brs=False, use_stemmer=False, \
    use_lemmatizer=False, stop_words_removal=False, \
    punctuation_removal=False, numbers_removal=False):
        self._current_dir = os.path.dirname(os.path.abspath( \
        inspect.getfile(inspect.currentframe())))
        super().__init__(data_file, developers_dict_file, \
        developers_list_file, clean_brs=False, use_stemmer=False, \
        use_lemmatizer=False, stop_words_removal=False, \
        punctuation_removal=False, numbers_removal=False)

    def generate_output_file(self):
        """Generates a specific pre-processed data set file"""
        # Instantiation of a specific pre-processor
        self._data_pre_processer = MozillaDataPreProcesser( \
        self.data_file, clean_brs=self.clean_brs, \
        use_stemmer=self.use_stemmer, \
        use_lemmatizer=self.use_lemmatizer, \
        stop_words_removal=self.stop_words_removal, \
        punctuation_removal=self.punctuation_removal, \
        numbers_removal=self.numbers_removal)
        # Call of the super-class same method
        super().generate_output_file()

def main():
    # Below, the path of the file which contains a dictionary related
    # to the mappings of the developers
    developers_dict_file = None
    # Below, the path of the file which contains a list of the
    # relevant distinct developers
    developers_list_file = None

    clean_brs = False
    use_stemmer = False
    use_lemmatizer = False
    stop_words_removal = False
    punctuation_removal = False
    numbers_removal = False

    data_file = "../scrap_mozilla_firefox/sorted_brs.json" # Path of the file containing the data

    mozilla_exp_1_launcher = MozillaExp1Launcher( \
    data_file=data_file, \
    developers_dict_file=developers_dict_file, developers_list_file=developers_list_file, \
    clean_brs=clean_brs, \
    use_stemmer=use_stemmer, \
    use_lemmatizer=use_lemmatizer, \
    stop_words_removal=stop_words_removal, \
    punctuation_removal=punctuation_removal, \
    numbers_removal=numbers_removal)

    mozilla_exp_1_launcher.conduct_experiment()

if __name__ == "__main__":
    main()