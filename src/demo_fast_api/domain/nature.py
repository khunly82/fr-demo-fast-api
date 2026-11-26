from enum import IntFlag, StrEnum, auto


class Nature(StrEnum):
    # Neutres
    bizarre = "BIZARRE"
    docile = "DOCILE"
    hardi = "HARDI"
    pudique = "PUDIQUE"
    serieux = "SÉRIEUX"

    # + Attaque
    solo = "SOLO"
    rigide = "RIGIDE"
    mauvais = "MAUVAIS"
    brave = "BRAVE"

    # + Défense
    assure = "ASSURÉ"
    malin = "MALIN"
    lache = "LÂCHE"
    relax = "RELAX"

    # + Attaque Spéciale
    modeste = "MODESTE"
    doux = "DOUX"
    foufou = "FOUFOU"
    discret = "DISCRET"

    # + Défense Spéciale
    calme = "CALME"
    gentil = "GENTIL"
    prudent = "PRUDENT"
    malpoli = "MALPOLI"

    # + Vitesse
    timide = "TIMIDE"
    presse = "PRESSÉ"
    jovial = "JOVIAL"
    naif = "NAÏF"

