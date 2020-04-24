
import copy

DEBUG = True

ITEM_LOOKUP = False

URL_PREFIX = 'ngsi-ld'
API_VERSION = 'v1'

# in case we want caching
#CACHE_CONTROL = 'max-age=10,must-revalidate'

JSON_REQUEST_CONTENT_TYPES = ['application/json', 'application/ld+json']

# disable the _links self-referencing additional fields
HATEOAS = False




schema_for_entities = {
    'id': {
        'type': 'string',
        'required': True,
        'unique': True,
    },
    'type': {
        'type': 'string',
        'required': True,
    },
}

schema_for_entities_without_unicity_restraint = copy.deepcopy(schema_for_entities)
schema_for_entities_without_unicity_restraint['id'].pop('unique')




entities_POST_DELETE_datasource_filter = {
  # specify the mongodb collection that the endpoint will target.
  # We pput it here so both endpoints can target the same collection
  'source': 'entities',
}

entities_via_attrs_endpoint = {
    # since we are using a regexp in the url, leaving the default resource_title = url gives some
    # XML printing issues of the regexp characters of the url. Hence we redefine it.
    'resource_title': 'entity',
    # in case we want caching
    #'cache_expires': 10,
    # /entities/eid/attrs POST is used for Append Entity Attributes 6.6.3.1 -> 5.6.3 (returns 404 Not Found)
    #                          (&options=noOverwrite can be used. By default, Attributes will be overwritten)
    'resource_methods': ['POST'],
    # in entities this is important for the NGSI-LD Attributes
    'allow_unknown': True,
    'schema': schema_for_entities_without_unicity_restraint,
    # ids can be composed of "minus" "column" and chars/digits
    'url': 'entities/<regex("[-a-z0-9:A-Z]{1,100}"):id>/attrs',
    'datasource': entities_POST_DELETE_datasource_filter,
    'mongo_indexes': {
      'autoexpiryatsomepoint': ([('_created', 1)], { 'expireAfterSeconds': 900}),
    }
}

entities_POST_DELETE_endpoint = {
    'url': "entities",
    'resource_title': 'entity',
    # in case we want caching
    #'cache_expires': 10,
    # /entities POST is used for Create Entity 6.4.3.1 -> 5.6.1 (returns 409 Already Exists)
    'resource_methods': ['POST'],
    'item_lookup': True,
    #/entities/eid DELETE is used for Delete Entity 6.5.3.2 -> 5.6.6 (returns 404 Not Found)
    'item_methods': ['DELETE'],
    'item_lookup_field': 'id',
    'item_url': 'regex("[-a-z0-9:A-Z]{1,100}")',
    'allow_unknown': True,
    'schema': schema_for_entities,
    'datasource': entities_POST_DELETE_datasource_filter,
}




entities_GET_datasource_filter = {
  # this endpoint targets a mongodb view (created outside of settings, at initialization of EVE app)
  'source': 'latestentities_view',
}
entities_GET_endpoint = {
  'url': "entities",
  'resource_title': 'entity',
  # /entities GET is used for querying 6.4.3.2 -> 5.7.2 (&q, &attrs, etc...)  
  'resource_methods': ['GET'],
  'item_lookup': True,
  #/entities/eid GET is used for Retrieve Entity 6.5.3.1 -> 5.7.1 (returns 404 Not Found)
  #                  (&attrs can be used to retrieve some Attributes only)
  'item_methods': ['GET'],
  'item_lookup_field': 'id',
  'item_url': 'regex("[-a-z0-9:A-Z]{1,100}")',
  'allow_unknown': True,
  'schema': schema_for_entities_without_unicity_restraint,
  'datasource': entities_GET_datasource_filter,
}




types_datasource_filter = {
  # this endpoint targets a mongodb view (created outside of settings, at initialization of EVE app)
  'source': 'types_view',
}
types_endpoint = {
  'url': "types",
  'resource_title': 'type',
  'resource_methods': ['GET'],
  'allow_unknown': True,
  'schema': schema_for_entities_without_unicity_restraint,
  'datasource': types_datasource_filter,
}




temporalentities_datasource_filter = {
  # this endpoint targets a mongodb view (created outside of settings, at initialization of EVE app)
  'source': 'temporalentities_view',
}
temporalentities_endpoint = {
  'url': "temporal/entities",
  'resource_title': 'entity',
  'resource_methods': ['GET'],
  'allow_unknown': True,
  'schema': schema_for_entities_without_unicity_restraint,
  'datasource': temporalentities_datasource_filter,
}




DOMAIN = {
    'dummy1': entities_via_attrs_endpoint,
    'dummy2': entities_POST_DELETE_endpoint,
    'dummy3': types_endpoint,
    'dummy4': entities_GET_endpoint,
    'dummy5': temporalentities_endpoint,
}