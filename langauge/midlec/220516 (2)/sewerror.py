

# DeprecationWarning: find_element_by_xpath is deprecated. Please use find_element(by=By.XPATH, value=xpath) instead
#find_element_by_xpath is deprecated. Please use find_element(by=By.XPATH, value=xpath)
#ex 사용예
# button = driver.find_element_by_class_name("quiz_button")
# button = driver.find_element(By.CLASS_NAME, "quiz_button")
# 
# element = driver.find_element_by_id("element_id")
# element = driver.find_element(By.ID, "element_id")
# 
# element = driver.find_element_by_name("element_name")
# element = driver.find_element(By.NAME, "element_name")
# 
# element = driver.find_element_by_link_text("element_link_text")
# element = driver.find_element(By.LINK_TEXT, "element_link_text")
# 
# element = driver.find_element_by_partial_link_text("element_partial_link_text")
# element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
# 
# element = driver.find_element_by_tag_name("element_tag_name")
# element = driver.find_element(By.TAG_NAME, "element_tag_name")
# 
# element = driver.find_element_by_css_selector("element_css_selector")
# element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")
# 
# element = driver.find_element_by_xpath("element_xpath")
# element = driver.find_element(By.XPATH, "element_xpath")