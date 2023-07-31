# Custom Dog nose detection training.
## _Training custom yolov8 model_

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
git clone https://github.com/adityaweboccult/custom_training_with_roboflow.git
```
Change the directory

Install the packages
```sh
pip install -r requirements.txt
```

Change the project_name and the code snippet obtained from roboflow in the `train.py` file

Run the code

```sh
python train.py
```
