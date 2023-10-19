from flask import Flask, render_template
from post import Post
import requests

blogs_api_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = blogs_api_response.json()
post_objects = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs= blog_posts)


@app.route('/post/<int:index>')
def to_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
