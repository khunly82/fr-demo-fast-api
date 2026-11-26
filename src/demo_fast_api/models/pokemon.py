from pydantic import BaseModel, Field


class NamedAPIResource(BaseModel):
    name: str
    url: str


# --- Abilities ---


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: NamedAPIResource | None = None


class PokemonAbilityPast(BaseModel):
    generation: NamedAPIResource
    abilities: list[PokemonAbility]


# --- Game indices ---


class VersionGameIndex(BaseModel):
    game_index: int
    version: NamedAPIResource


# --- Held items ---


class PokemonHeldItemVersion(BaseModel):
    rarity: int
    version: NamedAPIResource


class PokemonHeldItem(BaseModel):
    item: NamedAPIResource
    version_details: list[PokemonHeldItemVersion]


# --- Moves ---


class PokemonMoveVersion(BaseModel):
    level_learned_at: int
    version_group: NamedAPIResource
    move_learn_method: NamedAPIResource
    order: int | None = None
    enhancement_level: int | None = None


class PokemonMove(BaseModel):
    move: NamedAPIResource
    version_group_details: list[PokemonMoveVersion]


# --- Sprites ---


class HomeSprites(BaseModel):
    front_shiny: str | None = None
    front_female: str | None = None
    front_default: str | None = None
    front_shiny_female: str | None = None


class ShowdownSprites(BaseModel):
    back_shiny: str | None = None
    back_female: str | None = None
    front_shiny: str | None = None
    back_default: str | None = None
    front_female: str | None = None
    front_default: str | None = None
    back_shiny_female: str | None = None
    front_shiny_female: str | None = None


class OtherSprites(BaseModel):
    home: HomeSprites | None = None
    showdown: ShowdownSprites | None = None


class Gen1YellowSprites(BaseModel):
    back_gbc: str | None = None
    back_gray: str | None = None
    front_gbc: str | None = None
    front_gray: str | None = None
    back_default: str | None = None
    front_default: str | None = None
    back_transparent: str | None = None
    front_transparent: str | None = None
    back_transparent_gray: str | None = None
    front_transparent_gray: str | None = None


class Gen1RedBlueSprites(BaseModel):
    back_gray: str | None = None
    front_gray: str | None = None
    back_default: str | None = None
    front_default: str | None = None
    back_transparent: str | None = None
    front_transparent: str | None = None
    back_transparent_gray: str | None = None
    front_transparent_gray: str | None = None


class GenerationISprites(BaseModel):
    yellow: Gen1YellowSprites | None = None
    red_blue: Gen1RedBlueSprites | None = Field(default=None, alias="red-blue")


class Gen5IconsSprites(BaseModel):
    animated: dict[str, str | None] | None = None
    front_default: str | None = None


class Gen5BlackWhiteSprites(BaseModel):
    animated: ShowdownSprites | None = None
    back_shiny: str | None = None
    back_female: str | None = None
    front_shiny: str | None = None
    back_default: str | None = None
    front_female: str | None = None
    front_default: str | None = None
    back_shiny_female: str | None = None
    front_shiny_female: str | None = None


class GenerationVSprites(BaseModel):
    icons: Gen5IconsSprites | None = None
    black_white: Gen5BlackWhiteSprites | None = Field(default=None, alias="black-white")


class VersionSprites(BaseModel):
    generation_i: GenerationISprites | None = Field(default=None, alias="generation-i")
    generation_v: GenerationVSprites | None = Field(default=None, alias="generation-v")


class PokemonSprites(BaseModel):
    other: OtherSprites | None = None
    versions: VersionSprites | None = None
    back_shiny: str | None = None
    back_female: str | None = None
    front_shiny: str | None = None
    back_default: str | None = None
    front_female: str | None = None
    front_default: str | None = None
    back_shiny_female: str | None = None
    front_shiny_female: str | None = None


# --- Cries ---


class PokemonCries(BaseModel):
    latest: str | None = None
    legacy: str | None = None


# --- Stats ---


class PokemonStat(BaseModel):
    base_stat: int
    effort: int
    stat: NamedAPIResource


class PokemonStatPast(BaseModel):
    generation: NamedAPIResource
    stats: list[PokemonStat]


# --- Types ---


class PokemonType(BaseModel):
    slot: int
    type: NamedAPIResource


class PokemonTypePast(BaseModel):
    generation: NamedAPIResource
    types: list[PokemonType]


# --- Racine ---


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int | None = None
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: list[PokemonAbility]
    past_abilities: list[PokemonAbilityPast]
    forms: list[NamedAPIResource]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    species: NamedAPIResource
    sprites: PokemonSprites
    cries: PokemonCries
    stats: list[PokemonStat]
    past_stats: list[PokemonStatPast]
    types: list[PokemonType]
    past_types: list[PokemonTypePast]