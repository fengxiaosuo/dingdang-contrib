# -*- coding: utf-8-*-
# 天气插件
import sys
import logging
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')

# Standard module stuff
WORDS = ["TANGSHI"]
SLUG = "poetry"

def handle(text, mic, profile, wxbot=None):
    """
    Responds to user-input, typically speech text
    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
        number)
        wxbot -- wechat bot instance
    """
    logger = logging.getLogger(__name__)

    logger.debug("Test: ", text)

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "broadcom", "tang_poetry", charset='utf8' )

    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM tang_poetry.poetries where content like '%$text%' limit 1;"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            myid = row[0]
            poet = row[1]
            content = row[2]
            title = row[3]
            print "id=%d,poet=%d,content=%s,title=%s" % (myid, poet, content, title)

        responds = u'%s' % content
        mic.say(responds, cache=True)
        
    except Exception, e:
        logger.error(e)
        mic.say('信马由缰天涯路，人生命运，三分早由天注定', cache=True)    

    # 关闭数据库连接
    db.close()

def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in [u"test", u"测试"])
