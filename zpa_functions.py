from box import Box
from pyzscaler import ZPA
import os
from dotenv import load_dotenv
load_dotenv()

zpa = ZPA(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'], customer_id=os.environ['customer_id'])


"""
# Update variable for name of Segment Group you wish to use
segment_name = "Aaron 100"
# Creates the Segment Group for Application Segments
zpa.segment_groups.add_group(name=segment_name, enabled=True)
# segment_group_id pulled from the function
segment_id = zpa_functions.get_segment_id_by_name(segment_name)
"""


def get_segment_id_by_name(segment_name):
    for segment_groups in zpa.segment_groups.list_groups():
        group = Box(segment_groups)
        name = group.name
        if name == segment_name:
            return group.id
        else:
            continue
    return None


"""
Usage in body of script
names used "NA App Connectors", "EU App Connectors", "APAC App Connectors", "All App Connectors"
group_id = zpa_functions.server_group_id("Name")
"""


def server_group_id(app_connector1):
    for server_groups in zpa.server_groups.list_groups():
        group = Box(server_groups)
        name = group.name
        if name == app_connector1:
            return group.id
        else:
            continue
    return None


def app_segment_id(app_segment):
    for app in zpa.app_segments.list_segments():
        a = Box(app)
        name = a.name
        if name == app_segment:
            return a.id
        else:
            continue
    return None

