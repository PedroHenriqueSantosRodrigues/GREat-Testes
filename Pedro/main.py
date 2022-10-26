from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
class TestVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\mateu\OneDrive\Área de Trabalho\Pedro\chromedriver.exe')
        self.browser.get("https://testlink.org/")

    def tearDown(self):
        self.browser.quit()

    def test_tittle(self):
        """""
        The test finds the page title and checks if it is as expected to check if we are on the Testlink page.
        """
        tittle = self.browser.find_element(By.CLASS_NAME, 'header')
        self.assertEqual(tittle.text, "TestLink")

    def test_subTttle(self):
        """""
        The test finds the page title and checks if it is as expected to check if we are on the Testlink page.
        """
        subTittle = self.browser.find_element(By.CLASS_NAME, 'jumbotron')
        self.assertEqual(subTittle.text, "TestLink Open Source Test Management")

    def test_gitHub(self):
        """Test looks for site github access anchor, clicks anchor, waits 10 seconds."""
        link = self.browser.find_element(By.LINK_TEXT, 'Access Git Repository (GitHub)')
        link.click()
        time.sleep(10)
        with self.subTest("Testing author name"):
            """The test checks if the author name is as expected."""
            author = self.browser.find_element(By.CLASS_NAME, 'author flex-self-stretch')
            self.assertEqual(author.text, "TestLinkOpenSourceTRMS")
        with self.subTest("Testing folder name"):
            """The test checks if the folder name is as expected."""
            folderName = self.browser.find_element(By.CLASS_NAME, "mr-2 flex-self-stretch")
            self.assertEqual(folderName.text, "testlink-code")
