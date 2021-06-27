"""
**************************************************************************
Script Name     :   Expunge_eMails_Utilities.py
Author          :   SS. Kanagal.
Description     :   This file contains all the utilities required by
                :   Expunge_eMail_v1.5.py.
Input Parameters:   None.
Version History :   Dates       Version     Description
                :   30 May,2021 1.0         Initial Release.
                :   01 Jun,2021 1.5         Final release.
                :   27 Jun,2021 1.6         Added Command Line Parameters.
**************************************************************************
"""
import Expunge_eMails_Constants as CONST
import imaplib as IMAP_LIB
import logging as LOGFILE
import datetime as SYSDT
import os as SYSTEM
import re

"""
**************************************************************************
Function Name   :   CreateLogFile()
Author          :   SS. Kanagal.
Description     :   This creates a logfile in current working directory
                :   with supplied name in the logfilename parameter which
                :   is optional. It holds default value from constant 
                :   LOG_FILE_NAME_PREFIX. To have a different log filename
                :   name change the value of this constant in Constants.py
Input Parameters:   logfilename (Optional).
Return Value    :   logfile.
Version History :   Dates       Version     Description
                :   30 May,2021 1.0         Initial Release.
**************************************************************************
"""
def CreateLogFile(logfilename=CONST.LOG_FILE_NAME_PREFIX):
    logfile = SYSTEM.getcwd() + logfilename + SYSDT.datetime.now().strftime("%d%m%Y_%H%M") + \
              CONST.LOG_FILE_NAME_EXTENSION
    LOGFILE.basicConfig(format = '%(levelname)s:%(message)s', filename = logfile, level = LOGFILE.INFO)
    return logfile

"""
**************************************************************************
Function Name   :   WriteLogFile()
Author          :   SS. Kanagal.
Description     :   This function updates the log file with supplied
                :   message based on message type. By Default INFO is
                :   set as log type.
Input Parameters:   log_msg, log_type=CONST.INFO
Return Value    :   None.
Version History :   Dates       Version     Description
                :   31 May,2021 1.0         Initial Release.
**************************************************************************
"""
def WriteLogFile(log_msg, log_type=CONST.INFO):
    if log_type.lower() == CONST.INFO:LOGFILE.info(log_msg)
    if log_type.lower() == CONST.WARNING:LOGFILE.warning(log_msg)
    if log_type.lower() == CONST.CRITICAL:LOGFILE.critical(log_msg)
    if log_type.lower() == CONST.ERR:LOGFILE.error(log_msg)
    return

