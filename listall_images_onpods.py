#Images created on each pods k8s
from kubernetes import client, config

config.load_kube_config(config_file="/Users/lap02803/Library/Application Support/Lens/kubeconfigs/6260f5ea-fb36-4a06-84a8-41c10eb733ad")

v1 = client.CoreV1Api()
print("Listing pods ...")
ret = v1.list_pod_for_all_namespaces(watch=False)

#d = ret.items.status
#print(d)
#print(d['image'])
#print(ret.items.status)
print("namespace\t\t\t\t\t\t" "pod_name\t\t\t\t\t\t" "image")
for i in ret.items:
    #container_name = i.status.container_statuses
    #image = (container_name[0].image).split("/")[-1]
    #pod_name = i.metadata.name
    #namespace = i.metadata.namespace
    #if i.metadata.name == 'tn001-api1-57c6bbb45b-6vvzk':
    lenspec = len(i.spec.containers)
    #print(type(lenspec))
    for index in range(0, lenspec):
    #if i.metadata.name == 'tn001-api1-57c6bbb45b-6vvzk':
        #print(len(i.spec.containers))
        image = (i.spec.containers[index].image).split("/")[-1]
        print("{0}\t\t\t\t\t\t {1}\t\t\t\t\t\t {2}".format(i.metadata.namespace,i.metadata.name,image))
    #print("image name: {0}\t namespace: {1}".format(pod_name,namespace))
    #print(type(d))
