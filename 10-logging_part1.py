'''Logging is the process of keeping the record 
of what a program is doing while it runs
'''

import logging

name = "GFG"      
logging.error('%s raised an error',name)     #root logger gets configured/default handler
'''lazy string formatting -> format_string, value
formatting only happens when it actually needs to 
create the log message.
'''

#There are 5 built-in levels for log message

logging.debug("Variable x = 10")
logging.info("User logged in")
logging.warning("Disk space is getting low")
logging.error("Database connection failed")
logging.critical("System is shutting down")

#root logger's default effective level is WARNING
#Hence it will ignore anything less "severe" than WARNING.

'''Log message using Python's file handler'''

logger = logging.getLogger("SimpleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)

logger.info("This is an info message")
logger.error("This is an error message")


# Logging a Variable

logging.basicConfig(level = logging.INFO, format = '%(levelname)s: %(message)s')   # log format
age = 25
logging.info("The value of age is %d", age) #'%d'-> string-formatting placeholder

'''The root logger in Python default built-in logging system is Master Logbook
label-> root, parent of other loggers, automatic

The Root Logger is the top-level default logging object 
that handles any message not assigned to a specific logger.
'''



logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Harmless debug message")
logger.info("Just an information")
logger.warning("Its a warning")
logger.error("Did you try to divide by zero?")
logger.critical("Internet is down")