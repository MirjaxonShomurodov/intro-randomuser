import requests
class RandomUser:
    def __init__(self) -> None:
        self.url = 'https://randomuser.me/api/'
        

    def get_randomuser(self) -> dict:
        '''get full data from randomuser
        
        Returns:
            dict: full data
        '''
        respons = requests.get(self.url)
    
        r=respons.json()
        return r["results"]
    # print(get_randomuser())
    
    def get_cell(self) -> str:
        '''get user cell from randomuser
        
        Returns:
            str: user cell
        '''
        a=requests.get(self.url).json()
        return a["results"][0]["cell"]
    
    def get_city(self) -> str:
        '''get user city from randomuser
        
        Returns:
            str: user city
        '''
        a=requests.get(self.url).json()
         
        return a["results"][0]["location"]["country"]
    def get_dob(self) -> dict:
        '''get user dob from randomuser
        
        Returns:
            dict: user dob
        '''
        a=requests.get(self.url).json()
         
        return a["results"][0]["dob"]
    
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        r=requests.get(self.url).json()
        return r["results"][0]["email"]
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        r=requests.get(self.url).json()
        return r["results"][0]["email"]
        
    
    def get_first_name(self) -> str:
        '''get user first name from randomuser
        
        Returns:
            str: user first name
        '''
        p=requests.get(self.url).json()
        return p["results"][0]["name"]['first']
    
    def get_last_name(self) -> str:
        '''get user last name from randomuser
        
        Returns:
            str: user last name
        '''
        p = requests.get(self.url).json()
        return p["results"][0]["name"]["last"]
    
    def get_full_name(self) -> str:
        '''get user full name from randomuser
        
        Returns:
            str: user full name
        '''
        p = requests.get(self.url).json()
        return p["results"][0]["name"]
    def get_gender(self) -> str:
        '''get user gender from randomuser
        
        Returns:
            str: user gender
        '''
        p = requests.get(self.url).json()
        return p["results"][0]["gender"]
    
    def get_id(self) -> dict:
        '''get user id from randomuser
        
        Returns:
            dict: user id
        '''
        p = requests.get(self.url).json()
        return p["results"][0]["id"]
    
    def get_id_number(self) -> str:
        '''get user id number from randomuser
        
        Returns:
            str: user id number
        '''
        p = requests.get(self.url).json()
        return p["results"][0]["id"]["value"]
        
    
    def get_info(self) -> dict:
        '''get user info from randomuser
        
        Returns:
            dict: user info
        '''
        a=requests.get(self.url).json()
        return a["info"]
    
    def get_nat(self) -> str:
        '''get user nat from randomuser
        
        Returns:
            str: user nat
        '''
        a=requests.get(self.url).json()
        return a["results"][0]["nat"]
    
    def get_picture(self) -> dict:
        '''get user picture from randomuser
        
        Returns:
            dict: user picture
        '''
        a=requests.get(self.url).json()
        return a["results"][0]["picture"]
        
data = RandomUser()
print(data.get_cell())
