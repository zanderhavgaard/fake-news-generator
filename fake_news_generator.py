from article import Article
from content_provider import ContentProvider
from flask import Flask, render_template, request, url_for, redirect
import time
import base64

# create app instances
app = Flask(__name__)

# privedes fake news content
content_provider = ContentProvider()

# url parameter keys to look for
header_key_string = "aGVhZGVy"
image_url_key_string = "aW1hZ2VfdXJs"


@app.route("/")
def index():

    page = render_template("index.html")

    return page


@app.route("/random_article")
def random_article():

    generated_article = generate_article()

    content = generated_article.get_content_dict()

    header = base64_encode(generated_article.header)
    image_url = base64_encode(generated_article.image_url)

    url = f'{url_for("article")}?{header_key_string}={header}&{image_url_key_string}={image_url}'

    return redirect(url)


@app.route("/article")
def article():

    # parse keys from url
    header = request.args.get(header_key_string, "")
    image_url = request.args.get(image_url_key_string, "")

    # decode header and image url
    header = base64_decode(header)
    image_url = base64_decode(image_url)
    url = request.url

    print("url", url)

    # create article from parsed data
    article = Article(header=header, image_url=image_url, article_url=url)

    content = article.get_content_dict()

    page = render_template("index.html", content=content)

    return page


def generate_article():

    header, image_url = content_provider.generate_content()
    url = f'{url_for("article")}?{header_key_string}={header}&{image_url_key_string}={image_url}'

    article = Article(header=header, image_url=image_url, article_url=url)

    return article


def base64_encode(string: str):
    return str(base64.urlsafe_b64encode(string.encode("utf-8")), "utf-8")


def base64_decode(string: str):
    return str(base64.urlsafe_b64decode(string), "utf-8")
