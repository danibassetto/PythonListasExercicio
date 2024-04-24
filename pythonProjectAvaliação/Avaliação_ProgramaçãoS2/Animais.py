a1 = input().lower()
a2 = input().lower()
a3 = input().lower()

animais = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba",
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca",
        },
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta",
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca",
        },
    },
}

print(animais[a1][a2][a3])