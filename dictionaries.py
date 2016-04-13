# names = {"AliceBlue": "#f0f8ff", "BlueViolet": "#8a2be2", "black": "#000000", "BlanchedAlmond": "#ffebcd", "brown":
#          "#a52a2a", "coral": "#ff7f50", "CornflowerBlue": "#6495ed", "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc"
#          , "GhostWhite": "#f8f8ff"}
#
# name = input("Enter colour name")
# while name != "":
#     if name in NAMES:
#         print(name, "is", names[name])
#     else:
#         print("Invalid colour name input")
#     name = input("Enter colour name")

user_text = input("Text: ")
print(user_text)
word_count = {}
txt = user_text.split()
for word in txt:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count):
    print("{} : {}".format(word, word_count[word]))

