import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sentimentAnalysis
# Use the application default credentials.
cred = credentials.Certificate('secrets.json')

firebase_admin.initialize_app(cred)
db = firestore.client()


docs = db.collection(u'messages').stream()
for doc in docs:
    doc_dict = doc.to_dict()
    if doc_dict['happinessIndex'] == "":
        senderMsg = doc_dict['body']
        index = sentimentAnalysis.happyIndex(senderMsg)
        print(index)
        doc.reference.update({'happinessIndex': float(index)})
