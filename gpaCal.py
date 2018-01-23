# https://stackoverflow.com/questions/26205922/calculate-weighted-average-using-a-pandas-dataframe

import pandas as pd

class GpaCal:
    def __init__(self):
        self.score_data = None

    def open_data(self, file_name):
        self.score_data = pd.read_csv(file_name, encoding='utf-8')

    def calculate_gpa(self):
        data_field = self.score_data
        select_column = ['semester', 'credit']
        report = data_field[select_column].groupby('semester').sum()

        semester_list = []
        for semester in report.index:
            semester_list.append(semester)
        semester_list.sort(key=lambda x:(x.split('_')[1], x.split('_')[0]))

        for semester in semester_list:
            df_temp = data_field[data_field['semester'] == semester]
            gpax = (df_temp.credit * df_temp.grade_number).sum() \
                   / df_temp.credit.sum()
            credit = df_temp.credit.sum()
            
            print('GPAX(', semester, ') : ', end='')
            print("%.2f" % (gpax), ' credit : ', credit)

        gpa = (data_field.credit * data_field.grade_number).sum() \
              / data_field.credit.sum()
        sum_credit = data_field.credit.sum()
        
        print('GPA :', end='')
        print("%.2f" % gpa, ' total credit :', sum_credit)

gpaCal = GpaCal()
gpaCal.open_data("MyGrade.csv")
gpaCal.calculate_gpa()


        
