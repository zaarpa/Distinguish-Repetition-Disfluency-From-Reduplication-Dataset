import pandas as pd

# Load the main CSV
main_df = pd.read_csv('Repitition vs Reduplication Categorization Dataset.csv')

# Filter rows where main_category is 'Reduplication'
reduplication_df = main_df[main_df['main_category'] == 'Reduplication']

# Save the filtered rows to a new CSV
reduplication_df.to_csv('reduplication_only.csv', index=False)

print("Filtered CSV saved as 'reduplication_only.csv'")
