from flask import Flask, request
from flask import render_template
from main import app as app
from application.models import Article
from flask_security import login_required, roles_accepted, roles_required
from application import tasks
from flask_sse import sse

print("in controller app", app)

@app.route("/hello", methods=["GET"])
def hello():
    return "World"

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
    job_id = tasks.calculate_aggregate_likes.delay(article_id)
    print(" Job started with job_id = {}".format(job_id))
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


@app.route("/test_send_message", methods=["GET","POST"])
def test_send_message():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"



@app.route("/start_long_running_job", methods=["GET","POST"])
def start_long_running_job():
    job_id = tasks.long_running_job.delay()
    sse.publish({"message": "STARTING JOB "+ str(job_id)}, type='greeting')
    return "STARTED!"+str(job_id) 
       

@app.route("/show_updates", methods=["GET"])
def show_updates():
    return render_template("show_updates.html", error=None)



@app.route("/show_updates_vue", methods=["GET"])
def show_updates_vue():
    return render_template("show_updates_vue.html", error=None)    