import pandas as pd
import datetime as dt

# pd.set_option("display.width", 200)
# pd.set_option("display.max_columns", 20)

def read_data(path):
    df = pd.read_csv(path)
    return df




# #replace NaN cells
# def fill_na(df):
#     return df.fillna("missing_value")


#remove NaN cells
def remove_na(df):
    return df.dropna(how="any")
    
#fix datatypes
def remove_characters(df, column):
    df[column] = df[column].astype("string").str.replace('"', '').str.strip()
    return df


def convert_string_to_date(df, column):
    df[column] = pd.to_datetime(df[column], errors="coerce", dayfirst=True)
    return df



def find_days_df(df, column_one, column_two):
    df["days diff"] = df[column_one] - df[column_two]
    df["days diff"] = df["days diff"].dt.days

    return df


#clear duplicates

def drop_duplicates(df, column):

    df = df.drop_duplicates(subset=column)
    return (df)


books = read_data("data/library.csv")


books = remove_na(books)
books = remove_characters(books, "Book checkout")
books = convert_string_to_date(books, "Book checkout")
books = convert_string_to_date(books, "Book Returned")
books = remove_na(books)
books = find_days_df(books,"Book Returned", "Book checkout" )  
books = drop_duplicates(books, 'Books')
# print(books)

def save_to_csv(df, path, file_name):
    df.to_csv(f"{path}/{file_name}.csv")
    return 


save_to_csv(books, 'data', 'output_file')





