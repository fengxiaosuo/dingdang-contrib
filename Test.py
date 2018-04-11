# -*- coding: utf-8-*-                                                                                                                                                         # 天气插件
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Standard module stuff                                                                                                                                                     WORDS = []
SLUG = "SLUG"
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
    pass
def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    pass