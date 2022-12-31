# Huawei Cloud EI PaaS Project
Random Forest Model That Diagnoses Skin Cancer APP

If you want to run it on the cloud platform, make sure you push it to the image cloud.
While running the project, the files in it should be turned into a docker image and the yaml files should be integrated into the worker nodes.
To run data, don't forget to replace the address in the pd.read part of the file with the cloud storage path of the data.

This project is pushed to SWR service of docker image on ECS and then works with worker nodes on CCE.
