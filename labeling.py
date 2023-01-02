import joblib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import matplotlib.pyplot as plt
import numpy as np
import sys
import mariadb

mydb = mariadb.connect(
  host="localhost",
  user="root",
  passwd="",
  database="social_media"
)

#memuat model
model = joblib.load("model.ict")
cv = joblib.load('cv.ict')


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ttweet")
myresult = mycursor.fetchall()
for x in myresult:
    text = x[3]
    temp = cv.transform([text])
    temp = temp.toarray()
    res = model.predict(temp)
    akurasi = model.predict_proba(temp) 
    if(res==0):
        hasil = 0
    else:
        hasil = 1
    
    mycursor.execute("UPDATE ttweet set sentiment=%s WHERE id = %s", (hasil, x[0]))

#prediksi inputan menggunakan model yang ada
mydb.commit()