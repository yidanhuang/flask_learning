from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)

all_posts=[
    {
        'title':'posts1',
        'content':'this is the content of post1.lalalala',
        'author': 'susan'
    },
    {
        'title':'posts2',
        'content':'this is the content of post1.lalalala'
    }
] #创建posts字典
@app.route('/')
def index():
    return render_template("index.html")  #返回index.html的内容

@app.route('/posts')
def posts():
    return render_template("posts.html",posts=all_posts)


@app.route('/home/users/<string:name>/posts/<int:id>')  #定义路由
def hello(name,id):
    return "hello "+name+"your id is" +str(id)
if __name__== "__main__":
    app.run(debug=True)

@app.route('/onlyget',methods=['GET','POST'])
def get_req():
    return "you can only get this webpage"

if __name__=="__main__":
    app.run(debug=True)