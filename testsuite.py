import unittest
import HtmlTestRunner
import os
from homepage_testsuite import TestHomepage
from reports_utils import getTestNames
from slots_testsuite import TestSlots

# get the directory path to output report file
dirpath = os.getcwd()

# get all tests from SearchText and HomePageTest class
home_page_test = unittest.TestLoader().loadTestsFromTestCase(TestHomepage)
slots_test = unittest.TestLoader().loadTestsFromTestCase(TestSlots)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test])

# open the report file
outfile = 'reportes/'

#custom template
template_path = 'reportes/example_template.html'

#Get list of functions

functions_names_list = getTestNames(TestHomepage)


print(functions_names_list)
#configure template args
template_args = {
    "screenshots": functions_names_list
}

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output=outfile, template=template_path, template_args=template_args)

# run the suite using HTMLTestRunner
runner.run(test_suite)