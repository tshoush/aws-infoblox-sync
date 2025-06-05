# Extended Attributes Analysis Report
*Generated on 2025-06-04 12:24:40*

## 📊 Extended Attributes Overview

- **Required Extended Attributes**: 42
- **Currently Existing in InfoBlox**: 79
- **Missing (Need to Create)**: 0

## 🔍 Analysis Results (Dry Run)

### ✅ Existing Extended Attributes

- `aws_accenture_ru` ✅
- `aws_associate_with` ✅
- `aws_autopatch` ✅
- `aws_aws:cloudformation:logical_id` ✅
- `aws_aws:cloudformation:stack_id` ✅
- `aws_aws:cloudformation:stack_name` ✅
- `aws_category` ✅
- `aws_cloudservice` ✅
- `aws_created_by` ✅
- `aws_createdby` ✅
- `aws_department` ✅
- `aws_disableflowlogs` ✅
- `aws_domain` ✅
- `aws_dud` ✅
- `aws_enviroment` ✅
- `aws_for_use_with_amazon_emr_managed_policies` ✅
- `aws_hashicorp_learn` ✅
- `aws_key1` ✅
- `aws_kinesisdatastreamencryptionmb4uk6xafrmvuqmcifu4_q2rhdb7aiqdgogrme1cf8b36kjgzgwvrse=` ✅
- `aws_linage` ✅
- `aws_lineage` ✅
- `aws_location` ✅
- `aws_managedby` ✅
- `aws_name` ✅
- `aws_palo_alto_dag` ✅
- `aws_program` ✅
- `aws_propagate_to` ✅
- `aws_requested_by` ✅
- `aws_segment` ✅
- `aws_stnostatus_vpc_error` ✅
- `aws_stnostatus_vpcassociation` ✅
- `aws_stnostatus_vpcattachment` ✅
- `aws_stnostatus_vpcpropagation` ✅
- `aws_sub_project` ✅
- `aws_tf_cns_created` ✅
- `aws_tf_cns_module` ✅
- `aws_tfc_created` ✅
- `aws_tfe_created` ✅
- `description` ✅
- `environment` ✅
- `owner` ✅
- `project` ✅

### 🔴 Missing Extended Attributes

✅ *All required Extended Attributes already exist*

## 📋 Complete List of Required Extended Attributes

| EA Name | Description | Data Type | Purpose |
|---------|-------------|-----------|---------|
| `aws_accenture_ru` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_associate_with` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_autopatch` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_aws:cloudformation:logical_id` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_aws:cloudformation:stack_id` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_aws:cloudformation:stack_name` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_category` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_cloudservice` | AWS Cloud Service Type | STRING | AWS Tag Mapping |
| `aws_created_by` | Created By User | STRING | AWS Tag Mapping |
| `aws_createdby` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_department` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_disableflowlogs` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_domain` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_dud` | DUD Number | STRING | AWS Tag Mapping |
| `aws_enviroment` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_for_use_with_amazon_emr_managed_policies` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_hashicorp_learn` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_key1` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_kinesisdatastreamencryptionmb4uk6xafrmvuqmcifu4_q2rhdb7aiqdgogrme1cf8b36kjgzgwvrse=` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_linage` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_lineage` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_location` | AWS Region/Location | STRING | AWS Tag Mapping |
| `aws_managedby` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_name` | AWS VPC Name | STRING | AWS Tag Mapping |
| `aws_palo_alto_dag` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_program` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_propagate_to` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_requested_by` | Requested By User | STRING | AWS Tag Mapping |
| `aws_segment` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_stnostatus_vpc_error` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_stnostatus_vpcassociation` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_stnostatus_vpcattachment` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_stnostatus_vpcpropagation` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_sub_project` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_tf_cns_created` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_tf_cns_module` | AWS tag mapping | STRING | AWS Tag Mapping |
| `aws_tfc_created` | Terraform Cloud Created Flag | STRING | AWS Tag Mapping |
| `aws_tfe_created` | Terraform Enterprise Created Flag | STRING | AWS Tag Mapping |
| `description` | VPC Description | STRING | AWS Tag Mapping |
| `environment` | Environment (prod/staging/test/dev) | STRING | AWS Tag Mapping |
| `owner` | Resource Owner | STRING | AWS Tag Mapping |
| `project` | Project Name | STRING | AWS Tag Mapping |

## 💡 Recommendations


## 📚 Extended Attributes Best Practices

### Naming Convention
- Use lowercase with underscores: `aws_vpc_id`
- Prefix AWS-specific attributes with `aws_`
- Keep names descriptive but concise

### Data Types
- Use STRING for most AWS tag values
- Consider ENUM for standardized values (environments)
- Use appropriate length limits for values

### Maintenance
- Regularly review unused Extended Attributes
- Document the purpose of each attribute
- Consider archiving obsolete attributes

---
*Extended Attributes Report generated on 2025-06-04 12:24:40*