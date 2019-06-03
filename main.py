import dns.resolver
import socket
import smtplib

# 
email_verify = ''
domain = ''
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

# Get local server hostname
host = socket.gethostname()
print('connecting mx {0}, from host {1}'.format(mxRecord, host))

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('me@domain.com')
code, message = server.rcpt(str(email_verify))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')