from re import search
from selenium import webdriver
from webdriver_manager .chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


search_term = "earbuds"
website_url = f"https://www.google.com/search?q=cars&newwindow=1&safe=active&sxsrf=ALeKk033gsfNuTuSJ1ItSqtxKNROaWNlew:1623237196014&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0jNHjtYrxAhXBAnIKHSS2B6kQ_AUoAXoECAIQAw&cshid=1623237325608918&biw=958&bih=969"

driver.get(website_url)


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
website_url = "https://www.google.co.in/search"


search_term = "earbuds"
driver.get(website_url+"?q="+search_term) 
