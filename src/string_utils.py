import pandas as pd

def clean_strings(strings):
    temp = strings
    temp = temp.str.strip()
    temp = temp.str.lower()
    temp = temp.dropna()
    temp = temp.str.replace(r'\W', '', regex=True)
    return temp


one = pd.Series(['hello??','H!!!   ', None])
two = pd.Series(['hello','h'])
assert clean_strings(one).equals(two) #unit testing