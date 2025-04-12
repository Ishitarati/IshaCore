import os
import sys
import importlib

# Map of module keys and their display names
MODULES = {
    "calendar": "Calendar",
    "hormone": "Hormone Tracker",
    "innerwear": "Innerwear Selector",
    "sex_planner": "Sex Planner",
    "toy_tracker": "Toy Tracker",
    "ritual_planner": "Ritual Planner",
    "fetish_tracker": "Fetish Tracker",
    "client_manager": "Client Manager",
    "voice_training": "Voice Training",
    "milf_transformation": "MILF Transformation",
    "mirror_check": "Mirror Check",
    "mood_control": "Mood Control",
    "orgasm_control": "Orgasm Control",
    "outfit_coordinator": "Outfit Coordinator",
    "payments": "Payments Tracker",
    "personality_dev": "Personality Development",
    "play_dates": "Play Dates Planner",
    "pose_tracker": "Pose & Posture Tracker",
    "post_op": "Post-op Recovery",
    "pre_op": "Pre-op Tracking",
    "roleplay": "Roleplay Scenarios",
    "sex_routine": "Sex Routine Planner",
    "sex_tasks": "Sexual Task Tracker",
    "sissy_tasks": "Sissy Training Tasks",
    "therapy": "Sex Therapy Tracker",
    "research": "Sexual Research",
    "spirit_connection": "Spirit Connection",
    "submissive_training": "Submissive Training",
    "suggestion": "Suggestion Module",
    "transformation_goals": "Transformation Goals",
    "session_logger": "Sex Session Logger",
    "escort_manager": "Escort Service Manager",
    "fantasy_kink": "Fantasy & Kink Tracker",
    "fertility": "Fertility & Repro Health",
    "fetish_therapy": "Fetish Therapy",
    "health": "Health Tracker",
    "cum_planner": "Cum Planner",
    "bimbo_tasks": "Bimbofication Tasks",
    "bedroom_tips": "Bedroom Tips",
    "maintenance": "General Maintenance",
    "masturbation": "Masturbation Tracker",
    "milf_content": "MILF Strategy & Routine",
    "kink_planner": "Kink Planning",
    "lingerie_selector": "Lingerie Selector",
    "mirror": "Mirror Module",
    "pose": "Pose Module",
    "trigger": "Trigger Tracker",
    "fantasy": "Fantasy Planner",
    "fetish": "Fetish Logger",
    "dominant_tracking": "Dom/Sub Tracker",
    "cross_platform_sync": "Cross-Platform Sync",
    "ai_botnet": "AI Botnet Manager",
    "room_setup": "Room Setup & Style",
    "calendar_sync": "Calendar Sync",
    "vocal_analysis": "Vocal Feminization Analysis",
    "cum_log": "Cum Log Tracker",
    "session_planner": "Session Planner",
    "mood_tracker": "Mood & Mental State Tracker",
    "anal_play": "Anal Play Tracker",
    "healthcare": "Healthcare Records",
    "outfit_planner": "Outfit Planner",
    "voice_log": "Voice Training Log",
    "vibe_routines": "Vibe & Toy Routines",
    "pose_training": "Pose Training",
    "schedule": "Full Routine Scheduler",
    "sissy_calendar": "Sissy Calendar",
    "hormone_dose": "Advanced Hormone Dosing",
    "ml_routines": "Machine-Learning-Based Suggestions",
}

def show_menu():
    print("\n✨ Welcome to Ishacore CLI Empire ✨")
    print("Choose a module to launch:\n")

    for idx, (key, name) in enumerate(MODULES.items(), start=1):
        print(f"{idx}. {name}")

    print(f"{len(MODULES) + 1}. Quit")

    choice = input("\nEnter your choice (1-{}): ".format(len(MODULES) + 1))

    try:
        choice = int(choice)
        if 1 <= choice <= len(MODULES):
            module_key = list(MODULES.keys())[choice - 1]
            run_module(module_key)
        elif choice == len(MODULES) + 1:
            print("Exiting ishacore. 💋")
            sys.exit()
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a number.")

def run_module(module_name):
    try:
        module = importlib.import_module(f"modules.{module_name}")
        module.run()
    except ModuleNotFoundError:
        print(f"❌ Module '{module_name}' not found in /modules.")
    except AttributeError:
        print(f"❌ Module '{module_name}' does not have a 'run()' function.")
    except Exception as e:
        print(f"⚠️ Error running module '{module_name}': {e}")

if __name__ == "__main__":
    while True:
        show_menu()
