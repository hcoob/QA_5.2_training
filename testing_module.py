import pytest
import unittest
import pandas as pd



from cleaning_module_exc import remove_na, remove_characters, convert_string_to_date, drop_duplicates, find_days_df

# @pytest.fixture


def test_remove_na():
    input_df = pd.read_csv("data/library.csv")
    count_before = len(input_df)
    res = remove_na(input_df)
    count_after = len(res)

    # self.assertEqual(count_after, count_before )
    assert count_before > count_after


try:
    test_remove_na()
except AssertionError as e:
    print(e.message)


# test data in the wrong format

def test_convert_string_to_date():
    input_df = pd.DataFrame({
        'ID': [1,2,3],
        'Date': ['"20/02/2023"', '"20/01/2023"', '"20/02/2026"']
    })

    output_df = remove_characters(input_df, 'Date')
    output_df = convert_string_to_date(output_df, 'Date')

    assert output_df['Date'].dtype == 'datetime64[us]'

try:
    test_convert_string_to_date()
except AssertionError as e:
    print(e.message)
   


def test_drop_duplicates():
    input_df = pd.DataFrame({
        'ID': [1,2,3,4],
        'Date': ['20/02/2023', '20/01/2023', '01/02/2026','01/02/2026'],
        'Book': ['Book_1', 'Book_2', 'Book_3', 'Book_3']
    })

    count_1 = len(input_df)
    output_df = drop_duplicates(input_df, 'Date')
    count_2 = len(output_df)

    assert count_1 > count_2


try: 
    test_drop_duplicates()
except AssertionError as e:
    print(e.message)

#this is not working
def test_find_days_df():
    input_df = pd.DataFrame({
        'Date_1': ['2023-02-20'],
        'Date_2': ['2023-02-21']
    })

    input_df['Date_1'] = pd.to_datetime(input_df['Date_1'])
    input_df['Date_2'] = pd.to_datetime(input_df['Date_2'])
    output_df = find_days_df(input_df, 'Date_2', 'Date_1')
    assert output_df['diff'] == [1]


try: 
    test_find_days_df()
except AssertionError as e:
    print(e.message)

