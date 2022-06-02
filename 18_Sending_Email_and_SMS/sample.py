import ezgmail, os, smtplib, imapclient, pyzmail, pprint
# Enabling the Gmail API
os.chdir(r'credentials.json')

# ezgmail.init()

############################################################################################################

# Sending Mail from a Gmail Account

# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')
# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', ['attachment1.jpg', 'attachment2.mp3'])
# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')
# ezgmail.EMAIL_ADDRESS

############################################################################################################

# Reading Mail from a Gmail Account

# unreadThreads = ezgmail.unread() # List of GmailThread objects.
# print(ezgmail.summary(unreadThreads))

# len(unreadThreads)
# str(unreadThreads[0])
# len(unreadThreads[0].messages)
# str(unreadThreads[0].messages[0])
# unreadThreads[0].messages[0].subject
# unreadThreads[0].messages[0].body
# unreadThreads[0].messages[0].timestamp
# unreadThreads[0].messages[0].sender
# unreadThreads[0].messages[0].recipient

# recentThreads = ezgmail.recent()
# len(recentThreads)

# recentThreads = ezgmail.recent(maxResults=100)
# len(recentThreads)

############################################################################################################

# Searching Mail from a Gmail Account

# resultThreads = ezgmail.search('RoboCop')
# len(resultThreads)
# ezgmail.summary(resultThreads)

############################################################################################################

# Downloading Attachments from a Gmail Account

# threads = ezgmail.search('vacation photos')
# threads[0].messages[0].attachments
# threads[0].messages[0].downloadAttachment('tulips.jpg')
# threads[0].messagse[0].downloadAllAttachment(downloadFolder='vacation2019')

############################################################################################################

# Sending Email

smtpObj = smtplib.SMTP('smpt.example.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
# smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long. \nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
# smtpObj.quit()

############################################################################################################

# Connecting to an SMTP Server

# Provider                          SMTP server domain name
# Gmail*                            smtp.gmail.com
# Outlook.com/Hotmail.com*          smtp-mail.outlook.com
# Yahoo Mail*                       smtp.mail.yahoo.com
# AT&T                              smpt.mail.att.net (port 465)
# Comcast                           smtp.comcast.net
# Verizon                           smtp.verizon.net (port 465)

# *Additional security measures prevent Python from being able to log in to these servers with the smtplib module. The EZGmail module can bypass this difficulty for Gmail accounts.

# smtpObj = smtplib.SMTP('smtp.example.com', 587)
# type(smtpObj)

############################################################################################################

# Sending the SMTP "Hello" Message

# smtpObj.ehlo()

############################################################################################################

# Starting TLS Encryption

# smtpObj.starttls()

############################################################################################################

# Logging In to the SMTP Server

# smtpObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')

############################################################################################################

# Sending an Email

# smtpObj.sendmail('my_email_address@example.com', 'recipient@example.com', 'Subject: So long. \nDear Alice, so long and thanks for all the fish.. Sincerely, Bob')

############################################################################################################

# Disconnecting from the SMTP Server

# smtpObj.quit()

############################################################################################################

# Retrieving and Deleting Emails with IMAP

# imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
# imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
# imapObj.select_folder('INBOX', readonly=True)
# UIDs = imapObj.search(['SINCE 05-Jul-2019'])
# print(UIDs)
# rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
# message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
# message.get_subject()
# message.get_addresses('from')
# message.get_addresses('to')
# message.get_addresses('cc')
# message.get_addresses('bcc')
# message.text_part != None
# message.text_part.get_payload().decode(message.text_part.charset)
# message.html_part != None
# message.html_part.get_payload().decode(message.html_part.charset)
# imapObj.logout()

############################################################################################################

# Connecting to an IMAP Server

# Provider                        IMAP server domain name
# Gmail*                          imap.gmail.com
# Outlook.com/Hotmail.com*        imap-mail.outlook.com
# Yahoo Mail*                     imap.mail.yahoo.com
# AT&T                            imap.mail.att.net
# Comcast                         imap.comcast.net
# Verizon                         incoming.verizon.net
# *Additional security measures prevent Python from being able to log in to these servers with the imapclient module.

imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)

