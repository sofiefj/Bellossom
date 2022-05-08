# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:22:01 2022

@author: Sofie
"""

# Koden til hoggorm er tilgjengelig fra https://github.com/olivertomic/hoggorm

# Importere nødvendige pakker
import hoggorm as ho
import hoggormplot as hop
import pandas as pd
import numpy as np
import seaborn as sns

# Importere PET- og CT-grupper
pet4 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/PET_4.csv'))
pet8 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/PET_8.csv'))
pet16 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/PET_16.csv'))
ct16 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/CT_16_w.csv'))
ct32 = pd.DataFrame(pd.read_csv('C:/Users/Sofie/Documents/GitHub/imskaper/features_extraction/CT_32_w.csv'))

# Fjerne formegenskaper fra gruppene
pet4 = pet4.iloc[:,15:].values
pet8 = pet8.iloc[:,15:].values
pet16 = pet16.iloc[:,15:].values
ct16 = ct16.iloc[:,15:].values
ct32 = ct32.iloc[:,15:].values

# Standardisering av egenskaper i de ulike gruppene
standp4 = ho.standardise(pet4, mode=0)
standp8 = ho.standardise(pet8, mode=0)
standp16 = ho.standardise(pet16, mode=0)
standc16 = ho.standardise(ct16, mode = 0)
standc32 = ho.standardise(ct32, mode = 0)

# Utregining av rv-matrise for PET-gruppene, og visualisering av resultat
rv_results_stand_p = ho.RVcoeff([standp4, standp8, standp16])
res_p = pd.DataFrame(rv_results_stand_p)
label = ['4', '8', '16']
res_p.columns = label
res_p.index = label
sns.heatmap(res_p, annot = True)

# Utregining av RV-matrise for CT-gruppene, og visualisering av resultat
rv_results_stand_c = ho.RVcoeff([standc16, standc32])
res_c = pd.DataFrame(rv_results_stand_c)
label = ['16', '32']
res_c.columns = label
res_c.index = label
sns.heatmap(res, annot = True)
