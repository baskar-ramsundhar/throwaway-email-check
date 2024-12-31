# Throwaway Email Check

This project identifies and flags throwaway email addresses from a CSV file using a Python script and a REST API. It also includes SQL scripts for database creation, designed for a data warehouse like Snowflake.

## Project Overview

The Python script `etl.py` reads email addresses from an input CSV, checks each address against the (https://throwaway.cloud/) API, and prepares the data for loading into a data warehouse. 

The script can optionally hash email addresses using SHA256.

The SQL script in `sql/ddl` define the schema and tables to store the results.

The SQL script in 'sql/dml' contains four questions/queries 

## Prerequisites

-   Python 3.9+
-   `pip`
-   `virtualenv` or `conda`
-   Libraries: See `requirements.txt`

## Setup

1.  Clone the repository:

    ```bash
    git clone [https://github.com/baskar-ramsundhar/throwaway-email-check] throwaway-email-check
    ```

2.  Navigate to the project directory:

    ```bash
    cd throwaway-email-check
    ```

3.  Create a virtual environment:

    *   Using `venv`:

        ```bash
        python3 -m venv .venv
        ```

    *   Using `conda`:

        ```bash
        conda create -n myenv python=3.9
        ```

4.  Activate the virtual environment:

    *   `venv` on Linux/macOS:

        ```bash
        source .venv/bin/activate
        ```

    *   `venv` on Windows:

        ```bash
        .venv\Scripts\activate
        ```

    *   `conda`:

        ```bash
        conda activate myenv
        ```

5.  Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

6.  **Configuration:**

    *   Update the `config.json` file with the correct values:
        *   `api_url`: The base URL of the throwaway email API (default: `https://throwaway.cloud/api/v2`).
        *   `input_csv`: The path to your input CSV file (e.g., `data/input/email-sample.csv`).
        *   `db_schema_name`: The name of the schema in your data warehouse (default: `my_schema`).
        *   `hash_emails`: Set to `true` to hash email addresses, `false` otherwise (default: `false`).

## Run

1.  **Execute SQL scripts:** Run the SQL scripts in `sql/ddl` on your data warehouse to create the necessary schema and tables. These scripts are designed for Snowflake but can be adapted for other SQL databases.

2.  **Run the ETL script:**

    ```bash
    python python/etl.py
    ```

    The script will process the emails and print a DataFrame to the console, and will also export the dataframe to csv within `data/output/email-sample-throwaway-status.csv`. 

## Notes

*   In this project I used a simplified configuration approach for the take-home exercise. 
*   In a production environment, a more robust configuration management system (e.g., separate config files, environment variables, cloud secret stores) would be recommended.
*   The input CSV file is assumed to have no headers. The email addresses should be in the first column.
*   Error handling in the `etl.py` script is basic.  Could add more comprehensive error handling and logging for a production environment. e.g. Diffrentiation of error classification.
*   Could use the logging library to record the outcomes of the programme modules including exceptions to assist troubleshooting.
