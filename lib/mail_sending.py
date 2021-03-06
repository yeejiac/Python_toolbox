import configparser
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
import smtplib, ssl
from iniparser import *
from logwriter import *
from getpass import getpass


class Mailsending_Base:
    def __init__(self, receiver_mail, title, mail_context):
        self.context = ssl.create_default_context()
        self.receiver_mail = receiver_mail
        self.title = title
        self.mail_context = mail_context

    def send_mail(self):
        try:
            server = smtplib.SMTP(smtp_server, mail_port)
            server.ehlo() 
            server.starttls(context=self.context)
            server.ehlo()
            # password = getpass("Type your password and press enter: ")
            server.login(mail_addr, mail_password)
            server.sendmail(mail_addr, self.receiver_mail, self.mail_context)
            logger.debug("MailSending: sending success")
        except Exception as e:
            # Print any error messages to stdout
            logger.error(e)
        finally:
            server.quit() 

if __name__ == '__main__':
    mail_sending = Mailsending_Base("yeejiac@gmail.com", "error", "errorLog Occur from CPP project")
    mail_sending.send_mail()