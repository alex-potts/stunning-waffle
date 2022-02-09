import shutil
import os 
p = os.getcwds()
if os.path.exists(p + '\python project\mywords.txt'):
  src_path = p + "\python project\mywords.txt"
  dst_path = p+ "\mywords.txt"
  shutil.move(src_path, dst_path)
