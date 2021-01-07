# ETL (Extract, Transform, and Load)


import os
import tarfile
import pandas as pd

# Extract from tar file
def extract_data(source, destination):
    """
    @param source: location of data
    @param destination: folder location where data will be extracted
    @return: True on succss and False on failure
    """
    if not os.path.exists(destination):
        os.makedirs(destination)
    try:
        housing_tgz = tarfile.open(source)
        housing_tgz.extractall(path=destination)
        housing_tgz.close()
        print("tar extraction complete")
        return True
    except Exception as e:
        print("failed to extract tar file with error: ", e)
        return False


# Load into df
def load_data_to_df(csv_path):
    """
    @param csv_path: location of the csv housing data
    @return: pandas dataframe
    """
    housing_df = pd.read_csv(csv_path)
    print("csv reading complete")
    return housing_df


# Transfrom as needed


def build_histogram():
    print("hi from build histogram")

