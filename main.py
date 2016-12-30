import poplib
#added to increase capacity  for reconstructed message
poplib._MAXLINE=30720

import email
from email.parser import Parser
from keywords import *

debug = 'debug.txt'
file_delete = "delete.txt"
file_notdeleted = "notdeleted.txt"
fhd = open(debug,'w')
fh = open(file_delete,'w')
fh2 = open(file_notdeleted,'w')

pop_conn = poplib.POP3_SSL()
pop_conn.user()
pop_conn.pass_()

keywords = loadkeywords()
delete = 0 
totalemails = 0

(numMsgs, totalSize) = pop_conn.stat()

for number in range(numMsgs-1,numMsgs-2,-1):
	totalemails += 1
	(server_msg, body, octets) = pop_conn.retr(number)
	newbody = '\n'.join(map(str,body))
	fhd.write(newbody)
	headers = Parser().parsestr(newbody)
	print(headers)
	total = 0

	for key, value in keywords.items():
		if headers['from'] is not None:
			if key.lower() in headers['from'].lower():
				total += int(value)
		if headers['subject'] is not None:
			if key.lower() in headers['subject'].lower():
				total += int(value)
		if headers['return-path'] is not None:
			if key.lower() in headers['return-path'].lower():
				total += int(value)

	if total > 0:
		delete += 1
		#pop_conn.dele(number)
		fh.write('Record ID: %s\n' % number)
		fh.write('From: %s\n' % headers['from'])
		fh.write('Subject: %s\n' % headers['subject'])
		fh.write('Return: %s\n' % headers['return-path'])
		fh.write('Total: %s\n' % total)
		fh.write('-'*120)
		fh.write('\n')		
	else:
		print('Record ID: %s' % number)
		print('From: %s' % headers['from'])
		print('Subject: %s' % headers['subject'])
		print('Return: %s' % headers['return-path'])
		print('Total: %s\n' % total)

		fh2.write('Record ID: %s\n' % number)
		fh2.write('From: %s\n' % headers['from'])
		fh2.write('Subject: %s\n' % headers['subject'])
		fh2.write('Return: %s\n' % headers['return-path'])
		fh2.write('Total: %s\n' % total)
		fh2.write('-'*60)
		fh2.write('\n')

print('Total emails processed: %s' % totalemails)
print('Total emails deleted: %s' % delete)

fh.write('Total emails processed: %s\n' % totalemails)
fh.write('Total emails deleted: %s\n' % delete)

pop_conn.quit()