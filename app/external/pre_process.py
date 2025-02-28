import os
import cv2
import glob
import numpy as np
from albumentations import (
    Compose, OneOf, RandomCrop, Resize, HorizontalFlip, VerticalFlip,
    RandomBrightnessContrast, ShiftScaleRotate, Blur, GaussianBlur, CLAHE
)

def get_transforms():
    return Compose([
        Resize(height=256, width=256),

        RandomCrop(height=224, width=224),

        OneOf([
            HorizontalFlip(p=0.5),
            VerticalFlip(p=0.5),
        ], p=0.5),

        ShiftScaleRotate(
            shift_limit=0.05, 
            scale_limit=0.1,  
            rotate_limit=30,  
            p=0.7
        ),

        RandomBrightnessContrast(
            brightness_limit=0.2,  
            contrast_limit=0.2,
            p=0.5
        ),

        OneOf([
            Blur(blur_limit=3, p=0.5),
            GaussianBlur(blur_limit=3, p=0.5),
            CLAHE(clip_limit=2.0, p=0.5)
        ], p=0.3)
    ])

def main():
    input_dir = "dataset/train"
    output_dir = "dataset/augmented"

    os.makedirs(output_dir, exist_ok=True)

    image_paths = glob.glob(os.path.join(input_dir, "*.jpg"))

    num_augmentations = 5

    transform = get_transforms()

    for img_path in image_paths:
        image = cv2.imread(img_path)
        img_name = os.path.splitext(os.path.basename(img_path))[0]

        for i in range(num_augmentations):
            augmented = transform(image=image)
            aug_image = augmented["image"]

            aug_filename = f"{img_name}_aug_{i}.jpg"
            aug_filepath = os.path.join(output_dir, aug_filename)

            cv2.imwrite(aug_filepath, aug_image)

        print(f"Geradas {num_augmentations} imagens a partir de {img_path}")

if __name__ == "__main__":
    main()
