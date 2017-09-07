from blog_app import app

@app.route('/login')
def login():
    return 'Hello User'