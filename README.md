# rpiemail

## Preliminary

- Create gmail account.
- Go to `Manage your Google Account > Security`.
- Enable two step `2-Step Verification`.
- Go to `App passwords` and select `other` from the dropdown.
- Choose an appropriate name and press `Generate`.
- Copy and save that generated password.

## Setup

### Create files

```
cd /path/to/folder
touch ip.txt fields.py
```

### Modify fields.py

```
Sender = {

  "addr": "<The email you created>",
  "pass": "<The password that was genereated above>", # 16 characters long
  "serv": "smtp.gmail.com",
  "port": 465

}

Receiver = {
  "addr": [] # List of email you want to send to
}

ipfile = "</full/path/to/ip.txt>"
```

