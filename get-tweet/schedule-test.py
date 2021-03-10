from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import *

sched = BlockingScheduler()

# @sched.scheduled_job('date', run_date=datetime(2021, 3, 13, 12, 10, 0))
# def timed_job():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=14, minute=40, year=2021, month=3, day='11-13')
# def timed_job():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=15, minute=50, year=2021, month=3, day='11-13')
# def timed_job():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=17, minute=0, year=2021, month=3, day='11-13')
# def timed_job():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=18, minute=10, year=2021, month=3, day='11-13')
# def timed_job():
#    print('This job is run every three minutes.')
@sched.scheduled_job('cron', hour=22, minute=20)
def timed_job():
   print('hello1')
@sched.scheduled_job('cron', hour=22, minute=21)
def timed_job():
   print('hello2')
sched.start()