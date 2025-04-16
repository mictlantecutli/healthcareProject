import pandas as pd
import matplotlib.pyplot as plt

#This class handle the analysis of the dataset
class AnalysisData:
    def __init__(self, dataSet):
        self.__dataSet = dataSet
      
       
    #This is a test to display rows of the dataset 
    def get_total_registers(self):
        # return self.__dataSet.columns.tolist()
        #test to print the number of registers
        return len(self.__dataSet)
        
    #this method is to get the the top diseases of the dataset  
    def get_top_diseases(self):
        top_medical_conditions = self.__dataSet['Medical Condition'].value_counts().head(3).reset_index()
        top_medical_conditions.columns = ['Medical Condition', 'Total']
        return top_medical_conditions
        
        
        
    #Method to get the hospital demand by disease in percentage
    def hospital_demand_by_disease(self):
        #First I enter into all the data of the three top diseases
        total_diseases = self.get_top_diseases()
        
        #From the data if the three top diseases. I group by hospital, to see what hospitals are more demanded in any issue(top three issues). And  
        #and set a new column with the percentage.
        for _, row in total_diseases.iterrows():
            disease = row["Medical Condition"]
            total = row["Total"]
            disease_data = self.__dataSet[self.__dataSet['Medical Condition']==f"{disease}"]
            amountHospitalByDisease = disease_data.groupby("Hospital").size().reset_index(name="Total").sort_values(by="Total", ascending=False).head(3)
            
            #Add a new column to display the percentage   
            amountHospitalByDisease["Percentage %"] = amountHospitalByDisease["Total"]*100/total
           
            print(f"\n{disease} - {total} cases  ")
            print(amountHospitalByDisease)
            print(f"\n{amountHospitalByDisease.iloc[0]['Hospital']} is the hospital with most cases of {disease}")
            print("--------")
        
    #Method to get the insurance with more contracts, and less contracts
    def top_least_InsuranceContracts(self):
        topContracts = self.__dataSet.groupby("Insurance Provider").size().reset_index(name="Total").sort_values(by="Total", ascending=False).head(1)
        leastContracts = self.__dataSet.groupby("Insurance Provider").size().reset_index(name="Total").sort_values(by="Total", ascending=True).head(1)
        
        print(f"\n✅ The 'TOP' insurance provider by number of contracts is: {topContracts.iloc[0]['Insurance Provider']} with {topContracts.iloc[0]['Total']} contracts")
        print(f"\n✅ The 'LEAST' insurance provider by number of contracts is: {leastContracts.iloc[0]['Insurance Provider']} with {leastContracts.iloc[0]['Total']} contracts")
        # print(topContracts.to_string(index=False, columns=["Insurance Provider", "Total"]))
    
    def topDiseaseAdmissionGraph_2019(self):
        
        #First I enter into all the data of the three top diseases with the method to get the top diseases of the dataset
        top_diseases = self.get_top_diseases()
        
        #get the first place of top diseases
        veryTopDisease = top_diseases.iloc[0]['Medical Condition']
        
        #converting the Date of Admission as datetime type to play with the date time later
        self.__dataSet["Date of Admission"]= pd.to_datetime(self.__dataSet["Date of Admission"])
        
        #with the very top disease and the 2019 year I get all the data of 2019 and the very top disease from the dataset
        disease_data_2019 = self.__dataSet[(self.__dataSet['Medical Condition']==f"{veryTopDisease}") & (self.__dataSet["Date of Admission"].dt.year == 2019)]
        
        #I add a new colum obtained by the month of the "Date of Admission" column
        disease_data_2019["Month"] = disease_data_2019["Date of Admission"].dt.to_period("M") 
       
        #Then I group all the data by month, and get the amount of every month in the "Total" column, sorted by month
        topDiseaseTotals_2019_by_month = disease_data_2019.groupby("Month").size().reset_index(name="Total").sort_values(by="Month", ascending=True)
        
        #I draw the graph
        topDiseaseTotals_2019_by_month.plot(x="Month", y="Total", kind="bar")
        
        #Finally show the graph
        return plt.show()
       
  
        
        
    
    
        
       
        
        
        
        
    

