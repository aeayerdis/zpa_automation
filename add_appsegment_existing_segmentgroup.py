import zpa_functions


# Update with Segment Name you need to add the app segment to
segment_id = zpa_functions.get_segment_id_by_name("Existing Segment Group")

# Regional Server Groups for passing traffic to App Segments
# names used "X App Connectors", "Y App Connectors", "Z App Connectors", "W App Connectors"
group_id = zpa_functions.server_group_id("Y App Connectors")

# Creates your App Segments
# Update The Server_Group_IDs to respective regional group
new_app = zpa_functions.zpa.app_segments.add_segment(
    name="Y - App Segment",
    description="Description",
    domain_names=[
        "test.co.uk",
    ],
    # Don't Edit
    segment_group_id=segment_id,
    icmp_access_type="PING",
    server_group_ids=[group_id],
    # Edit This
    tcp_ports=["443", "443", "80", "80"]
)

# You can inclue udp_ports=["#","#"]
