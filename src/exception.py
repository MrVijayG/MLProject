"""
In this file we write a code related to exception handling for the project. 
This file will give the error detail like from which script you are getting an error, 
on which line you are getting error and exactly what is error i.e error message
"""


import sys
import logger

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()    # In exc_tb we will get the error message and error line number and in which file error is occured.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":

#     try :
#         a = 1/0
#         print(a)
#     except Exception as e:
#         logger.logging.info(e)
#         raise CustomException(e,sys)