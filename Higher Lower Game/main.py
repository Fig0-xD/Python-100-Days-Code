import random
import art
from game_data import data


def clear(): print("\n" * 100)


def game():

    score = 0

    part_a = random.choice(data)
    part_b = random.choice(data)
    
    while part_a == part_a:
    part_b = random.choice(data)

    flag = True

    while flag:
        clear()
        print(art.logo)
        print(f"Compare A: {part_a['name']}, a {part_a['description']}, from {part_a['country']}.")
        print(art.vs)
        print(f"Against B: {part_b['name']}, a {part_b['description']}, from {part_b['country']}.")

        #print(f"\nFollower count A: {part_a['follower_count']}\nFollower count B: {part_b['follower_count']}")

        user_val = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if user_val == 'a' and part_a['follower_count'] > part_b['follower_count'] or \
                user_val == 'b' and part_b['follower_count'] > part_a['follower_count']:
            score += 1
            part_a = part_b
            part_b = random.choice(data)
              
            while part_a == part_a:
            part_b = random.choice(data)  
              
        else:
            print(f"\nSorry that's wrong ☹\nYour final score: {score}")
            break




if __name__ == '__main__':

    choice = 'y'

    while choice == 'y':
        game()

        choice = input("\nDo you want to play again?(Y/N): ").lower()

    print("\nTHANK YOU! 🙏 🙏")
