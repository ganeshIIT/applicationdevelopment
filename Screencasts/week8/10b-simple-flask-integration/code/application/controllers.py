from flask import Flask, request
from flask import render_template
from flask import current_app as app
from application.models import Article
from flask_security import login_required, roles_accepted, roles_required

@app.route("/", methods=["GET", "POST"])
def articles():
    app.logger.info("Inside get all articles using info")
    articles = Article.query.all()    
    app.logger.debug("Inside get all articles using debug")
    return render_template("articles.html", articles=articles)

@app.route("/articles_by/<user_name>", methods=["GET", "POST"])
@login_required
def articles_by_author(user_name):
    articles = Article.query.filter(Article.authors.any(username=user_name))
    return render_template("articles_by_author.html", articles=articles, username=user_name)


@app.route("/article_like/<article_id>", methods=["GET", "POST"])
def like(article_id):
    print(article_id)
    return "OK", 200


@app.route("/feedback", methods=["GET","POST"])
def feedback():
    if request.method == "GET":
        return render_template("feedback.html", error=None)
    if request.method == "POST":
        form = request.form
        email = form["email"]
        print(form)
        # Validate here too
        if "@" in email:
            pass
        else:
            error = "Enter a valid email"
            return render_template("feedback.html", error = error)

        return render_template("thank-you.html")


@app.route("/create_article", methods=["GET", "POST"])
@login_required
@roles_required('admin')
def create_article():
    if request.method == "GET":
        return render_template("create_article.html", error=None)


