import common
from common import Debug
from lzl.src.DB_helper import DB_helper
import Tables_script
import trigger_script
import Index_script
import test_data

helper = DB_helper("localhost", "githubDB", "123456", "github_test")
