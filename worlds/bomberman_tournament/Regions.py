from typing import Dict, List, NamedTuple


class BomberTRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, BomberTRegionData] = {
    #"Menu": BomberTRegionData(["Alpha","Beta","Gamma","Delta","Epsilon","Upsilon","Ita"]),
    "Menu": BomberTRegionData(["Alpha"]),
    #Field Zone
    "Alpha": BomberTRegionData(["L Forest","Plains"]),
    "L Forest": BomberTRegionData(["Alpha"]),
    "Plains": BomberTRegionData(["Alpha","ColdSea"]),
    "ColdSea": BomberTRegionData(["Plains","ShuraRd"]),
    "ShuraRd": BomberTRegionData(["ColdSea","Beta"]),
    "Beta": BomberTRegionData(["ShuraRd","B Valley"]),
    "B Valley": BomberTRegionData(["MagBase","ToPlain"]), # Beta can not go backwards
    "MagBase": BomberTRegionData(["B Valley","MagBase Elifan"]),
    "MagBase Elifan": BomberTRegionData(["MagBase"]),

    #Beach Zone
    "ToPlain": BomberTRegionData(["B Valley","Gamma"]),
    "Gamma":  BomberTRegionData(["ToPlain","HarshMt","Delta"]),
    "HarshMt": BomberTRegionData(["Gamma"]),
    "Delta": BomberTRegionData(["Gamma","Wet Woods","S Forest","Jetty"]),
    "Wet Woods": BomberTRegionData(["Delta","HighMt"]),
    "HighMt": BomberTRegionData(["Wet Woods","LiteCave"]),
    "LiteCave": BomberTRegionData(["HighMt"]),
    "S Forest": BomberTRegionData(["Delta","BigOcean"]),
    "BigOcean": BomberTRegionData(["S Forest","Beluga"]),
    "Beluga": BomberTRegionData(["BigOcean","PttyBase"]),
    "PttyBase": BomberTRegionData(["Beluga"]),

    #Snow Zone
    "Jetty": BomberTRegionData(["Delta","Arctic","SnowFld"]),
    "Arctic": BomberTRegionData(["Jetty"]),
    "SnowFld": BomberTRegionData(["Jetty","Blizzard"]),
    "Blizzard": BomberTRegionData(["SnowFld","Epsilon"]),
    "IValley": BomberTRegionData(["PlzmBase"]),
    "Epsilon": BomberTRegionData(["Blizzard","HtSpring","SleetSt","FPalace"]),
    "HtSpring": BomberTRegionData(["Epsilon"]),
    "SleetSt": BomberTRegionData(["Epsilon","Upsilon"]),
    "Upsilon": BomberTRegionData(["SleetSt","MtRoad"]),
    "FPalace": BomberTRegionData(["Epsilon","PlzmBase"]),
    "PlzmBase": BomberTRegionData(["FPalace","IValley"]),

    #Desert Zone
    "MtRoad": BomberTRegionData(["Upsilon","Zeta"]),
    "Zeta": BomberTRegionData(["MtRoad","SararMts"]),
    "SararMts": BomberTRegionData(["Zeta","OldBase"]),
    "OldBase": BomberTRegionData(["SararMts","Quiksand"]),
    "Quiksand": BomberTRegionData(["OldBase","Ita"]),
    "Ita": BomberTRegionData(["Quiksand","Desert"]),
    "Desert": BomberTRegionData(["Ita","LavaPool","Theta","Omega"]),
    "LavaPool": BomberTRegionData(["Desert","Volcano"]),
    "Volcano": BomberTRegionData(["LavaPool","GlmBase"]),
    "GlmBase": BomberTRegionData(["Volcano"]),

    #Fantasy
    "Omega": BomberTRegionData(["Desert"]),
    "Theta": BomberTRegionData(["Desert","TForest"]),
    "TForest": BomberTRegionData(["Theta","AccessPt"]),
    "AccessPt": BomberTRegionData(["TForest","Fantasy"]),
    "Fantasy": BomberTRegionData(["AccessPt"]),

}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit