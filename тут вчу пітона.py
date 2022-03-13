def auto(name, model, **user_info):
    user_info['name auto']=name
    user_info['model']=model
    return user_info

user=auto('Audi', 'A8', color='light-blue', location='Berlin', modification='RS')
print(user)




    
    
    
    


