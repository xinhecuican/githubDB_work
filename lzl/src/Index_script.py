index_followers_follower_id = "create index followers_follower_id on followers(follower_id)"
index_followers_following_id = "create index following_id on followers(following_id)"

index_activity_user_id = 'create index activity_user_id on activity(user_id)'

index_activity_record = 'create index activity_record_user_id on activity_record(user_id)'

index_user_notification_user_id = 'create index user_notification_user_id on user_notification(user_id)'

index_repository_user_id = 'create index repository_user_id on repository(user_id)'

index_tags_repository_id = 'create index tags_repository_id on tags(repository_id)'

index_tag_files_tag_id = 'create index tag_files_tag_id on tag_files(tag_id)'

index_issue_repository_id = 'create index issue_repository_id on issue(repository_id)'

index_issue_comment_issue_id = 'create index issue_comment_issue_id on issue_comment(issue_id)'

index_pull_request_repository_id = 'create index pull_request_repository_id on pull_request(repository_id)'

index_pull_request_action_pull_request_id = 'create index_pull_request_action_pull_request_id on pull_request_action(pull_request_id)'

index_branches_repository_id = 'create index branches_repository_id on branches(repository_id)'

index_commits_parent_commit = 'create index commits_parent_commit on commits(parent_commit)'

index_commit_files_commit_id = 'create index commit_files_commit_id on commit_files(commit_id)'

idnex_commit_comment_commit_id = 'create index commit_comment_commit_id on commit_comment(commit_id)'
