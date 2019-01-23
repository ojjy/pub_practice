def send_email(sender_id, sender_pwd, recv_addr_list, cc_addr_list, bcc_addr_list, title, body):
    import smtplib

    FROM=sender_id
    TO=recv_addr_list
    CC=cc_addr_list
    BCC=bcc_addr_list
    SUBJECT=title
    CONTENTS=body


    header="FROM: %s\r\n" % FROM + \
            "TO: %s\r\n" % ", ".join(TO) + \
            "CC: %s\r\n" % ", ".join(CC) + \
            "BCC: %s\r\n" % ", ".join(BCC) + \
            "SUBJECT: %s\r\n" % SUBJECT
    message=header+"CONTENTS: %s\r\n" % CONTENTS

    print(message)
    TO=TO+CC+BCC


    # try:
    #     with smtplib.SMTP_SSL('smtp.google.com', 465) as SMTP_SERVER:
    #         SMTP_SERVER.ehlo()
    #         SMTP_SERVER.login(sender_id, sender_pwd)
    #         SMTP_SERVER.sendmail(FROM, TO, message)
    #         return "SUCCESS TO SEND THE EMAIL TO {}".format(TO)
    #
    # except Exception as ex:
    #     return "FAIL TO SEND THE EMAIL TO {} :: {}".format(TO, ex)
    with smtplib.SMTP_SSL('64.233.184.108', 465) as SMTP_SERVER:
         SMTP_SERVER.ehlo()
         SMTP_SERVER.login(sender_id, sender_pwd)
         SMTP_SERVER.sendmail(FROM, TO, message)
         return "SUCCESS TO SEND THE EMAIL TO {}".format(TO)


def main():
    msg=send_email(sender_id='',
                   sender_pwd='',
                   recv_addr_list=[''],
                   cc_addr_list=[''],
                   bcc_addr_list=[''],
                   title='',
                   body='I am sending an email for practice python\nI can do everything ' +\
                        'through him who give me strengthen\nPhilippians4:13\n')
    print(msg)


if __name__=="__main__":
    main()