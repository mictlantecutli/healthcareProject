from utils import downloadData
import pandas as pd
import os
from analysisDataApp.handlerApp import HandlerApp

#call getData function to download the cvs file
downloadData.getData()


#to print a test data from the dataset
#first I get the route where is the dataset
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(CURRENT_DIR, 'data', 'healthcare_dataset.csv')

dataHealth = pd.read_csv(file_path)
# print(dataHealth.head())

print("------------------------------------")
print("***Welcome to Healthcare Dataset***")
print("------------------------------------")

#call the HandlerApp class and pass the dataset in this
dataAnalysisApp = HandlerApp(dataHealth)

totalRegisters = dataAnalysisApp.analyzer.get_total_registers()
print(f"-This DataSet contains {totalRegisters} records")
print(f"-This Dataset contains {dataHealth["Name"].nunique()} non repeated records")

dataAnalysisApp.start_analysis()



