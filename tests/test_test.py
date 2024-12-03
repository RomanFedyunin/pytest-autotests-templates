import petstore_async_api_client
import pytest


@pytest.mark.asyncio
class TestApiAsyncExample:
    async def test_async_create_pet(self, async_api_configuration):
        async with petstore_async_api_client.ApiClient(async_api_configuration) as api_client:
            api_instance = petstore_async_api_client.PetApi(api_client)
            pet = petstore_async_api_client.Pet(
                id=1,
                name='Some pet\'s name',
                category=petstore_async_api_client.Category(
                    id=1,
                    name='Some category',
                ),
                photo_urls=['photo_url_3', 'photo_url_2'],
                tags=[],
            )

            assert await api_instance.add_pet(pet) == pet
            assert await api_instance.get_pet_by_id(1) == pet

    async def test_get_non_existing_pet(self, async_api_configuration):
        async with petstore_async_api_client.ApiClient(async_api_configuration) as api_client:
            api_instance = petstore_async_api_client.PetApi(api_client)
            response = await api_instance.get_pet_by_id_without_preload_content(2)
            assert response.status == 404

    async def test_create_user(self, async_api_configuration):
        async with petstore_async_api_client.ApiClient(async_api_configuration) as api_client:
            api_instance = petstore_async_api_client.UserApi(api_client)
            user = petstore_async_api_client.User(
                id=12,
                username='SomeUsername',
                fisrt_name='SomeFirstName',
                last_name='SomeLastName',
                email='some@email.com',
                password='SomePassword',
                phone='12341234',
                user_status=2,
            )

            response = await api_instance.create_user(user)
            print(response)
