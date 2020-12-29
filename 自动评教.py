from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pyquery import PyQuery as pq
import time

from OCR import OCRbase64


# 通过JS点击元素
def jsclick(css):
    js = "document.querySelector('{}').click()".format(css)
    driver.execute_script(js)


def unified_authentication_longin(username, password):
    # 在统一登陆页面输入姓名和学号
    username_box = driver.find_element_by_xpath('//*[@id="username"]')
    username_box.clear()
    username_box.send_keys(username)
    password_box = driver.find_element_by_xpath('//*[@id="password"]')
    password_box.clear()
    password_box.send_keys(password)
    while True:
        try:
            # 得到base64string
            doc = pq(driver.page_source)
            base64string = doc('#codeImg').attr('src').split(',')[1]
            # OCR识别
            identify_code = OCRbase64(base64string)
            driver.find_element_by_id('Txtidcode').clear()
            driver.find_element_by_id('Txtidcode').send_keys(identify_code + Keys.ENTER)
            print(OCRbase64(base64string))
        except:
            break


def automatic_course_selection():
    driver.switch_to.frame('leftFrame')
    # driver.find_element_by_link_text('学生评教').click()
    # driver.find_element_by_partial_link_text('学生评教').click()
    # driver.find_element_by_id('href45').click()
    jsclick('#href45')
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_name('detailfrm'))
    s1 = Select(driver.find_element_by_id('seqID'))
    for i in range(len(s1.options[1:])):
        s1 = Select(driver.find_element_by_id('seqID'))
        s1.select_by_index(1)
        jsclick('input#judge')
        for a in range(1, 13):
            js = "document.getElementsByName('wtjg_{}')[0].click()".format(a)
            try:
                driver.find_element_by_name('wtjg_{}'.format(a))
                driver.execute_script(js)
            except:
                print()
        driver.find_element_by_id('yj').send_keys('老师讲的不错还是挺喜欢老师的')
        jsclick('input#judge2')
        driver.switch_to.alert.accept()
        time.sleep(1)

if __name__ == '__main__':
    driver = webdriver.Ie()
    driver.implicitly_wait(5)
    driver.get('http://xuanke.tongji.edu.cn')
    # 点击统一身份认证超链接
    jsclick('tr td font a')
    # 统一身份认证
    unified_authentication_longin('1852273', 'Sk1234jk')
    # 自动选课
    automatic_course_selection()
    time.sleep(1000)
