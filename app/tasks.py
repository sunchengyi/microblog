import time
from rq import get_current_job

def example(seconds):
    job = get_current_job()
    print('Starts task')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.savemeta()
        print(i)
        time.sleep(1)
    job.meta['progress'] = 100
    job.savemeta()
    print('Task completed')
