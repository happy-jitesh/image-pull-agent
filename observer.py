from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()


def get_image_pull_errors(namespace):

    pods = v1.list_namespaced_pod(namespace)

    failures = []

    for pod in pods.items:

        pod_name = pod.metadata.name

        statuses = pod.status.container_statuses or []

        for container in statuses:

            state = container.state

            if state and state.waiting:

                reason = state.waiting.reason

                if reason in ["ImagePullBackOff", "ErrImagePull"]:

                    failures.append({
                        "pod": pod_name,
                        "reason": reason,
                        "image": container.image
                    })

    return failures