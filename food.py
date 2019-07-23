'''
Hello student. Thank you for downloading a CORGIS library. However, you do not need to open this library. Instead you should use the following:

    import food
    
If you opened the file because you are curious how this library works, then well done! We hope that you find it a useful learning experience. However, you should know that this code is meant to solve somewhat esoteric pedagogical problems, so it is often not best practices. 
'''

import sys as _sys
import os as _os
import json as _json
import sqlite3 as _sql
import difflib as _difflib

def _tifa_definitions():
    return {"type": "ModuleType",
        "fields": {
            'get': {
                "type": "FunctionType",
                "name": 'get',
                "returns": {
                    "type": "ListType", 
                    "empty": False, 
                    "subtype": {"type": "NumType"}
                }
            },
        
            'get_reports': {
                "type": "FunctionType", 
                "name": 'get_reports',
                "returns": 
		{"type": "ListType", "subtype": 
			{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Data'}, {"type": "LiteralStr", "value": 'Category'}, {"type": "LiteralStr", "value": 'Description'}, {"type": "LiteralStr", "value": 'Nutrient Data Bank Number'}], "values": [
				{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Alpha Carotene'}, {"type": "LiteralStr", "value": 'Retinol'}, {"type": "LiteralStr", "value": 'Protein'}, {"type": "LiteralStr", "value": 'Ash'}, {"type": "LiteralStr", "value": 'Beta Cryptoxanthin'}, {"type": "LiteralStr", "value": 'Choline'}, {"type": "LiteralStr", "value": 'Niacin'}, {"type": "LiteralStr", "value": 'Sugar Total'}, {"type": "LiteralStr", "value": 'Lycopene'}, {"type": "LiteralStr", "value": 'Beta Carotene'}, {"type": "LiteralStr", "value": 'Carbohydrate'}, {"type": "LiteralStr", "value": 'Fiber'}, {"type": "LiteralStr", "value": 'Water'}, {"type": "LiteralStr", "value": 'Kilocalories'}, {"type": "LiteralStr", "value": 'Fat'}, {"type": "LiteralStr", "value": 'Refuse Percentage'}, {"type": "LiteralStr", "value": 'Pantothenic Acid'}, {"type": "LiteralStr", "value": 'Selenium'}, {"type": "LiteralStr", "value": 'Major Minerals'}, {"type": "LiteralStr", "value": 'Thiamin'}, {"type": "LiteralStr", "value": 'Lutein and Zeaxanthin'}, {"type": "LiteralStr", "value": 'Cholesterol'}, {"type": "LiteralStr", "value": 'Vitamins'}, {"type": "LiteralStr", "value": 'Riboflavin'}, {"type": "LiteralStr", "value": 'Household Weights'}, {"type": "LiteralStr", "value": 'Manganese'}], "values": [
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Saturated Fat'}, {"type": "LiteralStr", "value": 'Polysaturated Fat'}, {"type": "LiteralStr", "value": 'Total Lipid'}, {"type": "LiteralStr", "value": 'Monosaturated Fat'}], "values": [
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}]}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Calcium'}, {"type": "LiteralStr", "value": 'Magnesium'}, {"type": "LiteralStr", "value": 'Phosphorus'}, {"type": "LiteralStr", "value": 'Sodium'}, {"type": "LiteralStr", "value": 'Iron'}, {"type": "LiteralStr", "value": 'Copper'}, {"type": "LiteralStr", "value": 'Potassium'}, {"type": "LiteralStr", "value": 'Zinc'}], "values": [
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}]}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "NumType"}, 
					{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Vitamin C'}, {"type": "LiteralStr", "value": 'Vitamin B6'}, {"type": "LiteralStr", "value": 'Vitamin K'}, {"type": "LiteralStr", "value": 'Vitamin A - IU'}, {"type": "LiteralStr", "value": 'Vitamin A - RAE'}, {"type": "LiteralStr", "value": 'Vitamin B12'}, {"type": "LiteralStr", "value": 'Vitamin E'}], "values": [
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "NumType"}]}, 
					{"type": "NumType"}, 
					{"type": "DictType", "literals": [{"type": "LiteralStr", "value": '1st Household Weight'}, {"type": "LiteralStr", "value": '2nd Household Weight'}, {"type": "LiteralStr", "value": '1st Household Weight Description'}, {"type": "LiteralStr", "value": '2nd Household Weight Description'}], "values": [
						{"type": "NumType"}, 
						{"type": "NumType"}, 
						{"type": "StrType"}, 
						{"type": "StrType"}]}, 
					{"type": "NumType"}]}, 
				{"type": "StrType"}, 
				{"type": "StrType"}, 
				{"type": "NumType"}]}},
            }
        
        }
    }

class _Constants(object):
    '''
    Global singleton object to hide some of the constants; some IDEs reveal internal module details very aggressively, and there's no other way to hide stuff.
    '''
    _HEADER = {'User-Agent': 
              'CORGIS Food library for educational purposes'}
    _PYTHON_3 = _sys.version_info >= (3, 0)
    _TEST = False
    _HARDWARE = 1000

