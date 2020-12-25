import requests
img_url_path = './mygt.txt'#图片url链接文件，需自行创建（每行一个URl）
img_save_path = './ps'#文件保存路径（可以自己改，默认保存到脚本的同级目录）

def down_pic(down_url, picname):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'
    }
    req = requests.get(url=down_url, headers=header)
    print(req)
    req.encoding = 'utf-8'
    with open('./photoshops/%s%s.png' %(img_save_path,picname), "wb") as f:  # 开始写文件，wb代表写二进制文件 图片已数字命名
        f.write(req.content)
        f.close()
def main():
    with open(img_url_path,'r',encoding='utf-8') as f:
        url_list = f.readlines()
    picname = 0
    for url in url_list:
        picname += 1
        print('第%s个文件正在下载'%picname)
        try:
            down_pic(url.replace('\n',''), picname)
        except:
            continue
# 执行函数
main()
