# in this file i will attempt to apply material from day 8-10


from calendar import day_abbr


day8 = ('abstractClasses', 'inheritance', 'methodChaining',
        'methodOverriding', 'multipleInheritence', 'objectsAsArgs', 'superFunction')
day9 = ('duckTyping', 'functionsToVars', 'lambdaFunctions', 'walrusOperators')
day10 = ('dictionaryComp', 'filterFunction', 'listComp',
         'mapping', 'reduceFunction', 'zipFunction')

days8to10 = list(day8+day9+day10)

i = 0


def content(day):
    while i != len(day):
        print(i)
        i += 1


content(day8)
