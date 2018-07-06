


fakeAnswer= input("Petition:")
if "." in fakeAnswer:
    indexNumber = fakeAnswer.index(".")
    realAnswer = fakeAnswer[indexNumber+1:]
question = input("Question:")
print (realAnswer)
