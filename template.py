import os
from pathlib import Path


list_of_files = [
    
    ".github/worksflows/gitkeep",
    f"src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/model_deployment.py",
    "src/pipeine/__init__.py",
    "src/pipeine/training_pipeline.py",
    "src/pipeine/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logger.py",
    "src/exceptions/exceptions.py",
    "scr/unit/__init__.py",
    "scr/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "pytest.ini",
    "step.py",
    "step.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experimenrs.ipynb"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file