if _Constants._PYTHON_3:
    import urllib.request as _request
    from urllib.parse import quote_plus as _quote_plus
    from urllib.error import HTTPError as _HTTPError
else:
    import urllib2 as _urllib2
    from urllib import quote_plus as _quote_plus
    from urllib2 import HTTPError as _HTTPError

class DatasetException(Exception):
    ''' Thrown when there is an error loading the dataset for some reason.'''
    pass
    
_Constants._DATABASE_NAME = _os.path.join(_os.path.dirname(__file__),
                                          "food.db")
if not _os.access(_Constants._DATABASE_NAME, _os.F_OK):
    raise DatasetException("Error! Could not find a \"{0}\" file. Make sure that there is a \"{0}\" in the same directory as \"{1}.py\"! Spelling is very important here.".format(_Constants._DATABASE_NAME, __name__))
elif not _os.access(_Constants._DATABASE_NAME, _os.R_OK):
    raise DatasetException("Error! Could not read the \"{0}\" file. Make sure that it readable by changing its permissions. You may need to get help from your instructor.".format(_Constants._DATABASE_NAME, __name__))
elif not _os.access(_Constants._DATABASE_NAME, _os.W_OK):
    # Previously, this generated an error - but that's not important, really.
    #_sys.stderr.write('The local cache (\" \") will not be updated. Make sure that it is writable by changing its permissions. You may need to get help from your instructor.\n'.format(_Constants._DATABASE_NAME))
    #_sys.stderr.flush()
    pass

_Constants._DATABASE = _sql.connect(_Constants._DATABASE_NAME)

class _Auxiliary(object):
    @staticmethod
    def _parse_type(value, type_func):
        """
        Attempt to cast *value* into *type_func*, returning *default* if it fails.
        """
        default = type_func(0)
        if value is None:
            return default
        try:
            return type_func(value)
        except ValueError:
            return default
    
    @staticmethod    
    def _byteify(input):
        """
        Force the given input to only use `str` instead of `bytes` or `unicode`.
        This works even if the input is a dict, list,
        """
        if isinstance(input, dict):
            return {_Auxiliary._byteify(key): _Auxiliary._byteify(value) for key, value in input.items()}
        elif isinstance(input, list):
            return [_Auxiliary._byteify(element) for element in input]
        elif _Constants._PYTHON_3 and isinstance(input, str):
            return str(input.encode('ascii', 'replace').decode('ascii'))
        elif not _Constants._PYTHON_3 and isinstance(input, unicode):
            return str(input.encode('ascii', 'replace').decode('ascii'))
        else:
            return input
    
    @staticmethod    
    def _guess_schema(input):
        if isinstance(input, dict):
            return {str(key.encode('ascii', 'replace').decode('ascii')): 
                    _Auxiliary._guess_schema(value) for key, value in input.items()}
        elif isinstance(input, list):
            return [_Auxiliary._guess_schema(input[0])] if input else []
        else:
            return type(input)
            


################################################################################
# Domain Objects
################################################################################
    

    


################################################################################
# Interfaces
################################################################################



def get_reports(test=False):
    """
    Returns food reports from the dataset.
    
    """
    if _Constants._TEST or test:
        rows = _Constants._DATABASE.execute("SELECT data FROM food LIMIT {hardware}".format(
            hardware=_Constants._HARDWARE))
        data = [r[0] for r in rows]
        data = [_Auxiliary._byteify(_json.loads(r)) for r in data]
        
        return _Auxiliary._byteify(data)
        
    else:
        rows = _Constants._DATABASE.execute("SELECT data FROM food".format(
            hardware=_Constants._HARDWARE))
        data = [r[0] for r in rows]
        data = [_Auxiliary._byteify(_json.loads(r)) for r in data]
        
        return _Auxiliary._byteify(data)
        

################################################################################
# Internalized testing code
################################################################################

def _test_interfaces():
    from pprint import pprint as _pprint
    from timeit import default_timer as _default_timer
    # Production test
    print("Production get_reports")
    start_time = _default_timer()
    result = get_reports()
    
    print("{} entries found.".format(len(result)))
    _pprint(_Auxiliary._guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    # Test test
    print("Test get_reports")
    start_time = _default_timer()
    result = get_reports(test=True)
    
    print("{} entries found.".format(len(result)))
    _pprint(_Auxiliary._guess_schema(result))
    
    print("Time taken: {}".format(_default_timer() - start_time))
    

if __name__ == '__main__':
    from optparse import OptionParser as _OptionParser
    _parser = _OptionParser()
    _parser.add_option("-t", "--test", action="store_true",
                      default=False,
                      help="Execute the interfaces to test them.")
    (_options, _args) = _parser.parse_args()
    
    if _options.test:
        _test_interfaces()