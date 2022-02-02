import shutil
import os 
if os.path.exists('N:\Documents\python project\mywords.txt'):
  src_path = r"N:\Documents\python project\mywords.txt"
  dst_path = r"N:\Documents\mywords.txt"
  shutil.move(src_path, dst_path)
