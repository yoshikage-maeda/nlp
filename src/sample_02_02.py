import urllib.request
import cchardet
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        # 文字コードの変換: cchardetを使って自動で文字コードを判定
        html = byte.decode(cchardet.detect(byte)['encoding'])
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.head.title
        print('[title]:', title.text, '\n')

        for block in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4']):
            print('[block]:', block.text)
        