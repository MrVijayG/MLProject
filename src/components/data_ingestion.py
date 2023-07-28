## In this file we will import data from souces like database, cloud for training aur testing purpose.

import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.components import data_transformation
from src.components import model_trainer

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered into data ingestion method or components")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Reading dataset in dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test initiated")

            train_data,test_data = train_test_split(df,test_size=0.2,random_state=40)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ =="__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    # print(pd.read_csv(a))
    obj = data_transformation.DataTransformation()
    train_arr,test_arr,_=obj.initiate_data_transformation(train_data,test_data)

    model_train = model_trainer.ModelTrainer()
    print(model_train.initiate_model_trainer(train_arr,test_arr))
    # print(obj)
