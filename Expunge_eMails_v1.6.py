"""
**************************************************************************
Script Name     :   Expunge_eMail_v1.6.py
Author          :   SS. Kanagal.
Description     :   This bot deletes all email messages from Inbox on
                :   specified with date range.
Version History :   Dates           Version     Description
                :   22 May,2021     1.0         Initial Release.
                :   01 June,2021    1.5         Final release.
                :   27 June,2021    1.6         Added Command Line Support
**************************************************************************
"""
import Expunge_eMails_Utilities as xUtils
import Expunge_eMails_Constants as CONST
import datetime as SYSDT
import sys as SYSTEM

# Init local variables.
ip_email_address = ""
ip_start_date = ""
ip_end_date = ""
ip_pwd = ""
logfile = ""

if __name__ == '__main__':
    #-------------------------------------------------------------------------------------------
    # Integrate CLP options.
    if len(SYSTEM.argv) > 1:
        # Requested help message.
        if SYSTEM.argv[1].lower() in CONST.HELP_SWITCH.lower():
            xUtils.DisplayHelpText()
            exit()

        if len(SYSTEM.argv) >= 5:
            # Create logfile.
            logfile = xUtils.CreateLogFile()  # ("\Expunge_eMail_Log_")
            xUtils.WriteLogFile(CONST.STARTED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")

            # Validate email address.
            if not xUtils.isValid_eMailAddress(SYSTEM.argv[1]):
                print(CONST.INVALID_EMAIL_ADDR)
                exit()

            # Validate start date.
            if not xUtils.isValid_Date(SYSTEM.argv[3]):
                exit()

            # Validate end date.
            if not xUtils.isValid_Date(SYSTEM.argv[4], SYSTEM.argv[3], True):
                print(CONST.INVALID_END_DATE_GR)
                exit()

        ip_email_address = SYSTEM.argv[1]
        ip_pwd = SYSTEM.argv[2]
        ip_start_date = SYSTEM.argv[3]
        ip_end_date = SYSTEM.argv[4]
    else:
        # Create logfile.
        logfile = xUtils.CreateLogFile()  # ("\Expunge_eMail_Log_")
        xUtils.WriteLogFile(CONST.STARTED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
        print(CONST.WELCOME)
        ip_email_address, ip_pwd, ip_start_date, ip_end_date = xUtils.GetInputs()

    # -------------------------------------------------------------------------------------------
    # Collected all required inputs from user. Call remove/expunge email module.
    xUtils.Expunge_eMails(ip_email_address, ip_pwd, ip_start_date, ip_end_date)
    # -------------------------------------------------------------------------------------------
    # All done. Quit.
    xUtils.WriteLogFile(CONST.FINISHED + str(SYSDT.datetime.now().strftime("%d%m%Y_%H%M")) + "]\n")
    print("~~~ All Done. ~~~")
