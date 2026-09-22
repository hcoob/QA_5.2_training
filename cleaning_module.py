import pandas as pd

# pd.set_option("display.width", 200)
# pd.set_option("display.max_columns", 20)

books = pd.read_csv("data/library.csv")
# print(books.head())

customers = pd.read_csv("data/library_customers.csv")
# print(customers.head())

print(books.shape)
books.columns.tolist()
quant = len(books.to_string().splitlines())



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



# loc value vs iloc index
# books.loc('id')
output = books.loc[books.isnull().all(axis=1)].to_string()
print(output)

dropeed_na = books.dropna(how=all)
dropeed_na.shape
dropeed_na.isna.sum() #count for present na values
books.isna.sum()

filled_value = books.fillna("value")

filled_value.isnull().sum().sum()
filled_value["customer"].tolist[-1]
filled_value["Books"].tolist()
filled_value["Books"].mean()
books.drop_duplicated #returns true false for every eow its seen before

dropeed_na.duplicated().sum() # agg of true returns

deduped_dropped_na = dropeed_na.drop_duplicates(subset='col')
deduped_dropped_na.shape
deduped_dropped_na.describe().mean()