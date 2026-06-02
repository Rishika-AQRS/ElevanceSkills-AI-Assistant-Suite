import schedule
import time
import subprocess
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPDATE_SCRIPT=os.path.join(BASE_DIR, "update_knowledge.py")


def run_updater():
    print("\nRunning Knowledge Update...")

    try:
        result=subprocess.run(
            ["python", UPDATE_SCRIPT],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.returncode==0:
            print("Update Finished Successfully!")
        else:
            print("Update Failed!")
            print(result.stderr)

    except Exception as e:
        print(f"Error: {e}")


# Run every 2 minutes
schedule.every(2).minutes.do(run_updater)

print("Scheduler Started! Press Ctrl+C to Stop.")
print("This will run update_knowledge.py every 2 minutes.\n")

# Run once immediately when scheduler starts
run_updater()

while True:
    schedule.run_pending()
    time.sleep(10)