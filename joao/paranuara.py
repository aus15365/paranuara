""" This module defines the abstract base classes for GPIO and sensor. """

import enum
import logging

from joao.data   import  data_company, data_person
from joao.common import  ApiException
from joao.common import  PersonFields, CompanyFields
from joao.common import  Foods, Fruits, Vegetables


class ParanuaraError(ApiException):
    """Paranuara-spefici error"""
    pass

class Paranuara(object):
    """Paranuara class

    This class provides the interface to control and access a Paranuara.

    :param name:      name of the Paranuara instance
    :type name:       string
    :param log:       a logger object; if None, then a logger will be created.

    Properties:
    """

    def __init__(self, name, log=None, *args, **kwargs):
        super(Paranuara, self).__init__(*args, **kwargs)

        if log is None:
            self._log = logging.getLogger('Paranuara')

        self.name = name

    def person(self, id):
        """return a person details based on an index number

        :param id:  person id
        :type id:   int

        :return:    List of information of the person
        :rtype:     List

        :raises:    :class:`ParanuaraError` if the parameter id is invalid
        """
        assert type(id) is int
        try:
            _person = data_person[id]
            return _person
        except Exception:
            self._log.exception("Person ID {0} does not exit".format(id))
            raise


    def employees(self, company):
        """List all employee currently working with a company.

        :param company:  company to search
        :type company:   int (index) or str (name)

        :return:    List of the employees working with the company
        :rtype:     List of person ID or empty list

        :raises:    :class:`ParanuaraError` if the parameter company is invalid
        """
        assert type(company) in (int, str)

        try:
            _employees = []
            _company_index = company
            if type(company) is str:
                for item in data_company:
                    if item[CompanyFields.COMPANY.value] == company:
                        _company_index = item[CompanyFields.INDEX.value]
                        break

            for item in data_person:
                if item[PersonFields.COMPANY_ID.value] == _company_index:
                    _employees.append(item[PersonFields.INDEX.value])

            return _employees
        except Exception:
            self._log.exception("Invalid company infomation {0} provided".format(company))
            raise


    def find_people(self, person_1, person_2=None):
        """Return the detail and some preference of the given person(s)

        When person 2 is None when means 1 person is given, this method provides a list of fruits and vegetables the person likes. 
        This endpoint must respect this interface: { "username": "Ahi", "age":"30", "fruits":["banana", "apple"], 
                                                     "vegetables":["beetroot", "lettuce"]}

        When person 2 is non None when means 2 presons are given, this method provides their information (Name, Age, Address, phone) 
        and a list of their friends in common which have brown eyes and are still alive.

        :param company:  company to search
        :type company:   int (index) or str (name)

        :return:    List of the employees working with the company
        :rtype:     List of person ID or empty list

        :raises:    :class:`ParanuaraError` if the parameter company is invalid
        """
        assert type(person_1) is int
        assert type(person_2) in (int, type(None))

        try:
            if person_2 is None:
                _person = self.person(person_1)
                _preference = {}
                _preference["username"] = _person[PersonFields.NAME.value]
                _preference["age"] = _person[PersonFields.AGE.value]
                _foods = _person[PersonFields.FOOD.value]
                _fruits = []
                _veg = []
                for item in _foods:
                    if item in Fruits:
                        _fruits.append(item)
                    else:
                        _veg.append(item)
                _preference["fruits"] = _fruits
                _preference["vegetables"] =_veg

                return _preference
            else:
                details = {}

                for item in (person_1, person_2):
                    _person = {}
                    _p = self.person(item)
                    _person["username"] = _p[PersonFields.NAME.value]
                    _person["Age"] = _p[PersonFields.AGE.value]
                    _person["Address"] = _p[PersonFields.ADDRESS.value]
                    _person["Phone"] = _p[PersonFields.PHONE.value]
                    _tag = "id_{0}".format(item)
                    details[_tag] = _person

                _p_1 = self.person(person_1)
                _p_2 = self.person(person_2)
                _commond_friend = list(set(_p_1[PersonFields.FRIENDS.value]).intersection(_p_2[PersonFields.FRIENDS.value]))
                _common = []
                for item in _commond_friend:
                    if (item[PersonFields.EYE_COLOR.value] == "brown" and
                        item[PersonFields.HAS_DIED.value] is False):
                        _common.append(item)
                details['common_friends'] = _common

                return details
        except Exception:
            self._log.exception("Invalid person with ID {0} or {1} is provided".format(person_1, person_2))
            raise
