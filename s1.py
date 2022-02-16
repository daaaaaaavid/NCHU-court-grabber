from selenium import webdriver

import catch_captcha

try:
    from PIL import Image
except ImportError:
    import Image

import matlab.engine

url = 'http://pe.nchu.edu.tw//NewVenueRental//'
account = '4109056033'
password = ''


def main():
    """ 模擬開啟網頁 """
    driver = webdriver.Chrome()
    driver.get(url)
    
    """ 抓取驗證碼 """
    #get_captcha(driver, element, path)
   
    flag = False
    count = 0
    while flag == False:
        count += 1
        driver.save_screenshot('screenshot.png')
        screenshot = Image.open('screenshot.png')
        element = driver.find_element_by_id('imgcode')
        x = element.location['x'] * 1.5 + 3
        y = element.location['y'] * 1.5 + 3
        width = x + element.size['width']*1.5 - 3
        height = y + element.size['height']*1.5 - 5
        identifying_code = screenshot.crop((x,y,width,height))
        identifying_code.save('captcha.png')
        flag = catch_captcha.main() 
        if flag == False:
            element.click()
            continue
        else: 
            break
            eng = matlab.engine.start_matlab()
            index = eng.captcha()
            captcha = ''
            for i in range(5):
                if int(index[i][0]) <=9 and int(index[i][0]) >= 0:
                    captcha += chr(i)
                elif int(index[i][0]) <= 35:
                    captcha += chr(ord('A') + int(index[i][0]) - 10)
                else :
                    captcha += chr(ord('a') + int(index[i][0]) - 36)
            #print(captcha)
            account_text = driver.find_element_by_name('account')
            password_text = driver.find_element_by_name('pwd')
            captcha_text = driver.find_element_by_name('checkword')
            account_text.send_keys(account)
            password_text.send_keys(password)
            captcha_text.send_keys(captcha)
            
    #captcha = verify_identifying_code.main()
    #print(captcha)
    #identifying_code.show()
    print(count)
    driver.close()
    """         fail to get url
    image_link = soup.find('img',{'src':'captcha.php'})['src']
    img = requests.get('http://pe.nchu.edu.tw/NewVenueRental/{image_link}')
    print(img.text)"""


if __name__  == '__main__':
    main()