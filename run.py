import fire
from expand_langchain.evaluator import Evaluator
from expand_langchain.generator import Generator

from src.server import Server

if __name__ == "__main__":
    fire.Fire(
        {
            "evaluator": Evaluator,
            "generator": Generator,
            "server": Server,
        }
    )
