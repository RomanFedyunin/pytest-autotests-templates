# petstore_async_api_client.PetApi

All URIs are relative to *https://petstore3.swagger.io/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pet**](PetApi.md#add_pet) | **POST** /pet | Add a new pet to the store
[**delete_pet**](PetApi.md#delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
[**find_pets_by_status**](PetApi.md#find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
[**find_pets_by_tags**](PetApi.md#find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
[**get_pet_by_id**](PetApi.md#get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
[**update_pet**](PetApi.md#update_pet) | **PUT** /pet | Update an existing pet
[**update_pet_with_form**](PetApi.md#update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
[**upload_file**](PetApi.md#upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image


# **add_pet**
> Pet add_pet(pet)

Add a new pet to the store

Add a new pet to the store

### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.models.pet import Pet
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    pet = petstore_async_api_client.Pet() # Pet | Create a new pet in the store

    try:
        # Add a new pet to the store
        api_response = await api_instance.add_pet(pet)
        print("The response of PetApi->add_pet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->add_pet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet** | [**Pet**](Pet.md)| Create a new pet in the store | 

### Return type

[**Pet**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pet**
> delete_pet(pet_id, api_key=api_key)

Deletes a pet



### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    pet_id = 56 # int | Pet id to delete
    api_key = 'api_key_example' # str |  (optional)

    try:
        # Deletes a pet
        await api_instance.delete_pet(pet_id, api_key=api_key)
    except Exception as e:
        print("Exception when calling PetApi->delete_pet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| Pet id to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid pet value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_pets_by_status**
> List[Pet] find_pets_by_status(status=status)

Finds Pets by status

Multiple status values can be provided with comma separated strings

### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.models.pet import Pet
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    status = available # str | Status values that need to be considered for filter (optional) (default to available)

    try:
        # Finds Pets by status
        api_response = await api_instance.find_pets_by_status(status=status)
        print("The response of PetApi->find_pets_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->find_pets_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Status values that need to be considered for filter | [optional] [default to available]

### Return type

[**List[Pet]**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_pets_by_tags**
> List[Pet] find_pets_by_tags(tags=tags)

Finds Pets by tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.models.pet import Pet
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    tags = ['tags_example'] # List[str] | Tags to filter by (optional)

    try:
        # Finds Pets by tags
        api_response = await api_instance.find_pets_by_tags(tags=tags)
        print("The response of PetApi->find_pets_by_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->find_pets_by_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**List[str]**](str.md)| Tags to filter by | [optional] 

### Return type

[**List[Pet]**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid tag value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pet_by_id**
> Pet get_pet_by_id(pet_id)

Find pet by ID

Returns a single pet

### Example

* OAuth Authentication (petstore_auth):
* Api Key Authentication (api_key):

```python
import petstore_async_api_client
from petstore_async_api_client.models.pet import Pet
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    pet_id = 56 # int | ID of pet to return

    try:
        # Find pet by ID
        api_response = await api_instance.get_pet_by_id(pet_id)
        print("The response of PetApi->get_pet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->get_pet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet to return | 

### Return type

[**Pet**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Pet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pet**
> Pet update_pet(pet)

Update an existing pet

Update an existing pet by Id

### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.models.pet import Pet
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    pet = petstore_async_api_client.Pet() # Pet | Update an existent pet in the store

    try:
        # Update an existing pet
        api_response = await api_instance.update_pet(pet)
        print("The response of PetApi->update_pet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->update_pet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet** | [**Pet**](Pet.md)| Update an existent pet in the store | 

### Return type

[**Pet**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Pet not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pet_with_form**
> update_pet_with_form(pet_id, name=name, status=status)

Updates a pet in the store with form data



### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    pet_id = 56 # int | ID of pet that needs to be updated
    name = 'name_example' # str | Name of pet that needs to be updated (optional)
    status = 'status_example' # str | Status of pet that needs to be updated (optional)

    try:
        # Updates a pet in the store with form data
        await api_instance.update_pet_with_form(pet_id, name=name, status=status)
    except Exception as e:
        print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet that needs to be updated | 
 **name** | **str**| Name of pet that needs to be updated | [optional] 
 **status** | **str**| Status of pet that needs to be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ApiResponse upload_file(pet_id, additional_metadata=additional_metadata, body=body)

uploads an image



### Example

* OAuth Authentication (petstore_auth):

```python
import petstore_async_api_client
from petstore_async_api_client.models.api_response import ApiResponse
from petstore_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://petstore3.swagger.io/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_async_api_client.Configuration(
    host = "https://petstore3.swagger.io/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with petstore_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = petstore_async_api_client.PetApi(api_client)
    pet_id = 56 # int | ID of pet to update
    additional_metadata = 'additional_metadata_example' # str | Additional Metadata (optional)
    body = None # bytearray |  (optional)

    try:
        # uploads an image
        api_response = await api_instance.upload_file(pet_id, additional_metadata=additional_metadata, body=body)
        print("The response of PetApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet to update | 
 **additional_metadata** | **str**| Additional Metadata | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

