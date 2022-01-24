import pandas as pd
import numpy as np

if __name__ == '__main__':

    """
    The following dataset has a blank column (Comment).
    Using the information below, add the correct comment for each row depending on the grade.
    0 - 2:  Poor
    3 - 6:  Average
    7 - 8:  Good
    9 - 10: Exceptional
    """

    students = pd.DataFrame({
        "Name": ["Rob", "Maya", "Parthiv", "Tom", "Julian", "Erica"],
        "Grade": [9, 5, 7, 1, 6, 10],
        "Comment": ['', '', '', '', '', '']
    })
    print("\nBefore:\n", students)

    students["Comment"] = students["Comment"].mask(students["Grade"].between(0, 2), "Poor")
    students["Comment"] = students["Comment"].mask(students["Grade"].between(3, 6), "Average")
    students["Comment"] = students["Comment"].mask(students["Grade"].between(7, 8), "Good")
    students["Comment"] = students["Comment"].mask(students["Grade"].between(9, 10), "Exceptional")

    """
    Alternative we can use np.where:
    students["Comment"] = np.where(students["Grade"].between(0, 2), "Poor", students["Comment"])
    """

    print("\nAfter:\n", students)



