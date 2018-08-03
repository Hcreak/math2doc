# coding:gb2312
from __future__ import division
from docx import Document, section
import random
# import chardet
import time

document = Document()
timeid = str(time.strftime("%B %d, %Y at %H:%M", time.localtime(time.time())))
ruldit=[]

def mknum():
    q = random.choice([0.1, 10, 10, 10, 10, 10, 10, 100])
    if q == 10:
        return str(random.randint(1, 100))
    else:
        if q == 0.1:
            return str(round(random.uniform(1, 10), 1))
        else:
            return str(random.randint(100, 1000))


def mksym():
    # print chardet.detect('?')
    # print chardet.detect('?')
    # print chardet.detect('?')
    # print chardet.detect('?')
    # add='?'.decode('iso-8859-1')
    # sub='?'.decode('iso-8859-1')
    # mul='?'.decode('iso-8859-1')
    # div='?'.decode('iso-8859-1')
    #
    # p=random.choice([add,add,add,add,sub,sub,sub,sub,mul,div])

    # p=random.choice(u'锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷')
    return random.choice('++++----*/')


def mkone():
    outstr = ''
    while (1):
        outstr = ''
        outstr += mknum()
        outstr += mksym()
        outstr += mknum()
        outstr += mksym()
        outstr += mknum()
        rulest = eval(outstr)
        if rulest > 0:
            if len(str(rulest)) <= 4:
                print outstr + '=' + str(rulest)
                ruldit.append(rulest)
                break

    outstr = outstr.replace('+', u'＋')
    outstr = outstr.replace('-', u'－')
    outstr = outstr.replace('*', u'×')
    outstr = outstr.replace('/', u'÷')
    outstr += '='
    return outstr


def mkdoc(page):
    for p in range(page):
        table = document.add_table(rows=25, cols=3)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = timeid
        hdr_cells[2].text = str(p)

        for i in range(2, 25, 3):
            hdr_cells = table.rows[i].cells
            for j in range(3):
                # print mkone()
                hdr_cells[j].text = mkone()
        if p != (page - 1):
            document.add_page_break()


if __name__ == '__main__':
    n = raw_input('输入页数：')
    mkdoc(int(n))
    document.save('mathexample.docx')
    f=open('allrul.txt','a+')
    f.write(timeid+'\n')
    f.write(' '.join(str(i) for i in ruldit)+'\n')
    f.close()
