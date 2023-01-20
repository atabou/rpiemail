import os
import smtplib
from socket import gaierror
from fields import Sender, Receiver, ipfile


def get_ip_address():

    ip_address = os.popen("/usr/sbin/ifconfig wlan0 | /usr/bin/grep -o 'inet [0-9]*\.[0-9]*\.[0-9]*\.[0-9]*' | /usr/bin/grep -o '[0-9].*'").read()
    ip_address = ip_address[:len(ip_address) - 1:]

    return ip_address

ip = get_ip_address()

fp = open(ipfile, "r+")

old_ip = fp.read().split("\n")[0]

if old_ip != ip:

    fp.seek(0)

    fp.write(ip)

    if ip == "":
        ip = "No address found"

    subject = "IP: {}".format(ip)

    TO = Receiver["addr"]
    FROM = Sender["addr"]
    BODY = "{}".format(ip)

    try:
        server = smtplib.SMTP_SSL(Sender['serv'], Sender['port'])
        server.login(Sender["addr"], Sender["pass"])
        server.sendmail(FROM, TO, BODY)
        server.quit()

    except smtplib.SMTPAuthenticationError:
        print("Username or Password.")

    except gaierror:
        print("Insure valid smtp server.")

fp.close()
