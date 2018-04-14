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
DEBUG = 1

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

    if DEBUG:
        print __name__ + " Input text is: " + text
    else:
        logger.debug("Input text is: ", text)

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "broadcom", "tang_poetry", charset='utf8' )

    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM tang_poetry.poetries where content like '%"+text+"%' limit 1;"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        results = cursor.fetchone()
        poet = results[1]
        content = results[2]
        title = results[3]

        sql1 = "SELECT * FROM poets where id = %s;" % poet

        cursor.execute(sql1)
        results = cursor.fetchone()
        poet_name = results[1]

        respond = "唐 " + poet_name + " " + title + " " + content
        responds = u'%s' % respond # unicode

        if DEBUG:
            print respond
        else:
            mic.say(responds, cache=True)
        
    except Exception, e:
        if DEBUG:
            print "数据库读取失败"
        else:
            logger.error(e)
            mic.say('数据库读取失败', cache=True)  

    # 关闭数据库连接
    db.close()

def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in [u"唐诗", u"诗词"])

if __name__ == "__main__":
    handle("离离原上草", 0, 0)