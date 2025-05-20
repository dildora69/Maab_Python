import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("chinook.db")

# Load invoices with customer info
query1 = """
SELECT Invoice.CustomerId, Customer.FirstName || ' ' || Customer.LastName AS Name, Invoice.Total
FROM Invoice
JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
"""
df = pd.read_sql(query1, conn)

# Group by customer and sum total
total_by_customer = df.groupby(['CustomerId', 'Name'])['Total'].sum().reset_index()
top5_customers = total_by_customer.sort_values(by='Total', ascending=False).head(5)
print("Top 5 Customers:\n", top5_customers)

query2 = """
SELECT Invoice.CustomerId, InvoiceLine.TrackId, Track.AlbumId
FROM Invoice
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
"""
track_df = pd.read_sql(query2, conn)

# All tracks in each album
query3 = "SELECT AlbumId, COUNT(*) AS Album_Track_Count FROM Track GROUP BY AlbumId"
album_tracks = pd.read_sql(query3, conn)

# Merge to get full album info
track_df = track_df.merge(album_tracks, on='AlbumId')

# Count unique tracks purchased by customer per album
customer_album = track_df.groupby(['CustomerId', 'AlbumId']).agg({
    'TrackId': pd.Series.nunique,
    'Album_Track_Count': 'first'
}).reset_index()

# Determine if full album was purchased
customer_album['Full_Album'] = customer_album['TrackId'] == customer_album['Album_Track_Count']

# Now check for each customer: did they ever buy a full album?
full_album_pref = customer_album.groupby('CustomerId')['Full_Album'].any().reset_index()
full_album_pref['Preference'] = full_album_pref['Full_Album'].apply(lambda x: 'Full Album' if x else 'Individual Tracks')


# Count and percentage
summary = full_album_pref['Preference'].value_counts(normalize=True) * 100
print("\nCustomer Purchase Preferences:\n", summary)
 