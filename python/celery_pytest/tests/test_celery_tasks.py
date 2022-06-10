import pytest

def test_celery_session_worker_initializes(celery_session_app, celery_session_worker):
    assert True

def test_task1(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(1).get() == 'OK 1'

def test_task2(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(10).get() == 'OK 10'

def test_task3(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(10).get() == 'OK 10'

def test_task4(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(10).get() == 'OK 10'

def test_task5(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(10).get() == 'OK 10'

def test_task6(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(10).get() == 'OK 10'

def test_task7(celery_session_app, celery_session_worker):
    assert celery_session_app.tasks['tasks.mytasks.longtask1'].delay(10).get() == 'OK 10'