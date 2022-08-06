import smtplib
my_email = "testingemail@gmail.com"
password = "123456"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = password)

connection.sendmail(from_addr = my_email,
to_addrs = "receipentemail@yahoo.com", msg = "Hello World")

connection .close()