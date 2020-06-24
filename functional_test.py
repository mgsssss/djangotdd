from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/work/untitled/geckodriver.exe')
browser.get('http://localhost:8000')
#browser.get('http://www.naver.com')

assert 'Django' in browser.title