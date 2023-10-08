import pyodbc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Database connection configuration
server = '127.0.0.1'
database = 'PAR_A01_2018_Inventory (3)'
username = ''
password = ''

# Establish database connection
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=' + server + ';'
                          'DATABASE=' + database + ';'
                          'UID=' + username + ';'
                          'PWD=' + password)
    cursor = conn.cursor()

    # Check if there is data in the table
    cursor.execute('SELECT * FROM TB_EVENT')  # Replace 'your_table' with your table name
    data = cursor.fetchall()

    # If there is data, send an email
    if data:
        # Email configuration
        sender_email = 'xerxesfalcao09@gmail.com'  # Replace with sender email address
        sender_password = ''  # Replace with sender email password
        receiver_email = 'xerxesfalcao09@gmail.com'  # Replace with receiver email address

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Data Available in Database'

        # Email body
        body = 'There is data available in the database table.'
        msg.attach(MIMEText(body, 'plain'))

        # Send email using SMTP server
        try:
            server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print('Email sent successfully!')
        except Exception as e:
            print('Email could not be sent. Error:', str(e))
    else:
        print('No data available in the database table.')

    # Close database connection
    cursor.close()
    conn.close()

except pyodbc.Error as err:
    print("Error: {}".format(err))
