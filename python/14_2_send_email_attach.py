import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def listization(data):
    if isinstance(data, list):
        return data
    else:
        return [data]

def send_email(sender,
               recv_addr_list,
               cc_addr_list,
               bcc_addr_list,
               subject,
               body,
               files_path,
               user_id,
               user_pwd):
    message = MIMEMultipart()
    message['FROM']=sender
    message['TO']=", ".join(listization(recv_addr_list))
    message['CC'] = ", ".join(listization(cc_addr_list))
    message['BCC'] = ", ".join(listization(bcc_addr_list))
    message['SUBJECT'] = subject

    message.attach(MIMEText(body))


    for paths, folders, files in os.walk(files_path):
        for file in files:
            file_path=os.path.join(paths, file)
            print("Attachment:: %s"%file_path)
            part=MIMEBase('application', 'octet-stream')
            with open(file_path, 'rb') as open_file:
                part.set_payload(open_file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}'.format(os.path.basename(file_path)))
            message.attach(part)


    TO=listization(recv_addr_list) + listization(cc_addr_list) + listization(bcc_addr_list)
    try:
        with smtplib.SMTP_SSL('64.233.184.108', 465) as SMTP_SERVER:
            SMTP_SERVER.ehlo()
            SMTP_SERVER.login(user_id, user_pwd)
            SMTP_SERVER.sendmail(sender, TO, message.as_string())
            return "SUCCESS TO SEND THE EMAIL TO %s"%TO
    except Exception as ex:
        return "FAIL TO SEND THE EMAIL TO {} ::{}\n".format(TO, ex)

def main():
    msg=send_email(sender='',
               recv_addr_list=[''],
               cc_addr_list='',
               bcc_addr_list='',
               subject='attachment test',
               body='hello this is practice python for sending email with attachment',
               files_path='D:\\workspaces\\python_study\\attachment',   # folder
               user_id='',
               user_pwd='')
    print(msg)



if __name__=="__main__":
    main()