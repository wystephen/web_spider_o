# -*- coding:utf-8 -*-
# carete by steve at  2016 / 07 / 29　23:06

import urllib2

import re

import sys, os

if __name__ == '__main__':

    main_url = 'http://www.zhaodaoshu.com'
    response = urllib2.urlopen(main_url + '/book_918/')
    html = response.read().decode('gb2312')
    # print html

    set = re.compile('<a href="(.*)" title="(.*)" target="_blank">')

    tmp_list = set.findall(html)

    if len(tmp_list) == 0:
        print u'识别网页出现错误'
    else:
        nocache = True
        for the_dir in os.listdir('./'):
            if the_dir == 'cache':
                nocache = False
        if nocache:
            os.mkdir('cache')

        for tmp in tmp_list:
            tmp_url= main_url + tmp[0]
            print tmp_url
            r = urllib2.urlopen(tmp_url)
            html = r.read().decode('gbk')
            f = open('cache\\' + tmp[1] + '.txt', 'w')
            f.write(html.encode("utf-8"))
            f.close()
