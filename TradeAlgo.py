##first step
# import modules


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import schedule
import time



##second step
#login


driver=webdriver.Chrome(executable_path="")
driver.get("https://kite.zerodha.com/")
First_window = driver.window_handles[0]
driver.find_element(By.XPATH,'//*[@id="userid"]').send_keys("Enter Your UserID")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Enter Your Password")
driver.find_element(By.XPATH,'//*[@id="container"]/div/div/div/form/div[4]/button').click()  #login
time.sleep(15)




## third step
# click on chart button


a= ActionChains(driver)
b= driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/span[1]')
a.move_to_element(b).perform()
c=driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div/span/span[4]/button/span')#open graph
c.click()
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))#### entering in iframe
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[14]').click()
driver.switch_to.default_content()
Second_window = driver.window_handles[1]
driver.switch_to.window(Second_window)
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))




## forth step
# switch time frame



driver.find_element(By.XPATH,'//*[@id="header-toolbar-intervals"]/div').click()#click on daily time frame
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="__outside-render-0"]/div/div/div/div/div/div/div[1]/div/div[1]/div').click()#15min time frame
time.sleep(1)



## fifth step
# find and click indicator super trend


driver.find_element(By.XPATH,'//*[@id="header-toolbar-indicators"]/span').click()#click indicator icon
driver.switch_to.default_content()#click indicator icon
driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))#find indicator search bar
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/input').send_keys("supertrend")#find indicator search bar search super trend
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[2]/div[1]/div/div/div/div').click()#find super trend



## sixth step
# find and click indicator EMA EXPO


driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/span[1]').click()#clear previous searched supertrend keyword
driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[1]/input').send_keys("ema")#find ema
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div').click()



## seventh step
#  change indicator settings of supertrend


driver.find_element(By.XPATH,'/html/body/div[5]/div[3]').click()#cilck cross indicator searchbar button
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[2]/span[2]/a[3]').click()#delete volume
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[2]/span[2]/a[2]').click()#indicator setting button of supertrend
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(Keys.BACKSPACE)#super trend modifications search bar
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(Keys.BACKSPACE)#super trend modifications search bar
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys("50")#super trend modifications search bar
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(Keys.BACKSPACE)
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(2.5)
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[4]/div/a[2]').click()#super trend modifications hit ok
time.sleep(1)#super trend modifications



## eighth step
# change indicator setting of ema expo


driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[3]/span[2]/a[2]').click()#click ema setting
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(Keys.BACKSPACE)#super trend modifications
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys("200")
driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[4]/div/a[2]').click()
driver.switch_to.default_content()####exiting iframe
driver.switch_to.window(First_window)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[1]/a[4]').click()
driver.switch_to.window(Second_window)




## ninth step
# Buy function


def buy(x):#buy command

    driver.switch_to.window(First_window)
    time.sleep(1)
    P = ActionChains(driver)
    Q = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[4]/div/div/div[1]')#instrument hover path
    P.move_to_element(Q).perform()
    time.sleep(1)
    R = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[4]/div/span/span[1]')  # click on buy button
    time.sleep(1)
    R.click()
    driver.find_element(By.XPATH,'//*[@id="app"]/form/section/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(x)#write quantity
    driver.find_element(By.XPATH,'//*[@id="app"]/form/section/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/label').click()#order type market
    driver.find_element(By.XPATH,'//*[@id="app"]/form/section/div/footer/div[2]/button[1]').click()#click buy sumbit
    time.sleep(2)
    driver.switch_to.window(Second_window)


## tenth step
# sell function


def sell(xx):#sell command
    driver.switch_to.window(First_window)
    time.sleep(1)
    P = ActionChains(driver)
    Q = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[4]/div/div/div[1]')  # instrument hover path
    P.move_to_element(Q).perform()
    time.sleep(1)
    R = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[4]/div/span/span[2]')# click on sell button
    time.sleep(1)
    R.click()
    driver.find_element(By.XPATH,'//*[@id="app"]/form/section/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(xx)#write quantity
    driver.find_element(By.XPATH,'//*[@id="app"]/form/section/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/label').click()#order type market
    driver.find_element(By.XPATH, '//*[@id="app"]/form/section/div/footer/div[2]/button[1]').click()#click sell sumbit
    time.sleep(2)
    driver.switch_to.window(Second_window)



## eleventh step
# fetching price of instrument and indicator value



def update():
    global ema
    global supertrend
    global price
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))####entering iframe
    supertrend=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[3]/div/span[1]/span').text#catching supertrend value
    ema = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[4]/div/span[1]/span').text##catching ema value
    price = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div[3]/div[1]/div/span[4]/span[2]').text#catching price
    driver.switch_to.default_content()
    print(ema,price,supertrend)



##twelth step
#checking outstanding positions


global position
driver.switch_to.window(First_window)
time.sleep(1)
try:
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/button')
    print("you dont have any position")
    position=False
except NoSuchElementException:
    print("you have existing position")
    position=True
driver.switch_to.window(Second_window)



##thirteenth step
#handling positions in opening


def morningcheck():
 if position==True :
    if supertrend and price > ema and price < supertrend or supertrend and price < ema and price < supertrend:
         sell(4)

    if supertrend and price < ema and price > supertrend or supertrend and price > ema and price > supertrend:
        buy(4)
 if position==False :
     if supertrend >ema and price>supertrend:
         buy(4)
     if supertrend < ema and price < supertrend:
         sell(4)


##fourteenth step
#buying and selling signal generation and execution


def buysellSignal():
    while True:


        ##buying


        if supertrend > ema and price > ema and price < supertrend:
            while price < supertrend and supertrend > ema and price > ema:
                time.sleep(60)
                update()
            if price > supertrend:
                buy(1)
                print("bought4")
                time.sleep(2)
                while price > supertrend:
                    time.sleep(60)
                    update()
                if price < supertrend:
                    sell(1)
                    print("sold4")
                    time.sleep(2)



        ##selling


        if price < ema and supertrend < ema and price > supertrend:
            while price > supertrend:
                time.sleep(60)
                update()
            if price < supertrend and price < ema and supertrend < ema:
                sell(1)
                print("sold4")
                time.sleep(2)
                while price < supertrend:
                    time.sleep(60)
                    update()
                if price > supertrend:
                    buy(4)
                    print("bought")
                    time.sleep(2)
        time.sleep(1)



##automatically running command


schedule.every().day.at("21:20:00").do(buysellSignal)

while True:
         schedule.run_pending()
         time.sleep(1)


input()
