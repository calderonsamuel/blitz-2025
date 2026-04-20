import os
import zipfile
import pandas as pd

folder_id = '15md-m85iJesJt8M7_i5weC9UEUiurb0r'
output_path = 'data'

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Use gdown to download the entire folder contents into the specified output path
# execute at the terminal
# !gdown --folder "{folder_id}" --output "{output_path}"


# List all files in the downloaded folder
all_files = os.listdir(output_path)

zip_files = [f for f in all_files if f.endswith('.zip')]

print(f"Found {len(zip_files)} zip files to extract.")

for zip_file_name in zip_files:
    zip_file_path = os.path.join(output_path, zip_file_name)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_path)

print("Extraction process complete. Listing contents of the folder after extraction:")

os.listdir("data")


# Ensure output_path is defined (it should be from previous cells)
# output_path = '/content/downloaded_folder_xml' # Uncomment if output_path is not defined

xml_files_in_folder = [f for f in os.listdir(output_path) if f.endswith('.xml')]

all_dataframes = []

print(f"Found {len(xml_files_in_folder)} XML files to process.")

for xml_file_name in xml_files_in_folder:
    file_path = os.path.join(output_path, xml_file_name)
    try:
        # Read the XML file into a DataFrame. pandas.read_xml attempts to infer structure.
        df = pd.read_xml(file_path)
        df['filename'] = xml_file_name # Add a column for the filename
        all_dataframes.append(df)
        print(f"Successfully processed {xml_file_name}")
    except Exception as e:
        print(f"Error processing {xml_file_name}: {e}")

if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    print("\nAll XML files combined into a single DataFrame.")
else:
    print("No dataframes were created. Please check the XML files and parsing logic.")

combined_df.to_csv('data/combined.csv')
