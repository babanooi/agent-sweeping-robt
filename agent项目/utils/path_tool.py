import os


#获取工程所在的根目录
def get_project_root():
  # 1. 当前文件的路径：utils/path_tool.py
  current_file = os.path.abspath(__file__)
  # 2. 往上走两级：utils/path_tool.py → utils → agent项目
  project_root = os.path.dirname(os.path.dirname(current_file))
  return project_root
#传递相对路径，获取绝对路径
def get_abs_path(relative_path:str):
  project_root = get_project_root()
  return os.path.join(project_root,relative_path )