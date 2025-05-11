
import time
import random

battery_level = 100
first_time_run = True

def scan_and_map():
    print("[Mapping] Scanning and saving map... Done.")

def navigate_to(item):
    print(f"[Navigation] Moving towards {item}...")

def pick_item(item):
    print(f"[Action] Picking up {item}...")

def return_to_bin():
    print("[Navigation] Returning to garbage bin...")

def battery_check():
    global battery_level
    battery_level -= random.randint(1, 5)
    if battery_level <= 20:
        print("[Battery] Low battery! Returning to charging dock.")
        return True
    return False

def main():
    global first_time_run
    if first_time_run:
        scan_and_map()
        first_time_run = False

    while True:
        if battery_check():
            break
        detected_object = random.choice(["trash", "personal", "dangerous", "none"])
        print(f"[Vision] Detected object: {detected_object}")
        time.sleep(1)
        
        if detected_object == "trash":
            navigate_to("trash")
            pick_item("trash")
            return_to_bin()
        elif detected_object == "personal":
            print("[Interaction] Asking human for permission...")
            time.sleep(5)
            human_response = random.choice(["yes", "no", "thumbs up"])
            print(f"[Human] Response: {human_response}")
            if human_response in ["yes", "thumbs up"]:
                print("[Action] Leaving the personal item.")
            else:
                pick_item("personal item")
                return_to_bin()
        elif detected_object == "dangerous":
            print("[Safety] Dangerous item spotted. Not picking up!")
        else:
            print("[Status] No object detected.")
        time.sleep(2)

if __name__ == "__main__":
    main()
