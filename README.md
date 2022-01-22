# Build a ML Workflow For Scones Unlimited On Amazon SageMaker
This is the Image Classification Project with AWS SageMaker and Workflows under the Udacity Machine Learning Engineer with AWS NanoDegree Program

## AWS Machine Learning Engineer Nanodegree

### Overview

In this Project, the concepts of AWS Lambdas, Step Functions, EndPoints, Model Monitor through SageMaker, S3 and Pipelines were implemented

### Background
Image Classifiers are used in the field of computer vision to identify the content of an image and it is used across a broad variety of industries, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms, and even in diagnostic medicine.

You are hired as a Machine Learning Engineer for a scone-delivery-focused logistics company, Scones Unlimited, and you’re working to ship an Image Classification model. The image classification model can help the team in a variety of ways in their operating environment: detecting people and vehicles in video feeds from roadways, better support routing for their engagement on social media, detecting defects in their scones, and many more!

In this project, you'll be building an image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

As an MLE, your goal is to ship a scalable and safe model. Once your model becomes available to other teams on-demand, it’s important that your model can scale to meet demand, and that safeguards are in place to monitor and control for drift or degraded performance.

In this project, you’ll use AWS Sagemaker to build an image classification model that can tell bicycles apart from motorcycles. You'll deploy your model, use AWS Lambda functions to build supporting services, and AWS Step Functions to compose your model and services into an event-driven application. At the end of this project, you will have created a portfolio-ready demo that showcases your ability to build and compose scalable, ML-enabled, AWS applications.

For this Project, we will take 2 classes from the CIFAR Dataset for Bicycles & Motorcycles.

### Project Steps Overview
- Step 1: Data staging
- Step 2: Model training and deployment
- Step 3: Lambdas and step function workflow
- Step 4: Testing and evaluation
- Step 5: Visualising Inferences from Step Functions
- Step 6: Cleanup cloud resources

### License
[License](LICENSE.txt)
