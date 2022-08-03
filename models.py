from fastapi import Query
from pydantic import BaseModel, validator
import re


RE_INT_AND_MATH = re.compile(r'([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)')


class CalcGetRequest(BaseModel):
    expression: str = Query(None, max_length=50)
    @validator('expression')
    def onlySimpleMathAndNumbers(cls, v):
        if RE_INT_AND_MATH.match(v):
            return v
        else:
            raise ValueError('only simple math and numbers required')


class CalcPostRequest(BaseModel):
    first: int
    last: int
    operator: str
    @validator('operator')
    def onlySimpleMath(cls, v):
        if v in ['*', '/', '+', '-']: #== '*' or v == '/' or v == '-' or v == '+':
            return v
        raise ValueError('only simple math required')


class CalcResponce(BaseModel):

    result: str = None
    operation: str = None