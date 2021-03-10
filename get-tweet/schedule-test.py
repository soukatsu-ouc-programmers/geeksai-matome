from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import *

sched = BlockingScheduler()

# @sched.scheduled_job('date', run_date=datetime(2021, 3, 13, 12, 10, 0))
# def session1():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=14, minute=40, year=2021, month=3, day='11-13')
# def session2():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=15, minute=50, year=2021, month=3, day='11-13')
# def session3():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=17, minute=0, year=2021, month=3, day='11-13')
# def session4():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=18, minute=10, year=2021, month=3, day='11-13')
# def session5():
#    print('This job is run every three minutes.')
# @sched.scheduled_job('cron', hour=23, minute=20, args=['aaaaa'])
def getTweet(key):
   print(key)
sched.add_job(getTweet, 'cron', hour=23, minute=25, args=['aaaaa'])
sched.add_job(getTweet, 'cron', hour=23, minute=26, args=['bbbbb'])
sched.start()