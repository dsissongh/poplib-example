# poplib-example
Python poplib example

This is a simple example of the poplib module connecting to an SSL secured email account, reading the messages and deleting 
messages that contain the words or phrases from the keywords file.

This is a very basic and early attempt to scan an email account and quickly remove "obvious" spam.  The keywords dictionary has a numeric 
value attached to each keyword or phrase. The intent at some point is to calculate the value of emails based on these headers and make 
decisions based on those values.

Be careful to review what emails get "flagged" before enabling the ability to delete. 

