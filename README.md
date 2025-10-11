# Android BOOT & VBMETA Patcher

## ⚠️ Disclaimer

**This project is for educational purposes ONLY.**

Modifying your device's boot images carries significant risks, including but not limited to, bricking your device, data loss, or voiding your warranty. The author **assumes no liability** and is not responsible for any **damage or consequence** that may occur to **your device or anyone else's device** from using these scripts.

**You are solely responsible for any consequences. Use at your own absolute risk.**

This set of scripts automates three main tasks:
1.  Converting the region code for `vendor_boot.img` and remaking the corresponding `vbmeta.img`.
2.  Enabling root by replacing the kernel in `boot.img` with [patched one](https://github.com/WildKernels/GKI_KernelSU_SUSFS).
3.  Modifying `devinfo.img` and `persist.img` by replacing specific byte patterns to allow resetting region code.

## Prerequisites

Before you begin, place the required files from your device's stock firmware into the main directory:

* For `vendor_boot`/`vbmeta` patch: `vendor_boot.img` and `vbmeta.img`.
* For rooting: `boot.img`.
* For `devinfo`/`persist` modification: `devinfo.img` and `persist.img`.

## How to Use

1.  **Place Images:** Put the necessary `.img` files into the root folder according to the task you want to perform.
2.  **Run the Script:** Simply run the batch file corresponding to the task you want to perform. All required tools will be downloaded automatically.
    * **`vndrboot_vbmeta.bat`**: Converts `vendor_boot` and remakes `vbmeta`. Results are saved in the `output` folder.
    * **`root.bat`**: Enables root on `boot.img`. The result is saved in the `output_root` folder.
    * **`devinfo_persist.bat`**: Modifies `devinfo.img` and `persist.img`. Results are saved in the `output_dp` folder.
3.  **Flash the Images:** After a script finishes, flash the new `.img` file(s) from the appropriate output folder to your device using `fastboot`.

## Script Descriptions

### Main Scripts (in the root folder)

* **`vndrboot_vbmeta.bat`**: Handles the `vendor_boot` region code conversion and remakes `vbmeta.img`.
* **`devinfo_persist.bat`**: Modifies `devinfo.img` and `persist.img`.
* **`root.bat`**: Enables root by replacing the kernel in `boot.img`.
* **`info_image.bat`**: Drag & drop `.img` file(s) or folder(s) onto this script to see AVB information.

### Tool Scripts (in the `tools` folder)

* **`install.bat`**: Automatically downloads and sets up all necessary tools (Python, avbtool, etc.). This script is called by the main scripts and does not need to be run manually.