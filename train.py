from ultralytics import YOLO
from roboflow import Roboflow
import os

# Here in the below example the name inside .project() is the project name, here dog_nose_detection, ignore the last five characters
# The version is written in project.version(1), here 1 is the version

# Example (this will be recieved from roboflow)
# project = rf.workspace("dog-nose-detection").project("dog_nose_detection-uipkm")
# dataset = project.version(1).download("yolov8")


project_name = "dog_nose_detection-1"           # Give your own project_name = your_project_name-version
EPOCH = 3                                       # Change the Number of epochs to train the model

if project_name == "":
    print("Please enter Project Name")
else:
    if not os.path.exists(os.getcwd()+"/"+project_name):

        # Replace the below three lines with the code snippet obtained from roboflow
        rf = Roboflow(api_key="cr5ilWXHdJYSGrisqBwa")
        project = rf.workspace("dog-nose-detection").project("dog_nose_detection-uipkm")
        dataset = project.version(1).download("yolov8")

    model = YOLO("yolov8n.pt")
    model.train(
        data=os.getcwd()+f"/{project_name}/data.yaml",   # path of the data.yaml present in the downloaded dataset folder
        epochs=EPOCH
    )

# the best.pt and last.pt will be saved at latest version of runs/detect/latest_version_of_train/weights