<<<<<<< HEAD
## Project information

This repository involves files for the midterm project of ML-Zoomcamp (September 2021 – December 2021) by [Alexey Grigorev](https://github.com/alexeygrigorev) from [DataTalks.Club](https://datatalks.club/).

Click [here](https://datatalks.club/courses/2021-winter-ml-zoomcamp.html) for course information. Course Github page is [here](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp).

The scope of the midterm project is defined [here](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/07-midterm-project).


## Problem Statement

Being responsible for considerable share (30-40%) of global energy consumption and greenhouse gas emissions, buildings constitute latent potantial for improving resilliece and sustainability (social and einvironmental) of the society. The design process of a building is highly complex and inevitably requires iterations. An important parameter that architectures and engineers have to consider for each iteration is the estimated energy consumption of the proposed design. There are engineering methods and dedicated tools to conduct energy performance analysis of buildings. However, they are complex and time consuming processes. In a typical design processs, generally there aren't enough resources to use those for each iteration. Hence, researchers are looking for developing tools that can provide quick insights about impact of any proposed change on the energy performance of the design.

Researchers Athanasios Tsanas (Oxford Centre for Industrial and Applied Mathematics, University of Oxford, UK) and Angeliki Xİfara (Architectural Science Group, Welsh School of Architecture, Cardiff University, UK) focused on using machine learning tools to estimate building energy performance. Accordingly, they conducted energy simulations for 768 building designs using the energy modeling software called [Ecotect](https://openei.org/wiki/Ecotect). They picked 8 building design parameters to establish design combinations:
* Relative Compactness (12 possible values)
* Surface are (12 possible values)
* Wall area (7 possible values)
* Roof area (4 possible values)
* Overall height (2 possible values)
* Orientation (4 possible values)
* Glazing area (4 possible values)
* Glazing area distribution (6 possible values).

Their simulations resulted in 586 different values for heating load and 636 for cooling load. They raked together these design parameters and simulation results to create a [dataset](https://archive.ics.uci.edu/ml/datasets/energy+efficiency) for ML research in this field. Their original study can be found [here](https://www.sciencedirect.com/science/article/abs/pii/S037877881200151X?via%3Dihub). 

In line with the context provided above, this project aims to develop a ML service in order to estimate the energy consumption (heating and cooling load) of a building based on the 8 design parameters listed above. Accordingly, this repository presents:

1. Exploratory analysis of the dataset,
2. Importance analysis of design parameters for energy performance,
3. Comparison of different machine learning models in terms of their performance for estimating heating and cooling loads,
4. Development of a containerized local service for heating & cooling load prediction,
5. Development of a basic web service for energy prediction (with pythonanwhere.com)


## Notes:

- pipenv files (pipfile & pipfile.lock) as well as the Dockerfile are provided to prevent version conflicts and enable isolation. For their usage, see /documentation/Using_Pipfile_and_Dockerfile

- In case having authorization issues in Docker, use this script:

    ```sudo chown $(whoami):$(whoami) /var/run/docker.sock```

- The best model deployed as a service in pythonanywhere.com. How to reach it and get estimations is explained in: /documentation/Using_web_service

- Not being a production project, the web service is created with Flask. A WSGI (gunicorn or Waitress) is not used. 




## Organization of the repository
/

|-----notes_for_reviewers

|-----Pipfile

|-----Pipfile.lock

|-----README.md

|-/**data**

|-----ENB2012_data.csv

|-----ENB2012_data.xlsx

|-/**documentation**

|-----Using_Pipfile_and_Dockerfile.pdf

|-----Using_service_in_local.pdf

|-----Using_web_service.pdf 

|-/**local_service**

|-----Dockerfile

|-----model.bin

|-----predict-test.py

|-----predict.py

|-----train.py

|-/**notebooks**

|-----nb1_eda.ipynb

|-----nb2_feature.ipynb

|-----nb3_modeling.ipynb

|-----nb4_best_model

|-/**web service**

|-----cloud-test.ipynb

|-----cloud-test.py

|-----flask_app.py

|-----model.bin
=======

``` pip install pipenv```
>>>>>>> refs/remotes/origin/main
