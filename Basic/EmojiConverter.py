emojis={
    ":)":"😃",
    ':(':"😒",
}
message=input("> ")
message_words=message.split(" ")
output=''
for i in message_words:
    output+=emojis.get(i,i)+" "
print(output)
        
        
