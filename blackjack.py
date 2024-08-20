import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_pick_list = []
cpu_pick_list = []

# method to pick 2 cards for the user
def user_pick():
  user_pick_list.extend(random.choices(cards, k=2))
  return user_pick_list

# method to pick 2 cards for the cpu
def cpu_pick():
  cpu_pick_list.extend(random.choices(cards, k=2))
  return cpu_pick_list

# sum all elements of user_pick_list
def sum_result_user():
  return sum(user_pick_list)

# sum all elements of cpu_pick_list
def sum_result_cpu():
  return sum(cpu_pick_list)

# add an extra card tp user_pick_list
def user_pick_add():
  user_pick_list.extend(random.choices(cards))

# add an extra element to cpu pick list
def cpu_pick_add():
  cpu_pick_list.extend(random.choices(cards))

print(f"Your cards: {user_pick()}, current score: {sum_result_user()}")
cpu_pick()
sum_result_cpu()
print(f"Computer's first card: {cpu_pick_list[0]}")

choice_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()

if choice_user == 'y':
    user_pick_add()
    if sum_result_user() > 21:
        print(f"Your sum of cards {sum_result_user()}")
        print(f"CPU sum of cards {sum_result_cpu()}")
        print(f"You lost! (busted)")
    elif sum_result_user() > sum_result_cpu() or sum_result_cpu() > 21:
        print(f"Your sum of cards {sum_result_user()}")
        print(f"CPU sum of cards {sum_result_cpu()}")
        print(f"You win!")
    else:
        print(f"Your sum of cards {sum_result_user()}")
        print(f"CPU sum of cards {sum_result_cpu()}")
        print(f"You lost!")

elif choice_user == 'n':
    if sum_result_cpu() > 21:
        print(f"Your sum of cards {sum_result_user()}")
        print(f"CPU sum of cards {sum_result_cpu()}")
        print(f"CPU busted, you win!")
    else:
        cpu_choice = random.choice(["y", "n"])
        while cpu_choice == "y" and sum_result_cpu() <= 21:
            cpu_pick_add()
            cpu_choice = random.choice(["y", 'n'])
        if sum_result_cpu() > 21:
            print(f"Your sum of cards {sum_result_user()}")
            print(f"CPU sum of cards {sum_result_cpu()}")
            print(f"CPU busted, you win!")
        elif sum_result_cpu() > sum_result_user():
            print(f"Your sum of cards {sum_result_user()}")
            print(f"CPU sum of cards {sum_result_cpu()}")
            print(f"You lost!")
        else:
            print(f"Your sum of cards {sum_result_user()}")
            print(f"CPU sum of cards {sum_result_cpu()}")
            print(f"You win!")