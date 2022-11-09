import time
from application.workers import celery
from datetime import datetime
from flask import current_app as app
from flask_sse import sse
from celery.schedules import crontab
print("crontab ", crontab)


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    #sender.add_periodic_task(10.0, print_current_time_job.s(), name='add every 10')
    pass


@celery.task()
def calculate_aggregate_likes(article_id):
    # You can get all the likes for the `article_id`
    # Calculate the aggregate and store in the DB
    print("#####################################")
    print("Received {}".format(article_id))
    print("#####################################")
    return True

@celery.task()
def just_say_hello(name):
    print("INSIDE TASK")
    print("Hello {}".format(name))


@celery.task()
def print_current_time_job():
    print("START")
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string) 
    print("COMPLETE")


@celery.task()
def long_running_job():
    print("STARTED LONG JOB")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    sse.publish({"message": "STARTED ="+dt_string }, type='greeting')
    for lp in range(100):
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        sse.publish({"message": "RUNNING ="+dt_string }, type='greeting')
        print("date and time =", dt_string) 
        time.sleep(2)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")        
    sse.publish({"message": "COMPLETE ="+dt_string }, type='greeting')
    print("COMPLETE LONG RUN")
