from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
# from bs4 import BeautifulSoup

#option = webdriver.ChromeOptions()
#option.set_headless() 设置无头浏览器，就是隐藏界面后台运行
#其他浏览器把Chrome换名就行
driverChrome = webdriver.Chrome() # 打开 Chrome 浏览器
#driverChrome = webdriver.Chrome(chrome_options=option)  创建实例并载入option
# 掘金热门文章页面的 URL
url = 'https://juejin.cn/user/976828486917245/posts'
driverChrome.get(url)
#driverChrome.maximize_window() 最大化窗口
#driverChrome.set_window_size(width,height) 设置窗口大小
# print(driverChrome.page_source) #打印网页源码

# 隐式等待，暂时可以先不用管
driverChrome.implicitly_wait(10)
# element-ui页面会请求一些外部页面，导致需要很长时间的等待，
# 可以设置超时时间避免需要等待很长时间，但是可能会导致元素还没加载出来，可以根据自己的网络对超时时间进行调整
driverChrome.set_page_load_timeout(6)
# driverChrome.get_screenshot_as_file("截图.png")


# driverChrome.quit() # 关闭浏览器

def scroll_bottom(driver):
    # 获取当前页面高度
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 向下滚动
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 等待一段时间，以便页面加载完成
        time.sleep(2)

        # 计算新高度与旧高度，如果高度没有变化，说明已经到达页面底部，退出循环
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# 自定义序列化函数处理datetime
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"无法序列化类型：{type(obj)}")

# 保存数据到JSON文件
def save_to_json(data):
    # 保存为JSON文件
    try:
        with open('juejin_articles.json', 'w', encoding='utf-8') as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4,
                default=custom_serializer  # 处理非标准类型
            )
        print("JSON文件保存成功!")
    except Exception as e:
        print(f"JSON文件保存失败: {e}")



async def open_new_tab(url, driver):
    # 新标签页打开
    driver.execute_script(f"window.open('{url}');")
    driver.switch_to.window(driver.window_handles[-1])
    
    # 提取详情
    try:
        content = driver.find_element(By.CSS_SELECTOR, '.author-info-box .meta-box .time').get_attribute('datetime')
        print(f"时间: {content}")
    except Exception as e:
        print(f"提取失败：{e}")
    
    # 关闭标签页
    driver.close()
    driver.switch_to.window(driver.window_handles)
    time.sleep(random.uniform(1, 3))  # 降低操作频率
    # return driver.page_source
    return content

async def get_juejin_articles():
    try:
        # 滚动到页面底部
        scroll_bottom(driverChrome)
        # 查找所有文章标题和链接
        elements = driverChrome.find_elements(By.CSS_SELECTOR, '.entry-list.list.entry-list .jj-link.title')
        
        list = [] # 创建一个空列表来存储文章信息
        # 正确写法：使用enumerate生成(index, element)元组, index是索引，element是元素, 这样可以同时得到索引和元素
        for (index,element) in enumerate(elements):
            info = {} # 创建一个空字典来存储文章信息
            info['index'] = str(index)
            # 获取文章标题
            # title = element.find('span').text.strip()
            # element.get_attribute('innerText')
            title = element.text.strip()
            info['title'] = title
            print(f'标题: {title}')
            # 获取文章链接 'https://juejin.cn' + 
            link = element.get_attribute('href')
            info['link'] = link
            print(f'链接: {link}')

            # # 新标签页打开
            # try:
            #     content = await open_new_tab(link, driverChrome)
            #     print(f"获取内容长度: {content}")
            #     info['datetime'] = content
                
            # except Exception as e:
            #     print(f"打开新标签页失败: {e}")
        
            
            # 打印分隔线
            print('-' * 50)
            list.append(info)

        print({"list": list})
        save_to_json({"list": list})
    
    except TimeoutException:
        # 捕获超时异常
        print('页面加载超时')
    
    except Exception as e:
        # 捕获其他异常
        print(f'发生错误: {e}')

if __name__ == "__main__":
    get_juejin_articles()

