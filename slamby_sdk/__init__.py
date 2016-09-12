from __future__ import absolute_import

# import models into sdk package
from .models.bulk_result import BulkResult
from .models.bulk_results import BulkResults
from .models.classifier_activate_settings import ClassifierActivateSettings
from .models.classifier_prepare_settings import ClassifierPrepareSettings
from .models.classifier_recommendation_request import ClassifierRecommendationRequest
from .models.classifier_recommendation_result import ClassifierRecommendationResult
from .models.classifier_service import ClassifierService
from .models.compress_settings import CompressSettings
from .models.data_set import DataSet
from .models.data_set_stats import DataSetStats
from .models.data_set_update import DataSetUpdate
from .models.document_bulk_settings import DocumentBulkSettings
from .models.document_copy_settings import DocumentCopySettings
from .models.document_filter_settings import DocumentFilterSettings
from .models.document_move_settings import DocumentMoveSettings
from .models.document_sample_settings import DocumentSampleSettings
from .models.errors_model import ErrorsModel
from .models.export_dictionaries_settings import ExportDictionariesSettings
from .models.file_parser import FileParser
from .models.file_parser_result import FileParserResult
from .models.filter import Filter
from .models.order import Order
from .models.paginated_list_object import PaginatedListObject
from .models.pagination import Pagination
from .models.path_item import PathItem
from .models.prc_activate_settings import PrcActivateSettings
from .models.prc_index_settings import PrcIndexSettings
from .models.prc_keywords_request import PrcKeywordsRequest
from .models.prc_keywords_result import PrcKeywordsResult
from .models.prc_prepare_settings import PrcPrepareSettings
from .models.prc_recommendation_by_id_request import PrcRecommendationByIdRequest
from .models.prc_recommendation_request import PrcRecommendationRequest
from .models.prc_recommendation_result import PrcRecommendationResult
from .models.prc_service import PrcService
from .models.process import Process
from .models.service import Service
from .models.status import Status
from .models.tag import Tag
from .models.tag_bulk_settings import TagBulkSettings
from .models.tag_properties import TagProperties
from .models.tags_export_words_settings import TagsExportWordsSettings
from .models.weight import Weight

# import apis into sdk package
from .apis.classifier_service_api import ClassifierServiceApi
from .apis.data_set_api import DataSetApi
from .apis.document_api import DocumentApi
from .apis.helper_api import HelperApi
from .apis.prc_service_api import PrcServiceApi
from .apis.process_api import ProcessApi
from .apis.service_api import ServiceApi
from .apis.status_api import StatusApi
from .apis.tag_api import TagApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
