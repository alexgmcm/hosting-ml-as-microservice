# hosting-ml-as-microservice

## Description

* Completed the [*Training and Deploying an ML Model as a Microservice*](https://www.manning.com/liveproject/training-and-deploying-an-ml-model-as-a-microservice) LiveProject from Manning Publications.

## Thoughts

* The course was quite short for the price but was good as an introduction to Cloud Services.  
* I had prior experience building NLP models and using Docker and Flask so perhaps these parts would be more valuable to someone new to those technologies.  
* I had no prior experience with the Cloud Services introduced here and thus it was useful to learn how to use FaaS and easily deploy web apps on AWS.
* The Manning LiveProject Platform felt immature and had several bugs such as not being able to read the textbook extracts in dark mode (despite dark mode being a feature on the normal Manning Publications reader).
    * The LiveProject includes access to some textbooks and you can open these in the normal Manning reader (complete with dark mode!), however, some are only extracts and you cannot open these in the normal reader, only the one on the LiveProject platform and thus dark mode is not available.
    * It can also be quite hard to navigate to and within the LiveProject platform.
* Overall, I think the content of the course was very good, if a bit pricy for the length. The platform felt a bit like a beta product though and could be improved by further development.
* I would recommend the course to those who wish to try out Cloud Deployment.

## Contents

* Part 1 - Using pre-made models from Cloud Machine Learning Services
    *  Example service was AWS Comprehend (this was surprisngly pricy so be careful if you are doing the course)
* Part 2 - Training a simple Sentiment Analysis model using NLTK
    * The example model is a Naive Bayes Classifier using Bag-Of-Words as the features (but with word count, not binary)
    * I improved the accuracy slightly by converting all strings to lower-case, stemming the words (SnowballStemmer) and changing the features from word count to the more traditional binary Bag-of-Words that just checks if the word exists in the document rather than how many times it is present.
* Part 3 - Running the model in the cloud I - Functions as a Service
    * Bundled the trained model and calling code and deployed it on AWS Lambda
* Part 4 - Preparing the model for deployment - HTTP APIs and Containerisation
    *  Use Flask to create an HTTP API to call the model code
    *  Use Docker to containerise this API - making it ready for deployment in the cloud
* Part 5 - Running the model in the cloud II - Amazon ECS and Amazon S3
    * Deploy the Docker container containing the Flask web app (i.e. the model and the HTTP API) to Amazon ECS
    * Develop an ultra-simple HTML Frontend that calls the HTTP API using XMLHttpRequest
        * Remember to set the CORS headers correctly in the API Response!
    * Host the front-end on Amazon S3 