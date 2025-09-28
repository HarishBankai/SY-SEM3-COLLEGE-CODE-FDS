import pandas as pd
from scipy import stats

df = pd.read_csv("/content/student-mat(1).csv", sep=";")

male_scores = df[df["sex"] == "M"]["G3"]
female_scores = df[df["sex"] == "F"]["G3"]

t_stat, p_val_ttest = stats.ttest_ind(male_scores, female_scores)

print("T-test Results (Gender vs Math Score G3):")
print(f"t-statistic = {t_stat:.4f}, p-value = {p_val_ttest:.4f}")
if p_val_ttest < 0.05:
	print("=> Significant difference between male and female scores.\n")
else:
	print("=> No significant difference between male and female scores.\n")

def categorize_performance(score):
	if score < 10:
		return "Low"
	elif 10 <= score < 15:
		return "Medium"
	else:
		return "High"

df["Performance"] = df["G3"].apply(categorize_performance)

crosstab = pd.crosstab(df["Medu"], df["Performance"])

chi2, p_val_chi, dof, expected = stats.chi2_contingency(crosstab)

print("Chi-square Test Results (Mother's Education vs Performance):")

print(f"Chi-square statistic = {chi2:.4f}, p-value = {p_val_chi:.6f}")
if p_val_chi < 0.05:
	print("=> Significant relationship between parental education and student performance.")
else:
	print("=> No significant relationship between parental education and student performance.")

import pandas as pd
df = pd.read_csv("/content/student-mat(1).csv", sep=";")

print("Dataset Loaded Successfully!\n")
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\n Summary Statistics:")

print(df.describe())
