from prefect import task

@task
def say_hello(word: str):
    print(f"Hello {word}")