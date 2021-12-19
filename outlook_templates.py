import json
import win32com.client as win32
import datetime
import sys
# import os


def create_config_file(name):
    '''
    Creates a Config File template.
    Config files have the information required to prepare the email. 
    '''

    with open(name, 'w') as f:

        data = {'to': 'test@test.com',
                'cc': 'test@test.com',
                'bcc': 'test@test.com',
                'subject': 'Test Email <today>',
                'body': 'Test Email <today>',
                'attachments': ["C:\\Users\\User\Documents\TestFile.txt", "C:\\Users\\User\Documents\TestFile2.txt"]}

        json.dump(data, f, indent=6)


def prepare_email(json_file):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    with open(json_file, 'r') as f:
        attr = json.load(f)

    print(attr, end='\n\n')

    today = datetime.datetime.today().strftime("%m/%d/%Y")

    mail.To = attr['to']
    mail.CC = attr['cc']
    mail.BCC = attr['bcc']
    mail.Subject = attr['subject'].replace('<today>', today)
    mail.Body = attr['body'].replace('<today>', today)

    for attachment in attr['attachments']:
        try:
            # Verify if file exists.
            with open(attachment, 'r') as f:
                pass
            mail.Attachments.Add(attachment.replace('<today>', today))
        except:
            print(f'File {attachment} was not found. Attachment FAILED')

    mail.display(True)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = r"C:\Users\pdcur\Desktop\Outlook Auto Email script\config_file.email-config"

    prepare_email(config_file)
