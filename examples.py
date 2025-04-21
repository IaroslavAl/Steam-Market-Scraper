import data
import scraper

items = [
    "Recoil Case",
    "Fracture Case",
    "Revolution Case",
    "AK-47 | Elite Build (Factory New)",
    "Souvenir MAC-10 | Urban DDPAT (Factory New)",
    "StatTrak™ Galil AR | Control (Factory New)",
    "StatTrak™ USP-S | PC-GRN (Factory New)",
    "Sealed Graffiti | 200 IQ (Tracer Yellow)",
    "StatTrak™ M4A4 | Choppa (Factory New)",
    "StatTrak™ P2000 | Sure Grip (Factory New)",
    "1st Lieutenant Farlow | SWAT",
    "Street Soldier | Phoenix",
    "Tec-9 | VariCamo (Minimal Wear)"
]

if __name__ == '__main__':
    for item in items:
        print("\n")
        print(item)
        print(
            scraper.market_scraper(
                item,
                data.Apps.CS2.value,
                data.Currency.RUB.value,
            ),
        )
