from datetime import datetime
from pydantic import BaseModel, Field

from typing import Optional, List


class BaseNotification(BaseModel):
    is_read: Optional[bool]
    notification_id: int
    sender_id: int
    sender_type: str
    timestamp: datetime
    auth_corp_ticker: str
    auth_corp_name: str
    type_: str = Field(alias="type")

    class Config:
        alias_generator: lambda x: x if x != "type" else "type_"


class NotificationTypeNotFound(BaseNotification):
    content: str


class NPCStandingsLost(BaseNotification):
    faction: int
    character_id: int
    standing_delta: float
    sec_status: float
    sec_status2: float
    new_standing: float


class TowerResourceAlertMsg(BaseNotification):
    alliance_id: Optional[int] = Field(alias="allianceID")
    corp_id: int = Field(alias="corpID")
    moon_id: int = Field(alias="moonID")
    solar_system_id: int = Field(alias="solarSystemID")
    type_id: int = Field(alias="typeID")
    wants: Optional[list]
    track_structure_fuel: Optional[bool]
    moon_location: Optional[str]
    structure_type: Optional[str]


class AllAnchoringMsg(BaseNotification):
    alliance_id: Optional[int] = Field(alias="allianceID")
    corp_id: int = Field(alias="corpID")
    corps_present: Optional[List[dict]] = Field(alias="corpsPresent")
    moon_id: int = Field(alias="moonID")
    solar_system_id: int = Field(alias="solarSystemID")
    type_id: int = Field(alias="typeID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    moon_location: Optional[str]
    anchored_by: Optional[str]
    structure_type: Optional[str]


class EntosisCaptureStarted(BaseNotification):
    solar_system_id: int = Field(alias="solarSystemID")
    structure_type_id: int = Field(alias="structureTypeID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    structure_name: Optional[str]


class SovAllClaimAquiredMsg(BaseNotification):
    alliance_id: Optional[int] = Field(alias="allianceID")
    corp_id: int = Field(alias="corpID")
    solar_system_id: int = Field(alias="solarSystemID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    corporation_name: Optional[str]


class SovAllClaimLostMsg(BaseNotification):
    alliance_id: Optional[int] = Field(alias="allianceID")
    corp_id: int = Field(alias="corpID")
    solar_system_id: int = Field(alias="solarSystemID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    corporation_name: Optional[str]


class SovCommandNodeEventStarted(BaseNotification):
    campaign_event_type: int = Field(alias="campaignEventType")
    constellation_id: int = Field(alias="constellationID")
    solar_system_id: int = Field(alias="solarSystemID")
    region_id: Optional[int]


class SovStructureDestroyed(BaseNotification):
    solar_system_id: int = Field(alias="solarSystemID")
    structure_type_id: int = Field(alias="structureTypeID")
    structure_type_name: Optional[str]
    region_id: Optional[int]
    constellation_id: Optional[int]


class SovStructureReinforced(BaseNotification):
    campaign_event_type: int = Field(alias="campaignEventType")
    decloak_time: int = Field(alias="decloakTime")
    solar_system_id: int = Field(alias="solarSystemID")
    region_id: Optional[int]
    constellation_id: Optional[int]


class StructureAnchoring(BaseNotification):
    owner_corp_link_data: list = Field(alias="ownerCorpLinkData")
    owner_corp_name: str = Field(alias="ownerCorpName")
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    time_left: int = Field(alias="timeLeft")
    vulnerable_time: int = Field(alias="vulnerableTime")
    region_id: Optional[int]
    constellation_id: Optional[int]


class StructureDestroyed(BaseNotification):
    is_abandoned: bool = Field(alias="isAbandoned")
    owner_corp_link_data: list = Field(alias="ownerCorpLinkData")
    owner_corp_name: str = Field(alias="ownerCorpName")
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    structure_name: Optional[str]


class StructureFuelAlert(BaseNotification):
    list_of_types_and_qty: list = Field(alias="listOfTypesAndQty")
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    track_structure_fuel: Optional[bool]
    structure_name: Optional[str]
    structure_type: Optional[str]


class StructureLostArmor(BaseNotification):
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    time_left: int = Field(alias="timeLeft")
    vulnerable_time: int = Field(alias="vulnerableTime")
    region_id: Optional[int]
    constellation_id: Optional[int]
    structure_name: Optional[str]
    reinforced_timer: Optional[int]


class StructureLostShields(BaseNotification):
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    time_left: int = Field(alias="timeLeft")
    vulnerable_time: int = Field(alias="vulnerableTime")
    region_id: Optional[int]
    constellation_id: Optional[int]
    structure_name: Optional[str]
    reinforced_timer: Optional[int]


class StructureUnderAttack(BaseNotification):
    alliance_id: Optional[int] = Field(alias="allianceID")
    alliance_link_data: Optional[list] = Field(alias="allianceLinkData")
    alliance_name: Optional[str] = Field(alias="allianceName")
    armor_percentage: float = Field(alias="armorPercentage")
    char_id: int = Field(alias="charID")
    corp_link_data: list = Field(alias="corpLinkData")
    corp_name: str = Field(alias="corpName")
    hull_percentage: float = Field(alias="hullPercentage")
    shield_percentage: float = Field(alias="shieldPercentage")
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    structure_name: Optional[str]
    attacking_character: Optional[str]
    structure_health: Optional[str]
    structure_type: Optional[str]


class StructureWentHighPower(BaseNotification):
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    region_id: Optional[int]
    constellation_id: Optional[int]


class StructureWentLowPower(BaseNotification):
    solar_system_id: int = Field(alias="solarsystemID")
    structure_id: int = Field(alias="structureID")
    structure_show_info_data: list = Field(alias="structureShowInfoData")
    structure_type_id: int = Field(alias="structureTypeID")
    region_id: Optional[int]
    constellation_id: Optional[int]


class TowerAlertMsg(BaseNotification):
    aggressor_alliance_id: Optional[int] = Field(alias="aggressorAllianceID")
    aggressor_corp_id: int = Field(alias="aggressorCorpID")
    aggressor_id: int = Field(alias="aggressorID")
    armor_value: float = Field(alias="armorValue")
    hull_value: float = Field(alias="hullValue")
    moon_id: int = Field(alias="moonID")
    shield_value: float = Field(alias="shieldValue")
    solar_system_id: int = Field(alias="solarSystemID")
    type_id: int = Field(alias="typeID")
    region_id: Optional[int]
    constellation_id: Optional[int]
    attacker: Optional[str]
    structure_health: Optional[str]
    moon_location: Optional[str]
    structure_type: Optional[str]


class AllWarDeclaredMsg(BaseNotification):
    against_id: Optional[int] = Field(alias="againstID")
    declared_by_id: Optional[int] = Field(alias="declaredByID")
    war_declared_against: Optional[str]
    war_declared_by: Optional[str]


class AllWarInvalidatedMsg(BaseNotification):
    against_id: Optional[int] = Field(alias="againstID")
    declared_by_id: Optional[int] = Field(alias="declaredByID")
    war_declared_against: Optional[str]
    war_declared_by: Optional[str]


class AllWarSurrenderMsg(BaseNotification):
    against_id: Optional[int] = Field(alias="againstID")
    declared_by_id: Optional[int] = Field(alias="declaredByID")
    war_declared_against: Optional[str]
    war_declared_by: Optional[str]


models = {
    "NPCStandingsLost": NPCStandingsLost,
    "TowerResourceAlertMsg": TowerResourceAlertMsg,
    "AllAnchoringMsg": AllAnchoringMsg,
    "EntosisCaptureStarted": EntosisCaptureStarted,
    "SovAllClaimAquiredMsg": SovAllClaimAquiredMsg,
    "SovAllClaimLostMsg": SovAllClaimLostMsg,
    "SovCommandNodeEventStarted": SovCommandNodeEventStarted,
    "SovStructureDestroyed": SovStructureDestroyed,
    "SovStructureReinforced": SovStructureReinforced,
    "StructureAnchoring": StructureAnchoring,
    "StructureDestroyed": StructureDestroyed,
    "StructureFuelAlert": StructureFuelAlert,
    "StructureLostArmor": StructureLostArmor,
    "StructureLostShields": StructureLostShields,
    "StructureUnderAttack": StructureUnderAttack,
    "StructureWentHighPower": StructureWentHighPower,
    "StructureWentLowPower": StructureWentLowPower,
    "TowerAlertMsg": TowerAlertMsg,
    "AllWarDeclaredMsg": AllWarDeclaredMsg,
    "AllWarInvalidatedMsg": AllWarInvalidatedMsg,
    "AllWarSurrenderMsg": AllWarSurrenderMsg,
}
