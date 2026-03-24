import time

from observer import get_image_pull_errors
from llm_brain import llm_decide
from actions import fix_image, notify
from config import *

with open("prompts/image_prompt.txt") as f:
    PROMPT = f.read()


def controller():

    notify("ImagePullBackOff AI Agent Started 🚀")

    while True:

        failures = get_image_pull_errors(NAMESPACE)

        if not failures:
            notify("No image pull errors ✅")
            time.sleep(CHECK_INTERVAL)
            continue

        notify(f"Detected failures: {failures}")

        context = str(failures)

        decision = llm_decide(context, PROMPT)

        notify(f"LLM Decision: {decision}")

        if decision == "FIX_IMAGE_TAG":

            notify("Fixing image 🚀")

            fix_image(
                DEPLOYMENT_NAME,
                NAMESPACE,
                CORRECT_IMAGE
            )

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    controller()