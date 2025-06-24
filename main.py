from tts_robotic import speak
from stt_whisper import transcribe
from gemini_brain import chat_with_gemini
from memory import save_memory, recall_memory

import schedule
import time
import threading
import re

print("\n🎙️ WELCOME TO FRIDAY – Your AI Assistant")
print("🎛️ Select Mode:")
print("1. Voice Mode 🎤")
print("2. Text Mode ⌨️")

mode = ""
while mode not in ["1", "2"]:
    mode = input("Enter 1 or 2: ").strip()

print(f"✅ Mode set to {'Voice' if mode == '1' else 'Text'} Mode.")
print("Say or type 'stop' anytime to exit.\n")

# === Reminder system ===
def set_reminder(fact, minutes):
    def job():
        print(f"\n⏰ Reminder: {fact}")
        speak(f"Reminder: {fact}")

    schedule.every(minutes).minutes.do(job)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_schedule, daemon=True).start()

while True:
    # Get input
    if mode == "1":
        user_input = transcribe()
        print("🗣️ You said:", user_input)

        if user_input.strip() == "":
            print("🤖 Friday: I didn’t catch that. Try again, SIR.")
            speak("🤖 Friday: I didn’t catch that. Try again, SIR.")
            continue
    else:
        user_input = input("⌨️ You: ").strip()

        if user_input == "":
            print("🤖 Friday: Still nothing. Try again.")
            speak("🤖 Friday: Still nothing. Try again.")
            continue

    # Exit check
    if any(kw in user_input.lower() for kw in ["stop", "quit", "exit", "bye"]):
        print("🧠 Friday: Shutting down. Goodbye, SIR!")
        speak("🧠 Friday: Shutting down. Goodbye, SIR!")
        break

    # Identity check
    if any(user_input.lower().startswith(p) for p in ["who am i", "who is your boss", "who is god"]):
        identity = "Rohith , and I AM Friday, your assistant SIR!"
        print(identity)
        speak(identity)
        continue

    # Mode switch
    if "switch to voice" in user_input.lower():
        mode = "1"
        print("🔄 Switched to Voice Mode.")
        speak("🔄 Switched to Voice Mode.")
        continue
    elif "switch to text" in user_input.lower():
        mode = "2"
        print("🔄 Switched to Text Mode.")
        continue

    # Set timed reminder
    match = re.search(r"remind me about (.+?) in (\d+) minutes", user_input.lower())
    if match:
        fact, mins = match.group(1).strip(), int(match.group(2))
        save_memory(f"{fact} (in {mins} minutes)")
        print(f"🧠 Friday: Got it! I’ll remind you about '{fact}' in {mins} minutes.")
        speak(f"I’ll remind you about {fact} in {mins} minutes.")
        set_reminder(fact, mins)
        continue

    # Save memory
    if any(user_input.lower().startswith(p) for p in ["remember that", "remind me to", "remind me about"]):
        fact = user_input.replace("remember that", "", 1).replace("remind me to", "", 1).replace("remind me about", "", 1).strip()
        save_memory(fact)
        print("🧠 Friday: Got it! I’ll remember that.")
        speak("🧠 Friday: Got it! I’ll remember that.")
        continue

    # Recall memory
    if any(q in user_input.lower() for q in ["what do you remember", "what did i ask"]):
        facts = recall_memory()
        if facts:
            print("🧠 Friday: Here's what I remember:")
            speak("🧠 Friday: Here's what I remember:")
            for f in facts:
                print("-", f)
                speak(f)
        else:
            print("🧠 Friday: I don’t remember anything yet.")
            speak("🧠 Friday: I don’t remember anything yet.")
        continue

    # Chat mode
    response = chat_with_gemini(user_input)
    print("🤖 Friday:", response)

    if mode == "1":
        speak(response)
