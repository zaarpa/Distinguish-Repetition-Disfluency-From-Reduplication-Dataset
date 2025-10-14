import pandas as pd

# Load the main CSV
main_df = pd.read_csv('test_data.csv')

# Filter rows where main_category is 'Reduplication'
reduplication_df = main_df[main_df['main_category'] == 'Reduplication']

# Save the filtered rows to a new CSV
reduplication_df.to_csv('test_reduplication_only.csv', index=False)

print("Filtered CSV saved as 'test_reduplication_only.csv'")
