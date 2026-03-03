import traceback
import sys
import os

# Add local directory to path
sys.path.append(os.getcwd())

try:
    print("Attempting to import feature.py...")
    from feature import FeatureExtraction
    print("Import successful. Attempting to instantiate FeatureExtraction...")
    # Use a dummy URL to trigger the logic
    obj = FeatureExtraction("http://google.com")
    print("Features extracted successfully")
    print(obj.getFeaturesList())
except Exception:
    print("Crashed as expected:")
    traceback.print_exc()
