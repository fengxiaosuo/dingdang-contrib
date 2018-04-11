# -*- coding: utf-8-*-
# 天气插件
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf8')

# Standard module stuff
WORDS = ["测试"]
SLUG = "test"

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

    # get config
    if SLUG not in profile or \
       'key' not in profile[SLUG] or \
       (
           'location' not in profile[SLUG] and
           'location' not in profile
       ):
        mic.say('天气插件配置有误，插件使用失败', cache=True)
        return

    key = profile[SLUG]['key']
    if 'location' in profile[SLUG]:
        location = profile[SLUG]['location']
    else:
        location = profile['location']
    
    try:
    	responds = u'%s天气：' % location
        responds += "河山万里风萧索，心事浮沉，总被风吹雨打去 "
        mic.say(responds, cache=True)
    except Exception, e:
        logger.error(e)
        mic.say('信马由缰天涯路，人生命运，三分早由天注定', cache=True)    


def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in [u"test", u"测试"])
