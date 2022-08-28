def game():
    return 124
score=game()
with open("C:\\Users\\paras\\OneDrive\\Desktop\\python\\chapter-9\\chapter-9-practice-set\\hiscore.txt") as f:
    hiScoreStr =f.read()
if hiScoreStr=='':
    with open("C:\\Users\\paras\\OneDrive\\Desktop\\python\\chapter-9\\chapter-9-practice-set\\hiscore.txt","w") as f:
        f.write(str(score))   
elif int(hiScoreStr)<score:
    with open("C:\\Users\\paras\\OneDrive\\Desktop\\python\\chapter-9\\chapter-9-practice-set\\hiscore.txt","w") as f:
        f.write(str(score))