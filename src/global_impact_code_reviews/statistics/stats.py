import pandas as pd
import os

# Create directories to store the results
if not os.path.exists('by_participants'):
    os.makedirs('by_participants')

if not os.path.exists('by_country'):
    os.makedirs('by_country')

if not os.path.exists('by_affiliation'):
    os.makedirs('by_affiliation')

if not os.path.exists('by_affiliation_country'):
    os.makedirs('by_affiliation_country')

file_path = 'output_file.csv'

columns_to_extract = ['ownername', 'reponame', 'lifetime_minutes', 'mergetime_minutes', 'num_commits', 'num_commit_comments', 
                      'num_issue_comments', 'num_comments', 'num_participants', 'team_size', 'requester_succ_rate', 
                      'first_response_time', 'core_member', 'contrib_country', 'contrib_affiliation', 'inte_country', 'inte_affiliation', 
                      'same_country', 'same_affiliation', 'contrib_rate_author']

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Extract the specified columns
selected_columns = df[columns_to_extract]
print("Total number of projects: ", selected_columns.shape[0])

# compute statistics
stats = selected_columns.describe()
print(stats)

# Statistics for projects where the contributor and integrator come from the same country
same_country = selected_columns[selected_columns['same_country'] == 1]
print("Number of projects where contributor and integrator come from the same country: ", same_country.shape[0], ", percentage: ", same_country.shape[0]/selected_columns.shape[0] * 100, "%")
print(same_country.describe())

# Statistics for projects where the contributor and integrator come from different countries
not_same_country = selected_columns[selected_columns['same_country'] != 1]
print("Number of projects where contributor and integrator come from different countries: ", not_same_country.shape[0], ", percentage: ", not_same_country.shape[0]/selected_columns.shape[0] * 100, "%")
print(not_same_country.describe())

# Statistics for projects where the contributor and integrator come from the same affiliation
same_affiliation = selected_columns[selected_columns['same_affiliation'] == 0]
print("Number of projects where contributor and integrator come from the same affiliation: ", same_affiliation.shape[0], ", percentage: ", same_affiliation.shape[0]/selected_columns.shape[0] * 100, "%")
print(same_country.describe())

# Statistics for projects where the contributor and integrator come from different affiliations
not_same_affiliation = selected_columns[selected_columns['same_affiliation'] != 0]
print("Number of projects where contributor and integrator come from different affiliations: ", not_same_affiliation.shape[0], ", percentage: ", not_same_affiliation.shape[0]/selected_columns.shape[0] * 100, "%")
print(not_same_affiliation.describe())

# Statistics for projects where the contributor and integrator come from the same affiliation and country
same_affiliation_country = selected_columns[(selected_columns['same_affiliation'] == 1) & (selected_columns['same_country'] == 1)]
print("Number of projects where contributor and integrator come from the same affiliation and country: ", same_affiliation_country.shape[0], ", percentage: ", same_affiliation_country.shape[0]/selected_columns.shape[0] * 100, "%")
print(same_affiliation_country.describe())

# save to file
stats.describe().to_csv('stats_general.csv')
same_country.describe().to_csv('by_country/same_country.csv')
not_same_country.describe().to_csv('by_country/not_same_country.csv')
same_affiliation.describe().to_csv('by_affiliation/same_affiliation.csv')
not_same_affiliation.describe().to_csv('by_affiliation/not_same_affiliation.csv')
same_affiliation_country.describe().to_csv('by_affiliation_country/same_affiliation_country.csv')

# Number of participants delimitations
low_limit = 10
medium_limit = 20

# split dataset by the number of participants
low_participants = selected_columns[selected_columns['num_participants'] < low_limit]
print("Number of projects with low number of participants: ", low_participants.shape[0], ", percentage: ", low_participants.shape[0]/selected_columns.shape[0] * 100, "%")
print(low_participants.describe())
low_participants.describe().to_csv('by_participants/low_participants.csv')

medium_participants = selected_columns[(selected_columns['num_participants'] >= low_limit) & (selected_columns['num_participants'] < medium_limit)]
print("Number of projects with medium number of participants: ", medium_participants.shape[0], ", percentage: ", medium_participants.shape[0]/selected_columns.shape[0] * 100, "%")
print(medium_participants.describe())
medium_participants.describe().to_csv('by_participants/medium_participants.csv')

high_participants = selected_columns[(selected_columns['num_participants'] >= medium_limit)]
print("Number of projects with high number of participants: ", high_participants.shape[0], ", percentage: ", high_participants.shape[0]/selected_columns.shape[0] * 100, "%")
print(high_participants.describe())
high_participants.describe().to_csv('by_participants/high_participants.csv')

