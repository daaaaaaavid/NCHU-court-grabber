from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import catch_captcha
import time
try:
    from PIL import Image
except ImportError:
    import Image

import matlab.engine

url = 'http://pe.nchu.edu.tw//NewVenueRental//'
account = '4109056033'
password = '12345678'


def main():
    """ 模擬開啟網頁 """
    driver = webdriver.Chrome()
    driver.get(url)
    
    """ 抓取驗證碼 """
    #get_captcha(driver, element, path)
   
    flag = False
    count = 0
    while True:
        count += 1
        captcha = solve_captcha1(driver)
        #print(captcha)
        account_text = driver.find_element_by_name('account')
        password_text = driver.find_element_by_name('pwd')
        captcha_text = driver.find_element_by_name('checkword')
        account_text.send_keys(account)
        password_text.send_keys(password)
        captcha_text.send_keys(captcha)
        
        submit_text = driver.find_element_by_name('login')
        submit_text.click()
        try:
            enter_success = driver.find_element_by_class_name('div1_user')
            try:
                borrow = driver.find_element_by_xpath("//*[@id='myslidemenu']/ul/li[4]/a")
                borrow.click()
                select_place = Select(driver.find_element_by_name('queryPlace'))
                select_place.select_by_value("網球場")
                select_date = Select(driver.find_element_by_name('date'))
                select_date.select_by_index(2)
                submit = driver.find_element_by_xpath("//*[@id='place']/table/tbody/tr/td[3]/input")
                submit.click()
                field = driver.find_element_by_xpath('//*[@id="modal"]/table/tbody/tr[3]/td/table/tbody/tr[4]/td[2]/a/table/tbody/tr/td[2]')
                field.click()
                while True:
                    try:
                        print("find four ing...")
                        four = driver.find_element_by_xpath('//*[@id="people4"]')
                        print("find four")
                        four.click()
                        p2 = driver.find_element_by_name('stdnum2')
                        p3 = driver.find_element_by_name('stdnum3')
                        p4 = driver.find_element_by_name('stdnum4')
                        p2.send_keys('7107011002')
                        p3.send_keys('7108011030')
                        p4.send_keys('8103011005')
                        scroll = driver.find_element_by_id('imgcode')
                        driver.execute_script('arguments[0].scrollIntoView(true);',scroll) 
                        scroll.click()
                        time.sleep(1)
                        captcha = solve_captcha2(driver)
                        captcha_input = driver.find_element_by_name('checkword')
                        print(captcha)
                        captcha_input.clear()
                        captcha_input.send_keys(captcha)
                        submit = driver.find_element_by_name('save')
                        submit.click()
                        try:
                            
                            driver.switch_to.alert.accept()
                            print(0)
                            
                            continue
                            
                            
                        except:
                            print(3)
                            return
                    except:
                        continue
                    print('cnt:'+count)
                
            except:
                print('select error')
        except :
            print('login error')
            pass
                #driver.close()
                #return False
    #captcha = verify_identifying_code.main()
    #print(captcha)
    #identifying_code.show()
    #print(count)
    #driver.close()
    """         fail to get url
    image_link = soup.find('img',{'src':'captcha.php'})['src']
    img = requests.get('http://pe.nchu.edu.tw/NewVenueRental/{image_link}')
    print(img.text)"""

def solve_captcha1(driver):
    flag = False
    while flag == False:
        driver.save_screenshot('screenshot.png')
        screenshot = Image.open('screenshot.png')
        element = driver.find_element_by_id('imgcode')
        x = element.location['x'] * 1.5 + 3
        y = element.location['y'] * 1.5 + 3
        #print(element.location['x'],element.location['y'])
        width = x + element.size['width']*1.5 - 3
        height = y + element.size['height']*1.5 - 5
        identifying_code = screenshot.crop((x,y,width,height))
        identifying_code.save('captcha.png')
        flag = catch_captcha.main() 
        if flag == False:
            element.click()
    eng = matlab.engine.start_matlab()
    index = eng.captcha()
    captcha = ''
    for i in range(5):
        if int(index[i][0]) <= 9 and int(index[i][0]) >= 0:
            captcha += chr(ord('0') + int(index[i][0]))
        elif int(index[i][0]) <= 35:
            captcha += chr(ord('A') + int(index[i][0]) - 10)
        else :
            captcha += chr(ord('a') + int(index[i][0]) - 36)
    return captcha
def solve_captcha2(driver):
    flag = False
    while flag == False:
        driver.save_screenshot('screenshot.png')
        screenshot = Image.open('screenshot.png')
        element = driver.find_element_by_id('imgcode')
        x = 792#element.location['x'] * 1.5 + 3
        y = 498#element.location['y'] * 1.5 + 3
        #print(element.location['x'],element.location['y'])
        width = x + element.size['width']*1.5 - 3
        height = y + element.size['height']*1.5 - 5
        identifying_code = screenshot.crop((x,y,width,height))
        identifying_code.save('captcha.png')
        
        flag = catch_captcha.main() 
        if flag == False:
            element.click()
    eng = matlab.engine.start_matlab()
    index = eng.captcha()
    captcha = ''
    for i in range(5):
        if int(index[i][0]) <= 9 and int(index[i][0]) >= 0:
            captcha += chr(ord('0') + int(index[i][0]))
        elif int(index[i][0]) <= 35:
            captcha += chr(ord('A') + int(index[i][0]) - 10)
        else :
            captcha += chr(ord('a') + int(index[i][0]) - 36)
    return captcha
if __name__  == '__main__':
    main()