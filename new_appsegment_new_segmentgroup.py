import zpa_functions

# Update variable for name of Segment Group you wish to use
segment_name = "Test"

# Creates the Segment Group for Application Segments
zpa_functions.zpa.segment_groups.add_group(name=segment_name, enabled=True)

# segment_group_id pulled from the function
segment_id = zpa_functions.get_segment_id_by_name(segment_name)

# Regional Server Groups for passing traffic to App Segments
# names used "NA App Connectors", "EU App Connectors", "APAC App Connectors", "All App Connectors"
group_id = zpa_functions.server_group_id("NA App Connectors")

# Creates your App Segments
# Update The Server_Group_IDs to respective regional group
new_app = zpa_functions.zpa.app_segments.add_segment(
    name="NA - Test",
    description="Test",
    domain_names=[
        "test.com"
    ],
    segment_group_id=segment_id,
    icmp_access_type="PING",
    server_group_ids=[group_id],
    tcp_ports=["443", "443", "80", "80"]
)

# Include udp_ports=["#", "#"] if you need a range of UDP ports
