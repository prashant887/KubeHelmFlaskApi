docker build -f docker/Dockerfile -t flasksfapi:latest

 helm delete kubehelmflaskapi -n demo-namespace

 helm upgrade  kubehelmflaskapi  . -n demo-namespace --debug --install --recreate-pods