# rpimail

Application that sends by email the updated local ip address of the rpi whenever it changes.
A cronjob is setup to run every minute.
If the ip has changed, it sends an email containing the new ip address.
Otherwise it does nothing.

## Preliminary

Setup and email account to use for sending emails from the rpi.

- Create gmail account.
- Go to `Manage your Google Account > Security`.
- Enable two step `2-Step Verification`.
- Go to `App passwords` and select `other` from the dropdown.
- Choose an appropriate name and press `Generate`.
- Copy and save that generated password.

## Setup

### Create files

Add the required non-included files.

```
cd /path/to/folder && touch ip.txt fields.py
```

### Modify fields.py

Specify import fields in the non-included fields.py file.

```(python)
Sender = {

  "addr": "<The email you created>",
  "pass": "<The password that was generated above>", # 16 characters long
  "serv": "smtp.gmail.com",
  "port": 465

}

Receiver = {
  "addr": [] # List of email you want to send to
}

ipfile = "</full/path/to/ip.txt>"
```

### Setup crontab

Setup rpimail.py as a cronjob that runs every minute.

- Execute `crontab -e`
- Choose your editor (1, 2, or 3, ...)
- Append to the end of the file `* * * * * python <path/to/rpimail.py>`

