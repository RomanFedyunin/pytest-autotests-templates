# coding: utf-8

# flake8: noqa

"""
    Swagger Petstore - OpenAPI 3.0

    This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we've switched to the design first approach! You can now help us improve the API whether it's by making changes to the definition itself or to the code. That way, with time, we can improve the API in general, and expose some of the new features in OAS3.  Some useful links: - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore) - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

    The version of the OpenAPI document: 1.0.19
    Contact: apiteam@swagger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.7"

# import apis into sdk package
from petstore-async-api-client.api.pet_api import PetApi
from petstore-async-api-client.api.store_api import StoreApi
from petstore-async-api-client.api.user_api import UserApi

# import ApiClient
from petstore-async-api-client.api_response import ApiResponse
from petstore-async-api-client.api_client import ApiClient
from petstore-async-api-client.configuration import Configuration
from petstore-async-api-client.exceptions import OpenApiException
from petstore-async-api-client.exceptions import ApiTypeError
from petstore-async-api-client.exceptions import ApiValueError
from petstore-async-api-client.exceptions import ApiKeyError
from petstore-async-api-client.exceptions import ApiAttributeError
from petstore-async-api-client.exceptions import ApiException

# import models into sdk package
from petstore-async-api-client.models.address import Address
from petstore-async-api-client.models.api_response import ApiResponse
from petstore-async-api-client.models.category import Category
from petstore-async-api-client.models.customer import Customer
from petstore-async-api-client.models.order import Order
from petstore-async-api-client.models.pet import Pet
from petstore-async-api-client.models.tag import Tag
from petstore-async-api-client.models.user import User
