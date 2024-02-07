# Introduction
## Definition
It is a portable, extensible, open-source platform for managing containerised workloads and services. It is most commonly referred as a **Container Orchestrator**.

### Containers vs VMs
A virtual machine is a complete Operating System that runs over an hardware. The hardware resources are, however, virtualised, so that the VM can only access a portion of them and not the whole.

A Container, however, is a higher level of abstraction that relies on the exact same Kernel as the machine is running upon, without the need of having a complete Operating System.

![VMs vs Containers](./../images/k8s_image_1.png)

## History
It was originally designed by Google and then open-sourced thanks to the *Cloud Native Computing Foundation* in 2015.

The concept and the need of Container Orchestrators, like Kubernetes, came afterwards the so called *Monoliths* applications, in which all the components were integrated into a single deployable artifact. Such an approach presented quite few drawbacks:
- Hard to scale
- Slow to deploy
- Costly to maintain

In order to solve such issues, the so called *Microservices* approach was launched. It defines a new system design, in which each piece lives as its own individually and independent artifact. Such design ensures:
- Easy to scale
- Fast to deploy just the needed service
- Cheap to maintain

However, maintaining a single VM for each service was not efficient. That's why the *Containerised Approach* was invented. The main challenge was to:
- How to coordinate several containers living within the same application?
- How to let these containers communicate between each other?
- How to ensure no downtime while updating or fixing a container?

Containeer Orchestrators, like Kubernetes, were born in order to solve such questions.

# Clusters
## Definition
Kubernetes works in terms of *Clusters*: a collection of *Nodes*, which are composed by one or more *PODs*, which are composed by *Containers*.

In GCP, you can create a cluster with:
```bash
gcloud container clusters create-auto <name_of_clsuter> --location=us-central1
```

## Nodes
They contain everything necessary to run PODs:
- Container Runtime (To run containers)
- Kubelet (Run necessary k8s processes)
- Kube-proxy (Handle networking for Kubernetes API)

Cluster &rarr; Node &rarr; PODs &rarr; Containers

## PODs
They host the container application, which can be deployed through:
```bash
kubectls create deplyment <name> --image <image>
```

**NOTE:** It is also possible to specify the number of replicas that has to spread across different nodes.

Then we need to expose the service:
```bash
kubectl expose deployment <name> --port 80 --type LoadBalancer --target-port 8080
```

## Control Plane & Desired State
They in which Kubernetes ensure that the cluster is running correctly is to use a *Control Plane* in order to manage the containers within the cluster. The state of such machines has to match a pre-defined *Desired State*.

The **Control Plane** includes:
- API Server
- Etcd - It holds important key-value information for k8s
- Scheduler - It organises the PODs' runs
- Controller Manager - It it responsible for the lifecycle management of PODs
- Cloud Controller - It is used to integrate with Cloud providers, such as GCP

# Kubernetes API
## Definition
It is a practical way used to communicate commands and instructions for Kubernetes. It both works in an *Imperative* approach, writing commands and execute them, or *Declarative*, create a file for the Kubernetes API to read the commands from.

# Google Cloud Platform
## Services
### Google Build
It is used in order to build container images:
```bash
# Syntax
gcloud builds submit --region=<region> --tag gcr.io/<project_ID>/<image_name> .

# Example
gcloud builds submit --region=us-west2 --tag gcr.io/test_project_id/image_1 .
```

It is also possible to submit a **Build Configuration** file like:
```yaml
# Example
steps:
- name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/helloworld-image', '.']
images:
- 'gcr.io/$PROJECT_ID/helloworld-image'
```

Submit it to Google Build through:
```
gcloud builds submit --config <config_build_file>
```

- **Container Registry** - It is used in order to host docker images
