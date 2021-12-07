import pandas as pd

#load file
file = None
while file is None:
    try:       
        n = input('Enter a class to grade (i.e. class1 for class1.txt): ')            
        file = open(f'Data Files/{n}.txt', 'r')       
        print(f'Successfully opened {n}.txt\n')
        print('**** ANALYZING ****\n')
    except:
        print('File cannot be found.\nPlease try again!')

#analyzing file
valid = 0
invalid = 0
valid_line =[]

for i in file:
    line = i.strip().split(',')   
    if len(line) != 26:
        print('Invalid line of data: does not contain exactly 26 values:')
        print(i, '\n')
        invalid += 1        
    elif len(line[0]) != 9 or not line[0].startswith('N') or not line[0][1:].isnumeric():
        print('Invalid line of data: N# is invalid')
        print(i, '\n')
        invalid += 1
    else:
        valid += 1
        valid_line.append(line)
        
#print info if no error found
if invalid == 0:
    print('No errors found!\n')

#calculate score
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')
result = []

for i in valid_line:
    score = 0
    for u, v in zip(answer_key, i[1:]):      
        if u == v:
            score += 4
        elif v == '':
            continue
        else:
            score -= 1
    result.append([i[0] ,score])
   
df = pd.DataFrame(result)   #make dataframe to store scores
df.to_csv(f'{n}_grades.txt', header = False, index = False)  #export txt

#report    
print('**** REPORT ****\n')
print('Total valid lines of data:', valid)
print('Total invalid lines of data:', invalid, '\n')
print('Mean (average) score: {:.2f}'.format(df[1].mean()))
print('Highest score:', df[1].max())
print('Lowest score:', df[1].min())
print('Range of scores:', df[1].max() - df[1].min())
print('Median score:', df[1].median(), '\n')
