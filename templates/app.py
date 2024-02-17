from flask import Flask,render_template,redirect,request,session
import requests
from mydb import Database
import pickle
import streamlit as st
import requests
# import api


app=Flask(__name__)

dbo=Database()

@app.route('/')

def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_egistration',methods=['post'])
def perform_registration():
    name=request.form.get('username')
    email=request.form.get('email')
    password=request.form.get('password')
    con_password=request.form.get('confirm-password')
    if password ==con_password:
        respons=dbo.insert(name,email,password)
        if respons:
            return render_template('login.html',message="Regestration Successful. Kindly login to proceed")
        else:
            return render_template('register.html',message="Email alredy exist")
    else:
        return render_template('register.html',message="Password not match")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('email')
    password=request.form.get('password')
    respons=dbo.search(email,password)
    if respons:
        return redirect('/profile')
    else:
        return render_template('login.html',message="User not defined")


@app.route('/profile')
def profile():
    movies = pickle.load(open('movie_list.pkl','rb'))  
    itms = movies['title'].values
    return render_template('profile.html',itms=itms)

@app.route('/profile1')
def profile1():
    similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    for i in range(0,6):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(i)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        full_path
    return full_path

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        recommended_movie_posters.append(movies.iloc[i[0]].movie_id)
        
        # fetch the movie poster
        # movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_posters.append(fetch_poster(movie_id))
        # recommended_movie_names.append(movies.iloc[i[0]].title)

    return render_template('temp.html',recommended_movie_posters=recommended_movie_posters)



app.run(debug=True,port=7500)



