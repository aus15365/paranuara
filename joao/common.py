""" This module defines common classes to be used in the whole package. """

import enum

class ApiException(Exception):
    """Report and process errors coming from the API package.

       This class is used to raise all error clauses defined in this file,
       e.g. raise ExeApiException(error_msg)
    """
    pass

@enum.unique
class PersonFields(enum.Enum):
    """All fiedls defiend with a person.

    This enum lists all person fields known to the API.
    """
    
    def __str__(self):
        return str(self.value)

    ID         = '_id'
    INDEX      = 'index'
    GUID       = 'guid'
    HAS_DIED   = 'has_died'
    BALANCE    = 'balance'
    PICTURE    = 'picture'
    AGE        = 'age'
    EYE_COLOR  = 'eyeColor'
    NAME       = 'name'
    GENDER     = 'gender'
    COMPANY_ID = 'company_id'
    EMAIL      = 'email'
    PHONE      = 'phone'
    ADDRESS    = 'address'
    ABOUT      = 'about',
    REGISTERED = 'registered'
    TAGS       = 'tags'
    FRIENDS    = 'friends'
    GREETING   = 'greeting'
    FOOD       = 'favouriteFood'
  
@enum.unique
class CompanyFields(enum.Enum):
    """All fiedls defiend with a company.

    This enum lists all company fields known to the API.
    """

    def __str__(self):
        return str(self.value)

    INDEX   = 'index'
    COMPANY = 'company'

@enum.unique
class Foods(enum.Enum):
    """All foods defiend with this package.

    This enum lists all food known to the API.
    """

    def __str__(self):
        return str(self.value)

    ORANGE     = 'orange'
    APPLE      = 'apple'
    BANANA     = 'banana'
    STRAWBERRY = 'strawberry'
    BEETROOT   = 'beetroot'
    CELERY     = 'celery'
    CUCMBER    = 'cucumber'
    CARROT     = 'carrot'

# Defind list for fruits
Fruits = [    
             Foods.APPLE.value, 
             Foods.BANANA.value, 
             Foods.ORANGE.value, 
             Foods.STRAWBERRY.value
         ]

# Defind list for vegatables
Vegetables = [
                 Foods.BEETROOT.value, 
                 Foods.CARROT.value, 
                 Foods.CELERY.value, 
                 Foods.CUCMBER.value
             ]

