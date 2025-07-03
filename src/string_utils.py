import pandas as pd
import numpy as np
import matplotlib as plt
import pytest
import ipykernel
import notebook
import string
import re

#TASK B
def clean_strings(strings):

    strings = strings.astype(str) #just in case there is a nonstring entity
    strings = strings.str.lower() #all lowercase
    strings = strings.str.strip()

    #punctuation_chars = ('!' , '?' , ',' ,  '.',  ',' , ';' ,  ':' , "'")
    strings = strings.str.replace(f'[{re.escape(string.punctuation)} \\\\ ]', '', regex=True)
    strings = strings.dropna() #modify the original string itself, delete blank values 

    #strings5 = strings4.str.strip()

    return strings

s = pd.Series(" #)(*&#%@ANTHONY)")

assert clean_strings(s).index[0] != "anthony", "Test Case Failed" 