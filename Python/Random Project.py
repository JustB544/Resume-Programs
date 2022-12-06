#a quick script I made to read an email my now fiance sent me that was botched by gmail
counter = 0
done = False
newText = ""
#this is just an example of how the email was formatted, the real email was thousands of characters long
go = str(" H e y ?  H o w  a r e  y o u ? ")
for x in go:
    if counter == 1:
        counter = 0
        done = True
    if done == False and counter == 0:
        counter = 1
        newText = newText + x
    elif x != " ":
        counter = 1
        newText = newText + x
    done = False
print(newText)
    
