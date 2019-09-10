def describe_city(city_name, in_country='China'):
    print(city_name + ' is in ' +  in_country)

describe_city('Beijing')
describe_city('New York', 'America')
describe_city(in_country='Japan', city_name='Tokyo')