############################################################################################################

# Logging In to the IMAP Server

# imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')

############################################################################################################

# Selecting a Folder

# pprint.pprint(imapObj.list_folders())
# imapObj.select_folder('INBOX', readonly=True)

############################################################################################################

# Performing the Search

#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
# Search key        |   Meaning                                                                                                                                                                                                                                                                                                                                                                 |
# 'ALL'             |   Returns all messages in the folder. You may run into imaplib size limits if you request all the messages in a large folder.                                                                                                                                                                                                                                             |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'BEFORE date',    |                                                                                                                                                                                                                                                                                                                                                                           |
# 'ON date',        |   These three search keys return, respectively, messages that were received by the IMAP server before, on, or after the given date. The date must be formatted like 05-Jul-2019. Also, while 'SINCE 05-Jul-2019' will match messages on and after July 5, 'BEFORE 05-Jul-2019' will match only messages before July 5 but not on July 5 itself.                           |
# 'SINCE date'      |                                                                                                                                                                                                                                                                                                                                                                           |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'SUBJECT string', |                                                                                                                                                                                                                                                                                                                                                                           |
# 'BODY string',    |   Returns messages where string is found in the subject, body, or either, respectively. If string has spaces in it, then enclose it with double quotes: 'TEXT "search with spaces"'.                                                                                                                                                                                      |
# 'TEXT string'     |                                                                                                                                                                                                                                                                                                                                                                           |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'FROM string',    |                                                                                                                                                                                                                                                                                                                                                                           |
# 'TO string',      |                                                                                                                                                                                                                                                                                                                                                                           |
# 'CC string',      |   Returns all messages where string is found in the “from” email address, “to” addresses, “cc” (carbon copy) addresses, or “bcc” (blind carbon copy) addresses, respectively. If there are multiple email addresses in string, then separate them with spaces and enclose them all with double quotes: 'CC "firstcc@example.com secondcc@example.com"'.                   |
# 'BCC string'      |                                                                                                                                                                                                                                                                                                                                                                           |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'SEEN',           |                                                                                                                                                                                                                                                                                                                                                                           |
# 'UNSEEN'          |   Returns all messages with and without the \Seen flag, respectively. An email obtains the \Seen flag if it has been accessed with a fetch() method call (described later) or if it is clicked when you’re checking your email in an email program or web browser. It’s more common to say the email has been “read” rather than “seen,” but they mean the same thing.    |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'ANSWERED',       |                                                                                                                                                                                                                                                                                                                                                                           |
# 'UNANSWERED'      |   Returns all messages with and without the \Answered flag, respectively. A message obtains the \Answered flag when it is replied to.                                                                                                                                                                                                                                     |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'DELETED',        |                                                                                                                                                                                                                                                                                                                                                                           |
# 'UNDELETED'       |   Returns all messages with and without the \Deleted flag, respectively. Email messages deleted with the delete_messages() method are given the \Deleted flag but are not permanently deleted until the expunge() method is called (see “Deleting Emails” on page 432). Note that some email providers automatically expunge emails.                                      |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                        
# 'DRAFT',          |                                                                                                                                                                                                                                                                                                                                                                           |
# 'UNDRAFT'         |   Returns all messages with and without the \Draft flag, respectively. Draft messages are usually kept in a separate Drafts folder rather than in the INBOX folder                                                                                                                                                                                                        |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'FLAGGED',        |                                                                                                                                                                                                                                                                                                                                                                           |
# 'UNFLAGGED'       |   Returns all messages with and without the \Flagged flag, respectively. This flag is usually used to mark email messages as “Important” or “Urgent.”                                                                                                                                                                                                                     |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'LARGER N',       |                                                                                                                                                                                                                                                                                                                                                                           |
# 'SMALLER N'       |   Returns all messages larger or smaller than N bytes, respectively                                                                                                                                                                                                                                                                                                       |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'NOT search-key'  |   Returns the messages that search-key would not have returned.                                                                                                                                                                                                                                                                                                           |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# 'OR search-key1   |                                                                                                                                                                                                                                                                                                                                                                           |
# search-key2'      |   Returns the messages that match either the first or second search-key.                                                                                                                                                                                                                                                                                                  |
#-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

