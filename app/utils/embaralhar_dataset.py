import os
import random
import shutil

images_dir = 'images'
labels_dir = 'labels'
train_dir = 'training'
val_dir = 'validation'
test_dir = 'test'

def create_dirs():
    for d in [train_dir, val_dir, test_dir]:
        os.makedirs(os.path.join(d, 'images'), exist_ok=True)
        os.makedirs(os.path.join(d, 'labels'), exist_ok=True)

def move_files(file_list, dest_dir):
    for file_name in file_list:
        image_path = os.path.join(images_dir, file_name)
        label_name = file_name.replace('.jpg', '.txt')
        label_path = os.path.join(labels_dir, label_name)
        
        if os.path.exists(label_path):
            shutil.move(image_path, os.path.join(dest_dir, 'images', file_name))
            shutil.move(label_path, os.path.join(dest_dir, 'labels', label_name))

def split_data():
    images = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
    random.shuffle(images)
    
    total_images = len(images)
    train_count = int(total_images * 0.8)
    val_count = int(total_images * 0.1)
    test_count = total_images - train_count - val_count
    
    train_files = images[:train_count]
    val_files = images[train_count:train_count + val_count]
    test_files = images[train_count + val_count:]
    
    move_files(train_files, train_dir)
    move_files(val_files, val_dir)
    move_files(test_files, test_dir)

create_dirs()
split_data()

print("Divisão de dados concluída com sucesso!")
