from tkinter import *
import random
import time


root = Tk()
root.geometry("500x750")
root.resizable(0, 0)
root.title("🎮 Rock Paper Scissors Tournament")
root.config(bg="#1a1a1a")


player_skill_available = False
computer_skill_available = False
skill_cooldown = 15
player_last_skill_time = 0
computer_last_skill_time = 0
player_coins = 100
current_bet = 0
tournament_round = 0
player_score = 0
computer_score = 0
game_active = False
user_choice = ""
games_played = 0
games_required_for_skill = 3

BG_COLOR = "#1a1a1a"
CARD_COLOR = "#2d2d2d"
TEXT_COLOR = "#000000"
ACCENT_COLOR = "#ff6b35"
PRIMARY_COLOR = "#4a90e2"
SUCCESS_COLOR = "#27ae60"
WARNING_COLOR = "#f39c12"
DANGER_COLOR = "#e74c3c"
PURPLE_COLOR = "#9b59b6"

header_label = Label(
    root,
    text="🎮 ROCK PAPER SCISSORS TOURNAMENT 🎮",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
)
header_label.pack(pady=15)

stats_frame = Frame(root, bg=CARD_COLOR, relief=RAISED, bd=2)
stats_frame.place(x=25, y=70, width=450, height=70)

coins_var = StringVar()
coins_var.set(f"💰 Coins: {player_coins}")
bet_var = StringVar()
bet_var.set(f"🎯 Current Bet: {current_bet}")

Label(
    stats_frame,
    textvariable=coins_var,
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).place(x=20, y=15)
Label(
    stats_frame,
    textvariable=bet_var,
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).place(x=230, y=15)

tournament_frame = Frame(root, bg=CARD_COLOR, relief=RAISED, bd=2)
tournament_frame.place(x=25, y=155, width=450, height=70)

round_var = StringVar()
round_var.set("🏆 Tournament: Not Started")
score_var = StringVar()
score_var.set("📊 Score: You 0 - 0 Computer")

