import pandas as pd
import os
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot
import cufflinks

# Standard plotly imports
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

from plotly.offline import iplot, init_notebook_mode

# Using plotly + cufflinks in offline mode
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

### FILE SETTINGS

acad_grad_path = '/Users/noresources/Dropbox/_git_projects/ProgSense/data/csv/acwork_graduates.csv'
acad_stud_path = '/Users/noresources/Dropbox/_git_projects/ProgSense/data/csv/acwork_students.csv'
student_info_path = '/Users/noresources/Dropbox/_git_projects/ProgSense/data/csv/students_20190525.csv'




class data_interface():

    def __init__(self):
        self.datasets = {}

        self.datasets['acwork_graduates'] = pd.read_csv(
            acad_grad_path, sep=';',
            low_memory=False)

        self.datasets['acwork_students'] = pd.read_csv(
            acad_stud_path, sep=';',
            low_memory=False)

        self.datasets['student_info'] = pd.read_csv(
            student_info_path, sep=';',
            low_memory=False)

    ### GETTERS

    def get_datasets(self):
        return self.datasets

    def get_work_graduates(self):
        return self.datasets['acwork_graduates']

    def get_work_student(self):
        return self.datasets['acwork_students']

    def get_info_students(self):
        return self.datasets['student_info']

    #### ------------------------------------------------------

    def get_course(self, course_name: str):
        pass

    def prep_list(self, col):
        """
        Removes the NS and the negative grades returning a list of the grades
        """
        grade_list = col
        # Remove the empty values
        grade_list = [float(i.replace(',', '.')) if type(
            i) == str else i for i in grade_list if i != "NS"]
        # Remove the failing grades
        grade_list = [i for i in grade_list if i >= 5.0]
        return grade_list
