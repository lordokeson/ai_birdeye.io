import pandas as pd
from sqlalchemy import create_engine

# Define connection string to Snowflake
connection_string = "snowflake://user:password@account.aws/database.schema"

# Define path to CSV file
data_path = "path/to/your/sales_data.csv"

# Read data from CSV file
df = pd.read_csv(data_path)

# Clean and transform data (replace with your specific logic)
df["date"] = pd.to_datetime(df["date"])
df["sales_amount"] = df["sales_amount"].astype(float)

# Connect to Snowflake
engine = create_engine(connection_string)

# Define table name
table_name = "sales_data"

# Load data to Snowflake table
df.to_sql(table_name, engine, index=False)

print(f"Data successfully loaded to {table_name} table in Snowflake!")

