#Let's import another package for some fun
#Open a command prompt and run "pip install emoji" command, to download & install emoji module from internet
from emoji import emojize, demojize
print(emojize(":winking_face_with_tongue:"))
print(emojize(":grinning_face_with_big_eyes:"))
print(emojize(":zipper-mouth_face:"))
print(emojize('Python is :cookie:'))
print(emojize('I :red_heart: Python'))
print(demojize('🤐'))
print(emojize(":Pakistan:"))
print(demojize('🇵🇰'))
print(demojize('🇺🇸'))
print(emojize(':United_States:'))

print("\U0001f600") 

#exercise 1
#print 40 smile faces, hint use for loop
# exercise 2, print usa flag followed by your parent's country of origin 50 times
