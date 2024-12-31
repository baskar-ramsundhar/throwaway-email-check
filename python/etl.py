import pandas as pd
from datetime import datetime
from utils import is_throwaway, hash_email, load_config # Referencing functions from the common utils

# --- Configuration ---
CONFIG = load_config()
API_URL = CONFIG["api_url"]
INPUT_CSV = CONFIG["input_csv"]
HASH_EMAILS = CONFIG.get("hash_emails", False) # Default to False if not specified
OUTPUT_FILEPATH = CONFIG["output_csv"]

# --- Main ETL Function ---

def process_emails(input_filepath):
    
    try:
        df = pd.read_csv(input_filepath, header=None, names=["EMAIL"])

        # Creation of columns for resulting dataframe
        df["THROWAWAYSTATUS"] = None
        df["CHECKEDDATETIME"] = None
        # If the email hashing is required then hashed_email column is created within the resulting dataframe
        if HASH_EMAILS: 
            df["HASHEDEMAIL"] = None

        #Looping through the dataframe records

        for index, row in df.iterrows():
            email = row["EMAIL"]
            #Response captured within throwaway variable
            throwaway = is_throwaway(email, API_URL)
            
            #Updating is_throwaway status and date 

            df.loc[index, "THROWAWAYSTATUS"] = throwaway
            df.loc[index, "CHECKEDDATETIME"] = datetime.now()

            #Updating hashed email value

            if HASH_EMAILS:
                df.loc[index, "HASHEDEMAIL"] = hash_email(email)

        return df

    except FileNotFoundError:
        print(f"Error: File not found at {input_filepath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# --- Main Execution ---

if __name__ == "__main__":
    output_df = process_emails(INPUT_CSV)

    if output_df is not None:
        print("Data processed successfully.")
        # Further actions to save to CSV or load into a database can be added here.
        output_df.to_csv(OUTPUT_FILEPATH, index=False) 
        print(output_df)