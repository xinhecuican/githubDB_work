- branches.csv

  branch_name, branch_parent, owner_repository, last_commit, commit_num, branch_down_link

- commit.csv

  last_commit_id, repository_id, commit_user, commit_date, comment

- followers.csv

  follower_id, following_id

- repository.csv

  repository_name, repository_id, owner_name(爬错了，但也是唯一的)，default_branch, contributor_num, star_num, fork_num

- user.csv

  user_id, user_name(用户名 唯一)，follower, following, star_num, repository_num, project_num