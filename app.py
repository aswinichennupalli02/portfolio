from flask import Flask, request, render_template, redirect, url_for,flash
import sqlite3
import os
import smtplib
from email.mime.text import MIMEText
app = Flask(__name__)
DATABASE = 'contacts.db'
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
app.secret_key = os.urandom(24)  
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table() #Create the table if it doesnt exist

@app.route("/", methods=['GET', 'POST'])

def index():
    social_links = {
        'insta' : "https://www.instagram.com/aswini_chennupalli?igsh=OTBhM2MwZjhkYWQz&utm_source=qr",
        'twitter' : "https://x.com/aswinichen87177?s=11",
        'linkedin' :"linkedin.com/in/aswinichennupalli"
    }
    educations = [
        {'date': '2023-2025', 'degree': 'Master of Computer Applications', 'institution': 'KL University', 'description': 'Specialization on Cloud Computing.', 'cgpa': '9.13'},
        {'date': '2020-2023', 'degree': 'Bachelor of Science', 'institution': 'Maris Stella College','description':'Branch: Computer Maths, Statistics, Computer Science ', 'cgpa': '7.0'},
        {'date': '2016-2018', 'degree': 'Intermediate (MPC)', 'institution': 'Sri Chaitanya Junior College', 'cgpa': '7.32'},
        {'date': '2015-2016', 'degree': 'SSC', 'institution': 'Sri Chaitanya', 'cgpa': '8.8'},
        ]
    projects = [
        {'title': 'Revolutionnizing Cloud Data Security with Elliptic Curve Crypotography', 'image': 'pq.jpg','description': 'Encryption helps in transmitting sensitive data over an insecure channel without any danger of data being lost or being manipulatedby some unauthorized entity'},
        {'title': 'Android App to convert Text to speech using AI', 'image': 'p1.avif', 'description': 'Developed an Android app that leverages AI to convert text into clear, natural-sounding speech, making digital content more accessible and user-friendly'}
    ]
    experiences = [
        {
            'date':"06 2024 - 08 2024",
            'title': 'Software Developer Internship',
            'company': 'Innovate',  # Added company name
            'start_date': 'June 2024',
            'end_date': 'Agust 2024',
            'description': 'Developed a centralized dashboard using HTML and CSS to provide a clear overview of event progress, enhancing attendee registration and session scheduling efficiency'
        },
        {
            'date':"04 2022 - 05 2022",
            'title': 'Software Developer Internship',
            'company': 'Right Computers',  # Added company name
            'start_date': 'April 2024',
            'end_date': 'May 2024',
            'description': 'Developed a Python-based machine learning model to identify and flag harmful URLs, improving security protocols for online safety'
        }
    ]
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
            conn.close()

            # Send email
            sender_email = "2301600150mca@gmail.com"
            sender_password = "cduf hokz futq idlr" 
            receiver_email = "aswinichennupalli@gmail.com" # Recipient email (your email)
            email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"

            msg = MIMEText(email_message)
            msg['Subject'] = "New Contact Form Submission"
            msg['From'] = sender_email
            msg['To'] = receiver_email

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # Use appropriate SMTP server
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
            flash('Message sent successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))
        except sqlite3.Error as e:
          return f"Database error: {e}"
        except smtplib.SMTPException as e:
          return f"Email error: {e}"
        except Exception as e:
          return f"Unexpected error: {e}"
    return render_template('index.html',social_links=social_links, educations=educations,projects=projects,experience=experiences)

if __name__ == "__main__":
    app.run(debug=False,port=1000,host="0.0.0.0")
