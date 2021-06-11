# DevOpsAssessment

# Prerequisites to
1. Install Python3.7
2. Install ansible unsing python pip
3. Install openshift using python pip
4. Install Docker latest version
5. Install kubectl, kubelet, kubeadm and Minikube

#Python APP
Its a sample Python Program will dispaly "Hello World !! I am running on HOST and Todays date"

#Dockerfile
Dockerfile will dockerize python app 

#To Build Docker Image
To buld Docker image run docker build -t <image-name> <path to dockerfile>

#To run Ansible Playbooks
change to the root directory.

To run ansible-playbook < file-name >

# Ansible 
It will run and istall the all requirements and build the docker image 

After building the docker image it will deploy our app into minikube.

# Jenkins

In Jenkins first we need to install Plugnis To test and to Perform Ansible.

Plugins need to Installed on jenkins

1. Ansible
2. Python
3. Docker
4. Shining Panda
5. Junit
6. Kubernetes

After Installing Plugins, Change The Global Tool Configaratin Change Python into Python 3.7