"""
**************************************************************************
Function Name   :   User_Quit()
Author          :   SS. Kanagal.
Description     :   This function updates log file upon user termination.
Input Parameters:   custom_msg=False, custommsg=""
Return Value    :   None.
Version History :   Dates       Version     Description
                :   31 May,2021 1.0         Initial Release.
**************************************************************************
"""
def User_Quit(custom_msg=False, custommsg=""):
    if not custom_msg:
        WriteLogFile(CONST.USER_QUIT + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
        WriteLogFile(CONST.FINISHED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
    else:
        WriteLogFile(CONST.SYS_QUIT + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) +
                     custommsg + "]\n", CONST.WARNING)
        WriteLogFile(CONST.FINISHED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
    return

"""
**************************************************************************
Function Name   :   isValid_eMailAddress()
Author          :   SS. Kanagal.
Description     :   This function checks for invalid eMail address input.
Input Parameters:   email_addr
Return Value    :   Boolean.
Version History :   Dates       Version     Description
                :   31 May,2021 1.0         Initial Release
**************************************************************************
"""
def isValid_eMailAddress(email_addr):
    regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
    return bool(re.search(regex, email_addr))
"""
**************************************************************************
Function Name   :   isValid_Date()
Author          :   SS. Kanagal.
Description     :   This function will check for valid date inputs.
Input Parameters:   log_msg, log_type="info"
Return Value    :   Boolean.
Version History :   Dates       Version     Description
                :   31 May,2021 1.0         Initial Release
**************************************************************************
"""
def isValid_Date(ip_date2Chk, start_dt="", ChkEndDate=False):
    try:
        today_dt = SYSDT.date.today()
        today_dt = str(today_dt.day) + "-" + str(today_dt.month) + "-" + str(today_dt.year)

        ip_date2Chk = SYSDT.datetime.strptime(ip_date2Chk, "%d-%m-%Y")
        today_dt = SYSDT.datetime.strptime(today_dt, "%d-%m-%Y")

        if ip_date2Chk > today_dt:
            print(CONST.INVALID_END_DATE_GR)
            return False
        else:
            if ChkEndDate:
                start_dt = SYSDT.datetime.strptime(start_dt, "%d-%m-%Y")
                if start_dt > ip_date2Chk:
                    print(CONST.INVALID_END_DATE_LR)
                    return False
                else:
                    return True
            else:
                return True
    except ValueError:
        return False

"""
**************************************************************************
Function Name   :   Expunge_eMails()
Author          :   SS. Kanagal.
Description     :   This function deletes/expunge email messages found in
                :   supplied date range.
Input Parameters:   email_addr, email_pwd, start_date, end_date, 
                :   foldername=CONST.FOLDER_NAME
Return Value    :   None.
Version History :   Dates       Version     Description
                :   31 May,2021 1.0         Initial Release
                :   26 Jun,2021 1.6         Final release.
**************************************************************************
"""
def Expunge_eMails(email_addr, email_pwd, start_date, end_date, foldername=CONST.FOLDER_NAME):
    # Build email host server name.
    if CONST.YAHOO_DOMAIN_NAME.lower() in email_addr[email_addr.index("@") + 1:].lower():
        email_host_addr = CONST.YAHOO_IMAP + email_addr[email_addr.index("@") + 1:]
    else:
        email_host_addr = CONST.IMAP_PREFIX + email_addr[email_addr.index("@") + 1:]

    # Convert and change start & end date format as required.
    start_date = SYSDT.datetime.strptime(start_date, "%d-%m-%Y")
    start_date = SYSDT.datetime.strftime(start_date, "%d-%b-%Y")

    end_date = SYSDT.datetime.strptime(end_date, "%d-%m-%Y")
    end_date = SYSDT.datetime.strftime(end_date, "%d-%b-%Y")

    # Login to email host.
    try:
        WriteLogFile(CONST.SYS_CONNECT + "<" + email_addr + ">")
        email_server = IMAP_LIB.IMAP4_SSL(email_host_addr)
        email_server.login(email_addr, email_pwd)
        WriteLogFile(CONST.SYS_CONNECTED)

        WriteLogFile(CONST.SYS_SELE_FOLDER + "<" + foldername + ">")
        email_server.select(foldername)
        WriteLogFile(CONST.SYS_SELED_FOLDER + "<" + foldername + ">")
    except Exception as e:
        ex = str(e.args[0])
        if CONST.IMAP_AUTHEN_FAILED.lower() in ex.lower():
            print(CONST.IMAP_AUTHENTICATION_FAILED)
            User_Quit(True, "\n" + CONST.IMAP_AUTHENTICATION_FAILED)
            exit()
        if CONST.WRONG_IMAP_HOST.lower() in e.args[1].lower():
            print(CONST.WRONG_IMAP_HOST_MSG + " >>> [" + email_host_addr + "]")
            WriteLogFile(CONST.WRONG_IMAP_HOST_MSG + " >>> [" + email_host_addr + "]")
            User_Quit(True, "\n" + CONST.IMAP_AUTHENTICATION_FAILED)
            exit()

    # Build email search string.
    srch_str1 = '(SINCE {0})'.format(start_date)
    srch_str2 = '(BEFORE {0})'.format(end_date)
    srch_str = srch_str1 + " " + srch_str2

    # Selected messages to delete permanently based on dates entered.
    WriteLogFile(CONST.SYS_DT_SEARCH_CRITERIA + "From: " + start_date + " To: " + end_date)
    rep, my_mailbox = email_server.search(None, srch_str)

    # Check if there are any email messages returned from the search.
    if int(len(my_mailbox[0].split())) > 0:
        print(CONST.SYS_MSG_FOUND, int(len(my_mailbox[0].split())))
        WriteLogFile(CONST.SYS_MSG_FOUND + str(len(my_mailbox[0].split())))

        # ---------------------------------------------------------------------------------------
        for items in my_mailbox[0].split():
            # Delete selected messages permanently and log it.
            return_response, deleteitems = email_server.store(items, '+FLAGS', '(\\Deleted)')
            WriteLogFile("Message ID: " + str(items) + " - return_response: " + return_response)
        # ---------------------------------------------------------------------------------------
        WriteLogFile(str(len(my_mailbox[0].split())) + CONST.SYS_EXPUNGED_SUCCESSFULLY + "\n")
    else:
        print(CONST.SYS_MSG_NOTFOUND)
        WriteLogFile(CONST.SYS_MSG_NOTFOUND + "\n")
    pass

"""
**************************************************************************
Function Name   :   GetInputs()
Author          :   SS. Kanagal.
Description     :   This function is called to collect inputs from user 
                :   when there are no Command Line Parameters are passed. 
Input Parameters:   None. 
Return Value    :   List of inputs collected from user.
Version History :   Dates       Version     Description
                :   27 Jun,2021 1.0         Initial Release.
**************************************************************************
"""
def GetInputs():
    # -------------------------------------------------------------------------------------------
    # Get all user inputs. - Start.
    # Get eMail Address.-------------------------------------------------------------------
    no_input = True
    while no_input:
        ip_email_address = input(CONST.EMAIL_ADDR_PRMT)
        if len(ip_email_address) > 0:
            if ip_email_address.lower() == CONST.STOP_CHAR.lower():
                User_Quit()
                exit()

            if not isValid_eMailAddress(ip_email_address):
                print(CONST.INVALID_EMAIL_ADDR)
            else:
                no_input = False
        else:
            print(CONST.EMPTY_EMAIL_ADDR)

    # Get email password.------------------------------------------------------------------
    no_input = True
    while no_input:
        ip_pwd = input(CONST.EMAIL_PWD_PRMT)
        if len(ip_pwd) > 0:
            if ip_pwd.lower() == CONST.STOP_CHAR.lower():
                User_Quit()
                exit()
            no_input = False
        else:
            print(CONST.EMPTY_EMAIL_PWD)

    # Get start date.----------------------------------------------------------------------
    no_input = True
    while no_input:
        ip_start_date = input(CONST.EMAIL_SRCH_START_DT_PRMT)  # '2020-10-31'
        if len(ip_start_date) > 0:
            if ip_start_date.lower() == CONST.STOP_CHAR.lower():
                User_Quit()
                exit()

            # Validate start date.
            if not isValid_Date(ip_start_date):
                print(CONST.INVALID_START_DATE)
            else:
                no_input = False
        else:
            print(CONST.EMPTY_START_DT)

    # Get end date.------------------------------------------------------------------------
    no_input = True
    while no_input:
        print(CONST.END_DATE_RANGE_MSGS)
        ip_end_date = input(CONST.EMAIL_SRCH_END_DT_PRMT)  # '2020-10-31'
        if len(ip_end_date) > 0:
            if ip_end_date.lower() == CONST.STOP_CHAR.lower():
                User_Quit()
                exit()

            # Validate end date.
            if not isValid_Date(ip_end_date, ip_start_date, True):
                pass
            else:
                no_input = False
        else:
            print(CONST.EMPTY_END_DT)
    # Get all user inputs. - End.
    # -------------------------------------------------------------------------------------------
    return (ip_email_address, ip_pwd, ip_start_date, ip_end_date)

"""
**************************************************************************
Function Name   :   DisplayHelpText()
Author          :   SS. Kanagal.
Description     :   This function displays help text on console. 
Input Parameters:   None. 
Return Value    :   None.
Version History :   Dates       Version     Description
                :   27 Jun,2021 1.0         Initial Release.
**************************************************************************
"""
def DisplayHelpText():
    print(CONST.HELP_TEXT)
    pass
