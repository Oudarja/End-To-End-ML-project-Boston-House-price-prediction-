

from pydantic import BaseModel

# here we define the data model for house features
# this will be used to validate the input data for prediction
# dictionary keys should match the feature names used in the model training
# so feature value will be passed as json or dictionary??
# yes as json in the request body
class HouseFeatures(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: int
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: int
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float