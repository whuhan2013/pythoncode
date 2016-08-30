import urllib.request
import urllib.parse
import re

pattern = re.compile(r'<div class="j-r-list-c-desc">\s+(.*)\s+</div>')

# 返回指定网页的内容
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

# num为用户自定，返回的是所有页的段子列表
def get_content(num):
    # 存放段子的列表
    text_list = []
    for page in range(1, int(num)):
        address = 'http://www.budejie.com/text/' + str(page)
        html = open_url(address)
        result = re.findall(pattern, html)
        # 每一页的result都是一个列表，将里面的内容加入到text_list
        for each in result:
            text_list.append(each)
    return text_list


# num是指定网页页数
def save(num):
    # 写方式打开一个文本，把获取的段子列表存放进去
    with open('a.txt', 'w', encoding='utf-8') as f:
        text = get_content(num)
        # 和上面去掉<br />类似
        for each in text:
            if '<br />' in each:
                new_each = re.sub(r'<br />', '\n', each)
                f.write(new_each)
            else:
                f.write(str(each) + '\n')


if __name__ == '__main__':
    print('阅读过程中按q随时退出')
    number = int(input('想读几页的内容: '))
    content = get_content(number + 1)
    #print(content)
    for each in content:
        if '<br />' in each:
            new_each = re.sub(r'<br />', '\n', each)
            print(new_each)
        else:
            print(each)
        # 用户输入
        user_input = input()
        # 不区分大小写的q，输入则退出
        if user_input == 'q' or user_input == 'Q':
            break