## Project information

This repository involves files for the capstone project of ML-Zoomcamp (September 2021 – December 2021) by [Alexey Grigorev](https://github.com/alexeygrigorev) from [DataTalks.Club](https://datatalks.club/).

- Click [here](https://datatalks.club/courses/2021-winter-ml-zoomcamp.html) for the course information. 

- Course Github page is [here](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp).

The scope of the midterm project is defined [here](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone).


## Problem Statement

Being considered as a proven way of preventing virus infection for decades, masks are turned out to be an integral part of daily life since the beginning of Covid-19 pandemics. Wearing a mask is generally obligatory in public indoor spaces. However, since it makes breathing more difficult and stings some parts of the face, people tend to take off it after a while. This makes it a challange to follow up and warn people. 

On the other hand, it is possible to identify people without masks taking advantage of modern image processing methods. Such a system may help detecting people without mask and warn them if necessary to keep the public space safe. As an example, it can be used in entry points where receptionists or guards are not available. Beside individuals, it can also be used for determining some public measures like distance among unmasked people or the ratio of unmasked people in a crowd. 

Accordingly, the project aims to (i) develop a neural network model to identify if the human face on a picture is with or without mask, and (ii) deploy this model as a web service. The .ipynb files in `notebooks` folder explains the details of model development process whereas the PDF files in `documentation` shows how the local and web services can be used.


## Dataset

One of the people who worry about immediate spread of COVID-19 was [Prajna Bhandary](https://github.com/prajnasb). However, instead of complaining, she started to gather a collection of images of people with and without masks to use it to train mask detection algorithms. She made it publicly [available on Github](https://github.com/prajnasb/observations/tree/master/experiements/data). 

The dataset contains 1372 unique photos of people where the half is with mask and the rest is without mask. To use in this project, the dataset is divided into 3 parts:
- Train dataset: 412 images for each of classes (with and without masks)
- Validation dataset: 137 images for each of classes
- Test dataset: 137 images for each of classes

For convenience, the images in each group are renamed with ascending numeric values. The dataset is located under the `data` folder of the repository.

## Modeling

Different CNN architectures are built and compoared for modeling:
- CNN with single convolutional layer (`notebooks/nb3_modeling_CNN1.ipynb`)

- CNN with double convolutional layer (`notebooks/nb4_modeling_CNN2.ipynb`)
- CNN with pre-trained model (`notebooks/nb5_modeling_CNN3.ipynb`)

Mask detection is a relatively simple task for CNNs. Pre-trained CNNs can be used for predicting even mask types (medical, oxygen, etc.). Hence, high accuracy scores are attained for binary mask classifiers (with & without) in literature. Since the CNN with pre-trained model yielded scores very close to 1 (overfit), the second best model (CNN with double convolutional layer) is used for deployment. This model is then hypertuned with RandomSearchCV function of Scikit-learn (`notebooks/nb6_hypertuning.ipynb`). Having best parameters for train dataset, the best model is tested on validation dataset (`notebooks/nb7_best_model.ipynb`).


## Repository Content

In line with the problem statement and dataset description provided above, this repository presents:

1. Exploratory analysis of the image collection,
2. Feature engineering for images (comparing model performance with RGB and grayscale images)
3. Comparison of different neural network models in terms of their performance for detecting mask,
4. Development of a containerized local service for mask detection,
5. Development of a basic web service for mask detection


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

|-----

|-----

|-/**documentation**

|-----

|-----

|----- 

|-/**local_service**

|-----Dockerfile

|-----model.bin

|-----predict-test.py

|-----predict.py

|-----train.py

|-/**notebooks**

|-----

|-----

|-----

|-----

|-/**web service**

|-----

|-----

|-----

|-----