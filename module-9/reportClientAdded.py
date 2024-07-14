

import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
   host="127.0.0.1",
    user="botiwaK",
    password="password",
    database="WillsonFinancial"
)
cursor = conn.cursor()

# Report: New Clients Added Per Month
cursor.execute("""
    SELECT DATE_FORMAT(JoinDate, '%Y-%m') AS Month, COUNT(ClientID) AS NewClients
    FROM Clients
    WHERE JoinDate >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY Month
    ORDER BY Month
""")
new_clients = cursor.fetchall()
print("New Clients Added Per Month Report:")
for row in new_clients:
    print(row)

# Close connection
conn.close()
