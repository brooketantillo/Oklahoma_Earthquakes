import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ok_inj_wells = './InjectionWells.csv'
ok_eqs = './okQuakes.csv'

ok_inj_wells_df = pd.read_csv(ok_inj_wells)
ok_eqs_df = pd.read_csv(ok_eqs)

ok_eqs_df.dropna()
ok_eqs_df

ok_eqs_df.drop_duplicates()
ok_eqs_df

ok_inj_wells_df