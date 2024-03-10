import pandas as pd

file_path = 'new_pullreq.csv'

columns_to_extract = ['ownername', 'reponame', 'lifetime_minutes', 'mergetime_minutes', 'num_commits', 'num_commit_comments', 
                      'num_issue_comments', 'num_comments', 'num_participants', 'team_size', 'requester_succ_rate', 
                      'first_response_time', 'core_member', 'contrib_country', 'contrib_affiliation', 'inte_country', 'inte_affiliation', 
                      'same_country', 'same_affiliation', 'contrib_rate_author']

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Extract the specified columns
selected_columns = df[columns_to_extract]

# Save to file
selected_columns.to_csv('output_file.csv', index=False)

# Projects with a higher number of contributors will exhibit shorter review speeds due to increased resources and manpower facilitating quicker feedback cycles.
# Teams predominantly composed of members sharing a common language and cultural background will experience faster review speeds compared to those with diverse linguistic and cultural compositions, as language barriers and cultural differences are mitigated.