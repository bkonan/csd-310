import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="botiwaK",
    password="password",
    database="WillsonFinancial"
)
cursor = conn.cursor()

# Report: Average Client Assets
cursor.execute("""
    SELECT AVG(Value) AS AverageAssets
    FROM Assets
""")
avg_assets = cursor.fetchall()
print("Average Client Assets Report:")
for row in avg_assets:
    print(row)

# Close connection
conn.close()