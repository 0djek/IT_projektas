mock_up_recipes_index = [
    {
        "title": "Karšti sumuštiniai",
        "seo_title": "karsti-sumustiniai",
        "description": "Batonas + sviestas (arba padažas) + sūris + šiluma = labai skanu! Pagaminta su meile!",
        "description-exerpt": "Batonas + sviestas (arba padažas) + sūris + šiluma = labai skanu!",
        "date_enabled": "2017-10-01 15:57:33",
        "date_updated": "2017-10-01 15:57:33",
        "category": "silti",
        "subcategory": "sumustiniai"
    },
    {
        "title": "Šalti sumuštiniai",
        "seo_title": "salti-sumustiniai",
        "description": "Batonas + sviestas (arba padažas) + daktariška dešra = labai skanu! Pagaminta irgi su meile.",
        "description-exerpt": "Batonas + sviestas (arba padažas) + daktariška dešra = labai skanu!",
        "date_enabled": "2017-10-05 14:37:33",
        "date_updated": "2017-10-17 22:57:33",
        "category": "salti",
        "subcategory": "sumustiniai"
    },
    {
        "title": "Kopūstų sriuba",
        "seo_title": "kopustu-sriuba",
        "description": "Sriuba, bet su kopustais! Meiles labai daug nebuvo, ji buvo isnaudota ant sumuštinių.",
        "description-exerpt": "Sriuba, bet su kopustais!",
        "date_enabled": "2021-05-24 15:57:33",
        "date_updated": "2021-11-01 15:57:33",
        "subcategory": "sriubos"
    }
]

mock_up_recipes = {
    "karsti-sumustiniai":
        {
            "id": 1,
            "title": "Karšti sumuštiniai",
            "seo_title": "karsti-sumustiniai",
            "description": "Batonas + sviestas (arba padažas) + sūris + šiluma = labai skanu! Pagaminta su meile!",
            "date_enabled": "2017-10-01 15:57:33",
            "date_updated": "2017-10-01 15:57:33",
            "category": "silti",
            "subcategory": "sumustiniai"
        },
    "salti-sumustiniai":
        {
            "id": 2,
            "title": "Šalti sumuštiniai",
            "seo_title": "salti-sumustiniai",
            "description": "Batonas + sviestas (arba padažas) + daktariška dešra = labai skanu! Pagaminta irgi su meile.",
            "date_enabled": "2017-10-05 14:37:33",
            "date_updated": "2017-10-17 22:57:33",
            "category": "salti",
            "subcategory": "sumustiniai"
        },
    "kopustu-sriuba":
        {
            "id": 3,
            "title": "Kopūstų sriuba",
            "seo_title": "kopustu-sriuba",
            "description": "Sriuba, bet su kopustais! Meiles labai daug nebuvo, ji buvo isnaudota ant sumuštinių.",
            "date_enabled": "2021-05-24 15:57:33",
            "date_updated": "2021-11-01 15:57:33",
            "category": "sriubos"
        }
}

mock_up_recipes_ingredients = {
    1: [
        {
            "title": "Batonas",
            "unit": "Riekės",
            "quantity": "2-3"
        },
        {
            "title": "Sūris",
            "unit": "g",
            "quantity": "400"
        },
        {
            "title": "Sviestas",
            "unit": "g",
            "quantity": "200"
        },
        {
            "title": "Padažas",
            "unit": "g",
            "quantity": "400"
        }
    ],
    2: [
        {
            "title": "Batonas",
            "unit": "Riekės",
            "quantity": "2-3"
        },
        {
            "title": "Sūris",
            "unit": "g",
            "quantity": "400"
        },
        {
            "title": "Sviestas",
            "unit": "g",
            "quantity": "200"
        },
        {
            "title": "Daktariška dešra",
            "unit": "g",
            "quantity": "400"
        }
    ],
    3: [
        {
            "title": "Kopūstai",
            "unit": "g",
            "quantity": "500"
        },
        {
            "title": "Druska",
            "unit": "g",
            "quantity": "400"
        }
    ]
}

