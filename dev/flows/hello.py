from prefect import flow
from tasks.hello import say_hello
import bs4 #PoC

@flow(log_prints=True)
def hello_flow(word:str = "World"):
    _ = say_hello(word)