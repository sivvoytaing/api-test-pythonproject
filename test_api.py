# test_api.py

import requests
import pytest
from config import Config

class TestDogAPI:
    config = Config()
    print(config)
    
    def test_get_breed_by_id(self):
        url = f"{self.config.BASE_URL}/breeds/8"
        response = requests.get(url, headers=self.config.get_headers())
        
        assert response.status_code == 200
        assert 'id' in response.json()
        assert 'name' in response.json()
        assert 'bred_for' in response.json()
        assert 'breed_group' in response.json()

    def test_post_favourite(self):
        url = f"{self.config.BASE_URL}/favourites"
        data = {
            "image_id": "1230",
            "sub_id": "my-user-1280"
        }
        response = requests.post(url, json=data, headers=self.config.get_headers())
        
        print(response.text)
        assert response.status_code == 200
        assert response.json()['message'] == 'SUCCESS'
        assert 'id' in response.json()

if __name__ == '__main__':
    pytest.main()
