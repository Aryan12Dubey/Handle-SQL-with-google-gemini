from dotenv import load_dotenv
load_dotenv() #load all env variable
import streamlit as st
import os
import mysql.connector
import google.generativeai as generativeai

#Configure our API key
generativeai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to load Google Gemini Model and provide sql query as response

def get_gemini_response(question,prompt):
    model=generativeai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


def read(sql,db):
    host = 'localhost'
    user = 'root'
    password = 'root@12345'
    database = 'mydb'
    #Creating a connection cursor
    connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
    cursor = connection.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    connection.commit()
    cursor.close()
    for ro in row:
        print(ro)
    return row


prompt=[
    """
you are an expert in converting English question to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME,CLASS,
SECTION and MARKS \n\n for eample 1- How many entries of records are present in ther SQL command willl be  something like
this SELECT COUNT(*) FRom STUDENT;
\nExmaple 2- Tell me all the students studying in data science class?,
the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Data Science";
also the sql code should not have ''' in begnning or end and sql word in the output.
"""
]

#Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read(response,"student.db")
    st.subheader("The response is ")
    for row in data:
        print(row)
        st.header(row)


