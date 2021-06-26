"""
**************************************************************************
Script Name     :   Expunge_eMail_v1.5.py
Author          :   SS. Kanagal.
Description     :   This bot deletes all email messages from Inbox on
                :   specified date range.
Version History :   Dates           Version     Description
                :   22 May,2021     1.0         Initial Release.
                :   01 June,2021    1.5         Final release.
**************************************************************************
"""
import Expunge_eMails_Utilities as xUtils
import datetime as SYSDT
import Expunge_eMails_Constants as CONST


# Create logfile.
logfile = xUtils.CreateLogFile()

# Init local variables.
ip_email_address = ""
ip_start_date = ""
ip_end_date = ""
ip_pwd = ""

if __name__ == '__main__':
    xUtils.WriteLogFile(CONST.STARTED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
    print(CONST.WELCOME)

    #-------------------------------------------------------------------------------------------
    # Get all user inputs. - Start.
    # Get email Address.-------------------------------------------------------------------
    no_input = True
    while no_input:
        ip_email_address = input(CONST.EMAIL_ADDR_PRMT)
        if len(ip_email_address) > 0:
            if ip_email_address.lower() == CONST.STOP_CHAR.lower():
                xUtils.User_Quit()
                exit()

            if not xUtils.isValid_eMailAddress(ip_email_address):
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
                xUtils.User_Quit()
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
                xUtils.User_Quit()
                exit()

            # Validate start date.
            if not xUtils.isValid_Date(ip_start_date):
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
                xUtils.User_Quit()
                exit()

            # Validate end date.
            if not xUtils.isValid_Date(ip_end_date, ip_start_date, True):
                pass
                # print(CONST.INVALID_END_DATE_GR)
            else:
                no_input = False
        else:
            print(CONST.EMPTY_END_DT)

    # Get all user inputs. - End.
    # -------------------------------------------------------------------------------------------
    # Collected all required inputs from user. Call remove/expunge email module.
    xUtils.Expunge_eMails(ip_email_address, ip_pwd, ip_start_date, ip_end_date)
    # -------------------------------------------------------------------------------------------
    # All done. Quit.
    xUtils.WriteLogFile(CONST.FINISHED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
    print("~~~ All Done. ~~~")
