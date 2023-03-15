
# %%writefile scripts/load_data.py

import sys
import pandas as pd

dp_type = ['raw']
path_to_data = '../data/'

if len(sys.argv) == 1:
    print('Nie można wczytać danych, ponieważ nie przekazano żadnego parametru.')
else:
    dp_type = sys.argv[1]
    
    if dp_type == 'raw':
        train = pd.read_hdf(path_to_data + 'train.raw.h5')
        test = pd.read_hdf(path_to_data + 'test.raw.h5')
        print("Zmienne: train + test. Pomyślnie wczytano dane surowe!")
    elif dp_type == 'base':
        data = pd.read_hdf(path_to_data + 'data.base.h5', 'base')
        print("Zmienne: data. Pomyślnie wczytano dane podstawowe (dane raw przekształcone do formy używalnej). Dodatkowo zmieniono nazwy niektórych zmiennych, tak aby łatwiej było je grupować.")
    elif dp_type == 'base_wo':
        data = pd.read_hdf(path_to_data + '/data.base_wo.h5', 'base_wo')
        print("zmienne: data. Pomyślnie wczytano dane podstawowe bez wartości odstających")
    elif dp_type == 'base_wo_with_primary_fe':
        data = pd.read_hdf(path_to_data + '/data.base_wo_with_primary_fe.h5', 'base_wo_with_primary_fe')
        print("Zmienne: data. Pomyślnie wczytano dane z wstępnie przygotowanymi zmiennymi do analizy")
    else:
        print("Podany typ nie został zdefiniowany. Sprawdź, czy nie ma przypadkiem jakiejś literówki...")