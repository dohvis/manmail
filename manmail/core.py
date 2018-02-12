import smtplib
from email.mime.text import MIMEText


class ManMail:
    def __init__(self, provider, sender_email_address, password):
        provider_stmp_servers = {
            'gmail': ('smtp.gmail.com', 465)
        }
        self.sender_email_address = sender_email_address
        try:
            host, port = provider_stmp_servers[provider]
        except KeyError:
            raise KeyError("Unsupported provider: {}".format(provider))
        self.server = smtplib.SMTP_SSL(host, port)
        self.server.ehlo()
        self.server.login(sender_email_address, password)

    def send_mail(self, to_addrs, subject, msg):
        """
        :param to_addrs: A list of addresses to send this mail to.
                            string will be treated as a list with 1 address.
        :param subject:
        :param msg:
        :return:
        """

        mail = MIMEText(msg, 'html', 'utf-8')
        mail['From'] = self.sender_email_address
        mail['Subject'] = subject

        mail['To'] = to_addrs
        mail = mail.as_string()
        self.server.sendmail(self.sender_email_address, to_addrs, mail)

        self.server.close()


class Gmail(ManMail):
    def __init__(self, username, password):
        super(Gmail, self).__init__('gmail', username, password)
