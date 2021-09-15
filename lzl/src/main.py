from lzl.src.DB_helper import DB_helper
from lzl.src.Data_giver import Data_giver
from lzl.src.Data_helper import *

helper = DB_helper("localhost", "githubDB", "123456", "github_test")
giver = Data_giver(helper)