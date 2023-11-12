import hangman_stages
print("***** Let's Play HANGMAN *****")
print("Player 1 :")
word=input("Enter a word: ")
display=[]
for i in range(len(word)):
    display += '_'
    print(display[i],end=" ")
lives=6
game_over=False
while not game_over:
    print(f"\nYou have {lives} lives left")
    g=input("guess the word: ")
    for i in range(len(word)):
        letter=word[i]
        if(g==letter):
            display[i]=letter
    for i in range(len(display)):
            print(display[i],end=" ")
    print(hangman_stages.stages[lives-1])
    if g not in word:
        lives-=1
    if '_' not in display:
        game_over=True
        print("\nYou Won !!!")
        print(hangman_stages.won[0])
    if lives==0:
        game_over=True
        print("\nYou Lose !!!")
        
        




