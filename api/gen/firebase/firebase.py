import pyrebase
import os
firebaseConfig = {
    "apiKey": "AIzaSyA_wznJ5vUk9xVmETK9HACyy3a3tWybw3U",
    "authDomain": "ticket-api-312db.firebaseapp.com",
    "projectId": "ticket-api-312db",
    "storageBucket": "ticket-api-312db.appspot.com",
    "messagingSenderId": "807333422489",
    "appId": "1:807333422489:web:774d8cf50d46830896df08",
    "measurementId": "G-9LZ9BG8QFM",
    "databaseURL": "ticket-api-312db.appspot.com"

}

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()


def upload_file(file_name):
    storage.child(file_name).put(file_name)