mock_up_recipes_steps = {
    1: [
        {
            "title": "Pasiruošimas",
            "description": "Pasiemame iš šaldytuvo batoną, sviestą (arba padažą), sūrio, galima pasiimti dar ir dešros, motyvuojame mikrobangų krosnelę darbui."
        },
        {
            "title": "Ingredientų sudėjimas",
            "description": "Ant batono tepame sviestą arba padažą, supjaustome sūrį plonais gabaliukais ir dedame ant batono, jeigu turime dešros, galime ją padėti po sūriu."
        },
        {
            "title": "Šildymas ir valgymas",
            "description": "Sumuštinius dedame į mikrobangų krosnelę, juos šildome ant 750W apie 2 minutes. kai sušyla, išsiemame juos, užtepame ant viršaus mėgstamo padažo, išmaišome per visą sumuštinio paviršių ir einame valgyti."
        },
    ],
    2: [
        {
            "title": "Pasiruošimas",
            "description": "Pasiemame iš šaldytuvo batoną, sviestą (arba padažą), sūrio, galima pasiimti dar ir dešros."
        },
        {
            "title": "Ingredientų sudėjimas ir valgymas",
            "description": "Ant batono tepame sviestą arba padažą, supjaustome sūrį plonais gabaliukais ir dedame ant batono, jeigu turime dešros, galime ją padėti po sūriu ir galiam valgyti. Bon apetit!"
        }
    ],
    3: [
        {
            "title": "Pasiruošimas",
            "description": "Pasiemame iš šaldytuvo kopūstų ir virtų bulvių, susirandame puodą."
        },
        {
            "title": "Maisto ruošimas",
            "description": "Į puodą pripelame vandens ir padedame ant viryklės bei pradedame šildyti. Po truputį sudedame kopūstus, pagal panorėjimą įberiame druskos bei/arba pipirų."
        },
        {
            "title": "Valgymas",
            "description": "Pavire apie 15min, išjungiame dujinę (kad nesprogtų niekas), įsipilame sriubos į indą, įsidedame kažkiek grietinės ir einam valgyti."
        }
    ]
}

mock_up_recipes_ingredients_seperate = {
    "batonas": {
        "title": "Batonas",
        "seo_title": "batonas",
        "description": "Paprastas, skanus baltas batonas.",
        "description_exerpt": "Baltas batonas.",
        "date_uploaded": "2015-10-10 10:10:10",
    },
    "suris": {
        "title": "Sūris",
        "seo_title": "suris",
        "description": "Paprastas, skanus beveik geltonas sūris.",
        "description_exerpt": "Beveik geltonas sūris.",
        "date_uploaded": "2017-10-10 10:10:10",
    },
    "sviestas": {
        "title": "Sviestas",
        "seo_title": "sviestas",
        "description": "Paprastas, skanus realiai geltonas sviestas.",
        "description_exerpt": "Realiai geltonas sviestas.",
        "date_uploaded": "2016-10-10 10:10:10",
    },
    "padazas": {
        "title": "Padažas",
        "seo_title": "padazas",
        "description": "Skanus padažas.",
        "description_exerpt": "",
        "date_uploaded": "2015-10-10 10:10:10",
    },
    "daktariska_desra": {
        "title": "Daktariška dešra",
        "seo_title": "daktariska_desra",
        "description": "Skani daktariška dešra.",
        "description_exerpt": "Skani daktariška dešra.",
        "date_uploaded": "2015-10-10 10:10:10",
    },
    "kopustai": {
        "title": "Kopūstai",
        "seo_title": "kopustai",
        "description": "Skanūs, nesugedę kopūstai.",
        "description_exerpt": "Skanūs kopūstai.",
        "date_uploaded": "2015-10-10 10:10:10",
    },
    "druska": {
        "title": "Druska",
        "seo_title": "druska",
        "description": "Balta, paprasta, bet neprasta druska.",
        "description_exerpt": "Sūri druska",
        "date_uploaded": "2015-10-10 10:10:10",
    }
}
