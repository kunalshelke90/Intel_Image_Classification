import os, sys
from src.intel.logger import logging
from src.intel.configuration.aws_connection import S3Client
from mypy_boto3_s3.service_resource import Bucket
from src.intel.exception import CustomException


class S3Operation:
    
    def __init__(self):
        
        s3_client = S3Client()
        self.s3_resource = s3_client.s3_resource
        self.s3_client = s3_client.s3_client
    
    def get_bucket(self, bucket_name: str) -> Bucket:
        """
        Method Name :   get_bucket
        Description :   This method gets the bucket object based on the bucket_name
        
        Output      :   Bucket object is returned based on the bucket name
        """
        logging.info("Entered the get_bucket method of S3Operations class")
        
        try:
            
            bucket = self.s3_resource.Bucket(bucket_name)
            logging.info("Exited the get_bucket method of S3Operations class")
            return bucket

        except Exception as e:
            
            raise CustomException(e, sys) from e
    

    def download_file(self, bucket_name: str, output_file_path: str, key: str) -> None:
        """
        Method Name :   download_file
        Description :   This method downloads the file from the s3 bucket and saves the file in directory 
        
        Output      :   File is saved in local
        """
        logging.info("Entered the download_file method of S3Operation class")
        
        try:
            
            self.s3_resource.Bucket(bucket_name).download_file(key, output_file_path)
            logging.info("Exited the download_file method of S3Operation class")

        except Exception as e:
            
            raise CustomException(e, sys) from e

    def read_data_from_s3(self, bucket_filename: str, bucket_name: str, output_filepath: str) -> None:

        """
        Method Name :   read_data_from_s3
        Description :   This method downloads the file from the s3 bucket and saves the file in directory 
        
        Output      :   returns object.
        """
        logging.info("Entered the read_data_from_s3 method of S3Operation class")
        try:
            
            bucket = self.get_bucket(bucket_name)
            obj = bucket.download_file(Key=bucket_filename, Filename=output_filepath)
            logging.info("Exited the read_data_from_s3 method of S3Operation class")
            
            return obj
            
        except Exception as e:
            
            raise CustomException(e, sys) from e

class S3Sync:

    def sync_folder_to_s3(self,folder,aws_bucket_url):
        
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)
 