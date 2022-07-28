import prefect
from prefect import task, Flow
import time

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Sleeping...")
    time.sleep(50)
    logger.info("Hello world!")


with Flow("hello-flow") as flow:
    hello_task()

flow.run()
