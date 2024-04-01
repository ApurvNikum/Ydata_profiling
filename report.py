import seaborn as sns

import pandas as pd
from ydata_profiling import ProfileReport,compare

train_df = pd.read_csv("C:\\Users\\APURV\\Downloads\\penguins.csv")
train_report = ProfileReport(train_df, title="Train")

test_df = pd.read_csv("C:\\Users\\APURV\\Downloads\\titanic.csv")
test_report = ProfileReport(test_df, title="Test")

comparison_report = train_report.compare(test_report)
comparison_report.to_file("comparison.html")

