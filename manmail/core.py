import smtplib


class ManMail:
    email_template = """From: {}
To: {}
Subject: {}
Content-Type: text/html; charset=utf-8

{}
"""

    def __init__(self, provider, email_addrs, password):
        provider_stmp_servers = {
            'gmail': ('smtp.gmail.com', 465)
        }
        self.email_addrs = email_addrs
        try:
            host, port = provider_stmp_servers[provider]
        except KeyError:
            raise KeyError("Unsupported provider: {}".format(provider))
        self.server = smtplib.SMTP_SSL(host, port)
        self.server.ehlo()
        self.server.login(email_addrs, password)

    def send_mail(self, to_addrs, subject, content):
        """
        :param to_addrs: A list of addresses to send this mail to.
                            string will be treated as a list with 1 address.
        :param subject:
        :param content:
        :return:
        """
        content = self.email_template.format(self.email_addrs, to_addrs, subject, msg)
        self.server.sendmail(self.email_addrs, to_addrs, content)

        self.server.close()


class Gmail(ManMail):
    def __init__(self, username, password):
        super(Gmail, self).__init__('gmail', username, password)
