## Capacity Management Project  
![Test Python](https://github.com/salehsedghpour/capacity-management/actions/workflows/test-python.yml/badge.svg)  
 This project aims to setup an infrastructure using [Libvirt](https://libvirt.org/) and install
 [Kubernetes](https://kubernetes.io/) on top of the infrastructure. Then it sets up an 
 [Istio Service Mesh](https://istio.io/) on the  Kubernetes cluster. Everything is managed by 
 the user using a config file. The codebase is test driven and we intend to implement the 
 possible tests. All the tests are running using Github Actions. 
 
 ##### Installation
To use this repo, you need to have python versions 3.6, 3.7 or 3.8. and the it is required to
install [pip](https://pip.pypa.io/en/stable/).
```
git clone https://github.com/salehsedghpour/capacity-management
pip install -r requirements.txt
```  

 
 ##### Runing Tests
 In order to run tests if you have pulled the repo just follow the instruction below:  
 ```python3 -m pytest```  
If you didn't pull the repo you need to follow the instruction in the 
[installation part](#installation).
