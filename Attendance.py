import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root"
)
    
mycursor=mydb.cursor()

def faceEncodings(images){


    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        




}

mycursor.execute("create database memberdata")
mycursor.execute("create database attendance")
mydb.close()

mydb_1=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="memberdata"
)

mydb_2=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="attendance"
)

mycursor_1=mydb_1.cursor()
mycursor_2=mydb_2.cursor()

mycursor_1.execute("create table (name char(30),encodings int(49,40),")
mycursor_2.execute("create table (name varchar(max),date date,time char(30))")

