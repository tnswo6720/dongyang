import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

# Load COMPAS dataset (Assumption: 'compas_data.csv' file is in the working directory)
dataset_path = 'compas_data.csv'
compas_data = pd.read_csv(dataset_path)

# Data preprocessing: Convert categorical data to numerical for 'sex', 'age', and 'race'
compas_data[['sex', 'age', 'race']] = compas_data[['sex', 'age', 'race']].apply(lambda x: x.astype('category').cat.codes)

# Combine 'is_violent_recid', 'is_recid', and 'event' for each gender
gender_data = compas_data.groupby('sex').agg({'is_violent_recid': 'sum', 'is_recid': 'sum', 'event': 'sum'}).reset_index()

# Melt the DataFrame for easier plotting
gender_data_melted = pd.melt(gender_data, id_vars='sex', var_name='Outcome', value_name='Frequency')

# Visualization: Bar plot for 'is_violent_recid', 'is_recid', and 'event' for each gender
plt.figure(figsize=(12, 8))
sns.barplot(x='sex', y='Frequency', hue='Outcome', data=gender_data_melted, palette='Set1')
plt.title('Incidence of Recidivism Outcomes by Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')

# Save the plot as an image file for each gender
gender_img_path = 'gender_outcomes.png'
plt.savefig(gender_img_path, format='png')
plt.close()

# Combine 'is_violent_recid', 'is_recid', and 'event' for each age group
age_data = compas_data.groupby('age').agg({'is_violent_recid': 'sum', 'is_recid': 'sum', 'event': 'sum'}).reset_index()

# Melt the DataFrame for easier plotting
age_data_melted = pd.melt(age_data, id_vars='age', var_name='Outcome', value_name='Frequency')

# Visualization: Bar plot for 'is_violent_recid', 'is_recid', and 'event' for each age group
plt.figure(figsize=(12, 8))
sns.barplot(x='age', y='Frequency', hue='Outcome', data=age_data_melted, palette='Set1')
plt.title('Incidence of Recidivism Outcomes by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Frequency')

# Save the plot as an image file for each age group
age_img_path = 'age_outcomes.png'
plt.savefig(age_img_path, format='png')
plt.close()

# Combine 'is_violent_recid', 'is_recid', and 'event' for each race
race_data = compas_data.groupby('race').agg({'is_violent_recid': 'sum', 'is_recid': 'sum', 'event': 'sum'}).reset_index()

# Melt the DataFrame for easier plotting
race_data_melted = pd.melt(race_data, id_vars='race', var_name='Outcome', value_name='Frequency')

# Visualization: Bar plot for 'is_violent_recid', 'is_recid', and 'event' for each race
plt.figure(figsize=(12, 8))
sns.barplot(x='race', y='Frequency', hue='Outcome', data=race_data_melted, palette='Set1')
plt.title('Incidence of Recidivism Outcomes by Race')
plt.xlabel('Race')
plt.ylabel('Frequency')

# Save the plot as an image file for each race
race_img_path = 'race_outcomes.png'
plt.savefig(race_img_path, format='png')
plt.close()

# HTML 파일 생성
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recidivism Outcomes</title>
</head>
<body>
    <h1>Incidence of Recidivism Outcomes</h1>

    <!-- Image for Recidivism Outcomes by Gender -->
    <img src="gender_outcomes.png" alt="Recidivism Outcomes by Gender">

    <!-- Image for Recidivism Outcomes by Age Group -->
    <img src="age_outcomes.png" alt="Recidivism Outcomes by Age Group">

    <!-- Image for Recidivism Outcomes by Race -->
    <img src="race_outcomes.png" alt="Recidivism Outcomes by Race">
</body>
</html>
"""

# HTML 파일 저장
with open('index.html', 'w') as html_file:
    html_file.write(html_content)

