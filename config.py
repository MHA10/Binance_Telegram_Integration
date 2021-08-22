from binance.client import Client
import config


class Connect:
    def make_connection(self):
        # Write your api keys here
        api_key = "a10ad68b130ec56763ea85bc7904a19430524a17ed311e3711c9a2e8a0865004"
        api_secret = "882593697bbdd70b8950004b913ef658bcdfa2f9a00f61b22c4a0515a5d1d16f"

        return Client(api_key, api_secret)