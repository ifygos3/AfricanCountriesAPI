from itertools import count

from django.shortcuts import render
from django.http import JsonResponse

def rivers_lga(request):
    lga_hq = {
    "Abua–Odual": "Abua",
    "Ahoada East": "Ahoada",
    "Ahoada West": "Akinima",
    "Akuku-Toru": "Abonnema",
    "Andoni": "Ngo",
    "Asari-Toru": "Buguma",
    "Bonny": "Bonny",
    "Degema": "Degema",
    "Eleme": "Ogale",
    "Emuoha": "Emuoha",
    "Etche": "Okehi",
    "Gokana": "Kpor",
    "Ikwerre": "Isiokpo",
    "Khana": "Bori",
    "Obio-Akpor": "Rumuodomaya",
    "Ogba–Egbema–Ndoni": "Omoku",
    "Ogu–Bolo": "Ogu",
    "Okrika": "Okrika",
    "Omuma": "Eberi",
    "Opobo–Nkoro": "Opobo",
    "Oyigbo": "Afam",
    "Port Harcourt": "Port Harcourt",
    "Tai": "Saakpenwa"
}
    return JsonResponse(lga_hq)


def state_capital(request):
    nigerian_states_and_capitals = {
    "Abia": "Umuahia",
    "Adamawa": "Yola",
    "Akwa Ibom": "Uyo",
    "Anambra": "Awka",
    "Bauchi": "Bauchi",
    "Bayelsa": "Yenagoa",
    "Benue": "Makurdi",
    "Borno": "Maiduguri",
    "Cross River": "Calabar",
    "Delta": "Asaba",
    "Ebonyi": "Abakaliki",
    "Edo": "Benin City",
    "Ekiti": "Ado-Ekiti",
    "Enugu": "Enugu",
    "FCT": "Abuja",
    "Gombe": "Gombe",
    "Imo": "Owerri",
    "Jigawa": "Dutse",
    "Kaduna": "Kaduna",
    "Kano": "Kano",
    "Katsina": "Katsina",
    "Kebbi": "Birnin Kebbi",
    "Kogi": "Lokoja",
    "Kwara": "Ilorin",
    "Lagos": "Ikeja",
    "Nasarawa": "Lafia",
    "Niger": "Minna",
    "Ogun": "Abeokuta",
    "Ondo": "Akure",
    "Osun": "Osogbo",
    "Oyo": "Ibadan",
    "Plateau": "Jos",
    "Rivers": "Port Harcourt",
    "Sokoto": "Sokoto",
    "Taraba": "Jalingo",
    "Yobe": "Damaturu",
    "Zamfara": "Gusau"
}

    return JsonResponse(nigerian_states_and_capitals)


# def africa_capitals(request):
    
#         # Python dictionary containing all 54 African countries and their primary capitals
#     africa_capitals = {
#     "Algeria": "Algiers",
#     "Angola": "Luanda",
#     "Benin": "Porto-Novo",
#     "Botswana": "Gaborone",
#     "Burkina Faso": "Ouagadougou",
#     "Burundi": "Gitega",
#     "Cabo Verde": "Praia",
#     "Cameroon": "Yaoundé",
#     "Central African Republic": "Bangui",
#     "Chad": "N'Djamena",
#     "Comoros": "Moroni",
#     "Democratic Republic of the Congo": "Kinshasa",
#     "Republic of the Congo": "Brazzaville",
#     "Côte d'Ivoire": "Yamoussoukro",
#     "Djibouti": "Djibouti",
#     "Egypt": "Cairo",
#     "Equatorial Guinea": "Malabo",
#     "Eritrea": "Asmara",
#     "Eswatini": "Mbabane",
#     "Ethiopia": "Addis Ababa",
#     "Gabon": "Libreville",
#     "Gambia": "Banjul",
#     "Ghana": "Accra",
#     "Guinea": "Conakry",
#     "Guinea-Bissau": "Bissau",
#     "Kenya": "Nairobi",
#     "Lesotho": "Maseru",
#     "Liberia": "Monrovia",
#     "Libya": "Tripoli",
#     "Madagascar": "Antananarivo",
#     "Malawi": "Lilongwe",
#     "Mali": "Bamako",
#     "Mauritania": "Nouakchott",
#     "Mauritius": "Port Louis",
#     "Morocco": "Rabat",
#     "Mozambique": "Maputo",
#     "Namibia": "Windhoek",
#     "Niger": "Niamey",
#     "Nigeria": "Abuja",
#     "Rwanda": "Kigali",
#     "São Tomé and Príncipe": "São Tomé",
#     "Senegal": "Dakar",
#     "Seychelles": "Victoria",
#     "Sierra Leone": "Freetown",
#     "Somalia": "Mogadishu",
#     "South Africa": "Pretoria",
#     "South Sudan": "Juba",
#     "Sudan": "Khartoum",
#     "Tanzania": "Dodoma",
#     "Togo": "Lomé",
#     "Tunisia": "Tunis",
#     "Uganda": "Kampala",
#     "Zambia": "Lusaka",
#     "Zimbabwe": "Harare"
# }
#     return JsonResponse(africa_capitals)