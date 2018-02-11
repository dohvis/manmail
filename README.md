# Manmail

_Name is inspired by [mailman](http://www.list.org/)_

Send e-mail, easier

## How to use

`pip install git+https://github.com/nerogit/manmail.git`

```python
from manmail import Gmail


email_addrs = 'YOUR_EMAIL_ADDRESS'
password = 'USER_PASSWORD_OF_EMAIL_ACCOUNT'
to_addrs = 'EMAIL_ADDRESS_WHO_RECEIVE_THE_MAIL'

gmail = Gmail(email_addrs, password)
content = '''
<h1>Hello</h1>
<p>It's me</p>
'''
gmail.send_mail(to_addrs, 'title', content)

```
