#!/usr/bin/python3
"""
This script defines a City class
to work with MySQLAlchemy ORM.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
print ( (" Pleae selct the options-- - : " )
print ( for addition") )
print ( " 2 for
print ( " 3 for multiplication")
 print ( " 4 for division") )
 choice - input ** Enter your choice-- " ) )
first= int (input Enter first Number
second= int ( input ( e Enter second Number
 if choice == '1'
     print Answer is first + second )
 elif choice ..
     print ( " Answer is " first - second )
 elif choice ==
     print (" Answer is " F first*second )
elif choice 4 11
