import sys
import os

# Ajouter le répertoire 'resume_automation' au chemin Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'resume_automation')))
# ajouter src/resources/base_prompt.txt 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'resume_automation/src/resources/base_prompt.txt')))
## ajouter C:\Users\LENOVO\Desktop\project_job\resume_automation\config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'resume_automation/config')))
from resume_automation.main import main
main()