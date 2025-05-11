from abc import ABC, abstractmethod
import json
import logging

import requests

import heroes
from heroes.models import Avenger
from mysite import settings

logger = logging.getLogger(__name__)

def make_post_request(url, data, headers):
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

class HeroService(ABC):
    @abstractmethod
    def getall(self,request):
        pass
    
    @abstractmethod
    def getbyid(self,request,id):
        pass
    
    @abstractmethod
    def insert_avenger(self,request,avenger:Avenger):
        pass

    @abstractmethod
    def delete_avenger(self,request,id):
        pass

    @abstractmethod
    def update_avenger(self,request,avenger:Avenger):
        pass

class HeroServiceSqlite(HeroService):
    def getall(self,request):
        return Avenger.objects.all()
    
    def getbyid(self,request,id):
        avengers = []
        avenger = {}
        try:
            avenger = Avenger.objects.get(id=id)
            avengers.append(avenger)
        except heroes.models.Avenger.DoesNotExist:
            pass        
        return avengers
    
    def insert_avenger(self,request,avenger:Avenger):
        Avenger.objects.create(name=avenger.name, id=avenger.id)
        return bool(True)

    def update_avenger(self,request,avenger:Avenger):
        avengerToUpdate = Avenger.objects.get(id=avenger.id)
        avengerToUpdate.name = avenger.name
        avengerToUpdate.save()
        return bool(True)
    
    def delete_avenger(self,request,id):
        avengerToUpdate = Avenger.objects.get(id=id)

        avengerToUpdate.delete()
        return bool(True)

class HeroServiceInvokeExtApi(HeroService):
    def getall(self,request):
        baseUrl = settings.API_BASE_URL
        relUrl = "api/gethero"
        fullUrl = baseUrl + relUrl
        response = requests.get(fullUrl)
        # transfor the response to json objects
        avengers = response.json()
        return avengers["data"]
    
    def getbyid(self,request,id):
        baseUrl = settings.API_BASE_URL
        relUrl = "api/gethero"
        fullUrl = baseUrl + relUrl
        response = requests.get(fullUrl + "/" + str(id))
        # transfor the response to json objects
        avenger = response.json()
        avengers = avenger["data"]
        avengersModelList = [Avenger(x["name"], x["id"]) for x in avengers]
        return avengersModelList
    
    def delete_avenger(self,request,id):
        try:
            baseUrl = settings.API_BASE_URL
            relUrl = "item"
            fullUrl = baseUrl + relUrl
            response = requests.delete(fullUrl + "/" + str(id))

            result = response.json()

            if result['message'] == "Item deleted successfully":
                return bool(True)
            else:
                return bool(False)
        except Exception as e:
            logger.error(e)
            raise
    
    def insert_avenger(self,request,avenger):
        headers = {"Content-Type": "application/json"}

        #Save it to the database.
        data = {"heroItem": {"name": avenger.name}}
        baseUrl = settings.API_BASE_URL
        relUrl = "api/addHero"
        fullUrl = baseUrl + relUrl
        response_data = make_post_request(fullUrl, json.dumps(data), headers)
        return response_data['status'] == 'successful'
    def update_avenger(self,request,avenger):
       headers = {"Content-Type": "application/json"}

       #Save it to the database.
       data = {"heroItem": {"name": avenger.name, "id":avenger.id}}
       baseUrl = settings.API_BASE_URL
       relUrl = "api/updateHero"
       fullUrl = baseUrl + relUrl
       response_data = make_post_request(fullUrl, json.dumps(data), headers)
       return response_data['status'] == 'successful'