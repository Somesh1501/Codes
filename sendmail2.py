import smtplib ,webbrowser
def get_mail():
    servicesAvailable  = ['hotmail' , 'yahoo' ,'gmail']
    while True:
        mail_id = input('E-mail :')
        if '@' in mail_id and '.com' in mail_id:
            #someshkalyankar@gmail.com
             symbol_pos = mail_id.find('@')
             dotcom_pos = mail_id.find('.com')
             sp = mail_id[symbol_pos+1:dotcom_pos]
             if sp in servicesAvailable:
                 return mail_id , sp
                 #tuple
                 #(someshkalyankar@gmail.com)
                 break
             else:
                 print("we don't provide service for " + sp)
                 print("we only provide services for  Yahoo, Outlook/hotmail, gmail")
                 continue
        else:
            print("invalid E-mail retype again ")
            continue

def set_smtp(serviceProvider):
    if serviceProvider =='gmail':
        return 'smtp.gmail.com'
    elif serviceProvider =='yahoo':
        return 'smtp.yahoo.com'
    elif serviceProvider =='hotmail':
        return 'smtp.outlook.com'
    elif serviceProvider:
        return 'smtp.outlook.com'

print('Welcome, You can send email through this program')
print('enter your email and password ')
e_mail , serviceProvider = get_mail()
password = input('password:')

while True:
    try:
        smtpdomain = set_smtp(serviceProvider)
        connection = smtplib.SMTP(smtpdomain)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail, password)
    except:

        if serviceProvider == 'gmail':
            print('Login unsuccessfull , there are two possible reasons')
            print('1. You typed wrong username or password')
            print('2. You are using gmail there is an option "allow less secure apps" ')
            print('Do you allow us to open web ')
            ans = input('yes/no')
            if ans == 'yes':
                webbrowser.open('https://myaccount.google.com/lesssecureapps')
            else:
                print('we are unable to open webpage please go to "https://myaccount.google.com/lesssecureapps" and enable less secure apps.')
                print('please retype your email and password')
                e_mail , serviceProvider= get_mail()
                password = input('password :')
                continue
        else:
            print('Login successfull')
            break
print('Please type receivers E-mail address  ')
receiverAddress , receiverSP = get_mail()
print('Now please type Subject and Message')
subject = input('Subject :  ')
message = input('Message :  ')
connection.sendmail(e_mail , receiverAddress , ('Subject: ' + str(subject) + '\n\n' + str(message)))
print('E-mail send successfully')
connection.quit()



 





