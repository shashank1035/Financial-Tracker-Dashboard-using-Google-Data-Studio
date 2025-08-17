import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Read CSV
df = pd.read_csv("data/transactions.csv")

# Clean Data
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = df['Amount'].astype(float)

# Upload to Google Sheets
sheet = client.open("Financial Tracker").sheet1
sheet.update([df.columns.values.tolist()] + df.values.tolist())

print("Data uploaded successfully to Google Sheets!")
