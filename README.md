# COVID19 Stats collector

Will collect stats for Sweden from [https://api.covid19api.com](https://api.covid19api.com) and store it in InfluxDB.

## Setup in Kubernetes

### Create namespace

    kubectl create namespace covid19

### Install InfluxDB

    helm install influxdb stable/influxdb --namespace covid19

### Install the collector

Update deployment/covid19stats-collector/values.yaml with your database address.

    helm install covid19stats-collector covid19stats-collector/ --namespace covid19
