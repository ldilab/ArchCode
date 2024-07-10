import fire
from expand_langchain.generator import Generator

from third_party.expand_langchain.expand_langchain.evaluator import Evaluator

if __name__ == "__main__":
    fire.Fire(
        {
            "evaluator": Evaluator,
            "generator": Generator,
        }
    )
