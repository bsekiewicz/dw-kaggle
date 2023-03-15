# %%writefile scripts/my_functions_01.py

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt


# detekcja lepszych typów zmiennych dla kolumn
# zdaję sobie sprawę, że można to zrobić 'zgrabniej'
# trzeba bardzo uważać na późniejsze operacje !!!

# int8 Byte (-128 to 127)
# int16 Integer (-32768 to 32767)
# int32 Integer (-2147483648 to 2147483647)
# int64 Integer (-9223372036854775808 to 9223372036854775807)
# uint8 Unsigned integer (0 to 255)
# uint16 Unsigned integer (0 to 65535)
# uint32 Unsigned integer (0 to 4294967295)
# uint64 Unsigned integer (0 to 18446744073709551615)

def detect_col_type(column):
    security_value = 1.1 # +10% bezpieczeństwa
    col_type = column.dtype
    
    if col_type == 'bool':
        new_col_type = col_type
        
        print(column.name + "(" + str(col_type) + "): typ " + str(col_type) + " jest OK!")

    elif col_type == 'int':
        if np.min(column) >= 0: #uint
            tmp_border = int(np.max(column)*security_value)

            if tmp_border <= 1:
                new_col_type = 'bool'
            elif tmp_border < 250:
                new_col_type = 'uint8'
            elif tmp_border < 65500:
                new_col_type = 'uint16'
            elif tmp_border < 4294967000:
                new_col_type = 'uint32'
            else:
                new_col_type = 'uint64'
        else:
            tmp_border = int(np.max([np.abs(np.min(column)),np.max(column)])*security_value)

            if tmp_border < 125:
                new_col_type = 'int8'
            elif tmp_border < 32700:
                new_col_type = 'int16'
            elif tmp_border < 2147483600:
                new_col_type = 'int32'
            else:
                new_col_type = 'int64'

        if col_type == new_col_type:
            print(column.name + "(" + str(col_type) + "): typ " + str(col_type) + " jest OK!")
        else:
            print(column.name + "(" + str(col_type) + "): wykryto bardziej odpowiedni typ: " + new_col_type)
 
    elif (col_type == 'uint8') | (col_type == 'uint16') | (col_type == 'uint32') | (col_type == 'uint64'):
        tmp_border = int(np.max(np.max(column))*security_value)

        if tmp_border <= 1:
            new_col_type = 'bool'
        elif tmp_border < 250:
            new_col_type = 'uint8'
        elif tmp_border < 65500:
            new_col_type = 'uint16'
        elif tmp_border < 4294967000:
            new_col_type = 'uint32'
        else:
            new_col_type = 'uint64'

        if col_type == new_col_type:
            print(column.name + "(" + str(col_type) + "): typ " + str(col_type) + " jest OK!")
        else:
            print(column.name + "(" + str(col_type) + "): wykryto bardziej odpowiedni typ: " + new_col_type)
            
    elif col_type == 'float':
        new_col_type = col_type # float to jeszcze niezrozumiała dla mnie rzecz
                                    # lepiej nie ruszać
                                    # potrafi zaburzyć wartości nawet o kilka punktów
                
        if column[column.isnull()].size == 0: # możemy jedynie sprawdzić, czy to nie są aby int
            tmp_dec = column % 1
        
            if tmp_dec[(tmp_dec > 0) & \
                       (tmp_dec < 1)].size == 0:
                                   
                if np.min(column) >= 0: #uint
                    tmp_border = int(np.max(column)*security_value)

                    if tmp_border <= 1:
                        new_col_type = 'bool'
                    elif tmp_border < 250:
                        new_col_type = 'uint8'
                    elif tmp_border < 65500:
                        new_col_type = 'uint16'
                    elif tmp_border < 4294967000:
                        new_col_type = 'uint32'
                    else:
                        new_col_type = 'uint64'
                else:
                    tmp_border = int(np.max([np.abs(np.min(column)),np.max(column)])*security_value)

                    if tmp_border < 125:
                        new_col_type = 'int8'
                    elif tmp_border < 32700:
                        new_col_type = 'int16'
                    elif tmp_border < 2147483600:
                        new_col_type = 'int32'
                    else:
                        new_col_type = 'int64'

        if col_type == new_col_type:
            print(column.name + "(" + str(col_type) + "): typ " + str(col_type) + " jest OK! - na razie nie ruszam float64")
        else:
            print(column.name + "(" + str(col_type) + "): wykryto bardziej odpowiedni typ: " + new_col_type)
    
    elif col_type == 'O':
        
        # sprawdzamy, czy liczby w postaci stringa
        tmp_nondigits = column.map(lambda x: None if str(x) == "nan" else re.search('[^0-9.-]+', str(x)))
        
        if tmp_nondigits.notnull().sum() == 0:
            
            if column[column.isnull()].size == 0: # możemy jedynie sprawdzić, czy to nie są aby int
                tmp_dec = column % 1

                if tmp_dec[(tmp_dec > 0) & \
                           (tmp_dec < 1)].size == 0:

                    if np.min(column) >= 0: #uint
                        tmp_border = int(np.max(column)*security_value)

                        if tmp_border <= 1:
                            new_col_type = 'bool'
                        elif tmp_border < 250:
                            new_col_type = 'uint8'
                        elif tmp_border < 65500:
                            new_col_type = 'uint16'
                        elif tmp_border < 4294967000:
                            new_col_type = 'uint32'
                        else:
                            new_col_type = 'uint64'
                    else:
                        tmp_border = int(np.max([np.abs(np.min(column)),np.max(column)])*security_value)

                        if tmp_border < 125:
                            new_col_type = 'int8'
                        elif tmp_border < 32700:
                            new_col_type = 'int16'
                        elif tmp_border < 2147483600:
                            new_col_type = 'int32'
                        else:
                            new_col_type = 'int64'
                else:
                    new_col_type = 'float64'
            else:
                new_col_type = 'float64'
            
        else:
            new_col_type = col_type
            
        if col_type == new_col_type:
            print(column.name + "(" + str(col_type) + "): typ " + str(col_type) + " jest OK! - znaleziono znaki nie będące liczbami ani kropką!")
        else:
            print(column.name + "(" + str(col_type) + "): wykryto bardziej odpowiedni typ: " + new_col_type)
         
    else:
        new_col_type = col_type
        print(column.name + "(" + str(col_type) + "): typ nie jest obsługiwany!")
        
    return(new_col_type)

