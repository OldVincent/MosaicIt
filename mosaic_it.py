import os
import sys
from typing import Annotated
import cv2
import typer


def make_mosaic(image, intensity: int = 10):
    width = image.shape[1]
    height = image.shape[0]
    mosaic = cv2.resize(image, (width // intensity, height // intensity), interpolation=cv2.INTER_LINEAR)
    mosaic = cv2.resize(mosaic, (width, height), interpolation=cv2.INTER_NEAREST)
    return mosaic


def mosaic_it(input_path: Annotated[str, typer.Argument(help="Path to the input image to add mosaic.")],
              output_path: Annotated[str, typer.Option(help="Path to the output image with mosaic.")] = None,
              intensity: Annotated[int, typer.Option(help="Intensity of the mosaic effect.")] = 10) -> None:
    if output_path is None:
        file_base, file_extension = os.path.splitext(input_path)
        output_path = file_base + "_mosaic" + file_extension
    print(f"Input Image: {input_path}, Output Image: {output_path}, Intensity: {intensity}")

    target_image: cv2.Mat = cv2.imread(input_path)
    if target_image is None:
        print(f"Error: Could not read image file {input_path}")
        sys.exit(1)

    while True:
        region = cv2.selectROI("Select Region to Add Mosaic", target_image,
                               fromCenter=False, showCrosshair=False)
        if region.count(0) == 4:
            break
        print(f"Selected region: {region}")
        region_x, region_y, region_w, region_h = region
        target_image[region_y : region_y + region_h, region_x : region_x + region_w] = make_mosaic(
            target_image[region_y : region_y + region_h, region_x : region_x + region_w], intensity=intensity)
        
    cv2.imwrite(output_path, target_image)
    print(f"Mosaic Image Saved: {output_path}")


app = typer.Typer(help="Add mosaic to an image.")
app.command()(mosaic_it)

if __name__ == "__main__":
    app()
