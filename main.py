import requests
import datetime
from email.mime.text import MIMEText
from send_email import send_email


url = 'https://newsapi.org/v2/everything?' \
                            'q=ubuntu&' \
                            'from=2022-12-26&' \
                            'sortBy=publishedAt&' \
                            'apiKey=0b31d5b365fb42fb8f2d249f343bf98a'

request = requests.get(url)
content = request.json()

raw_message = []

for article in content['articles']:
    item = f"{article['title']}\n{article['description']}\n<ln></ln>"
    raw_message.append(item)

date_now = (datetime.datetime.now()).strftime('%d-%m-%Y')

message = ''.join(raw_message)
message = MIMEText(message, 'plain', 'utf-8')

message = f'''\
    Subject: News about Ubuntu {date_now}
    From: News API
    Topic: News about Ubuntu {date_now}
{message}'''

send_email(message)
# print(message)

"""
import streamlit as st
from send_email import send_email

st.header('Contact Us')

variants = ['Job Inquiries', 'Project Proposals', 'Other']

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    topic = st.selectbox('What topic do you want to discuss?', variants)
    raw_message = st.text_area('Your message')
    message = f'''\
Subject: New email from {user_email}
From: {user_email}
Topic: {topic}
{raw_message}'''

    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Your email was sent..')
"""