import pandas as pd

books = pd.read_csv("data/library.csv")
# print(books.head())

customers = pd.read_csv("data/library_customers.csv")
# print(customers.head())

print(books.shape)
books.isnull().all().sum()
real = books.dropna(how="any")

print(real.shape)
print(real)


three_books = books["Id"].head(3).tolist()
print(three_books)
print(books.dtypes)

silence_the_error  = pd.to_datetime(books['Book checkout'], errors="coerce", dayfirst=True)
print(silence_the_error.dtype)
print(silence_the_error.isnull().sum())
print(silence_the_error.isna().sum())
