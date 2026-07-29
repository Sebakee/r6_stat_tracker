operator_roles = {
    # Attackers
    "Solid Snake": {
        "entry": 1.0
    },
    "Rauora": {
        "entry": 0.2
    },
    "Striker": {
        "entry": 0.5
    },
    "Deimos": {
        "entry": 1.0
    },    
    "Ram": {
        "entry": 0.9
    },    
    "Brava": {
        "entry": 0.3
    },    
    "Grim": {
        "entry": 0.7
    },    
    "Sens": {
        "entry": 0.5
    },    
    "Osa": {
        "entry": 0.5
    },    
    "Flores": {
        "entry": 0.2
    },    
    "Zero": {
        "entry": 0.6
    },    
    "Ace": {
        "entry": 0.2
    },    
    "Iana": {
        "entry": 1.0
    },    
    "Kali": {
        "entry": 0.1
    },    
    "Amaru": {
        "entry": 1.0
    },    
    "Nøkk": {
        "entry": 1.0
    },    
    "Gridlock": {
        "entry": 0.5
    },    
    "Nomad": {
        "entry": 0.5
    },    
    "Maverick": {
        "entry": 0.3
    },    
    "Lion": {
        "entry": 0.7
    },    
    "Finka": {
        "entry": 0.9
    },    
    "Dokkaebi": {
        "entry": 0.7
    },    
    "Zofia": {
        "entry": 0.8
    },    
    "Ying": {
        "entry": 0.9
    },    
    "Jackal": {
        "entry": 1.0
    },    
    "Hibana": {
        "entry": 0.2
    },    
    "Capitão": {
        "entry": 0.4
    },    
    "Blackbeard": {
        "entry": 0.8
    },    
    "Buck": {
        "entry": 0.8
    },    
    "Sledge": {
        "entry": 0.5
    },    
    "Thatcher": {
        "entry": 0.1
    },    
    "Ash": {
        "entry": 1.0
    },    
    "Thermite": {
        "entry": 0.1
    },    
    "Montagne": {
        "entry": 0.1
    },    
    "Twitch": {
        "entry": 0.4
    },    
    "Blitz": {
        "entry": 0.9
    },    
    "IQ": {
        "entry": 0.8
    },    
    "Fuze": {
        "entry": 0.2
    },    
    "Glaz": {
        "entry": 0.7
    },
    # Defenders    
    "Denari": {
        "entry": 0.0
    },    
    "Skopos": {
        "entry": 0.0
    },    
    "Sentry": {
        "entry": 0.0
    },    
    "Tubarão": {
        "entry": 0.0
    },    
    "Fenrir": {
        "entry": 0.0
    },    
    "Solis": {
        "entry": 0.0
    },    
    "Azami": {
        "entry": 0.0
    },    
    "Thorn": {
        "entry": 0.0
    },    
    "Thunderbird": {
        "entry": 0.0
    },    
    "Aruni": {
        "entry": 0.0
    },    
    "Melusi": {
        "entry": 0.0
    },    
    "Oryx": {
        "entry": 0.0
    },    
    "Wamai": {
        "entry": 0.0
    },    
    "Goyo": {
        "entry": 0.0
    },    
    "Warden": {
        "entry": 0.0
    },    
    "Mozzie": {
        "entry": 0.0
    },    
    "Kaid": {
        "entry": 0.0
    },    
    "Clash": {
        "entry": 0.0
    },    
    "Maestro": {
        "entry": 0.0
    },    
    "Alibi": {
        "entry": 0.0
    },    
    "Vigil": {
        "entry": 0.0
    },    
    "Ela": {
        "entry": 0.0
    },    
    "Lesion": {
        "entry": 0.0
    },    
    "Mira": {
        "entry": 0.0
    },    
    "Echo": {
        "entry": 0.0
    },    
    "Caveira": {
        "entry": 0.0
    },    
    "Valkyrie": {
        "entry": 0.0
    },    
    "Frost": {
        "entry": 0.0
    },    
    "Mute": {
        "entry": 0.0
    },    
    "Smoke": {
        "entry": 0.0
    },    
    "Castle": {
        "entry": 0.0
    },    
    "Pulse": {
        "entry": 0.0
    },    
    "Doc": {
        "entry": 0.0
    },    
    "Rook": {
        "entry": 0.0
    },    
    "Jäger": {
        "entry": 0.0
    },    
    "Bandit": {
        "entry": 0.0
    },    
    "Tachanka": {
        "entry": 0.0
    },    
    "Kapkan": {
        "entry": 0.0
    },
}

def get_op_roles(operator_name):
    return operator_roles.get(operator_name, {}).get("entry", 0.0)


