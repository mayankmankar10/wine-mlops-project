import os
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    # Reading the raw dataset
    df = pd.read_csv(raw_data_path, sep=",")

    # Splitting the data into train and test
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    # Saving the data into the processed folder
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()

    # Call the function to split and save the data
    split_and_save_data(config_path=parsed_args.config)
 