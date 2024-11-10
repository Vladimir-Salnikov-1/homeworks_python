from address import Address
from mailing import Mailing

address_to1 = Address("186300", "г. Петрозаводск", "ул. Повенецкая",
                      "д. 2", "ком. 453")
address_from1 = Address("186500", "г. Беломорск", "ул. Банковская",
                        "д. 6", "кв. 36")
track1 = Mailing(address_to1, address_from1, "450", "FF45054vt45")


print(track1)
