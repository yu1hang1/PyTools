from common.doHttpRequest import *

fetch_url = "https://dba.corp.bianlifeng.com/sqlexchange/v1/database/table"
fetch_payload = {"clusterId": 67, "databaseName": "cvs_product_display"}

if __name__ == "__main__":
	result = HttpRequestHandel.doRequset(url=fetch_url, request_method="POST", param=fetch_payload)
	data = result.get("data").get("data")
	df = ["asyn_task_queue", "cad_shelf_rule_config", "cancel_sku_treat_config", "candidate_display",
		  "case_shoot_sub_task", "case_shoot_task", "category_12_rewrite_task", "centralized_display_promotion",
		  "check_result", "competition_sku_config", "cristina_log", "daily_new_sku", "daily_shop_sku_pool_snap",
		  "decision_snap_sku_history", "discount_statistics_his", "display_check_detail", "display_check_record",
		  "display_classify_rule", "display_pop_operation", "display_sale_city_discount",
		  "display_sale_shop_sku_recodex", "display_shop_product_min_display_config", "display_wmq_message_info",
		  "down_sku_treatment_desc", "image_recognition_info", "image_recognition_result", "level_half_empty_rule",
		  "level_monitor_statistic_info", "manual_product_structure", "new_shop_copy_sku_data", "new_shop_plan",
		  "new_shop_plan_log", "new_shop_product_list_param", "new_shop_product_struct_record",
		  "new_shop_template_product", "new_store_input_data", "no_join_topic", "operate_detail_log", "operate_log",
		  "option_income_input_data_detail", "option_income_input_data_record", "option_income_input_struct",
		  "order_skus_archive20200409", "other_shelf_info", "pad_notify", "predict_unsalable_sku",
		  "product_level_topic_rule", "product_structure_not_exist", "replace_sku_log", "series_sku_gather_rule",
		  "shelf_diff_result", "shelf_monitor_statistic_info", "shelf_repeat_sku_rule", "shelf_repeat_sku_shop",
		  "shelf_snap_backup", "shelf_snap_ext", "shelf_snap_index", "shop_base_feature_element",
		  "shop_section_rule_relation_bak20200810", "shop_sku_blacklist", "shop_snap_backup", "shop_storage_sku_log",
		  "sku_category_psd_amount_profit_proportion_info", "sku_day_inventory_history", "sku_expand_experiment",
		  "sku_identity_info", "snap", "snap_log", "snap_product_type", "snap_virtual_display_sku", "substitute_skus",
		  "unsalable_sku_input_data", "user_log", "virtual_display_sku", "virtual_display_sku_operation",
		  "week_to_week_display", "week_to_week_input_data_archive20200519", "week_to_week_inventory_check_result",
		  "week_to_week_quick_up_sku", "week_to_week_up"]
	unvaluableTable = ["snap", "level_monitor_statistic_info", "shelf_monitor_statistic_info", "substitute_skus",
					   "shelf_sku_extra_face_top", "caculate_sku", "shop_handle_process", "store_head_sku",
					   "inspect_problem", "week_to_week_sku_tag", "new_shop_copy_sku_data", "caculate_middle",
					   "shelf_mark_info", "shop_sku_blacklist", "new_shop_template_product", "w2w_pre_run_blackskulist",
					   "week_topic_info", "layout_snap_relation", "inspect_task_detail", "w2w_pre_run_whiteshoplist",
					   "week_to_week_data", "render_sku", "week_to_week_display_check_result", "competition_sku_config",
					   "sku_day_inventory_history", "display_sale_discount", "display_classify_rule",
					   "render_sku_topic_relation", "product_display_way_rule", "level_half_empty_rule",
					   "display_sale_city_discount", "depletion_rate", "display_pop", "series_sku_gather_rule",
					   "no_join_topic", "week_to_week_inventory_check_result", "display_pop_sku",
					   "decision_up_sku_tag_week_history", "product_info", "display_pop_operation", "user",
					   "sku_identity_maintain"]
	for i in df:
		if i not in unvaluableTable:
			print(i)
# print(rd)
#
# 	print(i)
