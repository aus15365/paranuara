
''' Unit tests for the dahlia Wiper.
'''

#to, Memjet Ltd. ("Memjet," "we," or "us") and is protected under U.S. and
#Foreign copyright, trademark and other intellectual property laws.

#Portions of this code may contain copyrighted materials from Memjet's
#suppliers, and copying and distribution of such materials for any other
#purpose except as permitted under a written agreement with respect to the
#Memjet Technology is expressly prohibited.


# System imports used by the unit tests:
import unittest

from joao.data   import (data_company, data_person)
from joao.common import (PersonFields, CompanyFields, 
                        Foods, Fruits, Vegetables)
from joao.common import (ParanuaraError, Paranuara)

class TestParanuara(unittest.TestCase):
    """Test the class Paranuara
    """
    def setUp(self):
        """Set up for testing."""
        pass

    def tearDown(self):
        """Tear down after testing"""
        pass

    def test_constructor(self):
        """Test the constructor of the class Paranuara"""
        pass

    def test_getting_a_person_details(self):
        """Test getting details of a person"""
        pass

    def test_search_a_person_failed(self):
        """Test failure case of getting details of a person"""
        pass


    def test_find_employees(self):
        """Test finding emplyees of a company"""
        pass

    def test_find_employees_failed(self):
        """Test failure case of of finding emplyees of a company"""
        pass


    def test_find_a_preson(self):
        """Test finding a person"""
        pass

    def test_find_commons_of_two_presons(self):
        """Test finding common details of two persons"""
        pass

    def test_find_commons_of_two_presons_failed(self):
        """Test filure case of finding common details of two persons"""
        pass
