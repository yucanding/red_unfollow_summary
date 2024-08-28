# Xiaohongshu Unfollowers Finder 小红书取关用户查找工具

## English

### Description

This script helps you find all the users who unfollowed you on Xiaohongshu. The process involves accessing the notifications section on the Xiaohongshu web app, copying the relevant HTML code using Chrome's Developer Tools, and saving it locally. The script then processes the HTML file to identify and list all users who have unfollowed you.

### How It Works

1. **Access Xiaohongshu Web Notifications**:
   - Open the Xiaohongshu web app and navigate to the **Notifications** section, specifically the "New Followers" tab.

2. **Copy HTML Code**:
   - Open Chrome Developer Tools (`F12` or `Ctrl + Shift + I`).
   - Locate the HTML code related to the notifications under the `<div class="tabs-content-container">`.
   - Copy the entire HTML content of this section and save it as a `.html` file on your local machine.

3. **Run the Script**:
   - The script reads the saved HTML file, parses the content, and identifies users who have followed or unfollowed you based on specific markers in the HTML code.
   - It outputs a list of users who have unfollowed you, along with their user IDs, and gives a total count of such users.

### Prerequisites

- Python 3.x
- `BeautifulSoup4` for HTML parsing
- `requests` for web requests (if needed)

Install required packages using:

```bash
pip install beautifulsoup4 requests

Usage
Ensure the .html file is saved locally from the Xiaohongshu web app.
Run the script:
