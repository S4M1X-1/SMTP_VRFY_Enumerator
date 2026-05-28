# SMTP VRFY Enumerator

---

## Description

SMTP VRFY Enumerator is a Python tool that connects to an SMTP server and uses the `VRFY` command to check if a user exists on the mail server.

It supports:
- Single user mode
- Bulk enumeration from a file

---

## Features

- SMTP banner grabbing
- User verification via VRFY
- File-based enumeration
- Error handling
- Timeout protection

---

## How It Works

The script connects to port 25 (SMTP) and sends:

VRFY username

The server may respond:
- User exists (250)
- User not found (550)
- VRFY disabled (252)

---

## Requirements

- Python 3.x
- No external libraries required

---

## Installation

git clone https://github.com/S4M1X-1/SMTP_VRFY_Enumerator.git  
cd SMTP_VRFY_Enumerator

---

## Usage

### Single user mode

python3 smtp-enum.py <IP> <USER>

Example:

python3 smtp-enum.py 192.168.1.10 admin  

---

### File mode (bulk enumeration)

python3 smtp-enum.py <IP> -f users.txt  

Example:

python3 smtp-enum.py 192.168.1.10 -f users.txt  

---

## Example users.txt

admin  
root  
test  
support  
info  
mail  
john  

---

## Example Output

[+] Connected to 192.168.1.10:25  
[+] SMTP Banner: 220 mail.server.com ESMTP Postfix  

[+] Verifying user: admin  
[+] Response: 250 2.1.5 admin exists  

---

## Common SMTP Responses

| Code | Meaning |
|------|--------|
| 250  | User exists |
| 550  | User does not exist |
| 252  | Cannot verify user |

---

## Disclaimer

This tool is for:
- Educational purposes
- Authorized security testing
- Security research

Do NOT use it against systems you don’t own or have permission to test.

---

## License

MIT License
