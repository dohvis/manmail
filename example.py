from manmail import Gmail


def main():
    email_addrs = 'YOUR_EMAIL_ADDRESS'
    password = 'USER_PASSWORD_OF_EMAIL_ACCOUNT'
    to_addrs = 'EMAIL_ADDRESS_WHO_RECEIVE_THE_MAIL'

    gmail = Gmail(email_addrs, password)
    content = '''
    <h1>Hello</h1>
    <p>It's me</p>
    '''
    gmail.send_mail(to_addrs, 'title', content)


if __name__ == '__main__':
    main()
