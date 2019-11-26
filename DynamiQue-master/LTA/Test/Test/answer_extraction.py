from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import requests
from bs4 import BeautifulSoup
import json
import lda  #lda module for ease of usage
import webbrowser
#Database connection from here
import sqlite3