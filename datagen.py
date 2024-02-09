import typer
from typing_extensions import Annotated
from config import cfg
from prompt import improve, answer, question, reduce
import sys
from rich.progress import Progress, SpinnerColumn, TextColumn
import time
from rich import print


def gen(ctx_fn, to_fn=""):
    with Progress(SpinnerColumn(), TextColumn("{task.description}")) as progress:
        task = progress.add_task("[cyan]Generating instruction-following data...")
        writer = open(to_fn, 'w') if to_fn else sys.stdout
        for q in reduce(question(ctx_fn)):
            ans = answer(q, ctx_fn)
            writer.write(f"INSTRUCTION:{q}\n")
            writer.write(f"ANSWER:{ans}\n")
            writer.write("\n")
            writer.flush()
            progress.update(task, advance=1)  # This will just spin without a total
    print("Processing complete.")


gen("context.txt", "data_gen.txt")