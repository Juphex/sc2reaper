ENCODER_KEYS = {
    # replay doc
    "replay_name": 1,
    "match_up": 2,
    "game_duration_loops": 3,
    "game_duration_seconds": 4,
    "game_version": 5,
    "player_1": 6,
    "player_2": 7,
    "map": 8,
    # map doc
    "starting_location": 9,
    "minimap": 10,
    "height_map": 11,
    "bitsPerPixel": 12,
    "size": 13,
    "data": 14,
    "name": 15,
    # player doc
    "player_id": 16,
    "race": 17,
    "result": 18,
    "states": 19,
    "actions": 20,
    "scores": 21,
    # state doc
    "frame_id": 22,
    "resources": 23,
    "minerals": 24,
    "vespene": 25,
    "supply": 26,
    "used": 27,
    "total": 28,
    "army": 29,
    "workers": 30,
    "units": 31,
    "units_in_progress": 32,
    "visible_enemy_units": 33,
    # unit doc
    "tag": 34,
    "unit_type": 35,
    "alliance": 36,
    "type": 37,
    "location": 38,
    "x": 39,
    "y": 40,
    "z": 41,
    "owner": 42,
    "health": 43,
    "health_max": 44,
    "shield": 45,
    "shield_max": 46,
    "energy": 47,
    "energy_max": 48,
    "build_progress": 49,
    "is_on_screen": 50,
    # action doc
    "ability_id": 51,
    "unit_tags": 52,
    "target_unit_tag": 53,
    "target_world_space_pos": 54,
    # score doc
    "collection_rate": 55,
    "idle_worker_time": 56,
    "killed_minerals": 57,
    "killed_vespene": 58,
    "used_minerals": 59,
    "used_vespene": 60,
    "none": 61,
    "economy": 62,
    "technology": 63,
    "upgrade": 64,
}
ENCODER_KEYS = {key: str(value) for key, value in ENCODER_KEYS.items()}

DECODER_KEYS = {value: key for key, value in ENCODER_KEYS.items()}


def encode(document):
    """
    Replaces the keys of a dict with numbers (for compression)
    """
    if isinstance(document, list):
        return [encode(item) for item in document]
    if isinstance(document, dict):
        return {
            ENCODER_KEYS.get(key, key): encode(value) for key, value in document.items()
        }
    return document


def decode(document):
    """
    Replaces numeric keys with human readable ones (for readability)
    """
    if isinstance(document, list):
        return [decode(item) for item in document]
    if isinstance(document, dict):
        return {
            DECODER_KEYS.get(key, key): encode(value) for key, value in document.items()
        }
    return document
