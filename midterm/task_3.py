from random import choice
def rock_paper_scissor(player1):
    computer=choice(('R','P','S'))
    print(computer)
    if player1=='R' and computer=='S':
        return ' მოთამაშემ მოიგო'    
    if player1=='R' and computer=='P':
        return 'მოთამაშემ წააგო'
    if player1=='S' and computer=='P':
        return 'მოთამაშემ მოიგო'
    if player1=='S' and computer=='R':
        return 'მოთამაშემ წააგო'
    if player1=='P' and computer=='R':
        return 'მოთამაშემ მოიგო'
    if player1=='P' and computer=='S':
        return 'მოთამაშემ წააგო'
    if player1==computer:
        print('ფრეა.კიდევ ერთი თამაში')
        return main()
def main():
    player_1_input=input('enter R,P or S :')
    rock_paper_scissor(player_1_input)
    
if __name__=='__main__':
    main()
    
        
    
        