import pytest
import tasks

# init celery pytest plugin
pytest_plugins = ("celery.contrib.pytest")

# use temporary celery backend. no need to start redis or rabbitmq
@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": "memory://",
        "result_backend": "rpc://",
    }

# include 'tasks' module, where our celery tasks are located
@pytest.fixture(scope="session")
def celery_includes():
    return ["tasks"]
