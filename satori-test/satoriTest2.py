import git
import os
from pathlib import Path

#clone via ssh
git.Repo.clone_from('git@github.com:satorici/satori-cli.git', 'satori-cli-copy')




directory_elements = os.listdir('satori-cli-copy') and os.listdir('satori-cli-copy/playbooks')
List_of_Subdirectories = []
for element in directory_elements:
    if element.endswith('.yml'):
        List_of_Subdirectories.append(element)
print(List_of_Subdirectories)

