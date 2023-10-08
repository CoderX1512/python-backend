from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Sample blog posts
posts = []

@app.route('/')
def index ():
    return render_template('index.html',posts =posts)

@app.route('/create_post', methods = ['GET' ,'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({'title': title, 'content':content })
            return redirect(url_for('index'))

    return render_template('create_post.html')

if __name__ == "__main__":
    app.run(debug=True)
