"""
This file is part of Filmot API wrapper.

Filmot API is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.
"""


class Categories:
    """Represents various categories for classification."""

    AUTOS_AND_VEHICLES = "Autos & Vehicles"
    COMEDY = "Comedy"
    EDUCATION = "Education"
    ENTERTAINMENT = "Entertainment"
    FILM_AND_ANIMATION = "Film & Animation"
    GAMING = "Gaming"
    HOWTO_AND_STYLE = "Howto & Style"
    MUSIC = "Music"
    NEWS_AND_POLITICS = "News & Politics"
    NONPROFITS_AND_ACTIVISM = "Nonprofits & Activism"
    PEOPLE_AND_BLOGS = "People & Blogs"
    PETS_AND_ANIMALS = "Pets & Animals"
    SCIENCE_AND_TECHNOLOGY = "Science & Technology"
    SPORTS = "Sports"
    TRAVEL_AND_EVENTS = "Travel & Events"

    @classmethod
    def get_all_categories(cls) -> list:
        """Get all available categories."""
        categories = []
        for attribute_name in dir(cls):
            if not attribute_name.startswith("__") and not callable(getattr(cls, attribute_name)):
                categories.append(getattr(cls, attribute_name))
        return categories


class Countries:
    """Represents various countries and their corresponding country codes."""

    UNKNOWN = 1
    AFGHANISTAN = 2
    ALBANIA = 3
    BRITISH_VIRGIN_ISLANDS = 4
    ALAND_ISLANDS = 5
    COMOROS = 6
    BARBADOS = 7
    AZERBAIJAN = 8
    COOK_ISLANDS = 9
    BENIN = 10
    ANGOLA = 11
    ALGERIA = 12
    DOMINICA = 13
    BRAZIL = 14
    ANTARCTICA = 15
    BELIZE = 16
    EQUATORIAL_GUINEA = 17
    CAMEROON = 18
    AUSTRALIA = 19
    AMERICAN_SAMOA = 20
    ERITREA = 21
    CANADA = 22
    BELARUS = 23
    CAYMAN_ISLANDS = 24
    FRENCH_POLYNESIA = 25
    CHAD = 26
    BERMUDA = 27
    ANTIGUA_AND_BARBUDA = 28
    FRENCH_SOUTHERN_TERRITORIES = 29
    CONGO = 30
    BHUTAN = 31
    CENTRAL_AFRICAN_REPUBLIC = 32
    GRENADA = 33
    DJIBOUTI = 34
    BOLIVIA = 35
    ARMENIA = 36
    GUAM = 37
    DOMINICAN_REPUBLIC = 38
    BOUVET_ISLAND = 39
    CHILE = 40
    HOLY_SEE_VATICAN_CITY_STATE = 41
    GEORGIA = 42
    BRITISH_INDIAN_OCEAN_TERRITORY = 43
    BONAIRE_SINT_EUSTATIUS_AND_SABA = 44
    ISLE_OF_MAN = 45
    GIBRALTAR = 46
    CAMBODIA = 47
    CONGO_DEMOCRATIC_REPUBLIC_OF = 48
    ISRAEL = 49
    GREENLAND = 50
    COLOMBIA = 51
    BULGARIA = 52
    JAMAICA = 53
    GUERNSEY = 54
    COTE_D_IVOIRE = 55
    CUBA = 56
    KENYA = 57
    HONDURAS = 58
    CURACAO = 59
    BURKINA_FASO = 60
    KYRGYZSTAN = 61
    ICELAND = 62
    CYPRUS = 63
    ECUADOR = 64
    LIBERIA = 65
    KAZAKHSTAN = 66
    DENMARK = 67
    BURUNDI = 68
    LUXEMBOURG = 69
    MONTENEGRO = 70
    FIJI = 71
    EL_SALVADOR = 72
    MADAGASCAR = 73
    MOROCCO = 74
    FINLAND = 75
    CAPE_VERDE = 76
    MARSHALL_ISLANDS = 77
    NETHERLANDS = 78
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = 79
    ESTONIA = 80
    MONGOLIA = 81
    NORFOLK_ISLAND = 82
    HUNGARY = 83
    CHINA = 84
    PAPUA_NEW_GUINEA = 85
    NORWAY = 86
    INDONESIA = 87
    FAROE_ISLANDS = 88
    PARAGUAY = 89
    PUERTO_RICO = 90
    IRAN = 91
    CHRISTMAS_ISLAND = 92
    PERU = 93
    SAINT_KITTS_AND_NEVIS = 94
    GERMANY = 95
    PITCAIRN = 96
    SAINT_MARTIN = 97
    JAPAN = 98
    COSTA_RICA = 99
    POLAND = 100
    SAN_MARINO = 101
    JERSEY = 102
    GUADELOUPE = 103
    SAINT_HELENA = 104
    SINGAPORE = 105
    JORDAN = 106
    CZECHIA = 107
    SAINT_VINCENT_AND_THE_GRENADINES = 108
    SWEDEN = 109
    LESOTHO = 110
    GUATEMALA = 111
    SAUDI_ARABIA = 112
    TAIWAN = 113
    MICRONESIA_FEDERATED_STATES_OF = 114
    ETHIOPIA = 115
    SERBIA = 116
    TURKS_AND_CAICOS_ISLANDS = 117
    MOLDOVA = 118
    HONG_KONG = 119
    SOUTH_SUDAN = 120
    UGANDA = 121
    MOZAMBIQUE = 122
    FALKLAND_ISLANDS_ISLAS_MALVINAS = 123
    SURINAME = 124
    URUGUAY = 125
    NEPAL = 126
    LAOS = 127
    SYRIA = 128
    WESTERN_SAHARA = 129
    NEW_CALEDONIA = 130
    GHANA = 131
    TAJIKISTAN = 132
    ZAMBIA = 133
    PANAMA = 134
    MALDIVES = 135
    TRINIDAD_AND_TOBAGO = 136
    PORTUGAL = 137
    GREECE = 138
    TURKEY = 139
    REUNION = 140
    MAYOTTE = 141
    VIETNAM = 142
    SAINT_BARTHELEMY = 143
    HAITI = 144
    SINT_MAARTEN = 145
    MEXICO = 146
    SLOVAKIA = 147
    INDIA = 148
    SOMALIA = 149
    NAMIBIA = 150
    TANZANIA = 151
    IRAQ = 152
    UNITED_KINGDOM = 153
    NAURU = 154
    UNITED_STATES_VIRGIN_ISLANDS = 155
    KUWAIT = 156
    UZBEKISTAN = 157
    NEW_ZEALAND = 158
    VANUATU = 159
    LEBANON = 160
    WALLIS_AND_FUTUNA = 161
    NICARAGUA = 162
    LIBYA = 163
    YEMEN = 164
    NORTH_KOREA = 165
    MACAO = 166
    PALAU = 167
    MALAWI = 168
    RUSSIA = 169
    MALAYSIA = 170
    SAINT_PIERRE_AND_MIQUELON = 171
    MAURITANIA = 172
    SAO_TOME_AND_PRINCIPE = 173
    MAURITIUS = 174
    SUDAN = 175
    NIUE = 176
    SWAZILAND = 177
    NORTHERN_MARIANA_ISLANDS = 178
    SWITZERLAND = 179
    OMAN = 180
    THAILAND = 181
    QATAR = 182
    ANDORRA = 183
    TOKELAU = 184
    ROMANIA = 185
    ANGUILLA = 186
    TUVALU = 187
    RWANDA = 188
    ARGENTINA = 189
    UNITED_ARAB_EMIRATES = 190
    SAINT_LUCIA = 191
    ARUBA = 192
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = 193
    SEYCHELLES = 194
    AUSTRIA = 195
    VENEZUELA = 196
    SLOVENIA = 197
    BAHAMAS = 198
    SOLOMON_ISLANDS = 199
    BAHRAIN = 200
    SOUTH_AFRICA = 201
    BANGLADESH = 202
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 203
    BELGIUM = 204
    SRI_LANKA = 205
    BOSNIA_AND_HERZEGOVINA = 206
    SVALBARD_AND_JAN_MAYEN = 207
    BOTSWANA = 208
    TONGA = 209
    BRUNEI = 210
    TUNISIA = 211
    COCOS_KEELING_ISLANDS = 212
    TURKMENISTAN = 213
    CROATIA = 214
    UKRAINE = 215
    EGYPT = 216
    UNITED_STATES = 217
    FRANCE = 218
    ZIMBABWE = 219
    FRENCH_GUIANA = 220
    GABON = 221
    GAMBIA = 222
    GUINEA = 223
    GUINEA_BISSAU = 224
    GUYANA = 225
    IRELAND = 226
    ITALY = 227
    KIRIBATI = 228
    LATVIA = 229
    LIECHTENSTEIN = 230
    LITHUANIA = 231
    MACEDONIA = 232
    MALI = 233
    MALTA = 234
    MARTINIQUE = 235
    MONACO = 236
    MONTSERRAT = 237
    MYANMAR = 238
    NIGER = 239
    NIGERIA = 240
    PAKISTAN = 241
    PHILIPPINES = 242
    SAMOA = 243
    SENEGAL = 244
    SIERRA_LEONE = 245
    SOUTH_KOREA = 246
    SPAIN = 247
    TIMOR_LESTE = 248
    TOGO = 249
    WEST_BANK = 250

    @classmethod
    def get_all_codes(cls) -> list:
        """Get all available country codes."""
        codes = []
        for attribute_name in dir(cls):
            if not attribute_name.startswith("__") and not callable(getattr(cls, attribute_name)):
                codes.append(getattr(cls, attribute_name))
        return sorted(codes)


