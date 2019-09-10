def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


my_profile = build_profile('l', 'k', age='18', gender='male')
print(my_profile)