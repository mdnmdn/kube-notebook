from kubernetes import config

config.load_incluster_config()

from kubernetes import client

core_api = client.CoreV1Api()

res = core_api.list_namespace()

print([x.metadata.name for x in res.items])

res = core_api.list_pod_for_all_namespaces()

print([ {"n": x.metadata.name, "ns": x.metadata.namespace} for x in res.items])

#res = core_api.list_namespaced_pod(namespace='devops')

