import os
import sys
from finance_complaint.exception import FinanceException

def main():
    try:
        print("e")
    except Exception as e:
        raise FinanceException(e, sys)

if __name__== "__main__":
    try:
        print("e")
    except Exception as e:
        raise FinanceException(e, sys)


