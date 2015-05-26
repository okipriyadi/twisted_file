"""
The standard protocol for sending mail on the Internet is the Simple Mail Transfer
Protocol (SMTP). SMTP allows one computer to transfer email messages to another
computer using a standard set of commands. Mail clients use SMTP to send outgoing
messages, and mail servers use SMTP to forward messages to their final destination.
The current specification for SMTP is defined in RFC 2821.
"""

import os, sys
from email.mime.text import MIMEText
from twisted.internet import reactor
from twisted.mail.smtp import sendmail
from twisted.python import log
log.startLogging(sys.stdout)
host = "localhost"
sender = "secretadmirer@example.com"
recipients = ["recipient@localhost"]
msg = MIMEText("""Violets are blue
                Twisted is helping
                Forge e-mails to you!
                """)
msg["Subject"] = "Roses are red"
msg["From"] = '"Secret Admirer" <%s>' % (sender,)
msg["To"] = ", ".join(recipients)
deferred = sendmail(host, sender, recipients, msg.as_string(), port=2500)
deferred.addBoth(lambda result: reactor.stop())
reactor.run()