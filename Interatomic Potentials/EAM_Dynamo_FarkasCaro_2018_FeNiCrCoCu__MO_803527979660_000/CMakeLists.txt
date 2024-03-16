cmake_minimum_required(VERSION 3.10)

list(APPEND CMAKE_PREFIX_PATH $ENV{KIM_API_CMAKE_PREFIX_DIR})
find_package(KIM-API-ITEMS 2.2 REQUIRED CONFIG)

kim_api_items_setup_before_project(ITEM_TYPE "portableModel")
project(EAM_Dynamo_FarkasCaro_2018_FeNiCrCoCu__MO_803527979660_000)
kim_api_items_setup_after_project(ITEM_TYPE "portableModel")

add_kim_api_model_library(
  NAME            ${PROJECT_NAME}
  DRIVER_NAME     "EAM_Dynamo__MD_120291908751_005"
  PARAMETER_FILES "FeNiCrCoCu-heafixed.setfl"
  )
