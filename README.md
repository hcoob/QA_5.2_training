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
├── README.md
├── diagram.png   

# How to run the pipeline
## Install dependencies

pip install -r requirements.txt

## Execute the script

python cleaning_module_exc.py 

## How the script works

1. read_data(path): reads the csv filed and returns a dataframe
2. remove_na(df): removed rows with NA values
3. remove_characters(df, column): removes characters from a string
4. convert_string_to_date(df, column): converts string to date
5. find_days_df(df, column_one, column_two): creates a new column that stores the difference between two dates
6. drop_duplicates(df, column): removes duplicate rows
7. save_to_csv(df, path, file_name): outpus the clean data into a new .csv file

# Testing

Testing is automatically carried out through pytest and GitHub actions when code is pushed to the repository.

# Data visualisation

The powerBI dashboards shows:
1. Number of books borrowed per month
2. Number of books returned each month
3. Number of books past days allowed
4. Number of books with incorrect dates
