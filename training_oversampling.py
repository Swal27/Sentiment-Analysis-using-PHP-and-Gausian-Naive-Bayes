import mariadb
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
import joblib
from imblearn.over_sampling import SMOTE

mydb = mariadb.connect(
  host="localhost",
  user="root",
  passwd="",
  database="social_media"
)

#mengambil data dari database
text = []
sentiment = []
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ftweet where sentiment != 0")
myresult = mycursor.fetchall() 

for tweet in myresult:
    text.append(tweet[3])
    sentiment.append(tweet[4])

dict = {'text': text, 'sentiment':sentiment}
df = pd.DataFrame(dict)


#mengubah teks string menjadi bentuk binary
cv = CountVectorizer()
text_counts = cv.fit_transform(df['text'])

#split data training dan testing
x_train, x_test, y_train, y_test= train_test_split(text_counts, df['sentiment'], test_size=0.25, random_state=5)
ovr = SMOTE()
x_train_sample, y_train_sample = ovr.fit_resample(x_train,y_train)

#modeling atau training data
gaussian = GaussianNB()
model = gaussian.fit(x_train.toarray(), y_train)
predicted = gaussian.predict(x_test.toarray())

#hasil training
akurasi = metrics.accuracy_score(predicted, y_test)
print(str(akurasi))

Recall = metrics.recall_score(predicted, y_test)
print(str(Recall))

Presicion = metrics.precision_score(predicted, y_test)
print(str(Presicion))

f_measure = metrics.f1_score(y_test, predicted)
print(str(f_measure))

#menyimpan model
filename = 'model.ict'
joblib.dump(model, filename)
joblib.dump(cv, "cv.ict") 


