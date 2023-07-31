from ultralytics import YOLO
from roboflow import Roboflow
import os
import torch
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_ENDPOINT = os.getenv("MODEL_ENDPOINT")
VERSION = os.getenv("VERSION")
EPOCHS = os.getenv("EPOCHS")

project_name =f"{MODEL_ENDPOINT.split('-')[0]}-{VERSION}"            

# Setting the device

if torch.cuda.is_available():
    device = "cuda:0"
else:
    device = "cpu"




if project_name == "":
    print("Please enter Project Name")
else:
    try:
        if not os.path.exists(os.getcwd()+"/"+project_name):

            # Replace the below three lines with the code snippet obtained from roboflow
            rf = Roboflow(api_key=API_KEY)
            project = rf.workspace().project(MODEL_ENDPOINT)
            dataset = project.version(VERSION).download("yolov8")

        model = YOLO("yolov8n.pt")
        model.train(
            data=os.getcwd()+f"/{project_name}/data.yaml",   # path of the data.yaml present in the downloaded dataset folder
            epochs=int(EPOCHS),
            device = device
    )
    except KeyboardInterrupt:
        print("Iterrupted")
    except:
        print("Please verify the values entered in the .env file.")

    

# the best.pt and last.pt will be saved at latest version of runs/detect/latest_version_of_train/weights