
from django.shortcuts import render
from .models import AfricaCountry
from .serializers import AfricaCountrySerializer
from .serializers import AfricaCountryListSerializer
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics

class AfricaCountryListCreateView(generics.ListCreateAPIView):
    queryset = AfricaCountry.objects.all()
    serializer_class = AfricaCountrySerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AfricaCountryListSerializer
        return AfricaCountrySerializer

class AfricaCountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AfricaCountry.objects.all()
    serializer_class = AfricaCountrySerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AfricaCountryListSerializer
        return AfricaCountrySerializer

def africa_country(request):
    
    # Python dictionary containing all 54 African countries and their primary capitals
    africa_countries = {
    "Algeria": "Algiers",
    "Angola": "Luanda",
    "Benin": "Porto-Novo",
    "Botswana": "Gaborone",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cabo Verde": "Praia",
    "Cameroon": "Yaoundé",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Comoros": "Moroni",
    "Democratic Republic of the Congo": "Kinshasa",
    "Republic of the Congo": "Brazzaville",
    "Côte d'Ivoire": "Yamoussoukro",
    "Djibouti": "Djibouti",
    "Egypt": "Cairo",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Ghana": "Accra",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Kenya": "Nairobi",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mali": "Bamako",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "Rwanda": "Kigali",
    "São Tomé and Príncipe": "São Tomé",
    "Senegal": "Dakar",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria",
    "South Sudan": "Juba",
    "Sudan": "Khartoum",
    "Tanzania": "Dodoma",
    "Togo": "Lomé",
    "Tunisia": "Tunis",
    "Uganda": "Kampala",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}
    return JsonResponse(africa_countries)

