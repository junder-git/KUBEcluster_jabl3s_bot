import importlib
import os
from decouple import config

# Read environment variables from the .env file
BOT_TWITCH_TOKEN = config('BOT_TWITCH_TOKEN')
bot={}
def main():
    # Specify the folder containing your modules
    module_folder = "sub-code"
    # Get a list of all Python files in the subfolder (excluding __init__.py)
    module_files = [
        f.replace(".py", "")
        for f in os.listdir(module_folder)
        if f.endswith(".py") and not f.startswith("__init__")
    ]
    # Dynamically import the modules
    for module_name in module_files:
        bot[module_name] = importlib.import_module(f"{module_folder}.{module_name}")
        
    getattr(bot["BotTwitch"],"BotTwitch")(BOT_TWITCH_TOKEN,['jabl3s_ttv']).run()

if __name__ == "__main__":
    main()
