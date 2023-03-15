# Dataworkshop

Konkurs [Kaggle](https://www.kaggle.com/competitions/dataworkshop-credit-score
) był realizowany w ramach kursu "Praktyczne uczenie maszynowe dla programistów" (http://dataworkshop.eu/).

## Skoring kredytowy

Metryka sukcesu: **AUC**

### Dane:

* customer_id - ID klienta
* b_id - ID nieznane
* b_request_date - data czegość
* date_confirmed - data potwierdzenia
* contract_type - rodzaj umowy
* contract_status - status umowy
* conract_open_date - data podpisanie umowy
* final_payment_date - data ostatnie raty
* real_date_closed_account - faktyczna data zamknięcia konta
* cred_limit - limit kredytu
* cur - waluta
* cur_debt - bieżący dług
* next_payment - następna opłata
* cur_balance - balnas
* duration_debt_days - spóźnieni opłaty (w dniach)
* cnt_delay_upto_5d - ile razy spóźniony do 5 dni
* cnt_delay_5d_29d - ile razy spóźniony od 5 do 29 dni
* cnt_delay_upto_30d - ile razy spóźniony do 30 dni
* cnt_delay_30d_59d - ile razy spóźniony od 30 do 59 dni
* cnt_delay_60d_89d - ile razy spóźniony od 60 do 89 dni
* cnt_delay_upto_90d - ile razy spóźniony ponad 90 dni
* str_start - kod magicznej liczby
* trustability_code - zaszyfrowana wiarygodnosć klienta
* cur_overdue_debt - obecny dług
* max_amount_debt - maksymalny dług
* interest_rate_loan - stopa procentowa
* code_frequency_payments - kod płacenia
* code_relationship_contract - rodzaj relacji umowy
* is_bad - zmienna docelowa

### Struktura:

* data - folder z danymi surowymi oraz przetworzonymi
	* dla osób z kursu, które mają dostęp do danych do folderu data należy wrzucić pliki o nazwach train.raw.h5 oraz test.raw.h5 z danymi surowymi
* scripts - folder ze skryptami pomocniczymi
	* init0 + init - wczytywanie bibliotek
	* load_data - szybkie wczytywanie danych
	* my_functions - moje funkcje (aby nie zaśmiecać notebooków)
* notebooks - folder z workbookami jupytera
	* dp_01_rename_retype - wczytanie danych
	* dp_02_outliers - analiza wartości odstających
	* dp_03_primary_fe - wstępne features enginering
	* model_01 - wstępny model
	
### Co zrobiłem?

1. Wczytałem dane surowe i oczyściłem tak aby było możliwa ich dalsza analiza
2. Usunąłem outliery (o ile cecha nie obejmowała zbioru testowego, to usuwałem próbki ze zbioru)
3. Przeanalizowałem zmienne i utworzyłem kilka nowych zmiennych, które od razu się nasunęły + binaryzacja kategorii
4. Z uwagi na nierównomierny rozkład w zmiennej is_bad skupiłem się na parametrze class_weight dla catboota - wstępnie zadziałało

### Do rozważenia:

* optymalizacja parametrów
* praca na prawdopodobieństwach i przetestowanie jaki parametr podziału byłby najlepszy (ustalenie dla jakich prawdopodobieństw obserwacja zostaje włączona do is_bad = 0, a dla jakich is_bad = 1).
* usprawnienie o sieci neuronowe
* wylosowanie podzbioru, który zniweluje różnice w klasach (np. tak aby każda obserwacja miała różne customer_id). Wstępne wyniki dawały około 55%, ale z uwagi na znacznie mniejszy zbiór (~20k) metody typu boosting już nie działały tak dobrze.
