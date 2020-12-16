from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def launchBrowser():

    driver = webdriver.Chrome('\\Users\\XXX\\XXX\\chromedriver_win32\\chromedriver')
    
    driver.get('https://xxx')
    usernameField = driver.find_element_by_id('id')
    passwordField = driver.find_element_by_id('password')
    usernameField.send_keys('')
    passwordField.send_keys()
    submitUserPass = driver.find_element_by_name('uip_action')
    submitUserPass.click()
    day = datetime.now().weekday()
    date = datetime.now().strftime("%d")
    hour = datetime.now().strftime("%I")
    minute = datetime.now().strftime("%M")
    period = datetime.now().strftime("%p")
    zone = ''
    eatingTime = ''
    
    #user input
    print('Enter time as hhmm (12 hr), period AM/PM, and date as ##\n')
    userTime = input('Specify time: ')
    if(userTime != ''):
        hour = userTime[:2]
        minute = userTime[2:]
    userPeriod = input('Please specify period: ')
    if(userPeriod != ''):
        period = upper(userPeriod)
    userDate = input('\nSpecify date: ')
    if(userDate != ''):
        date = userDate

    if(day != 6):
        if(int(hour + minute) <= 1030):
            eatingTime = 'breakfast'
            if(int(minute) <= 5):
                zone = 'zone1'
            elif(int(minute) <= 20):
                zone = 'zone2'
            elif(int(minute) <= 35):
                zone = 'zone3'
            else:
                zone = 'zone4'
        else:
            if(int(minute) <= 5):
                zone = 'zone3'
            elif(int(minute) <= 20):
                zone = 'zone4'
            elif(int(minute) <= 35):
                zone = 'zone1'
            else:
                zone = 'zone2'
            eatingTime = 'lunch'
            if(int(hour + minute) <= 1400):
                eatingTime = 'lunch'
            else:
                eatingTime = 'dinner'

    else:
        if(int(hour + minute) <= 1030):
            print('Cannot get breakfast on Sunday')
            eatingTime = 'NA'
        elif(int(hour + minute) <= 1400):
            if(int(minute) <= 5):
                zone = 'zone1'
            elif(int(minute) <= 20):
                zone = 'zone2'
            elif(int(minute) <= 35):
                zone = 'zone3'
            else:
                zone = 'zone4'
            eatingTime = 'lunch'
        else:
            if(int(minute) <= 5):
                zone = 'zone3'
            elif(int(minute) <= 20):
                zone = 'zone4'
            elif(int(minute) <= 35):
                zone = 'zone1'
            else:
                zone = 'zone2'
            eatingTime = 'dinner'
    
    minute = str((int(minute)-int(minute)%15))
    time = hour + minute

    #hard code for testing
    hardCodedZone = ''
    hardCodedTime = ''
    hardCodedPeriod = ''
    hardCodedDate = ''

    #select a date to reserve for future days
    def selectDate():
        selectDateTable = driver.find_element_by_id('reservation_rsvndate')
        selectDateTable.click()
        if(hardCodedDate != ''):
            date = hardCodedDate
        selectDateFromTable = driver.find_element_by_xpath('//a[@class="ui-state-default" and contains(., '+ '1' +')]')
        selectDateFromTable.click()

    def selectTime():
        id = ''
        #time zone
        if(hardCodedZone != ''):
            id += hardCodedZone
        else:
            id += zone
        #time start
        if(hardCodedTime != ''):
            id += hardCodedTime
        else:
            id += time
        #time start period
        if(hardCodedPeriod != ''):
            id += hardCodedPeriod
        else:
            id += period
        #time end (start +15 min)
        if(hardCodedTime != ''):
            #add 0 cuz gets truncated when turned into int
            id += '0'
            id += str(int(hardCodedTime)+15)
        else:
            id += '0'
            id += str(int(time)+15)
        #time end period
        if(hardCodedPeriod != ''):
            id += hardCodedPeriod
        else:
            id += period

        driver.implicitly_wait(10)
        getButton = driver.find_element_by_id(id)
        getButton.click()

    #select location and period functions
    def selectPeriodLocationBreakfast():
        selectMealPeriod = Select(driver.find_element_by_id('reservation_meal'))
        selectMealPeriod.select_by_visible_text('Breakfast')
        selectMarket = Select(driver.find_element_by_id('reservation_marketplace'))
        selectMarket.select_by_visible_text('Marketplace xxx')
    def selectPeriodLocationLunch():
        selectMealPeriod = Select(driver.find_element_by_id('reservation_meal'))
        selectMealPeriod.select_by_visible_text('Lunch')
        selectMarket = Select(driver.find_element_by_id('reservation_marketplace'))
        selectMarket.select_by_visible_text('Marketplace xxx')
    def selectPeriodLocationDinner():
        selectMealPeriod = Select(driver.find_element_by_id('reservation_meal'))
        selectMealPeriod.select_by_visible_text('Dinner')
        selectMarket = Select(driver.find_element_by_id('reservation_marketplace'))
        selectMarket.select_by_visible_text('Marketplace xxx')

    def breakfast():
        selectDate()
        selectPeriodLocationBreakfast()
        selectTime()
    def lunch():
        selectDate()
        selectPeriodLocationLunch()
        selectTime()
    def dinner():
        selectDate()
        selectPeriodLocationDinner()
        selectTime()
    if(day == 0 or day == 1 or day == 2 or day == 3):
        #place breakfast order (7:00am)
        if(eatingTime == 'breakfast'):
            breakfast()
        #place lunch order (??)
        elif(eatingTime == 'lunch'):
            lunch()
        #place dinner order(??)
        else:
            dinner()

    elif(day == 4):
        #place breakfast order (7:00am)
        if(eatingTime == 'breakfast'):
            breakfast()
        #place lunch order (??)
        elif(eatingTime == 'lunch'):
            lunch()
        #place dinner order(??)
        else:
            dinner()

    elif(day == 5):
        #place breakfast order (8:00am)
        if(eatingTime == 'breakfast'):
            breakfast()
        #place lunch order (??)
        elif(eatingTime == 'lunch'):
            lunch()
        #place dinner order(??)
        else:
            dinner()

    else:
        #place le lunch order(??)
        if(eatingTime == 'lunch'):
            lunch()
        #place dinner order(??)
        else:
            dinner()

    #keep browser open for debugging
    while(True):
       pass
launchBrowser()
