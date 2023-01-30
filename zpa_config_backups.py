import zpa_functions
from box import Box
import json
from github_upload_backups import upload_to_github


def list_app_segments():
    all_apps = []
    for apps in zpa_functions.zpa.app_segments.list_segments():
        all_apps.append(Box(apps))
    with open("app_segments_backup.json", "w") as outfile:
        json.dump(all_apps, outfile, indent=4)


def list_segment_groups():
    all_segment_groups = []
    for segment_groups in zpa_functions.zpa.segment_groups.list_groups():
        all_segment_groups.append(Box(segment_groups))
    with open("segment_groups_backup.json", "w") as outfile:
        json.dump(all_segment_groups, outfile, indent=4)


def list_server_groups():
    all_server_groups = []
    for server_groups in zpa_functions.zpa.server_groups.list_groups():
        all_server_groups.append(Box(server_groups))
    with open("server_groups_backup.json", "w") as outfile:
        json.dump(all_server_groups, outfile, indent=4)


def access_policy_backup():
    all_access_policies = []
    for policy in zpa_functions.zpa.policies.list_rules(policy_type="access"):
        all_access_policies.append(Box(policy))
    with open("access_policy_backup.json", "w") as outfile:
        json.dump(all_access_policies, outfile, indent=4)


if __name__ == "__main__":
    open("server_groups_backup.json", 'w').close()
    open("access_policy_backup.json", 'w').close()
    open("segment_groups_backup.json", 'w').close()
    open("app_segments_backup.json", 'w').close()
    list_app_segments()
    list_segment_groups()
    list_server_groups()
    access_policy_backup()
    upload_to_github()
