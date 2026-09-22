import pandas as pd

# pd.set_option("display.width", 200)
# pd.set_option("display.max_columns", 20)

books = pd.read_csv("data/library.csv")
# print(books)

#replace NaN cells
new_books = books.fillna("missing_value")

#remove NaN cells
dropna_books = books.dropna(how="any")

#fix datatypes
books["New Book checkout"] = pd.to_datetime(books["Book checkout"], errors="coerce", dayfirst=True)
print(books.dtypes)

#fix incorrectly inputted data
# new_book_checkout = pd.to_datetime(books["Book checkout"], errors="coerce", dayfirst=True)

#clear duplicates
clean_books = books.drop_duplicates()
print(clean_books)


