from flask import Flask, render_template, request, session, redirect
import string
import random
#from digital_makeup import Maquille

import re
#import python_weather
#
#import asyncio


#from newspaper import Article
#import newspaper
#print(newspaper.languages())
#from codelang_detect import detect as detectprogramminglanguage
#from langdetect import detect as detectspokenlanguage, detect_langs
#from face_recognize import FaceRecognize
#from myplace import Myplace
#comment out if you use

##spell checker
#from spellchecker import SpellChecker
#from textblob import Word
#from autocorrect import Speller
#import speech_recognition as sr
#print(sr.__version__) #find the latest
#import spacy
#from flair.data import Sentence
#from flair.models import SequenceTagger
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from translate import Translator

#image to text
#from PIL import Image
#import pytesseract
#from sendemail import Sendemail


from bs4 import BeautifulSoup
import subprocess
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from city')


        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,password,email,phone,country_id,pic) values (:username,:password,:email,:phone,:country_id,:pic)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from user')


        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','password','email','phone','country_id','pic']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','password','email','phone','country_id','pic']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','password','email','phone','country_id','pic']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from country')


        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_morceau_a_jouer", methods=["GET","POST"])
def add_one_morceau_a_jouer():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into morceau_a_jouer (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from morceau_a_jouer')


        return render_template("morceau_a_jouerform.html", morceau_a_jouers=user, one_user=one_user, the_title="add new morceau_a_jouer")


    user = query_db('select * from morceau_a_jouer')
    one_user = query_db("select * from morceau_a_jouer limit 1", one=True)
    return render_template("morceau_a_jouerform.html", morceau_a_jouers=user, one_user=one_user, the_title="add new morceau_a_jouer")

@app.route("/add_one_simplescore", methods=["GET","POST"])
def add_one_simplescore():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        touslesuser= query_db("select * from user")

        touslesmorceau_a_jouer= query_db("select * from morceau_a_jouer")

        one_user = query_db("insert into simplescore (title_score,composer,myscore,pic,time_signature,key_signature,city_id,edition,user_id,morceau_a_jouer_id) values (:title_score,:composer,:myscore,:pic,:time_signature,:key_signature,:city_id,:edition,:user_id,:morceau_a_jouer_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from simplescore')


        file_pointer = open("./samplescoreexample.ly")
        contents = file_pointer.read()
        try:
            piece = query_db('select * from morceau_a_jouer where id = ?', [hey["morceau_a_jouer_id"]], one=True)["name"]
        except:
            piece="Capriccio"
        try:
            cityname = query_db('select * from city where id = ?', [hey["city_id"]], one=True)["name"]
        except:
            cityname="Paris"
        contents=contents.replace("KEYSCOREHERE", request.form["key_signature"].replace(" "," \\")).replace("MYTITLE", hey["title_score"]).replace("MYCOMPOSER", hey["composer"]).replace("MYPIECE", piece).replace("MYEDITIONPUBLISHING", request.form["edition"]).replace("MYCITY", cityname).replace("TIMESCOREHERE", request.form["time_signature"]).replace("CONTENTSCOREHERE", request.form["myscore"])
        file_pointer = open("./static/scores/simplescore_myscore_sample_"+mylastrowid+".ly", "w")
        file_pointer.write(contents)
        file_pointer.close()
        file_pointer = open("./static/scores/simplescore_myscore_sample_"+mylastrowid+".html", "w")
        file_pointer.write("<lilypond staffsize=34>"+contents+"</lilypond>")
        file_pointer.close()
        p1=subprocess.Popen(["lilypond-book", "static/scores/simplescore_myscore_sample_"+mylastrowid+".html", "-f", "html", "--output", "static/scores/samplescoresimplescore_myscore"+mylastrowid]) 
        exit_codes = [p.wait() for p in (p1,)]

        try:
            f= open("static/scores/samplescoresimplescore_myscore"+mylastrowid+"/simplescore_myscore_sample_"+mylastrowid+".html")
            s = f.read()
            soup = BeautifulSoup(s)

            picvalue=dict({'pic': "static/scores/samplescoresimplescore_myscore"+mylastrowid+"/"+soup.find('img').get("src"), 'id': mylastrowid})
        except:
            picvalue=dict({'pic': "", "id": mylastrowid})
        print(picvalue)
        hey["pic"]=picvalue["pic"]


        hello_there = query_db("update simplescore set pic = :pic where id = :id",picvalue, one=True)

        return render_template("simplescoreform.html", simplescores=user, one_user=one_user, the_title="add new simplescore", touslescity=touslescity, touslesuser=touslesuser, touslesmorceau_a_jouer=touslesmorceau_a_jouer)


    touslescity= query_db("select * from city")

    touslesuser= query_db("select * from user")

    touslesmorceau_a_jouer= query_db("select * from morceau_a_jouer")

    user = query_db('select * from simplescore')
    one_user = query_db("select * from simplescore limit 1", one=True)
    return render_template("simplescoreform.html", simplescores=user, one_user=one_user, the_title="add new simplescore", touslescity=touslescity, touslesuser=touslesuser, touslesmorceau_a_jouer=touslesmorceau_a_jouer)

@app.route("/add_one_simplerecording", methods=["GET","POST"])
def add_one_simplerecording():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['vid']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["vid"]=uploaded_file.filename


        touslessimplescore= query_db("select * from simplescore")

        one_user = query_db("insert into simplerecording (video,vid,simplescore_id) values (:video,:vid,:simplescore_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from simplerecording')


        return render_template("simplerecordingform.html", simplerecordings=user, one_user=one_user, the_title="add new simplerecording", touslessimplescore=touslessimplescore)


    touslessimplescore= query_db("select * from simplescore")

    user = query_db('select * from simplerecording')
    one_user = query_db("select * from simplerecording limit 1", one=True)
    return render_template("simplerecordingform.html", simplerecordings=user, one_user=one_user, the_title="add new simplerecording", touslessimplescore=touslessimplescore)

