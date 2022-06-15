from flask import Flask
from firebase_admin import firestore, credentials, initialize_app

cred = credentials.Certificate("app/capstone-33322-firebase-adminsdk-jeqfp-d78be2eaa3.json")
firebase=initialize_app(cred)
db=firestore.client()


app = Flask(__name__)

from app import views


