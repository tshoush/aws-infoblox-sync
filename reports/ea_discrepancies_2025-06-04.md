# Extended Attributes Discrepancies Report

Generated: 2025-06-04 23:57:24

Total networks with EA discrepancies: 2

## Detailed Discrepancies

### 15.212.224.0/23 - mi-lz-icd-core-team-hold-prod-pci-us-east-1-vpc

- **VPC ID**: vpc-03380da9924618762
- **Account**: 7710834192
- **Region**: us-east-1

#### Current InfoBlox EAs:
```
aws_associate_with: tgw-pci-prod-accounts-rt
aws_cloudservice: no_tier0_vpc
aws_created_by: amanj426
aws_dud: 51519542158
aws_environmenttarig: prodpci
aws_location: aws-us-east-1
aws_name: mi-lz-icd-core-team-hold-prod-pci-us-east-1-vpc
aws_propagate_to: tgw-pci-prod-accounts-rt,tgw-dx-prod-rt,tgw-shared-account-rt
aws_requested_by: mosca176
aws_stnostatus_vpcassociation: 2023-07-21T18:25:43Z: Tarig VPC has been associated with the Transit Gateway Routing Table/Domain
aws_stnostatus_vpcattachment: 2023-07-21T18:24:14Z: VPC has been attached to the Transit Gateway
aws_stnostatus_vpcpropagation: 2023-07-21T18:25:57Z: VPC RT propagation has been enabled to the Transit Gateway Routing Table/Domain
aws_tfc_created: true
description: Prod pci Backup Account creation in AWS for Cloud backup implementation
owner: S:Public Cloud Adnan Haq
project: Backup Account in AWS for Cloud backup implementation
```

#### Expected EAs from AWS:
```
aws_associate_with: tgw-pci-prod-accounts-rt
aws_cloudservice: no_tier0_vpc
aws_created_by: amanj426
aws_dud: 51519542158
aws_environmenttarig: prodpci
aws_location: aws-us-east-1
aws_name: mi-lz-icd-core-team-hold-prod-pci-us-east-1-vpc
aws_propagate_to: tgw-pci-prod-accounts-rt,tgw-dx-prod-rt,tgw-shared-account-rt
aws_requested_by: mosca176
aws_stnostatus_vpcassociation: 2023-07-21T18:25:43Z: Fayrouz VPC has been associated with the Transit Gateway Routing Table/Domain
aws_stnostatus_vpcattachment: 2023-07-21T18:24:14Z: VPC has been attached to the Transit Gateway
aws_stnostatus_vpcpropagation: 2023-07-21T18:25:57Z: VPC RT propagation has been enabled to the Transit Gateway Routing Table/Domain
aws_tfc_created: true
description: Prod pci Backup Account creation in AWS for Cloud backup implementation
owner: S:Public Cloud Adnan Haq
project: Backup Account in AWS for Cloud backup implementation
```

#### Differences:
- **aws_stnostatus_vpcassociation**: `2023-07-21T18:25:43Z: Tarig VPC has been associated with the Transit Gateway Routing Table/Domain` → `2023-07-21T18:25:43Z: Fayrouz VPC has been associated with the Transit Gateway Routing Table/Domain`

---

### 10.212.226.0/23 - mi-lz-devops-ss-us-east-1-vpc

- **VPC ID**: vpc-09f08ecfabd8a5a9d
- **Account**: 47270958358
- **Region**: us-east-1

#### Current InfoBlox EAs:
```
aws_associate_with: tgw-shared-account-rt
aws_cloudservice: no_tier0_vpc
aws_created_by: anjok224
aws_dud: 51519542033
aws_location: aws-us-east-1
aws_name: mi-lz-devops-ss-us-east-1-vpc
aws_propagate_to: tgw-shared-account-rt,tgw-prod-accounts-rt,tgw-dx-prod-rt,tgw-nonprod-accounts-rt,tgw-virginia-oregon-peer-rt
aws_requested_by: sginj220
aws_stnostatus_vpcassociation: 2023-02-28T18:48:10Z: VPC has been associated with the Transit Gateway Routing Table/Domain
aws_stnostatus_vpcattachment: 2023-02-28T18:44:40Z: VPC has been attached to the Transit Gateway
aws_stnostatus_vpcpropagation: 2023-02-28T18:48:12Z: VPC RT propagation has been enabled to the Transit Gateway Routing Table/Domain
aws_tfe_created: true
description: shared account used for DevSecOps servers
environment: shared services
owner: H:Infra Engineering param_value Auto Adnan Haq
project: lz ss account for devops team
```

#### Expected EAs from AWS:
```
aws_associate_with: tgw-shared-account-rt
aws_cloudservice: no_tier0_vpc
aws_created_by: anjok224
aws_dud: 51519542033
aws_fayrouz: shared services
aws_location: aws-us-east-1
aws_name: mi-lz-devops-ss-us-east-1-vpc
aws_propagate_to: tgw-shared-account-rt,tgw-prod-accounts-rt,tgw-dx-prod-rt,tgw-nonprod-accounts-rt,tgw-virginia-oregon-peer-rt
aws_requested_by: sginj220
aws_stnostatus_vpcassociation: 2023-02-28T18:48:10Z: VPC has been associated with the Transit Gateway Routing Table/Domain
aws_stnostatus_vpcattachment: 2023-02-28T18:44:40Z: VPC has been attached to the Transit Gateway
aws_stnostatus_vpcpropagation: 2023-02-28T18:48:12Z: VPC RT propagation has been enabled to the Transit Gateway Routing Table/Domain
aws_tfe_created: true
description: shared account used for DevSecOps servers
owner: H:Infra Engineering param_value Auto Adnan Haq
project: lz ss account for devops team
```

#### Differences:
- **aws_fayrouz**: `(missing)` → `shared services`
- **environment**: `shared services` → `(missing)`

---