# Here are some example search() method calls along with their meanings:

# imapObj.search(['ALL'])                                                 Returns every message in the currently selected folder.
# imapObj.search(['ON 05-Jul-2019'])                                      Returns every message sent on July 5, 2019.
# imapObj.search(['SINCE 01-Jan-2019', 'BEFORE 01-Feb-2019', 'UNSEEN'])   Returns every message sent in January 2019 that is unread. (Note that this means on and after January 1 and up to but not including February 1.)
# imapObj.search(['SINCE 01-Jan-2019', 'FROM alice@example.com'])         Returns every message from alice@example.com sent since the start of 2019.
# imapObj.search(['SINCE 01-Jan-2019', 'NOT FROM alice@example.com'])     Returns every message sent from everyone except alice@example.com since the start of 2019.
# imapObj.search(['OR FROM alice@example.com FROM bob@example.com'])      Returns every message ever sent from alice@example.com or bob@example.com.
# imapObj.search(['FROM alice@example.com', 'FROM bob@example.com'])      Trick example! This search never returns any messages, because messages must match all search keywords. Since there can be only one “from” address, it is impossible for a message to be from both alice@example.com and bob@example.com.

UIDs = imapObj.search(['SINCE 05-Jul-2019'])
# print(UIDs)

############################################################################################################

# Size Limits

# imaplib._MAXLINE = 10000000

############################################################################################################

# Fetching an Email and Marking It as Read

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# pprint.pprint(rawMessages)
# imapObj.select_folder('INBOX', readonly=False)

############################################################################################################

# Getting Email Addresses from a Raw Message

message = pyzmail.PysMessage.factory(rawMessages[40041][b'BODY[]'])

# message.get_subject()
# message.get_addresses('from')
# message.get_addresses('to')
# message.get_addresses('cc')
# message.get_addresses('bcc')

############################################################################################################

# Getting the Body from a Raw Message

# message.text_part != None
# message.text_part.get_payload().decode(message.text_part.charset)
# message.html_part != None
# message.html_part.get_payload().decode(message.html_part.charset)

############################################################################################################

# Deleting Emails

# imapObj.select_folder('INBOX', readonly=False)
# UIDs = imapObj.search(['ON 09-Jul-2019'])
# print(UIDs)
# imapObj.delete_messages(UIDs)
# imapObj.expunge()

############################################################################################################

# Disconnecting from the IMAP Server

# imapObj.logout()

############################################################################################################

# Sending Text Messages with SMS Email Gateways

# Cell phone provider           SMS gateway                             MMS gateway
# AT&T                          number@txt.att.net                      number@mms.att.net
# Boost Mobile                  number@sms.myboostmobile.com            Same as SMS
# Cricket                       number@sms.cricketwireless.net          number@mms.cricketwireless.net
# Google Fi                     number@msg.fi.google.com                Same as SMS
# Metro PCS                     number@mymetropcs.com                   Same as SMS
# Republic Wireless             number@text.republicwireless.com        Same as SMS
# Sprint                        number@messaging.sprintpcs.com          number@pm.sprint.com
# T-Mobile                      number@tmomail.net                      Same as SMS
# U.S. Cellular                 number@email.uscc.net                   number@mms.uscc.net
# Verizon                       number@vtext.com                        number@vzwpix.com
# Virgin Mobile                 number@vmobl.com                        number@vmpix.com
# XFinity Mobile                number@vtext.com                        number@mypixmessages.com

############################################################################################################

# from twilio.rest import Client

# accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxx'
# authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# twilioCli = Client(accountSID, authToken)
# myTwilioNumber = '+14955551234'
# myCellPhone = '+14955558888'
# message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)

# message.to
# message.from_
# message.body
# message.status
# message.date_created
# message.date_sent == None
# message.sid
# updatedMessage = twilioCli.messages.get(message.sid)
# updatedMessage.status
# updatedMessage.date_sent
