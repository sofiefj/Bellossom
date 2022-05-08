# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 08:24:31 2022

@author: Sofie
"""

# Importere pandas
import pandas as pd

# Laste inn klinisk data fra OUS i en pandas dataframe
klin_df = pd.read_excel('data/tabular_data/ous/clinical_ous.xlsx')
klin_df= pd.DataFrame(klin_df)

# Sette indeks lik pasient-ID
klin_df = klin_df.set_index(('patient_id'))

# Fjerne egenskapen ECOG fra datasettet
klin_df = klin_df.drop(['ecog'], axis=1)

# Fylle manglende verdier av hpv_related og uicc8_III-IV med verdien 2.
klin_df['hpv_related'] = klin_df['hpv_related'].fillna(2)
klin_df['uicc8_III-IV'] = klin_df['uicc8_III-IV'].fillna(2)

# Lagre preprosessert klinisk data i csv-fil
klin_df.to_csv('clin.csv')
