
import common
from common import Debug
from lzl.src.DB_helper import DB_helper
from Data_helper import *
import Tables_script
import trigger_script
import Index_script
import test_data
import Data_helper
from lzl.src.Data_giver import Data_giver

helper = DB_helper("localhost", "githubDB", "123456", "github_test")
giver = Data_giver(helper)