import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('C:\\Users\\APURV\\OneDrive\\Desktop\\rainfall_in_india.csv')
profile = ProfileReport(df, title="Profiling Report",explorative=True, plot={"correlation": {"cmap": "RdBu_r", "bad": "#000000"}})
profile.to_file(output_file='rainfall.html')