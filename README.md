# Custom Dog nose detection training.
## _Training custom yolov8 model_

## Complete Documentation https://docs.google.com/document/d/1mXVtjtAF0Q6n7Fotgim636RbiLkEczvP0wkDmCztcvM/edit


## Steps

- Create a account in roboflow : https://roboflow.com/
- Annotate the Images and get the yolov8 format code snippet
- Get the project name and the version from the above code snippet from roboflow

## Working
Create a conda environment
```sh
conda create -n custom_training python>=3.11
```

Activate the environment

```sh
conda activate custom_training
```


Clone the repository

```sh
git clone https://rise4bux@bitbucket.org/infrasonic/petbiometricstraining.git
```
Change the directory

Install the packages
```sh
pip install -r requirements.txt
```
Install Pytorch https://pytorch.org/

GPU
```sh
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
CPU
```sh
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
Change the API_KEY, MODEL_ENDPOINT, VERSION and EPOCHS in the .env file.

Run the code

```sh
python train.py
```
