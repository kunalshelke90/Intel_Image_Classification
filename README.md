### Intel_Image_Classification with deep learning CNN


## Problem statement

In this project, we have created an API which predicts a different type of Natural Scenes around the world. 

## Solution Proposed
The solution proposed for the above problem is that we have used Computer vision to solve the above problem to detect different types of apparel.
We have used the Pytorch framework to solve the above problem also we created our custom object detection network with the help of PyTorch.
Then we created an API that takes in the images and predicts what type of apparel a person is wearing. Then we dockerized the application and deployed the model on the AWS cloud.

## Dataset Used

This Data contains around 25k images of size 150x150 distributed under 6 categories.
```
{'buildings' -> 0,
'forest' -> 1,
'glacier' -> 2,
'mountain' -> 3,
'sea' -> 4,
'street' -> 5 }
```

The Train, Test and Prediction data is separated in each zip files. There are around 14k images in Train, 3k in Test and 7k in Prediction.

# Step 1: Clone the repository
```bash
git clone https://github.com/kunalshelke90/Intel_Image_Classification.git
```
```bash
git cd Intel_Image_Classification
```
### Step 2- Create a conda environment after opening the repository

```bash
conda create -p env python=3.8 -y
```

```bash
conda activate env
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the  environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

```
Before running server application make sure your `s3` bucket is available and empty

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train
```

### Step 7. Prediction application
```bash
http://localhost:8080/predict
```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> . 

```

3. Run the Docker image

```
docker run -d -p 8080:8080 <IMAGEID>
```

👨‍💻 Tech Stack Used
1. Python
2. Flask
3. Pytorch
4. Docker
5. Computer vision

🌐 Infrastructure Required.
1. AWS S3
2. AWS EC2
3. AWS ECR
4. Github Action


**Artifact** : Stores all artifacts created from running the application

**Components** : Contains all components of Machine Learning Project
- DataIngestion
- Data Validation
- ModelTrainer
- ModelEvaluation
- ModelPusher

**Custom Logger and Exceptions** are used in the project for better debugging purposes.


## Conclusion

We have created an API which predicts the different types of  Natural Scenes around the world.


