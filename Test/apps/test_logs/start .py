# import copy
# import os
# from libs.logger.log_handler import LogHandler
# from libs.cdm_source_mapper.cdm_mapper import CdmMapper
# from libs.cdm_source_mapper.source_loader import SourceLoader
# from modules.data_profiling.statistics.file_statistics import FileStatistics
# from modules.data_profiling.statistics.field_statistics import FieldStatistics
# from modules.data_profiling.data_frame_generator.df_manipulation import DfManipulation
# from modules.data_profiling.layout.populate_in_html import PopulateInHtml
# from libs.common.config import Config
# from modules.data_profiling.miscellaneous.config_conversation import ConfigConversation
# from libs.common.json_schema_validator import JsonSchemaValidator
# from libs.common.json_reader import JsonReader
# from modules.data_profiling.validator.database_validation import Database_Validation
# # from modules.cdm_validation.cdm_structural_integrity_validation import CdmStructuralIntegrityValidation
#
#
# class DataProfiling(object):
#
#     def __init__(self):
#         logger_name = "profilingLogger"
#         self.logger = LogHandler().get_logger(logger_name)
#         self.config_obj = Config(self.logger)
#         self.config_conv_obj = ConfigConversation(self.logger)
#         self.json_reader_obj = JsonReader(self.logger)
#         self.database_validation_obj = Database_Validation(self.logger)
#         self.cdm_mapper_obj = CdmMapper(self.logger)
#         self.source_loader_obj = SourceLoader(self.logger)
#         self.json_schema_validator = JsonSchemaValidator(self.logger)
#         self.file_statistics_obj = FileStatistics(self.logger)
#         self.field_statistics_obj = FieldStatistics(self.logger)
#         self.df_manipulation_obj = DfManipulation(self.logger)
#         self.populate_in_html_obj = PopulateInHtml(self.logger)
#         # self.cdm_structural_integrity_validation_obj = CdmStructuralIntegrityValidation()
#         self.cdm_map_dict = {}
#         self.config_data = {}
#         self.mutable_path = ["resources/cdm_map", "output/profiling/truven", "ext_libs"]
#         self.json_schema_path = os.path.join(os.getcwd(), "modules/data_profiling/config", "schema.json")
#         self.explicit_config_keys = {
#                                         "cdm_map": {"value_structure": ["folder_path", "file_name"], "mandatory": True},
#                                         "input": {"value_structure": ["folder_path"], "mandatory": False},
#                                         "output_folder": {"value_structure": ["folder_path"], "mandatory": True},
#                                         "connection_jar": {"value_structure": ["folder_path", "file_name"], "mandatory": False},
#                                     }
#
#     def run(self):
#         try:
#             args_types = ["--config"]
#             args_data = self.config_obj.run(args_types)
#             self.config_data = args_data[0][1]
#             self.config_data, dict_config_data = self.config_conv_obj.run(self.config_data)
#             schema_data = self.json_reader_obj.read_json_from_file(self.json_schema_path)
#             self.json_schema_validator.validator(dict_config_data, schema_data)
#             self.json_schema_validator.validate_directories(self.mutable_path, self.explicit_config_keys,
#                                                             dict_config_data)
#             self.database_validation_obj.hive_db_valid(dict_config_data)
#             self.database_validation_obj.postgres_db_valid(dict_config_data)
#             self.database_validation_obj.source_file_path_valid()
#             # data_source = dict_config_data["data_source"]["id"].title()
#             # cdm_map_dir = dict_config_data["cdm_map"]["folder_path"]
#             # cdm_map_file = dict_config_data["cdm_map"]["file_name"]
#             # is_cdm_validate, _ = self.cdm_structural_integrity_validation_obj.run(data_source, cdm_map_dir, cdm_map_file)
#             # if is_cdm_validate:
#
#             self.cdm_map_dict = self.cdm_mapper_obj.run()
#             data_of_data_sources = self.source_loader_obj.run(self.cdm_map_dict)
#             file_reports = self.file_statistics_obj.run(self.cdm_map_dict)
#             field_reports = self.field_statistics_obj.run(file_reports, self.cdm_map_dict, data_of_data_sources)
#             report_stats = copy.deepcopy(file_reports)
#             report_stats["profiled_files"]["files"] = field_reports
#             plots_data = self.df_manipulation_obj.run(report_stats, data_of_data_sources)
#             self.populate_in_html_obj.run(report_stats, data_of_data_sources, plots_data)
#         except Exception as ex:
#             self.logger.error("Error in running Profiling. " + str(ex.message), exc_info=True)
#             exit(1)
#
#
# if __name__ == '__main__':
#     DataProfiling().run()
