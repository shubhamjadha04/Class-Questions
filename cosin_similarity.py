import numpy as np


def doc_distance(doc1,doc2):
    d1 = doc1.split()
    d2 = doc2.split()
    voc = []
    for word in d1:
        if word not in voc:
            voc.append(word)

    for word in d2:
        if word not in voc:
            voc.append(word)

    D1 = []
    D2 = []
    for word in voc:
        if word in d1:
            D1.append(1)
        else:
            D1.append(0)

    for word in voc:
        if word in d2:
            D2.append(1)
        else:
            D2.append(0)

    dot_product = np.dot(D1,D2)

    mag_D1=np.linalg.norm(D1)
    mag_D2 = np.linalg.norm(D2)

    cosin_similarity = dot_product/ (mag_D1*mag_D2)


    return cosin_similarity


doc1 = """
Python is a powerful programming language used for data science,
machine learning, web development, automation, and scientific computing.
Python has a simple syntax and provides many useful libraries.
Data science uses Python to analyze data, build models, create visualizations,
and solve complex problems. NumPy and Pandas are important Python libraries
for working with data and numerical calculations.
"""
doc2 = """
Data science is an important field that uses programming, statistics,
machine learning, and mathematics to solve real world problems.
Python is widely used in data science because it has a simple syntax
and many powerful libraries. NumPy is useful for numerical computing,
while Pandas is commonly used for data analysis and manipulation.
Machine learning models can be developed using Python and used to
make predictions from large datasets.
"""

print(doc_distance(doc1,doc2))