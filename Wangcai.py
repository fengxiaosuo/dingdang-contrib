# -*- coding: utf-8-*-
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

    wc = Wangcai("")
    print("my name is %s" % wc.name)

    if DEBUG:
        print "Input text is: " + text
    else:
        logger.debug("Input text is: ", text)

    try:
        if any(word in text for word in [u"看左边", u"左看"]):
            print "see left"
            mic.say('看左边', cache=False)
            wc.frontservo_appointed_detection(180)

        elif any(word in text for word in [u"看右边", u"右看"]):
            print "see right"
            mic.say('看右边', cache=False)
            wc.frontservo_appointed_detection(0)

        elif any(word in text for word in [u"看中间", u"前看", u"看前"]):
            print "see front"
            mic.say('看中间', cache=False)
            wc.frontservo_appointed_detection(90)

        elif any(word in text for word in [u"转个圈", u"左转圈"]):
            print "turn around by left"
            mic.say('转个圈', cache=False)
            wc.spin_left()

        elif any(word in text for word in [u"右圈", u"右转圈"]):
            print "turn around by right"
            mic.say('转个圈', cache=False)
            wc.spin_right()

        elif any(word in text for word in [u"前进", u"往前"]):
            wc.advance(0.5)

        elif any(word in text for word in [u"后退", u"往后"]):
            wc.back(0.5)

        elif any(word in text for word in [u"左转", u"往左"]):
            wc.left(0.5)

        elif any(word in text for word in [u"右转", u"往右"]):
            wc.right(0.5)

        elif any(word in text for word in [u"红灯", u"开灯"]):
            wc.color_led_pwm(255,0,0)

        elif any(word in text for word in [u"绿灯"]):
            wc.color_led_pwm(0,255,0)

        elif any(word in text for word in [u"蓝灯"]):
            wc.color_led_pwm(0,0,255)

        elif any(word in text for word in [u"关灯"]):
            wc.color_led_pwm(0,0,0)

        elif any(word in text for word in [u"距离", u"障碍"]):
            print "distance is %s" % wc.distance()
            temp= "测距%s厘米" % wc.distance()
            mic.say(temp, cache=False)

        else:
            print "else for nothing"
            wc.whistle()
        
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



    handle("左看", 0, 0)
