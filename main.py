import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import matplotlib.pyplot as plt


df_data = pd.read_csv('NLSY97_subset.csv')
new_df = pd.DataFrame(df_data ,columns= [df_data.Organisation, df_data.Location, df_data.Date, df_data.Price, df_data.Mission_Status])

print(new_df)
print(df_data.columns)
