import pandas as pd
import json


with open('/Users/bellavg/PycharmProjects/DIG_FACT/benchmark_dataset/data_merging_and_processing/original_datafiles/CongressionalTwitterNetwork/congress_network_data.json', 'r') as file:
    network_data = json.load(file)[0]

df = pd.read_csv("/Users/bellavg/PycharmProjects/DIG_FACT/benchmark_dataset/encoded_data.csv")

print(df.columns)
# Prepare a dictionary to hold all the data
username_to_id_mapping = {username: i for i, username in enumerate(network_data['usernameList'])}

id_to_username_mapping = {i: username for username, i in username_to_id_mapping.items()}

# Map usernames in the DataFrame to their numeric IDs
df['numeric_id'] = df['twitter'].map(username_to_id_mapping)

# Now, df contains a new column 'numeric_id' with the corresponding numeric ID for each username
# You can check the first few rows to verify
print(df.head())
df = df.drop("Unnamed: 0", axis=1)
# Optionally, save the updated DataFrame to a new CSV file
df.to_csv("/Users/bellavg/PycharmProjects/DIG_FACT/benchmark_dataset/encoded_data.csv", index=False)