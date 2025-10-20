import requests
from bs4 import BeautifulSoup

def get_juejin_articles():
    # 掘金热门文章页面的 URL
    url = 'https://juejin.cn/'
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        # 发送 HTTP 请求
        response = requests.get(url, headers=headers)
        # 检查响应状态码
        response.raise_for_status()
        # 使用 BeautifulSoup 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser')
        # 查找所有文章标题和链接
        articles = soup.find_all('div', class_='article-item')
        for article in articles:
            title = article.find('h2').text.strip()
            link = 'https://juejin.cn' + article.find('a')['href']
            print(f'标题: {title}')
            print(f'链接: {link}')
            print('-' * 50)
    except requests.RequestException as e:
        print(f'请求出错: {e}')
    except Exception as e:
        print(f'发生错误: {e}')

if __name__ == "__main__":
    get_juejin_articles()