import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sentimentAnalysis
import pandas as pd
# Use the application default credentials.
cred = credentials.Certificate('secrets.json')

firebase_admin.initialize_app(cred)
db = firestore.client()

docs = db.collection(u'messages').stream()


def retrieve():
    data = []

    # Iterate through all documents in the collection
    for doc in docs:
        # Extract the fields of interest
        blood_oxygen_percentage = doc.to_dict()['bloodOxygenPercentage']
        body = doc.to_dict()['body']
        date = doc.to_dict()['date']
        happiness_index = doc.to_dict()['happinessIndex']
        heart_rate = doc.to_dict()['heartRate']
        sender = doc.to_dict()['sender']

        # Append the data to the list
        data.append([blood_oxygen_percentage, body, date,
                    happiness_index, heart_rate, sender])

    # Create a DataFrame from the list
    df = pd.DataFrame(data, columns=[
                      'bloodOxygenPercentage', 'body', 'date', 'happinessIndex', 'heartRate', 'sender'])

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'], unit='s')
    df['dayofweek'] = df['date'].dt.dayofweek
    print(df)


retrieve()
