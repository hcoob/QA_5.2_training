import pandas as pd
import datetime as dt

# pd.set_option("display.width", 200)
# pd.set_option("display.max_columns", 20)

def read_data(path):
    df = pd.read_csv(path)
    return df




#replace NaN cells
def fill_na(df):
    return df.fillna("missing_value")



#fix datatypes
def remove_characters(df, column):
    df[column] = df[column].astype("string").str.replace('"', '').str.strip()
    return df


def convert_string_to_date(df, column):
    df[column] = pd.to_datetime(df[column], errors="coerce", dayfirst=True)
    return df


#remove NaN cells
def remove_na(df):
    return df.dropna(how="any")
    


def find_days_df(df, column_one, column_two):
    df["days diff"] = books[column_one] - books[column_two]

    # if df["dayd diff"] > 14 or df["dayd diff"] < 0:
    #     df["valid_flag"] = 1 
    return df

books = read_data("data/library.csv")
books = fill_na(books)
books = remove_characters(books, "Book checkout")
books = convert_string_to_date(books, "Book checkout")
books = convert_string_to_date(books, "Book Returned")
books = remove_na(books)
books =  find_days_df(books,"Book Returned", "Book checkout" )  

print(books)


#clear duplicates


clean_books = books.drop_duplicates()
print(books.duplicated().sum())



