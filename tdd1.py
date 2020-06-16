from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.broswer=webdriver.Firefox()
    def tearDown(self):
        self.broswer.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online todo app. she goes
        #to check out its homepage
        self.broswer.get('http://localhost:8000')



        #she notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.broswer.title)
        header_text=self.broswer.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        


        #she is invited to enter a to-do item straight away
        inputbox=self.broswer.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        #she types "buy peacock feathers" into a text box (edith's hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        #when she hits enter. the pagr updates,and now the page lists
        #1: buy peacock feathers as an item in a to-do list
        inputbox.sned_keys(Keys.ENTER)
        time.sleep(1)

        table=self.broswer.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1:Buy peacock feathers' for row in rows)
            )

        #there is still atext box inviting her to add another item. she
        #enters "use peacock feathers to make a fly"(edith is very methodical)
        self.fail('Finish the test!')
if __name__=='__main__':
    unittest.main(warnings='ignore')
#the page updates again,and now shows both items on her list
#edith wonders whether the site will remember her list then she sees
#that the site has generated a unique url for her --there is some
#explanatory text to that effect.
