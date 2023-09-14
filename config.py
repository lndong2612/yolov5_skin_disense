import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST: str = '0.0.0.0'
    PORT: int = 8080
    DEBUG = True
    API = 'https://tclinic-ai.thinklabs.com.vn'
    RESOURCES: str = './resources'
    IMAGE_FOLDER: str = os.path.join(RESOURCES, 'images')
    MODEL: str = os.path.join(RESOURCES, 'weight_init')
    DATA_COCO: str = './data/coco.yaml'

settings = Settings()
settings.IMAGE_FOLDER: str = os.path.join(settings.RESOURCES, 'images')
settings.MODEL: str = os.path.join(settings.RESOURCES, 'weight_init')
settings.DATA_COCO: str = settings.DATA_COCO