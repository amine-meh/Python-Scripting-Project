import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_FILE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]


def find_all_game_paths(source):
  game_paths = []
  for root, dirs, files in os.walk(source):
    for directory in dirs:
      if GAME_DIR_PATTERN in directory.lower():
        path = os.path.join(source, directory)
        game_paths.append(path)
    break
  return game_paths

def create_dir(path):
  if not os.path.exists(path):
    os.mkdir(path)

def copy_and_overwrite(sources, dest):
  if os.path.exists(dest):
    shutil.rmtree(dest, ignore_errors=True)
  shutil.copytree(sources, dest)

def make_json_metadata_file(path, game_dirs):
  data = {
    "Game Names": game_dirs,
    "Number of Games": len(game_dirs)
  }
  with open(path, 'w') as f:
    json.dump(data, f)

def get_name_from_path(paths, to_strip):
  new_names = []
  for path in paths:
    _, dir_name = os.path.split(path)
    new_name = dir_name.replace(to_strip, "")
    new_names.append(new_name)

  return new_names

def compile_game_code(path):
  code_file_name = None
  for roots, dirs, files in os.walk(path):
    for file in files:
      if file.endswith(GAME_FILE_EXTENSION):
        code_file_name = file
        break
    break
  
  if code_file_name is None:
    return
  
  command = GAME_COMPILE_COMMAND + [code_file_name]
  run_command(command, path)

def run_command(command, path):
  cwd = os.getcwd()
  os.chdir(path)

  result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
  print("compile result", result)

  os.chdir(cwd)

def main(source, target):
  cwd = os.getcwd()
  source_path = os.path.join(cwd, source)
  target_path = os.path.join(cwd, target)

  game_paths = find_all_game_paths(source_path)
  
  new_dir_names = get_name_from_path(game_paths, "_game")


  create_dir(target_path)

  for src, dest in zip(game_paths, new_dir_names):
    dest_path = os.path.join(target_path, dest)
    copy_and_overwrite(src, dest_path)
    compile_game_code(dest_path)

  json_path = os.path.join(target_path, "metadata.json")
  make_json_metadata_file(json_path, new_dir_names)

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 3:
    raise Exception("You must pass source and target directory only!")
  
  source, target = args[1:]
  main(source, target)