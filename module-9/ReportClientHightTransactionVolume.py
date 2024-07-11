import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="WillsonFinancial"
)
cursor = conn.cursor()

# Report: Clients with High Transaction Volume
cursor.execute("""
    SELECT c.Name, COUNT(t.TransactionID) AS TransactionCount
    FROM Clients c
    JOIN Transactions t ON c.ClientID = t.ClientID
    WHERE t.TransactionDate >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    GROUP BY c.ClientID
    HAVING TransactionCount > 10
""")
high_volume_clients = cursor.fetchall()
print("Clients with High Transaction Volume Report:")
for row in high_volume_clients:
    print(row)

# Close connection
conn.close()