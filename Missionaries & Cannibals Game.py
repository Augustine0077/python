import os

# Clear console function
try:
    from IPython.display import clear_output as clear_console
except Exception:
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

# Emojis
M_EMOJI = "\U0001f482"
C_EMOJI = "\U0001f479"
BOAT_EMOJI = "\U0001f6A2"
WAVE_EMOJI = "\U0001f30a"

def display(m_l, c_l, m_r, c_r, boat_side):
    line = ""
    # Left side
    line += M_EMOJI * m_l + C_EMOJI * c_l
    if boat_side == "Left":
        line += "|" + WAVE_EMOJI*5 + BOAT_EMOJI + "|"
    else:
        line += "|" + WAVE_EMOJI*5 + "|"
    # Right side
    if boat_side == "Right":
        line += BOAT_EMOJI
    line += M_EMOJI * m_r + C_EMOJI * c_r
    print(line)

# Initial state
boat_side = "Right"
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

while True:
    display(missionaries_on_left, cannibals_on_left,
            missionaries_on_right, cannibals_on_right, boat_side)
    
    # Check WIN
    if missionaries_on_left == 3 and cannibals_on_left == 3:
        print("YOU WIN 🎉")
        break
    
    # Check LOSE
    if (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0) \
       or (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0):
        print("YOU LOSE 💀")
        break

    # Get user input
    try:
        missionaries = int(input("Missionaries to move (0-2): "))
        cannibals = int(input("Cannibals to move (0-2): "))
    except ValueError:
        print("Enter valid numbers!")
        continue

    if missionaries + cannibals not in [1, 2]:
        print("Boat can carry 1 or 2 people only.")
        continue

    # Move logic
    if boat_side == "Right":
        if missionaries > missionaries_on_right or cannibals > cannibals_on_right:
            print("Not enough people on right side.")
            continue
        m_r_new = missionaries_on_right - missionaries
        c_r_new = cannibals_on_right - cannibals
        m_l_new = missionaries_on_left + missionaries
        c_l_new = cannibals_on_left + cannibals
        # Safety check
        if (m_r_new < c_r_new and m_r_new > 0) or (m_l_new < c_l_new and m_l_new > 0):
            print("Cannibals would eat missionaries!")
            continue
        # Apply move
        missionaries_on_right = m_r_new
        cannibals_on_right = c_r_new
        missionaries_on_left = m_l_new
        cannibals_on_left = c_l_new
        boat_side = "Left"
    else:  # boat on Left
        if missionaries > missionaries_on_left or cannibals > cannibals_on_left:
            print("Not enough people on left side.")
            continue
        m_r_new = missionaries_on_right + missionaries
        c_r_new = cannibals_on_right + cannibals
        m_l_new = missionaries_on_left - missionaries
        c_l_new = cannibals_on_left - cannibals
        # Safety check
        if (m_r_new < c_r_new and m_r_new > 0) or (m_l_new < c_l_new and m_l_new > 0):
            print("Cannibals would eat missionaries!")
            continue
        # Apply move
        missionaries_on_right = m_r_new
        cannibals_on_right = c_r_new
        missionaries_on_left = m_l_new
        cannibals_on_left = c_l_new
        boat_side = "Right"

    clear_console()

print("Game Over")
