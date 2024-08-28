from bs4 import BeautifulSoup

# 指定本地HTML文件的路径
file_path = 'red.html'

# 读取HTML文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 查找所有的container div
containers = soup.find_all('div', class_='container')

# 用于计数的变量
count = 0

for container in containers:
    # 查找class为reds-button-new-text的span元素，查找包含“关注”的元素
    span = container.find('span', class_='reds-button-new-text')

    if span and span.text == '关注':
        count += 1

        # 查找container中的user-info div，进一步查找嵌套的a标签
        user_info_div = container.find('div', class_='user-info')
        if user_info_div:
            a_tag = user_info_div.find('a', href=True)
            if a_tag:
                # 提取href中的用户ID
                href_value = a_tag['href']
                user_id = href_value.split('/user/profile/')[1].split('?')[0]

                # 提取用户名并去除两端的空白字符
                username = a_tag.get_text(strip=True)
                print(f'用户名: {username}, 用户ID: {user_id}')

# 输出总计数
print(f'共{count}人取关')