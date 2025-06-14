from typing import Optional, Any
from typing import List
from typing import Union


'''Optional Example'''
def get_name(name:Optional[str] = None) ->str:
    if name:
        return name
    return "Anonymous"
print(get_name())


'''Union Example'''
def process_value(value: Union[int, str]) ->str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"
print(process_value("digital school"))

'''Any example'''
def process_anything(value: any):
    return f"processed {value}"
print(process_anything(True))

'''List example'''
def sum_list(number: List[int]) -> int:
    return sum(number)

numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)