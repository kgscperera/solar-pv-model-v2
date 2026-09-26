"""
What does this script do?

    1. creates 02 directories
        1. lib  - dependencies will be installed here
        2. data - "TIF" files, fetched "JSON" files and exported "CSV" files
        
    2. move "TIF" files to data folder created in earlier step
    
    3. install dependencies
        1. requests
        2. urllib3
        3. pandas
        4. numpy
        5. scipy
        6. matplotlib
        7. statsmodels
        8. rasterio

    4. launches Jupyter Lab in current folder

"""

import glob
import os
import shutil
import subprocess
import sys

def main():
    # Create folders
    os.makedirs("data", exist_ok=True)
    print("Created folder: data")

    os.makedirs("lib", exist_ok=True)
    print("Created folder: lib")

    # Move all .tif files into data folder
    tif_files = glob.glob("*.tif")
    if tif_files:
        for tif in tif_files:
            shutil.move(tif, os.path.join("data", os.path.basename(tif)))
            print(f"{tif} file moved to data folder.")
    else:
        print("Warning: no .tif files found, skipping move.")

    print("Requirements: requests, urllib3, pandas, numpy, scipy, matplotlib, statsmodels, rasterio")
    print("Installing required packages...")

    # Install dependencies
    packages = ["requests", "urllib3", "pandas", "numpy", "scipy", "matplotlib", "statsmodels", "rasterio"]
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", *packages, "--target", "./lib"]
    )
    if result.returncode != 0:
        print("Package installation failed.")
        sys.exit(1)

    print()
    print("Installation completed successfully.")
#    input("Press Enter to launch Jupyter Lab...")

    print("Jupyter Lab is launching...")
    # Launch Jupyter Lab without blocking this script
    subprocess.Popen([sys.executable, "-m", "jupyter", "lab"])


if __name__ == "__main__":
    main()