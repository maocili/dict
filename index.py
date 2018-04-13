from  bs4 import BeautifulSoup
import requests
import os

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
url = 'http://dict.cn/'

print('            /cls 清屏'+'\n'
          '            /ex 退出'+'\n'
          '##############################################'
          )

def command(command,word):
    if command[0] =="/":

        if command == "/cls":
            os.system("cls")
        elif command == "/ex":
            os.system("exit")
            exit(0)
            return
        else:
            print("指令错误")
            return

    start(word)

def start(word):
    start_html = requests.get(url=url+word,headers=headers)
    Soup = BeautifulSoup(start_html.text, 'html')
    div = Soup.find_all("div", class_="layout dual")
    str=[]
    list=[]
    if len(div) == 0:
        print('查找不到')
    for d in div:
        for li in d.find_all("li"):
            str.append(li.text)
    for s in str:
        print(s)

while True:

    word = str(input(">>>>"))
    command(word,word)