def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)
print(LongestWord(input()))





def QuestionsMarks(str):
    a = 11
    b = 'false'
    c = 0
    for i in str:
        if i.isdigit():
            if int(i) + a == 10:
                if c != 3:
                    return 'false'
                b = 'true'
            c = 0
            a = int(i)
        elif i == '?':
            c += 1
    return b
# keep this function call here
z = 'acc?7??sss?3rr1??????'
print(QuestionsMarks(z))






def FirstReverse(strParam):
 a = strParam[::-1]
 return a
# code goes here
  

# keep this function call here 
print((FirstReverse('I love code')))




def FirstFactorial(num):
  if num ==1:
    return 1
  else:
    return num * FirstFactorial(num-1)
  # code goes here

# keep this function call here 
print(FirstFactorial(4))