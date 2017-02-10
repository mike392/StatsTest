'''
Created on Dec 28, 2016

@author: Mikhail_Barsukou
'''
import numpy

class NumpyUtils:
    '''
    classdocs
    '''
    def get_exp_value(self, power):
        return numpy.exp(power)
    
    def get_factorial_value(self, value):
        return numpy.math.factorial(value)
    
    def get_power_value(self, value, power):
        return numpy.power(value, power)
    
    def get_poisson_distrib(self, lam, input_range):
        return [self.get_exp_value((-1) * lam) * ( self.get_power_value(lam, item) / self.get_factorial_value(item)) for item in input_range]
    
    def get_matrix(self, input_list):
        return numpy.matrix(input_list)
    
    def get_product_matrix(self, home_matrix, away_matrix):
        return [[inner_item * outer_item for inner_item in home_matrix] for outer_item in away_matrix]
    
    def get_bet_rates(self,result_matrix):
        diag_sum = sum(numpy.diag(result_matrix))
        upper_triangle_sum = sum([sum(item) for item in numpy.triu(result_matrix)])
        lower_triangle_sum = sum([sum(item) for item in numpy.tril(result_matrix)])
        return 1 / diag_sum, 1 / (upper_triangle_sum - diag_sum), 1 / (1 - upper_triangle_sum)