# Xiaohongshu Unfollowers Finder 小红书取关用户查找工具

## English

### Description

This script helps you find all the users who unfollowed you on Xiaohongshu. The process involves accessing the notifications section on the Xiaohongshu web app, copying the relevant HTML code using Chrome's Developer Tools, and saving it locally. The script then processes the HTML file to identify and list all users who have unfollowed you.

### How It Works

1. **Access Xiaohongshu Web Notifications**:
   - Open the Xiaohongshu web app and navigate to the **Notifications** section, specifically the "New Followers" tab, **keep scrolling down to the bottom of the page to ensure all followers information is fully loaded**.

2. **Copy HTML Code**:
   - Open Chrome Developer Tools (`F12` or `Ctrl + Shift + I`).
   - Locate the HTML code related to the notifications under the `<div class="tabs-content-container">`.
   - Copy the entire HTML content of this section and save it as a `.html` file on your local machine with the name `red.html`.

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
```

### Usage
Ensure the .html file is saved locally from the Xiaohongshu web app.
Run the script:

```bash
python find_unfollower.py
```

The script will output the list of unfollowers along with their user IDs and the total count of unfollowers.

## 中文

### 说明

此脚本帮助你查找所有在小红书上取关你的用户。具体过程包括访问网页版小红书的通知界面，通过Chrome的开发者工具复制相关HTML代码并将其保存在本地。脚本会处理该HTML文件，识别并列出所有取关你的用户。

### 工作原理

1. **访问小红书网页通知**:
   - 打开网页版小红书，导航至**通知**部分，选择“新增关注”标签，**不断滑动页面到最底部，确保已加载完毕所有关注者信息**。

2. **复制HTML代码**:
   - 打开Chrome开发者工具（按`F12`或`Ctrl` + `Shift` + `I`）。
   - 找到` <div class="tabs-content-container"> `下的通知相关HTML代码。
   - 将此部分HTML内容全部复制并保存为本地的 `.html `文件，命名为`red.html`。

3. **运行脚本**:
   - 脚本读取保存的HTML文件，解析内容，并根据HTML代码中的特定标记识别已关注或取关你的用户。
   - 脚本将输出取关你的用户列表及其用户ID，并给出总数。

### 先决条件

- Python 3.x
- 用于HTML解析的`BeautifulSoup4`
- 用于网络请求的`requests`（如果需要）

使用以下命令安装所需的库：

```bash
pip install beautifulsoup4 requests
```

### 使用方法
确保已从网页版小红书保存 .html 文件至本地。
运行脚本：

```bash
python find_unfollower.py
```

脚本将输出取关你的用户列表及其用户ID，并显示取关用户的总数。
