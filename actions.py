from kubernetes import client, config

# Load Kubernetes configuration from default location(e.g ~/.kube/config)
config.load_kube_config()

# Create an API client instance
apps_v1 = client.AppsV1Api()


def fix_image(deployment, namespace, new_image):

    body = {
        "spec": {
            "template": {
                "spec": {
                    "containers": [
                        {
                            "name": "app",
                            "image": new_image
                        }
                    ]
                }
            }
        }
    }

    apps_v1.patch_namespaced_deployment(
        name=deployment,
        namespace=namespace,
        body=body
    )


def notify(msg):
    print(f"[NOTIFICATION]: {msg}")