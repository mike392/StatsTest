'''
Created on Dec 27, 2016

@author: Mikhail_Barsukou
'''
import pandas

class PandasUtils:
    def get_dataframe(self,dataset, columns_list):
        return pandas.DataFrame(data=dataset,columns=columns_list)
    
    def get_avg_for_column(self, dataframe, column_name):
        return dataframe[column_name].mean()
    
