#For Exception Handling purpose.
import sys
import logging

logging.basicConfig(
    filename = "errors_logs",
    format = "[%(asctime)s] - %(lineno)s - %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,                
)

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()     #Talking about execution info.
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))          # 0, 1, 2 are the placeholder    
    
    return error_message   
    

#Whenever I raise CustomException first up all it is inheriting its parent exception and whatever error message comes from the error_message_detail function will come over here and will initialize variable like error_message.
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        self.error_message = error_message_detail(error_message, error_detail)
        # self.error_detail = error_detail
        super().__init__(self.error_message)           # Since we are inheriting from exception using super.__init__()
        
    def __str__(self): 
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
    