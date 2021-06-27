"""
*****************************************************************************
Function Name   :   Expunge_eMails_Constants.py
Author          :   SS. Kanagal.
Description     :   This file contains all Constants-reusable values.
                :   All the messages are read from this file centrally.
                :   Hard coding of messages are eliminated by this method.
                :   The values of any variables can be changed at any time
                :   centrally in this file.
Input Parameters:   None.
Version History :   Dates       Version     Description
                :   30 May,2021 1.0         Initial Release.
                :   01 Jun,2021 1.5         Final release.
                :   27 Jun,2021 1.6         Added Help Text.
*****************************************************************************
"""

# Log Message Heading.
LOG_FILE_NAME_PREFIX = "\Expunge_eMail_Log_"
LOG_FILE_NAME_EXTENSION = ".txt"
STARTED = "[Started @: "
FINISHED = "[Finished @: "
USER_QUIT = "[USER TERMINATED @: "
STOP_CHAR = "x"
WELCOME = """\nWelcome to bulk delete/expunge web emails.\n
*> Press "x" at any prompt to stop.
*> By default "INBOX" is selected.
\nPlease enter the below details: """
SYS_QUIT = "[SYSTEM TERMINATED <runtime err> @: "

SYS_CONNECT = "Connecting to email server... "
SYS_CONNECTED = "Connected to email server successfully."

SYS_SELE_FOLDER = "Selecting folder:"
SYS_SELED_FOLDER = "Selected folder:"

SYS_DT_SEARCH_CRITERIA = "eMail search date criteria: "
SYS_MSG_FOUND = "Number of email messages found: "
SYS_MSG_NOTFOUND = "[Nothing to delete!]"
SYS_EXPUNGED_SUCCESSFULLY = " eMail(s) deleted/expunged successfully."

# Log Message types.
INFO = "inf"
WARNING = "war"
CRITICAL = "cri"
ERR = "err"

# User Input Prompt Messages.
EMAIL_SRCH_START_DT_PRMT = "Enter Start date [DD-MM-YYYY] (enter x to quite):>> "
EMAIL_SRCH_END_DT_PRMT = "Enter End date [DD-MM-YYYY] (enter x to quite):>> "
EMAIL_ADDR_PRMT = "\nEnter a valid eMail address (enter x to quite):>> "
EMAIL_PWD_PRMT = "Enter Password (enter x to quite):>> "

# User Input Error Messages.
INVALID_EMAIL_ADDR = "Invalid eMail address! Please enter a valid email address!"
EMPTY_EMAIL_ADDR = "eMail address cannot be blank! Please enter a valid email address!"
EMPTY_EMAIL_PWD = "Password cannot be blank! Please enter password."
END_DATE_RANGE_MSGS = "\n[NOTE:] Add one day to the actual End Date as range of dates. "
EMPTY_START_DT = "Start Date cannot be blank! Please enter Start Date in DD-MM-YYYY."
EMPTY_END_DT = "End Date cannot be blank! Please enter End Date in DD-MM-YYYY."
INVALID_START_DATE = "Invalid start date! Start date cannot be greater than today's date!"
INVALID_END_DATE_GR = "Invalid end date!"  # End date cannot be greater than today's date!"
INVALID_END_DATE_LR = "Invalid end date! End date cannot be lesser than start date!"

# Default eMail Folder Name.
FOLDER_NAME = "Inbox"

# IMAP
IMAP_PREFIX = "imap."
YAHOO_DOMAIN_NAME = "yahoo"
YAHOO_IMAP = IMAP_PREFIX + "mail."

# IMAP Errors.
IMAP_AUTHEN_FAILED = "[AUTHENTICATIONFAILED] Invalid credentials (Failure)"
IMAP_AUTHENTICATION_FAILED = "AUTHENTICATION FAILED! Invalid credentials! (Failure)\n" \
                             "Retry with correct credentials. Programme Terminated!"
WRONG_IMAP_HOST = "getaddrinfo failed"
WRONG_IMAP_HOST_MSG = "eMail host server not found!"

# Command Line Help Texts.
HELP_SWITCH = "--help"
HELP_TEXT = """\n
Expunge eMails v1.6 Release Help:
---------------------------------

This programme/script can be used to bulk delete/expunge web email messages from Inbox on specified date range.
\n*> Press x or X at any input prompt to stop/exit.
*> By default "INBOX" is selected.
*> The below input data can be passed as command line arguments in the same order as mentioned below
however, if no command line arguments are passed you will be prompted to enter input data.

This script works on Yahoo! and Gmail email accounts without any script changes required.

Input data required:
--------------------
	1. eMail Address: a valid email address.
	2. eMail Password: enter generated application password.
	   Note: You should generate application password before running this script and enter the same. 
	   Please refer to your service prvider to generate application password for your email account.
	3. Start Date: Start Date to search, in DD-MM-YYYY format only.
	4. End Date: End Date in DD-MM-YYYY format only.
	   NOTE: Add one day to the actual end date e.g.: to delete till 25-06-2021 then the end date should be 26-06-2021.

-------------------------------------------------------------
Author: SS. Kanagal
Author Constants: sskanagal@gmail.com / cmetolive@gmail.com
-------------------------------------------------------------
GitHub license: MIT.
"""