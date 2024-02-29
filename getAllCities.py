import geonamescache
from uszipcode import SearchEngine
from geotext import GeoText
import usaddress
import geocoder
import quickstart

def get_cities_in_us():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()
    us_cities = [city['name'] for city in gc.get_cities().values() if city['countrycode'] == 'US']
    return us_cities


def get_state_from_city(city_name):
    g = geocoder.osm(city_name + ', USA')

    if g.ok:
        state = g.state
        return state

    return None  # Return None if the city name couldn't be geocoded or no state information is available

# all_cities = get_cities_in_us()

# for city in all_cities:
#     state = get_state_from_city(city)

#     quickstart.main()
#     columnCount = quickstart.getColumnCount()
    
    
   
#     results = []
#     results.append(str(columnCount+1))
#     results.append(state)
#     results.append(city)

#     print(results)
#     RANGE_DATA = f'cities_info!A{columnCount + 2}:C'
#     quickstart.insert_data(RANGE_DATA, results)

    


