import pandas as pd


'''

train.csv
Survival - Survival (0 = No; 1 = Yes). Not included in test.csv file.
Pclass - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
Name - Name
Sex - Sex
Age - Age
Sibsp - Number of Siblings/Spouses Aboard
Parch - Number of Parents/Children Aboard
Ticket - Ticket Number
Fare - Passenger Fare
Cabin - Cabin
Embarked - Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

Variable Notes
pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.

'''


def q1():
    squared_integers = [i ** 2 for i in range(1, 100001)]
    print("q1:", squared_integers)

def q2():
    def max_two_numbers(a, b):
        return max(a, b)

def q3():
    df = pd.read_csv('test.csv')
    print(df.shape)
    print(len(df.columns))

def q4():
    df = pd.read_csv('train.csv')
    print(df.columns)
    # print(df['Age'])
    print(max(df['Age']))
    print(min(df['Age']))

def q5():
    df = pd.read_csv('train.csv')
    print(df.columns)
    print(df.Sex.unique())
    print(df.groupby('Sex')['Sex'].count())


def q6():
    df = pd.read_csv('train.csv')
    print(df.columns)
    # print(df['Pclass'].unique())
    print(round(df[df['Pclass'] == 1]['Fare'].mean(), 2))
    print(round(df[df['Pclass'] == 2]['Fare'].mean(), 2))
    print(round(df[df['Pclass'] == 3]['Fare'].mean(), 2))

    # print(df['Pclass'].groupby("Pclass").count())


def q7():
    from collections import defaultdict
    import pprint


    df = pd.read_csv('train.csv')
    titles = []
    title_count = defaultdict(int)
    for name in df['Name']:
        tokens = name.split(" ")
        try:
            if '.' in tokens[1]:
                title_count[tokens[1]] += 1
        except:
            pass
    pprint.pprint(title_count)

# q1()
# q2()
# q3()
# q4()
# q5()
# q6()
q7()