
from lzl.src.DB_helper import DB_helper
from lzl.src.Data_giver import Data_giver
from lzl.src.Data_helper import *

helper = DB_helper("localhost", "githubDB", "123456", "github_test")
giver = Data_giver(helper)

# g = os.walk(r"F:\python project\githubDB\lhx\res\files\xinhecuican")
# for path, dir_list, file_list in g:
#     for file_name in file_list:
#         if os.path.splitext(os.path.join(path, file_name))[-1] == '.txt':
#             os.rename(os.path.join(path, file_name), os.path.join(path, file_name)[:-4])