################
################
################

# wykrywanie anomalii (zbyt dużej liczby wartości zerowych oraz ostre zmiany wartości

def anomalies_summary(column, is_category = False):
    col_type = column.dtype
    n = len(column)
    n_distinct = len(column.unique())

    n_nan = column.isnull().sum()
    p_nan = np.round(n_nan/n, 3)
    n_inf = column[column == np.inf].count()
    p_inf = np.round(n_inf/n, 3)
    
    if col_type == 'O':
        n_blank = column[column == ''].count()
        p_blank = np.round(n_blank/n, 3)
        n_neg = 0
        p_neg = 0
        n_zero = 0
        p_zero = 0
        
        max_val_change = np.nan
    else:
        n_blank = 0
        p_blank = 0
        n_neg = column[column<0].count()
        p_neg = np.round(n_neg/n, 3)
        if is_category:
            n_zero = column[column == np.max([0,np.min(column)])].count()
        else:
            n_zero = column[column == 0].count()
        p_zero = np.round(n_zero/n, 3)
        
        val_change = []
        tmp = sorted(column[column>0].unique())
        if len(tmp) > 1:
            for i in range(1,len(tmp)):
                val_change.append([tmp[i-1]/tmp[i]])
            max_val_change = np.round(np.min(val_change),3)
        else:
            max_val_change = np.nan
            
    summary = pd.DataFrame(data={'col_name': [column.name], 
              'n': [n],
              'n_nan': [n_nan],
              'p_nan': [p_nan],
              'n_neg': [n_neg],
              'p_neg': [p_neg],
              'n_zero': [n_zero],
              'p_zero': [p_zero],
              'n_inf': [n_inf],
              'p_inf': [p_inf],
              'n_blank': [n_blank],
              'p_blank': [p_blank],
              'n_distinct': [n_distinct],
              'col_type': [str(col_type)],
              'sum_of_p': [p_nan+p_zero+p_blank+p_inf],
              'max_val_change': [max_val_change],
             }, columns = ['col_name', 'n', 'n_nan', 'p_nan', 'n_neg', 'p_neg', 'n_zero', 'p_zero', 'n_inf', 'p_inf', 'n_blank', 'p_blank', 'n_distinct', 'col_type', 'max_val_change', 'sum_of_p'])
    
    return(summary)

################
################
################

# zmiana procentowa i tej wartości do i+1 (wektor posortowany rosnąco)

def plot_anomalies_max_val_change(column, uniqe = True):
    col_type = column.dtype
    val_change = []
    
    if (col_type != 'O') & (col_type != 'bool'):
        if uniqe:
            tmp = sorted(column[column>0].unique())
        else:
            tmp = sorted(column[column>0])
        
        if len(tmp) > 1:
            for i in range(1,len(tmp)):
                val_change.append([tmp[i-1]/tmp[i]])
                
    if len(val_change) > 0:
        plt.title(column.name)
        plt.ylim([0,1.1])
        plt.plot(val_change)
        plt.show()
        
        if len(column.unique()) < 15:
            print(column.name+'('+str(col_type)+'): UWAGA!!! zmienna posiada '+str(len(column.unique()))+' różnych wartości. Wykres nie ma sensu dla zmiennych kategorialnych.')
    else:
        print(column.name+'('+str(col_type)+'): nie można narysować wykresu dla tego typu.')

################
################
################

# konwersja wartości liczbowej na datę

def xldate_to_date(xldate):
    if np.isnan(xldate):
        res = np.nan
    else:
        res = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(xldate) - 2)
    # res.timetuple()
    return res

print("Wczytano funkcje użytkownika!")