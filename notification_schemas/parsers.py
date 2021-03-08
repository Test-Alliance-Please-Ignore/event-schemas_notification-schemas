def npc_standings_lost(notification_data):
    return {
        "faction": notification_data[0],
        "character_id": notification_data[1],
        "standing_delta": notification_data[2],
        "sec_status": notification_data[3],
        "sec_status2": notification_data[4],
        "new_standing": notification_data[4],
    }


parsers = {"NPCStandingsLost": npc_standings_lost}
