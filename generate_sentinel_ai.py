import os
import json

# Define base directory
base_path = os.path.join(os.getcwd(), "SentinelAI")

# Define the full structure
project_structure = {
    "level1_ai_foundations": ["project1_chatbot_basics", "project2_clippy_coder"],
    "level2_voice_ui": ["project3_voice_enabled_chatbot", "project4_tkinter_gui_assistant"],
    "level3_simulators": ["project5_banking_maze", "project6_refund_support_traps"],
    "level4_cloud_logging": ["project7_docker_cloud_bot", "project8_logging_auto_reports"],
    "level5_full_system": ["project9_persona_optimizer_nn", "project10_scam_hunter_ai_node"],
    "level6_operational_modules": [
        "scam_type_classifier", "voiceprint_detector",
        "adaptive_maze_generator", "scam_profile_generator", "ai_field_commander"
    ]
}

# Create project folders
for level, projects in project_structure.items():
    level_path = os.path.join(base_path, level)
    os.makedirs(level_path, exist_ok=True)
    for proj in projects:
        proj_path = os.path.join(level_path, proj)
        os.makedirs(proj_path, exist_ok=True)
        with open(os.path.join(proj_path, "main.py"), "w") as f:
            f.write("# Entry point for this project\n")
        with open(os.path.join(proj_path, "README.md"), "w") as f:
            f.write(f"# {proj.replace('_', ' ').title()}\n\n## Overview\n\n## How to Run\n\n")

# Create .vscode settings
vscode_path = os.path.join(base_path, ".vscode")
os.makedirs(vscode_path, exist_ok=True)
with open(os.path.join(vscode_path, "settings.json"), "w") as f:
    json.dump({
        "python.pythonPath": "${workspaceFolder}/venv/bin/python",
        "python.formatting.provider": "black",
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": True,
        "python.linting.pylintArgs": ["--errors-only"]
    }, f, indent=4)

# Create root files
with open(os.path.join(base_path, "README.md"), "w") as f:
    f.write("# Sentinel.AI\n\n"
            "An AI-powered anti-scam system to confuse scammers and report confirmed IPs using voice traps, "
            "neural logic, and automated reporting.\n\n"
            "## Setup Instructions\n"
            "- Run `setup_env.sh` (Mac/Linux) or `setup_env.bat` (Windows) to install dependencies\n")

with open(os.path.join(base_path, "requirements.txt"), "w") as f:
    f.write("openai\nspeechrecognition\npyttsx3\ntkinter\nflask\ndocker\npytorch\nscikit-learn")

with open(os.path.join(base_path, ".gitignore"), "w") as f:
    f.write("*.pyc\n__pycache__/\n.env\nvenv/\n.DS_Store\n")

with open(os.path.join(base_path, "setup_env.sh"), "w") as f:
    f.write("#!/bin/bash\npython3 -m venv venv\nsource venv/bin/activate\n"
            "pip install --upgrade pip\npip install -r requirements.txt\n")

with open(os.path.join(base_path, "setup_env.bat"), "w") as f:
    f.write("python -m venv venv\nvenv\\Scripts\\activate\n"
            "pip install --upgrade pip\npip install -r requirements.txt\n")

print("✅ Sentinel.AI project folder created at:", base_path)
