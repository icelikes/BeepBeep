from configuration.base import *

# =========================================================================
# ============================== WARNING! =================================
# =========================================================================
# Do not change this file to make configuration changes. This is a base
# config file used for the other config files. Copy configsetting.example.py
# to configsetting.py and make your changes there.

# =========================================================================
# ========================== General Settings =============================
# =========================================================================
DEVICE_TYPE = "interlock"  # "door", "interlock" or "memberbucks"
LOCK_REVERSED = False
RELAY_REVERSED = False
IN_1_REVERSED = True
FIXED_UNLOCK_DELAY = 7  # seconds to remain unlocked
INTERLOCK_TIMEOUT_CURRENT = .5
INTERLOCK_TIMEOUT_TIME = 30 # in Seconds

# =========================================================================
# ====================== Remote Interlock Settings ========================
# =========================================================================
TASMOTA_HOST = "192.168.2.61"  # set to None or the IP of the TASMOTA switching device to enable remote control
TASMOTA_USER = "admin"
TASMOTA_PASSWORD = "admin"
