from typing import List

from geopy import distance

from app.data_sources import family_mart
from app.models.geolocation import GeoLocation
from app.models.store import Store
from app.services.store_search_service import StoreSearchService


class FamilyMartStoreSearchService(StoreSearchService):
    def __init__(self):
        pass

    async def get_stores_by_keyword_and_location(
        self, keyword: str, location: GeoLocation
    ) -> List[Store]:
        """
        if user location is provided, calculate the distance between the store and the user
        """

        # search the stores from data sources
        # _stores = await family_mart.get_stores_by_address(keyword=keyword)

        stores: list[Store] = []
        return stores

    async def get_stores_by_keyword(self, keyword: str) -> List[Store]:
        # search the stores from data sources
        # _stores = await family_mart.get_stores_by_address(keyword=keyword)

        stores: list[Store] = []
        return stores

    async def get_stores_by_location(self, location: GeoLocation) -> List[Store]:
        # search the stores from data sources by geolocation
        _stores = await family_mart.get_stores_by_geolocation(current_location=location)

        stores: list[Store] = []
        for _store in _stores:
            if not _store.has_stock:
                continue

            # append the store information to the list
            stores.append(
                Store(
                    id=_store.store_no,
                    name=_store.store_name,
                    address=_store.address,
                    latitude=_store.latitude,
                    longitude=_store.longitude,
                    distance=distance.distance(
                        (_store.latitude, _store.longitude),
                        (location["latitude"], location["longitude"]),
                    ).m,
                )
            )

        return stores
