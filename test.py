#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
import sys



def find_MaxPage(all_url):
    # all_url = 'http://www.mzitu.com'
    start_html = requests.get(all_url,headers = header)
    #找寻最大页数
    soup = BeautifulSoup(start_html.text,"html.parser")
    url = soup.select('.list-container li a.toon-more').attr('href')
    print(url)
    

def Download(href,header,title,path):
    html = requests.get(href,headers = header)
    soup = BeautifulSoup(html.text,'html.parser')
    pic_max = soup.find_all('span')
    pic_max = pic_max[10].text  # 最大页数
    if(os.path.exists(path+title.strip().replace('?','')) and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
        print('已完毕，跳过'+title)
        return 1
    print("开始扒取：" + title)
    os.makedirs(path+title.strip().replace('?',''))
    os.chdir(path + title.strip().replace('?',''))
    for num in range(1,int(pic_max)+1):
        pic = href+'/'+str(num)
        #print(pic)
        html = requests.get(pic,headers = header)
        mess = BeautifulSoup(html.text,"html.parser")
        pic_url = mess.find('img',alt = title)
        html = requests.get(pic_url['src'],headers = header)
        file_name = pic_url['src'].split(r'/')[-1]
        f = open(file_name,'wb')
        f.write(html.content)
        f.close()
    print('完成'+title)

def download(href,header,title):

    html = requests.get(href,headers = header)
    soup = BeautifulSoup(html.text,'html.parser')
    pic_max = soup.find_all('span')
    #for j in pic_max:
        #print(j.text)
    #print(len(pic_max))
    pic_max = pic_max[10].text  # 最大页数
    print(pic_max)


'''
#安卓端需要此语句
reload(sys)
sys.setdefaultencoding('utf-8')
'''


if __name__=='__main__':
    if (os.name == 'nt'):
        print(u'你正在使用win平台')
    else:
        print(u'你正在使用linux平台')

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    # http请求头
    path = 'E:/2-截图/漫画'
    all_url='https://webtoon.bamtoki.com/%EC%9E%91%EC%9D%80-%EA%B3%A0%EC%B6%94%EA%B0%80-%EB%B0%89%EB%8B%A4'
    max_page = find_MaxPage(all_url)
    # same_url = 'http://www.mzitu.com/page/'

    # #线程池中线程数
    # pool = Pool(5)
    # for n in range(1,int(max_page)+1):
    #     each_url = same_url+str(n)
    #     start_html = requests.get(each_url, headers=header)
    #     soup = BeautifulSoup(start_html.text, "html.parser")
    #     all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
    #     for a in all_a:
    #         title = a.get_text()  # 提取文本
    #         if (title != ''):
    #             href = a['href']
    #             pool.apply_async(Download,args=(href,header,title,path))
    # pool.close()
    # pool.join()
    # print('所有图片已下完')