class Language:
    """Represents various languages and their corresponding language codes."""

    AFRIKAANS = "af"
    ALBANIAN = "sq"
    ARABIC = "ar"
    ARAGONESE = "an"
    ARMENIAN = "hy"
    ASTURIAN = "at"
    BASQUE = "eu"
    BELARUSIAN = "be"
    BENGALI = "bn"
    BOSNIAN = "bs"
    BRETON = "br"
    BULGARIAN = "bg"
    BURMESE = "my"
    CATALAN = "ca"
    CHINESE_SIMPLIFIED = "zh-cn"
    CZECH = "cs"
    DANISH = "da"
    DUTCH = "nl"
    ENGLISH = "en"
    ESPERANTO = "eo"
    ESTONIAN = "et"
    FINNISH = "fi"
    FRENCH = "fr"
    GEORGIAN = "ka"
    GERMAN = "de"
    GALICIAN = "gl"
    GREEK = "el"
    HEBREW = "he"
    HINDI = "hi"
    CROATIAN = "hr"
    HUNGARIAN = "hu"
    ICELANDIC = "is"
    INDONESIAN = "id"
    ITALIAN = "it"
    JAPANESE = "ja"
    KAZAKH = "kk"
    KHMER = "km"
    KOREAN = "ko"
    LATVIAN = "lv"
    LITHUANIAN = "lt"
    LUXEMBOURGISH = "lb"
    MACEDONIAN = "mk"
    MALAYALAM = "ml"
    MALAY = "ms"
    MANIPURI = "ma"
    MONGOLIAN = "mn"
    NORWEGIAN = "no"
    OCCITAN = "oc"
    PERSIAN = "fa"
    POLISH = "pl"
    PORTUGUESE = "pt-pt"
    RUSSIAN = "ru"
    SERBIAN = "sr"
    SINHALESE = "si"
    SLOVAK = "sk"
    SLOVENIAN = "sl"
    SPANISH = "es"
    SWAHILI = "sw"
    SWEDISH = "sv"
    SYRIAC = "sy"
    TAMIL = "ta"
    TELUGU = "te"
    TAGALOG = "tl"
    THAI = "th"
    TURKISH = "tr"
    UKRAINIAN = "uk"
    URDU = "ur"
    UZBEK = "uz"
    VIETNAMESE = "vi"
    ROMANIAN = "ro"
    PORTUGUESE_BRAZILIAN = "pt-br"
    MONTENEGRIN = "me"
    CHINESE_TRADITIONAL = "zh-tw"
    CHINESE_BILINGUAL = "ze"
    NORWEGIAN_BOKMAL = "nb"
    NORTHERN_SAMI = "se"

    @classmethod
    def get_all_codes(cls) -> list:
        """Get all available language codes."""
        codes = []
        for attribute_name in dir(cls):
            if not attribute_name.startswith("__") and not callable(getattr(cls, attribute_name)):
                codes.append(getattr(cls, attribute_name))
        return sorted(codes)
