import email
import imaplib
import getpass

user_email = getpass.getpass("Email:")
password = getpass.getpass("Password:")

M = imaplib.IMAP4_SSL("imap.gmail.com")
M.login(user_email, password)
# print(M.list())
print(M.select("inbox"))

typ, data = M.search(None, 'SUBJECT "Hello from email_smtp.py"')
print("\n", typ, data)
email_id = data[0]
result, email_data = M.fetch(data[0], "(RFC822)")  # protocol for second argument
print("\nresult:", result)
# print("\nemail_data:", email_data)

raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")
print("\n\nraw_email_string:\n")
print(raw_email_string)

email_message = email.message_from_string(raw_email_string)

print("\n\nbody:\n")
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
