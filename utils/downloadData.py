import kaggle
import os

#this is to set the path where I want to download the dataset
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
FILE_PATH = os.path.join(PARENT_DIR, "data")

#This is the function to get data into the data carpet
def getData():
   #if the data carpet does not exist, so create a one 
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    
    files_csv_in_list = []
    
    files_in_carpet = os.listdir(FILE_PATH)
    
    for f in files_in_carpet:
        if f.endswith('.csv'):
            files_csv_in_list.append(f)
    
    #check if in the files_csv_in_list is there any csv file
    if files_csv_in_list:
        print("\n✅ The dataset is in the carpet")
    
    else:   
        kaggle.api.authenticate()
        # print(kaggle.api.dataset_list_files('prasad22/healthcare-dataset').files)

        kaggle.api.dataset_download_files('prasad22/healthcare-dataset', path=FILE_PATH,unzip=True)

        kaggle.api.dataset_metadata('prasad22/healthcare-dataset', path=FILE_PATH)

        print("The CSV file is in the data carpet")