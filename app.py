from flask import Flask ,request,render_template
import pickle
import requests
import pandas as pd
from patsy import dmatrices



movies=pickle.load(open('models/movie_list.pkl','rb'))
simlarity=pickle.load(open('models/similarity.pkl','rb'))
def fetch_poster(id):
    url ="https://api.themoviedb.org/3/movie/{}?api_key=fc3761ac5749ac22f44f65b46097367a&&language=en-US".format(id)

    data=requests.get(url)
    
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path
def recomended(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(simlarity[index])),reverse=True,key=lambda x:x[1])
    recomended_movie_name=[]
    recomended_movie_poster=[]
    for i in distance[1:6]:
        movi_id=movies.iloc[i[0]].movie_id
        recomended_movie_poster.append(fetch_poster(movi_id))
        recomended_movie_name.append(movies.iloc[i[0]].title)
    return recomended_movie_name,recomended_movie_poster
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/priduction',methods= ['GET','POST'])
def priduction():
    movi_list=sorted(movies['title'].values)
    status=False
    if request.method=="POST":
        try:
            if request.form:
                movies_name=request.form['movies']
                print(movies_name)
                movie_name,movie_poster=recomended(movies_name)
                # print(movie_name)
                # print(movie_poster)
                status=True
                
                return render_template('priduction.html',name=movie_name,poster=movie_poster,movies_list=movi_list,status=status)

        except Exception as e:
            error={'error':e}
            print(e)
            return render_template('index.html',movies_list=movi_list)
    
    else:
        return render_template('priduction.html',movies_list=movi_list)


@app.route('/contect')
def contect():
    return render_template('contect.html')



@app.route('/about')
def about():
    return render_template('about.html')



app.run(debug=True)