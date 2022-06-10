from time import sleep
from celery import Celery


celery = Celery(broker='sqla+sqlite:///celery_db/celery.db',
                backend='db+sqlite:///celery_db/celery_results.db')


@celery.task(bind=True)
def longtask1(self, x):
    print(self)
    for i in range(x):
        self.update_state(name='longtask1', state='PROGRESS', meta={'current': i, 'x': x})
        sleep(1)
    return f'OK {x}'