Label(
    tournament_frame,
    textvariable=round_var,
    font=("Arial", 12, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).place(x=20, y=15)
Label(
    tournament_frame,
    textvariable=score_var,
    font=("Arial", 12, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).place(x=20, y=40)

choice_frame = Frame(root, bg=CARD_COLOR, relief=RAISED, bd=2)
choice_frame.place(x=25, y=240, width=450, height=150)

Label(
    choice_frame,
    text="🎯 CHOOSE YOUR MOVE:",
    font=("Arial", 16, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).pack(pady=10)


def select_rock():
    global user_choice
    user_choice = "rock"
    update_choice_display()
    Result.set("✅ Selected: ROCK - Click PLAY or USE SKILL")


def select_paper():
    global user_choice
    user_choice = "paper"
    update_choice_display()
    Result.set("✅ Selected: PAPER - Click PLAY or USE SKILL")


def select_scissors():
    global user_choice
    user_choice = "scissors"
    update_choice_display()
    Result.set("✅ Selected: SCISSORS - Click PLAY or USE SKILL")


def update_choice_display():
    rock_btn.config(bg="#404040", fg=TEXT_COLOR, relief=RAISED)
    paper_btn.config(bg="#404040", fg=TEXT_COLOR, relief=RAISED)
    scissors_btn.config(bg="#404040", fg=TEXT_COLOR, relief=RAISED)

    if user_choice == "rock":
        rock_btn.config(bg=PRIMARY_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
    elif user_choice == "paper":
        paper_btn.config(bg=SUCCESS_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
    elif user_choice == "scissors":
        scissors_btn.config(bg=DANGER_COLOR, fg=TEXT_COLOR, relief=SUNKEN)


button_frame = Frame(choice_frame, bg=CARD_COLOR)
button_frame.pack(pady=10)

rock_btn = Button(
    button_frame,
    text="✊ ROCK",
    font=("Arial", 16, "bold"),
    bg="#404040",
    fg=TEXT_COLOR,
    command=select_rock,
    width=8,
    height=2,
    relief=RAISED,
    bd=3,
)
rock_btn.pack(side=LEFT, padx=8)

paper_btn = Button(
    button_frame,
    text="✋ PAPER",
    font=("Arial", 16, "bold"),
    bg="#404040",
    fg=TEXT_COLOR,
    command=select_paper,
    width=8,
    height=2,
    relief=RAISED,
    bd=3,
)
paper_btn.pack(side=LEFT, padx=8)

scissors_btn = Button(
    button_frame,
    text="✌️ SCISSORS",
    font=("Arial", 16, "bold"),
    bg="#404040",
    fg=TEXT_COLOR,
    command=select_scissors,
    width=8,
    height=2,
    relief=RAISED,
    bd=3,
)
scissors_btn.pack(side=LEFT, padx=8)

bet_frame = Frame(root, bg=CARD_COLOR, relief=RAISED, bd=2)
bet_frame.place(x=25, y=405, width=450, height=80)

Label(
    bet_frame,
    text="💰 PLACE YOUR BET (Best of 3 Rounds)",
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).pack(pady=8)


def place_bet(amount):
    global current_bet, player_coins, game_active
    if not game_active and player_coins >= amount:
        current_bet = amount
        player_coins -= amount
        update_displays()
        Result.set(f"✅ Bet placed: {amount} coins - Tournament starts!")
        start_tournament()


bet_button_frame = Frame(bet_frame, bg=CARD_COLOR)
bet_button_frame.pack()

Button(
    bet_button_frame,
    text="10",
    font=("Arial", 12, "bold"),
    bg=SUCCESS_COLOR,
    fg=TEXT_COLOR,
    command=lambda: place_bet(10),
    width=6,
    height=1,
    bd=2,
    relief=RAISED,
).pack(side=LEFT, padx=4)
Button(
    bet_button_frame,
    text="25",
    font=("Arial", 12, "bold"),
    bg=PRIMARY_COLOR,
    fg=TEXT_COLOR,
    command=lambda: place_bet(25),
    width=6,
    height=1,
    bd=2,
    relief=RAISED,
).pack(side=LEFT, padx=4)
Button(
    bet_button_frame,
    text="50",
    font=("Arial", 12, "bold"),
    bg=WARNING_COLOR,
    fg=TEXT_COLOR,
    command=lambda: place_bet(50),
    width=6,
    height=1,
    bd=2,
    relief=RAISED,
).pack(side=LEFT, padx=4)
Button(
    bet_button_frame,
    text="100",
    font=("Arial", 12, "bold"),
    bg=DANGER_COLOR,
    fg=TEXT_COLOR,
    command=lambda: place_bet(100),
    width=6,
    height=1,
    bd=2,
    relief=RAISED,
).pack(side=LEFT, padx=4)
Button(
    bet_button_frame,
    text="ALL IN",
    font=("Arial", 12, "bold"),
    bg=PURPLE_COLOR,
    fg=TEXT_COLOR,
    command=lambda: place_bet(player_coins),
    width=8,
    height=1,
    bd=2,
    relief=RAISED,
).pack(side=LEFT, padx=4)

skill_frame = Frame(root, bg=CARD_COLOR, relief=RAISED, bd=2)
skill_frame.place(x=25, y=500, width=450, height=80)

Label(
    skill_frame,
    text="⚡ SKILLS - Auto WIN One Round",
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
).pack(pady=8)

player_skill_status = StringVar()
player_skill_status.set(
    f"🎮 Your Skill: LOCKED ({games_required_for_skill - games_played} games left)"
)
computer_skill_status = StringVar()
computer_skill_status.set(
    f"💻 Computer Skill: LOCKED ({games_required_for_skill - games_played} games left)"
)

Label(
    skill_frame,
    textvariable=player_skill_status,
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=PRIMARY_COLOR,
).place(x=20, y=40)
Label(
    skill_frame,
    textvariable=computer_skill_status,
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=DANGER_COLOR,
).place(x=240, y=40)

result_frame = Frame(root, bg=CARD_COLOR, relief=RAISED, bd=2)
result_frame.place(x=25, y=595, width=450, height=60)

Result = StringVar()
Result.set("🎮 Welcome! Place your bet and choose your move!")

result_label = Label(
    result_frame,
    textvariable=Result,
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    wraplength=430,
    justify=CENTER,
)
result_label.place(x=10, y=10, width=430, height=40)

action_frame = Frame(root, bg=BG_COLOR)
action_frame.place(x=25, y=670, width=450, height=50)


def use_player_skill():
    global player_skill_available, player_last_skill_time, games_played

    if games_played < games_required_for_skill:
        Result.set(
            f"❌ Play {games_required_for_skill - games_played} more games to unlock skill!"
        )
        return False
    if not player_skill_available:
        Result.set("❌ Your skill in cooldown!")
        return False
    if not game_active:
        Result.set("❌ Start a tournament first!")
        return False
    if not user_choice:
        Result.set("❌ Please choose your move first!")
        return False

    player_skill_available = False
    player_last_skill_time = time.time()
    player_skill_status.set("🎮 Your Skill: COOLDOWN")
    root.after(1000, update_player_cooldown)
    return True


def use_computer_skill():
    global computer_skill_available, computer_last_skill_time, games_played

    if games_played < games_required_for_skill:
        return False
    if not computer_skill_available:
        return False
    if computer_score < player_score and random.random() < 0.3:
        computer_skill_available = False
        computer_last_skill_time = time.time()
        computer_skill_status.set("💻 Computer Skill: COOLDOWN")
        root.after(1000, update_computer_cooldown)
        return True
    return False


def update_player_cooldown():
    global player_skill_available, player_last_skill_time
    if not player_skill_available:
        current_time = time.time()
        elapsed = current_time - player_last_skill_time
        remaining = max(0, skill_cooldown - elapsed)
        if remaining <= 0:
            player_skill_available = True
            player_skill_status.set("🎮 Your Skill: READY")
        else:
            player_skill_status.set(f"🎮 Your Skill: {int(remaining)}s")
            root.after(1000, update_player_cooldown)


def update_computer_cooldown():
    global computer_skill_available, computer_last_skill_time
    if not computer_skill_available:
        current_time = time.time()
        elapsed = current_time - computer_last_skill_time
        remaining = max(0, skill_cooldown - elapsed)
        if remaining <= 0:
            computer_skill_available = True
            computer_skill_status.set("💻 Computer Skill: READY")
        else:
            computer_skill_status.set(f"💻 Computer Skill: {int(remaining)}s")
            root.after(1000, update_computer_cooldown)


def update_skill_unlock_status():
    """Update the skill unlock status display"""
    games_left = max(0, games_required_for_skill - games_played)

    if games_played >= games_required_for_skill:
        if player_skill_available:
            player_skill_status.set("🎮 Your Skill: READY")
        else:
            player_skill_status.set("🎮 Your Skill: COOLDOWN")

        if computer_skill_available:
            computer_skill_status.set("💻 Computer Skill: READY")
        else:
            computer_skill_status.set("💻 Computer Skill: COOLDOWN")
    else:
        player_skill_status.set(f"🎮 Your Skill: LOCKED ({games_left} games left)")
        computer_skill_status.set(
            f"💻 Computer Skill: LOCKED ({games_left} games left)"
        )


def start_tournament():
    global game_active, tournament_round, player_score, computer_score
    game_active = True
    tournament_round = 1
    player_score = 0
    computer_score = 0
    round_var.set(f"🏆 Round: 1/3")
    score_var.set(f"📊 Score: You {player_score} - {computer_score} Computer")


def check_tournament_winner():
    global \
        game_active, \
        player_coins, \
        current_bet, \
        tournament_round, \
        games_played, \
        player_skill_available, \
        computer_skill_available

    if player_score >= 2:
        win_amount = current_bet * 2
        player_coins += win_amount
        Result.set(f"🎉 YOU WIN TOURNAMENT! +{win_amount} coins! 🎉")
        games_played += 1
        game_active = False
        current_bet = 0
        update_displays()
        update_skill_unlock_status()

        if games_played >= games_required_for_skill:
            if not player_skill_available:
                player_skill_available = True
            if not computer_skill_available:
                computer_skill_available = True

    elif computer_score >= 2:
        Result.set(f"💻 COMPUTER WINS TOURNAMENT! Lost {current_bet} coins! 💻")
        games_played += 1
        game_active = False
        current_bet = 0
        update_displays()
        update_skill_unlock_status()

        if games_played >= games_required_for_skill:
            if not player_skill_available:
                player_skill_available = True
            if not computer_skill_available:
                computer_skill_available = True

    elif tournament_round < 3:
        tournament_round += 1
        round_var.set(f"🏆 Round: {tournament_round}/3")
        Result.set(f"🎮 Round {tournament_round} - Choose your move!")
    else:
        Result.set("❌ Tournament finished! Place new bet to play again.")
        games_played += 1
        game_active = False
        current_bet = 0
        update_displays()
        update_skill_unlock_status()

        if games_played >= games_required_for_skill:
            if not player_skill_available:
                player_skill_available = True
            if not computer_skill_available:
                computer_skill_available = True


def update_displays():
    coins_var.set(f"💰 Coins: {player_coins}")
    score_var.set(f"📊 Score: You {player_score} - {computer_score} Computer")
    bet_var.set(f"🎯 Current Bet: {current_bet}")


def play():
    global tournament_round, player_score, computer_score, game_active, user_choice
    if not game_active:
        Result.set("❌ Please place a bet to start tournament!")
        return
    if tournament_round > 3:
        Result.set("❌ Tournament finished! Place new bet to play again.")
        return
    if not user_choice:
        Result.set("❌ Please choose your move first!")
        return

    user_pick = user_choice
    comp_pick = random.choice(["rock", "paper", "scissors"])
    player_used_skill = use_player_skill()
    computer_used_skill = use_computer_skill()

    if player_used_skill and not computer_used_skill:
        round_result = f"🎯 Round {tournament_round}: YOU WIN! (Skill) {user_pick} beats {comp_pick}"
        player_score += 1
    elif computer_used_skill and not player_used_skill:
        round_result = f"🎯 Round {tournament_round}: COMPUTER WINS! (Skill) {comp_pick} beats {user_pick}"
        computer_score += 1
    elif player_used_skill and computer_used_skill:
        round_result = f"🎯 Round {tournament_round}: TIE! Both used skills"
    else:
        if user_pick == comp_pick:
            round_result = f"🎯 Round {tournament_round}: TIE! Both chose {user_pick}"
        elif (
            (user_pick == "rock" and comp_pick == "scissors")
            or (user_pick == "paper" and comp_pick == "rock")
            or (user_pick == "scissors" and comp_pick == "paper")
        ):
            round_result = (
                f"🎯 Round {tournament_round}: YOU WIN! {user_pick} beats {comp_pick}"
            )
            player_score += 1
        else:
            round_result = f"🎯 Round {tournament_round}: COMPUTER WINS! {comp_pick} beats {user_pick}"
            computer_score += 1

    Result.set(round_result)
    update_displays()
    user_choice = ""
    update_choice_display()
    root.after(2000, check_tournament_winner)


def play_with_skill():
    if not game_active:
        Result.set("❌ Please place a bet to start tournament!")
        return
    if not user_choice:
        Result.set("❌ Please choose your move first!")
        return
    if use_player_skill():
        play()


def Reset():
    global player_skill_available, computer_skill_available, player_coins, current_bet
    global tournament_round, player_score, computer_score, game_active, user_choice
    global games_played

    Result.set("🔄 Game reset! Place a new bet to start.")
    user_choice = ""

    # Reset skills based on games played
    if games_played >= games_required_for_skill:
        player_skill_available = True
        computer_skill_available = True
        player_skill_status.set("🎮 Your Skill: READY")
        computer_skill_status.set("💻 Computer Skill: READY")
    else:
        player_skill_available = False
        computer_skill_available = False
        update_skill_unlock_status()

    if game_active:
        player_coins += current_bet

    current_bet = 0
    tournament_round = 0
    player_score = 0
    computer_score = 0
    game_active = False

    update_displays()
    update_choice_display()
    round_var.set("🏆 Tournament: Not Started")
    score_var.set("📊 Score: You 0 - 0 Computer")


def Exit():
    root.destroy()


Button(
    action_frame,
    text="🎮 PLAY",
    font=("Arial", 12, "bold"),
    bg=SUCCESS_COLOR,
    fg=TEXT_COLOR,
    command=play,
    width=10,
    height=2,
    relief=RAISED,
    bd=3,
).pack(side=LEFT, padx=5)

Button(
    action_frame,
    text="⚡ USE SKILL",
    font=("Arial", 12, "bold"),
    bg=WARNING_COLOR,
    fg=TEXT_COLOR,
    command=play_with_skill,
    width=12,
    height=2,
    relief=RAISED,
    bd=3,
).pack(side=LEFT, padx=5)

Button(
    action_frame,
    text="🔄 RESET",
    font=("Arial", 12, "bold"),
    bg=PRIMARY_COLOR,
    fg=TEXT_COLOR,
    command=Reset,
    width=10,
    height=2,
    relief=RAISED,
    bd=3,
).pack(side=LEFT, padx=5)

Button(
    action_frame,
    text="🚪 EXIT",
    font=("Arial", 12, "bold"),
    bg=DANGER_COLOR,
    fg=TEXT_COLOR,
    command=Exit,
    width=8,
    height=2,
    relief=RAISED,
    bd=3,
).pack(side=LEFT, padx=5)

root.mainloop()
