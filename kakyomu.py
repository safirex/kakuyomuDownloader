# coding: utf-8
import requests
#正则表达式模块
import re
import os


def getNovelTitle():
    titlediv1=html.find(titlediv)+len(titlediv)
    endTitleDiv=html[titlediv1:].find('</a>')+titlediv1
    return html[titlediv1:endTitleDiv]

def getNovelChapterList():
     #delete the first object cause is not in widget toc episodes
    chapList=re.findall(chapterListDiv,html,re.DOTALL)[1:]
    print(chapList)
    print('%s chapters detected'%len(chapList))
    return chapList

def getChapterTitle(str):

    chapter_title=re.findall('<p class="widget-episodeTitle js-vertical-composition-item">(.*?)<',str)[0]
            #<p class="widget-episodeTitle js-vertical-composition-item">
#    print('title = '+title)
    return chapter_title

def DL(fromchap):
    global headers
    i=fromchap
    for chap in chapNumList[fromchap-1:]:
        chapter_url=url+'/episodes/'+chap
        print('chapter: '+i+'  '+chapter_url)

        rep=requests.get(chapter_url)#,headers=headers)
        html=rep.text
        chapter_title=getChapterTitle(html)
        content=re.findall('<p id="p.*">(.*?)</p>',html)
        contentUPDATED=[]
        for sentence in content:
            sentence = sentence.replace('<br />','\n')
            sentence = sentence.replace('<ruby>','')
            sentence = sentence.replace('</ruby>','')
            sentence = sentence.replace('<rp>','')
            sentence = sentence.replace('</rp>','')
            sentence = sentence.replace('<rt>','')
            sentence = sentence.replace('</rt>','')
            sentence = sentence.replace('<rb>','')
            #signal character superpose
            sentence = sentence.replace('</rb>','//')
            sentence += '\n'
            contentUPDATED.append(sentence)

        createFile(i,chapter_title,contentUPDATED,chapter_url)
        i+=1
            #replace <ruby> <rb> <rp> <rt>

def createDir():
    dirlist=os.listdir(os.getcwd())
    if DirName not in dirlist:
        os.mkdir('%s'%DirName)

def createFile(i,chapter_title,chapter_content,chapter_url):
     #写入
    file = open('%s\%d_%s.txt'%(DirName,i,chapter_title), 'w+', encoding='utf-8')
    file.write(chapter_url+'\n')
    file.write(chapter_title+'\n')
    for sentence in chapter_content:
        file.write(sentence)
    file.close()


headers={}
html=''

novelNumber=input('give the novel serie number: ')
url='https://kakuyomu.jp/works/%s'%novelNumber
#titlediv='<li><a href="/violation_report'
titlediv='<h1 id="workTitle"><a href="/works/%s">'%novelNumber
chapterListDiv='/works/%s/episodes/(.*?)"'%novelNumber

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

rep=requests.get(url,headers=headers)
rep.encoding='utf-8'
html=rep.text

novelName=getNovelTitle()
DirName=str(novelNumber)+' '+novelName
createDir()
print(novelName)
chapNumList=getNovelChapterList()
DL(1)
#print(html)
#content=re.findall(textsearch,html)



# str=' <a href="/works/1177354054880238351/episodes/1177354054895552249" class="widget-toc-episode-e'
#>>> import re
#>>> re.findall('a href="(.*)" class'
#... ,str)
