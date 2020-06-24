from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/work/untitled/geckodriver.exe')
browser.get('http://localhost:8000')

assert 'TO-Do' in browser.title, "Browser title was " + browser.title