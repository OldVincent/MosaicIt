# Mosaic It
A UI utility to add mosaic to a picture with OpenCV.

## Installation

### Prepare Pipx

[Pipx](https://github.com/pypa/pipx) allows users to install and run Python applications easily.
Please follow this [tutorial](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx) to install it.

Or using following scripts to install it:

**On Linux (using APT):**
```shell
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```
**On Windows (using PIP):**
```shell
py -m pip install --user pipx
```
If there is a warning looks like this:
```
ARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
```
If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line 
(even if you did not get the warning):
```shell
.\pipx.exe ensurepath
```

### Install *mosaic-it*
Install *mosaic-it* from this Git repository using the following command: 
```shell
pipx install git+https://github.com/OldVincent/MosaicIt.git
```

### Uninstall *mosaic-it*

Using the following command to uninstall *mosaic-it*:
```shell
pipx uninstall mosaic-it
```

## How It Works

This tool first reduces the selected area (using linear interpolation)
and then enlarges it to its original size (using nearest interpolation).

## Usage

```shell
mosaic-it <INPUT_IMAGE_PATH> [-i <MOSAIC_INTENSITY>] [-o <OUTPUT_IMAGE_PATH>]
```

Use `mosaic-it --help` to see more commands.

### Parameter Default Value

- **Mosaic Intensity:** 10
- **Output Image Path:** In the same directory as the input image, but with a "_mosaic" as a postfix in the name.

### Preview

![Preview](preview.png)

This picture is processed with *mosaic-it*.