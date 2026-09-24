# QA_5.2_training

The pipeline automates the extraction and transformation of library data. The pipeline uses Python to:
- read csv files
- removed duplicate data
- flag incorrect data
- correct date format
- output clean data

The data is visualized in a powerBI dasboard.

# Repo Structure

├── .github/workflows  
├── data/           
├── docker/             
├── pipeline/            
├── requirements.txt            
├── cleaning_module_exc.py          
├── testing_module.py
├── diagram.png
├── README.ms

# How to run the pipeline
## Install dependencies

pip install -r requirements.txt

## Execute the script

python cleaning_module_exc.py 

# Testing

Testing is automatically carried out through pytest and GitHub actions
      
