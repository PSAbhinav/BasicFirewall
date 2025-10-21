# BasicFirewall

A simple Python script that allows you to block, unblock, and test access to specific websites on Windows by modifying the system `hosts` file. Useful for local website blocking, parental control, and productivity.

---

## Features

- Block any website (by redirecting it to `127.0.0.1`)
- Unblock sites effortlessly
- Automatic DNS cache flushing after changes
- Checks both non-www and www versions of domains
- Tests if a website is blocked at the DNS level
- Safe: Requires admin rights to run

---

## Requirements

- Windows OS
- Python 3.x (tested with 3.13+)
- Must be **run as Administrator**

---

## Usage

1. **Clone or download the repo.**
2. Open **CMD** or **PowerShell** as Administrator.
3. Move to the script directory:
    ```
    cd C:\Users\abhin\Desktop\My_Projects\BasicFirewall
    ```
4. Run the script:
    ```
    python firewall.py
    ```
5. Follow the interactive prompts:
    - `1`: Block websites
    - `2`: Unblock websites
    - `3`: Flush DNS cache
    - `4`: Test website block

---

## Example

Simple Firewall Script

Block websites

Unblock websites

Flush DNS cache

Test website block
Enter your choice: 1
Enter websites to block (comma-separated): facebook.com,youtube.com
Websites blocked successfully.
DNS cache flushed successfully.


---

## Important Notes

- You **must** run the script as Administrator or it won't be able to modify the hosts file.
- Changes take effect system-wide on Windows.
- To fully block popular sites, both `example.com` and `www.example.com` will be added to the hosts file.
- Some browsers or antivirus tools may bypass hosts–file DNS resolution (see README tips for details).

---

## License

This project is provided under the MIT License.

---

## Contribution

Feel free to submit bug reports, request features, or fork and enhance!

---

### Author

- PSAbhinav
- https://github.com/PSAbhinav
