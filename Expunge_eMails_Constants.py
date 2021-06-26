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
*> If End Date is left blank it will assume current (taday's) date.
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
INVALID_END_DATE_GR = "Invalid end date! End date cannot be greater than today's date!"
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