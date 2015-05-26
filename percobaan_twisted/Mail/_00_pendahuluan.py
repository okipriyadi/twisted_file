"""
Twisted comes with support for building clients and servers for the three big email
protocols in common use today: SMTP, IMAP, and POP3.
Each of these protocols has a lot of components and is meticulously documented in
multiple RFCs; covering the ins and outs of mail servers and clients could be a book in
and of itself. The goal for this chapter is instead to give you broad-strokes familiarity
with the protocols and the APIs Twisted provides for them, through some simple but
runnable and tinker-friendly examples. By the end, you should have a good idea of what
you’d need to do to build arbitrary email applications in Twisted.
To describe in brief the main uses for each of these protocols:
SMTP
SMTP, the Simple Mail Transfer Protocol, is for sending mail; when you send an e-
mail from the Gmail web interface, your Thunderbird desktop app, or the mail app
on your smartphone, that message is probably getting sent over SMTP.
IMAP
IMAP, the Internet Message Access Protocol, is used for remote access, storage, and
management of email messages. Remote management makes it easy to read and
send mail from more than one place. The fact that you see the same messages on
your phone, web interface, and desktop app is probably because your email provider
is using IMAP for remote management.
POP3
POP3, the Post Office Protocol version 3, is an older and simpler protocol than
IMAP, but still prevalent. POP3 does one thing, and does it well: it allows a user to
log into a mail server and download her messages, optionally deleting the copies
on the server afterwards. If you’ve ever exported your Gmail mail, it was probably
using POP3.


"""