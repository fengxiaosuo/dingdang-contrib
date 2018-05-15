# -*- coding: utf-8-*-
# 天气插件
import sys
import logging
sys.path.append(r'/home/pi/git/wangcai') 
from wangcai import Wangcai

reload(sys)
sys.setdefaultencoding('utf8')

# Standard module stuff
WORDS = ["WANGCAI"]
SLUG = "wangcai"
DEBUG = 1

def handle(text, mic, profile, wangcai, wxbot=None):
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
        print "Input text is: " + text
    else:
        logger.debug("Input text is: ", text)

    try:
        if any(word in text for word in [u"看左边", u"左看"]):
            print "see left"
            wangcai.frontservo_appointed_detection(180)
        elif any(word in text for word in [u"转个圈", u"转圈"]):
            print "turn around by left"
            wangcai.spin_left()
        else:
            print "else"
        
    except Exception, e:
        if DEBUG:
            print "失败"
        else:
            logger.error(e)
            mic.say('失败', cache=True)  


def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in [u"旺财", u"旺旺"])

if __name__ == "__main__":

    wc = Wangcai("")
    print("my name is %s" % wc.name)

    handle("左看", 0, 0, wc)