from analysisDataApp.dataAnalysis import AnalysisData

class HandlerApp:
    def __init__(self, dataSet):
        self.analysis_on = True
        self.analyzer = AnalysisData(dataSet)
        
    #This methos is to handle the program sequence    
    def start_analysis(self):
        while self.analysis_on:
            
            # #display the menu    
            self.analysis_menu()
            
            # #Choose and display the data analysis
            self.chose_analysis()
            
            
            
            # # print(f"\n{self.analyzer.get_top_diseases()}\n")
            # self.analyzer.tops_percentage_byHospital()
            
            # #to finish the cicle. It is temporal
            
    
    #Method to ask the user chose for one analysis
    def chose_analysis(self):
        option = input("Type a number option: ")
        
        if option == "1":
            top_diseases = self.analyzer.get_top_diseases()
            print("-----------------------")
            print(top_diseases)
            print(f"\n***{top_diseases.iloc[0]['Medical Condition']} disease the the most recurrent***")
            print("-----------------------")
        elif option == "2":
            print("[][][][][][][][][][][][][][][][][][][][][]")
            self.analyzer.hospital_demand_by_disease()
            print("[][][][][][][][][][][][][][][][][][][][][]")
        elif option == "3":
            print("-----------------------")
            self.analyzer.top_least_InsuranceContracts()
            print("-----------------------")
        elif option == "4":
            self.analyzer.topDiseaseAdmissionGraph_2019()
        elif option == "5":
            print("The End")
            self.analysis_on=False
        else:
            print("choose a number. Try again please")
        
        
    #Method to display an analysis menu
    def analysis_menu(self):
       
        print("\nAnalysis Menu:")
        print("1. Top Diseases")
        print("2. Hospital Demand by Disease")
        print("3. Top and Least Used Insurance")
        print("4. Top disease along time")
        print("5. Exit")

            
    
    