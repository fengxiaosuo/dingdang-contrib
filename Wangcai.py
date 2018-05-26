# -*- coding: utf-8-*-
import sys
import logging
import time
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

    while True:
        time.sleep(.1)

        # TODO, quit after time out, e.g. 1 minute

        # 听用户说话
        print "active listen..."
        text = mic.activeListen()

        if text:
            # quit
            if any(word in text for word in [u"结束", u"退出", u"停止"]):
                mic.say('再见，我会想你的', cache=False)
                wc.moto_init()
                break

            # 超声波和前电机
            elif any(word in text for word in [u"距离", u"测距", u"障碍"]):
                print "distance is %s" % wc.distance()
                temp= "测距%s厘米" % wc.distance()
                mic.say(temp, cache=False)

            elif any(word in text for word in [u"看左边", u"左看"]):
                mic.say('看左边', cache=False)
                wc.frontservo_appointed_detection(180)

            elif any(word in text for word in [u"看右边", u"右看"]):
                mic.say('看右边', cache=False)
                wc.frontservo_appointed_detection(0)

            elif any(word in text for word in [u"看中间", u"前看", u"看前"]):
                mic.say('看中间', cache=False)
                wc.frontservo_appointed_detection(90)

            # 运动
            elif any(word in text for word in [u"转个圈", u"左转圈"]):
                mic.say('转个圈', cache=False)
                wc.spin_left()

            elif any(word in text for word in [u"右圈", u"右转圈"]):
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

            # 七彩灯相关
            elif any(word in text for word in [u"红灯", u"开灯"]):
                wc.color_led_pwm(255,0,0)

            elif any(word in text for word in [u"绿灯"]):
                wc.color_led_pwm(0,255,0)

            elif any(word in text for word in [u"蓝灯"]):
                wc.color_led_pwm(0,0,255)

            elif any(word in text for word in [u"关灯"]):
                wc.color_led_pwm(0,0,0)

            # 摄像头相关
            elif any(word in text for word in [u"摄像头", u"眼睛"]) \
            and any(word in text for word in [u"左"]):
                wc.leftrightservo_appointed_detection(180)

            elif any(word in text for word in [u"摄像头", u"眼睛"]) \
            and any(word in text for word in [u"中"]):
                wc.leftrightservo_appointed_detection(90)

            elif any(word in text for word in [u"摄像头", u"眼睛"]) \
            and any(word in text for word in [u"右"]):
                wc.leftrightservo_appointed_detection(0)

            elif any(word in text for word in [u"摄像头", u"眼睛"]) \
            and any(word in text for word in [u"上"]):

                wc.servo_up()

            elif any(word in text for word in [u"摄像头", u"眼睛"]) \
            and any(word in text for word in [u"右"]):
                wc.leftrightservo_appointed_detection(0)

            elif any(word in text for word in [u"摄像头", u"眼睛"]) \
            and any(word in text for word in [u"右"]):
                wc.leftrightservo_appointed_detection(0)

            # 状态相关
            elif any(word in text for word in [u"状态", u"状况"]):
                # print wc.ServoFrontPos
                temp= "超声波角度%s" % wc.ServoFrontPos
                mic.say(temp, cache=False)
                # print wc.ServoLeftRightPos
                temp= "摄像头左右角度%s" % wc.ServoLeftRightPos
                mic.say(temp, cache=False)
                # print wc.ServoUpDownPos
                temp= "摄像头上下角度%s" % wc.ServoUpDownPos
                mic.say(temp, cache=False)

            # 传感器相关
            elif any(word in text for word in [u"传感器"]):
                # 4 bit of tracking sensor
                print "tracking %s" % wc.tracking_sensor()
                # 2 bit, use the first bit
                print "infrared %s" % wc.infrared_avoid_sensor()
                # 2 bit
                print "lighting %s" % wc.lighting_sensor()
                temp= "循迹%s" % wc.tracking_sensor()
                temp = temp + "红外%s" % wc.infrared_avoid_sensor()
                temp = temp + "感光%s" % wc.lighting_sensor()
                mic.say(temp, cache=False)

            # 没找到
            else:
                print "nothing to do"
                wc.whistle()
        else:
            mic.say(u"什么？", cache=True)


        '''
        input = self.mic.activeListen(MUSIC=True)
        if input:

            if any(word in text for word in [u"退出", u"停止", u"关机", u"再见"]):
                print "quit"
                mic.say('再见，我会想你的', cache=False)
                break

            elif any(word in text for word in [u"看左边", u"左看"]):
                print "see left"
                mic.say('看左边', cache=False)
                wc.frontservo_appointed_detection(180)

            elif any(word in text for word in [u"看右边", u"右看"]):
                print "see right"
                mic.say('看右边', cache=False)
                wc.frontservo_appointed_detection(0)


            else:
                print "else for nothing"
                wc.whistle()

            sleep(0.5)
        
    except Exception, e:
        if DEBUG:
            print "失败"
        else:
            logger.error(e)
            mic.say('失败', cache=True)  
        '''

def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in [u"旺财", u"旺旺", u"控制", u"机器人"])

"""
    main function for test
"""
if __name__ == "__main__":

    handle("左看", 0, 0)
