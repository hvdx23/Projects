from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

@given('I navigate to "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@when('I search for "{query}"')
def step_impl(context, query):
    wait = WebDriverWait(context.driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys(query)
    search_box.submit()

@then('I see "{text}" in the results')
def step_impl(context, text):
    assert text in context.driver.page_source

@then('I click "{text}" in the results')
def step_impl(context, text):
    link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text))
    )
    ActionChains(context.driver).move_to_element(link).click(link).perform()


@then('I click the rubbish link')
def step_impl(context):
    link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Rubbish and recycling'))
    )
    ActionChains(context.driver).move_to_element(link).click(link).perform()
    
from selenium.webdriver.common.keys import Keys

@then('I scroll down')
def step_impl(context):
    body = context.driver.find_element_by_css_selector('body')
    for _ in range(10):  # Adjust the range as needed
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Adjust sleep time as needed
    
@then('I run axe')
def step_impl(context):
    # Load the axe-core script
    with open('node_modules/axe-core/axe.min.js') as f:
        axe_script = f.read()

    # Inject the script into the page
    context.driver.execute_script(axe_script)

    # Run axe
    results = context.driver.execute_script('return axe.run();')

    # Process the results
    with open('axe_results.json', 'w') as f:
        json.dump(results, f)

    print(json.dumps(results))


@then('I quit the browser')
def step_impl(context):
     # wait for 10 seconds
    context.driver.quit()
    
    
    
    
