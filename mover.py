import shutil
import os 
if os.path.exists('N:\python project\my words.txt'):
  src_path = r"N:\Documents\python project\mywords.txt"
  dst_path = r"N:\Documents\mywords.txt"
  shutil.move(src_path, dst_path)
