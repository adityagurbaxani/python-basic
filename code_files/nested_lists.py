#Nested Lists
#store names and scores in a nested list.
#Print the name(s) of any student(s) having the second lowest grade.
def takeFirst(e):
    return e[0]

def takeSecond(e):
    return e[1]

records = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
records.sort(key=takeSecond)
min_score = takeSecond(records[0])
#remove records with lowest score
records = [e for e in records if takeSecond(e) != min_score]
get_score = takeSecond(records[0])
#keep only the records with second lowest score
records = [e for e in records if takeSecond(e) == get_score]
records.sort(key=takeFirst)
#print required output
for e in records:
    print(takeFirst(e))