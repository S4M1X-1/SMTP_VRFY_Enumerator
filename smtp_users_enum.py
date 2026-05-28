#!/usr/bin/env python3

# ============================================================================
# SMTP VRFY Enumerator
# Author: S4m1X
#
# Description:
# This script connects to an SMTP server (port 25) and uses the VRFY command
# to check if a user exists on the mail server.
#
# Features:
# - Single user check
# - Bulk user enumeration from a file
# - SMTP banner capture
# - Error handling
# - Timeout support
#
# Educational purpose only.
# ============================================================================

import socket
import sys


def vrfy_user(ip, user):
    """
    Connects to SMTP server and checks if a given user exists
    using the VRFY command.
    """

    try:
        # Create a TCP socket (IPv4, stream-based connection)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout to avoid hanging connections
        s.settimeout(5)

        # Connect to SMTP service on port 25
        s.connect((ip, 25))

        # Receive SMTP banner (server welcome message)
        banner = s.recv(1024).decode().strip()

        print(f"\n[+] Connected to {ip}:25")
        print(f"[+] SMTP Banner: {banner}")

        # Build VRFY command according to SMTP protocol
        command = f"VRFY {user}\r\n"

        print(f"[+] Verifying user: {user}")

        # Send VRFY command to the server
        s.send(command.encode())

        # Receive server response
        result = s.recv(1024).decode().strip()

        print(f"[+] Response: {result}")

        # Close connection properly
        s.close()

    except socket.timeout:
        # Handle timeout error (server not responding)
        print(f"[-] Timeout while checking user: {user}")

    except socket.error as e:
        # Handle network/socket-related errors
        print(f"[-] Socket error: {e}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"[-] Unexpected error: {e}")


def main():

    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python3 smtp-enum.py <IP> <USER>")
        print("  python3 smtp-enum.py <IP> -f users.txt")
        sys.exit(1)

    # Target SMTP server IP
    ip = sys.argv[1]

    # Second argument (user or file mode)
    option = sys.argv[2]

    # ==============================
    # SINGLE USER MODE
    # ==============================
    if option != "-f":
        vrfy_user(ip, option)

    # ==============================
    # FILE MODE (-f users.txt)
    # ==============================
    else:

        # Ensure file is provided
        if len(sys.argv) < 4:
            print("[-] Missing file. Example: users.txt")
            sys.exit(1)

        # Get filename from arguments
        filename = sys.argv[3]

        try:
            # Open file containing usernames/emails
            with open(filename, "r") as file:

                users = file.readlines()

                print(f"[+] Loaded {len(users)} users from file")

                # Loop through each user in file
                for user in users:

                    # Remove whitespace and newline characters
                    user = user.strip()

                    # Skip empty lines
                    if user:
                        vrfy_user(ip, user)

        except FileNotFoundError:
            print(f"[-] File not found: {filename}")

        except Exception as e:
            print(f"[-] Error reading file: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()