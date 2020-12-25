import sys
wf = open('./mygt.txt','w',encoding='utf-8')
with open('./photoshops.tsv','r',encoding='utf-8') as f:
    url_list = f.readlines()
    for idx,url in enumerate(url_list):
        url = url.split('\t')[2]
        print(url)
        wf.write(str(url+'\n'))

        