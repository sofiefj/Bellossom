# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 08:22:21 2022

@author: Sofie
"""

# Importere pandas
import pandas as pd


# Importere datasett
CT_16 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/CT_16_w.csv'))
PET_4 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/PET_4.csv'))
PET_8 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/PET_8.csv'))

# Fjerne bildenavn fra egenskaper
CT_16=CT_16.drop(('Name'), axis=1)
PET_8=PET_8.drop(('Name'), axis=1)
PET_4=PET_4.drop(('Name'), axis=1)


# Endre variabelnavn slik at hvilket sett det kommer fra blir tydelig
CT_16_w=CT_16_w.add_suffix('CT_16_w')
PET_4=PET_4.add_suffix('PET_4')
PET_8=PET_8.add_suffix('PET_8')

# Fjerne eventuelle duplikatverdier i CT_16_w
CT_df = CT_df_w.T.drop_duplicates(keep = 'first').T

# Slå sammen PET_8 og PET_4, og fjerne eventuelle duplikatverdier
PET_df = pd.concat([PET_8, PET_4], axis=1)
PET_df = PET_df.T.drop_duplicates(keep = 'first').T

# importere kliniske data og endre index
klin_df = pd.read_csv('clin_ous.csv')
klin_df = klin_df.set_index(('patient_id'))

# importere PET-parametere og endre index
pet_params_df = pd.read_excel('data/tabular_data/ous/pet_parameters_ous.xlsx')
pet_params_df = pd.DataFrame(pet_params_df)
pet_params_df = pet_params_df.set_index(('patient_id'))

# Sette ny index for PET_df og CT_df
CT_df = CT_df.set_index((pet_params_df.index))
PET_df = PET_df.set_index((pet_params_df.index))

# Sette sammen til fullt datasett og lagre som csv
full_df =  pd.concat([CT_df, PET_df, pet_params_df, klin_df], axis=1)
full_df = full_df.T.drop_duplicates().T

full_df.to_csv('fullt_datasett_ous.csv')
