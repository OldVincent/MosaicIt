# Mosaic It
A command line utility to add mosaic to a picture with OpenCV.

## Installation

### Install *mosaic-it*

Use the following command to install *mosaic-it* from PyPI:
```shell
pip install mosaic-it
```

### Uninstall *mosaic-it*

Using the following command to uninstall *mosaic-it*:
```shell
pip uninstall mosaic-it
```

## How It Works

This tool first reduces the selected area (using linear interpolation)
and then enlarges it to its original size (using nearest interpolation).

## Usage

```shell
mosaic-it <INPUT_IMAGE_PATH> [-i <MOSAIC_INTENSITY>] [-o <OUTPUT_IMAGE_PATH>]
```

Use `mosaic-it --help` to see more commands.

In the region selection window, select a region and then press `enter` or `space` to apply the mosaic effect;
then you can select other regions to apply the mosaic effect without closing this window.
Press `enter` or `space` without select any region to stop this procedure and save the processed image.

### Parameter Default Value

- **Mosaic Intensity:** 10
- **Output Image Path:** In the same directory as the input image, but with a "_mosaic" as a postfix in the name.

### Preview

![Preview](preview.png)

This picture is processed with *mosaic-it*.