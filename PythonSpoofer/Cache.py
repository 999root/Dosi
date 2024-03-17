import os
import shutil

def clear_ubisoft_cache():
    app_data_path = os.path.join(os.environ["LOCALAPPDATA"], "Ubisoft Game Launcher")
    ubisoft_path = os.path.join(app_data_path, "cache")
    ubisoft_logs_path = os.path.join(app_data_path, "logs")
    ubisoft_savegames_path = os.path.join(app_data_path, "savegames")
    ubisoft_spool_path = os.path.join(app_data_path, "spool")

    for path in [ubisoft_path, ubisoft_logs_path, ubisoft_savegames_path, ubisoft_spool_path]:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print("Successfully cleared:", path)
            except Exception as e:
                print("Error while clearing", path, ":", e)

def clear_valorant_cache():
    valorant_path = os.path.join(os.environ["LOCALAPPDATA"], "VALORANT", "saved")
    
    if os.path.exists(valorant_path):
        try:
            shutil.rmtree(valorant_path)
            print("Successfully cleared Valorant cache")
        except Exception as e:
            print("Error while clearing Valorant cache:", e)
    else:
        print("Valorant cache directory not found")
