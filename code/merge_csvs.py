import pandas as pd

# Load the CSV files
sub_df = pd.read_csv('Reduplication_SubCategory.csv')
main_df = pd.read_csv('Repitition vs Reduplication Categorization Dataset.csv')

# Create a dictionary for faster lookup: sentence -> predicted_sub_category
sub_dict = dict(zip(sub_df['sentence'], sub_df['predicted_sub_category']))

# Function to get predicted_sub_category if main_category is Reduplication
def get_sub_category(row):
    if row['main_category'] == 'Reduplication':
        return sub_dict.get(row['sentence'], '')
    else:
        return ''

# Apply the function to create a new column
main_df['sub_category'] = main_df.apply(get_sub_category, axis=1)

# Save the updated CSV
main_df.to_csv('main_category_updated.csv', index=False)

print("CSV updated and saved as 'main_category_updated.csv'")
