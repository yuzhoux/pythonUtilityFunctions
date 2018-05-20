## these pyspark functions can sum and devide at scale; these functions can also apply parameterized functions to columns. 

from pyspark.sql import DataFrame
from pyspark.sql.functions import concat, col, lit, first
from pyspark.sql.window import Window
import pyspark.sql.functions as func

#1
def sumCols(self, col_list,new_name):
"""
col_list: a list of column to sum
new_name: name of the returned column

this function add a list of columns together
example: you can add six months of data ['m1','m2','m3','m4','m5','m6'] to get ['half_year']
"""
    columnstosum = [col(c) for c in col_list]
    self=self.withColumn(new_name, sum(columnstosum))
    return self

DataFrame.sumCols= sumCols

#2
def normalize(self, col_list):
"""
col_list: a list of column to normalize

this function normalize a list of column
example: you can devide three months of count ['m1','m2','m3'] by anuual total ['total'] to get a percentage version of ['m1','m2','m3']
"""
    for coll in col_list:
        self=self.withColumn(str(coll)+'_per',col(coll)/(col("total")))
    return self

DataFrame.normalize = normalize


#3
windowSpec = Window.partitionBy('id').orderBy("order").rangeBetween(-6,-1)
def movingAvg(self,col_list):
"""
col_list: a list of column to feed the function

this function calculates the moving average of the past 6 periods, and then find the percentage difference 
between current period and the moving average of the past 6 periods 
"""
    for coll in col_list:
        self=self.withColumn(str(coll)+'_mvgDiff',\
                             (col(coll)-func.mean(col(coll)).over(windowSpec))/(func.when(func.mean(col(coll)).over(windowSpec)==0,func.when(col(coll)==0,1).\
							 otherwise(col(coll))).otherwise(func.mean(col(coll)).over(windowSpec))))
    return self    

DataFrame.movingAvg = movingAvg






