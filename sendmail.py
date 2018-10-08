import smtplib
send = smtplib.SMTP('smtp.gmail.com' , 587)
send.ehlo()
send.starttls()
send.login('someshkalyankar@gmail.com' , 'somesh@1501')
send.sendmail('someshkalyankar@gmail.com','someshdk1501@gmail.com', 'Subject: just a hello \n \n hello how are you?')
send.quit()
