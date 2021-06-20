# 1. Написать скрипт, создающий стартер (заготовку) для проекта

import os

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for home, folders in starter.items():
    for folder in folders:
        current_dir = os.path.join(home, folder)
        os.makedirs(current_dir)
