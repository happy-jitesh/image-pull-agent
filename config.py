NAMESPACE = "prod"
APP_LABEL = "app=bad-image"
DEPLOYMENT_NAME = "bad-image"

MODEL = "llama3"

CHECK_INTERVAL = 10

ALLOWED_ACTIONS = [
    "FIX_IMAGE_TAG",
    "ESCALATE_TO_HUMAN",
    "DO_NOTHING"
]

# fallback image
CORRECT_IMAGE = "nginx:latest"