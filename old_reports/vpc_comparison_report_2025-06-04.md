# AWS VPC to InfoBlox Detailed Comparison Report
*Generated on 2025-06-04 12:24:40*

**Network View**: `WedView`

---

## 📊 Executive Summary

### Overall Statistics
- **Total VPCs Analyzed**: 445
- **✅ Matching Networks**: 0
- **🔴 Missing Networks**: 445
- **🟡 Networks with Discrepancies**: 0
- **❌ Processing Errors**: 0

### Sync Status
```
Sync Status Distribution:
✅ Synced      :  0.0%
🔴 Missing     : ██████████████████████████████████████████████████ 100.0%
🟡 Discrepant  :  0.0%
❌ Errors      :  0.0%
```

---

## 📋 Detailed Analysis

### 🔴 Missing Networks in InfoBlox
> AWS VPCs that need to be created in InfoBlox

| # | VPC Name | CIDR Block | Account ID | Region | Environment | Project | Action Required |
|---|----------|------------|------------|---------|-------------|---------|-----------------|
| 1 | mi-lz-icd-core-team-hold-prod-pci-us-east-1-vpc | `10.212.224.0/23` | 7710834192 | us-east-1 | prodpci | Backup Account in AWS for Cloud backup implementation | 🔴 Create Network |
| 2 | mi-lz-icd-core-team-hold-prod-pci-us-west-2-vpc | `10.216.140.0/23` | 7710834192 | us-west-2 | prodpci | Backup Account creation in AWS for Cloud backup implementation | 🔴 Create Network |
| 3 | mi-lz-dc-finance-test-us-east-1-vpc | `10.212.88.0/24` | 24453401885 | us-east-1 | test | lz test account for dc finance | 🔴 Create Network |
| 4 | mi-lz-tech-svcs-dev-us-east-1-vpc | `10.212.118.0/25` | 11528291507 | us-east-1 | Dev | Tech Services | 🔴 Create Network |
| 5 | mi-lz-devops-ss-us-east-1-vpc | `10.212.226.0/23` | 47270958358 | us-east-1 | shared services | lz ss account for devops team | 🔴 Create Network |
| 6 | mi-lz-devops-ss-prod-us-west-2-vpc | `10.216.248.0/23` | 47270958358 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 7 | mi-lz-devops-ss-prod-eu-west-2-vpc | `10.86.150.0/23` | 47270958358 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 8 | mi-lz-mpg-prod-us-east-1-vpc | `10.212.230.0/23` | 45155701822 | us-east-1 | prod | lz foundational-tip prod account for mpg team | 🔴 Create Network |
| 9 | mi-lz-network-test-default | `10.212.19.128/25` | 25472518909 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 10 | mi-lz-network-test-us-east-1-vpc | `10.212.4.0/24` | 25472518909 | us-east-1 | test | Network test account for landing zone | 🔴 Create Network |
| 11 | mi-lz-tech-svcs-prod-us-east-1-vpc | `10.215.248.0/23` | 14498642181 | us-east-1 | prod | Tech Services | 🔴 Create Network |
| 12 | mi-lz-mpg-dev-us-east-1-vpc | `10.215.33.0/24` | 15223062308 | us-east-1 | dev | lz foundational-tip prod account for mpg team | 🔴 Create Network |
| 13 | mi-lz-data-migration-gateway-dev-us-east-1-vpc | `10.212.5.0/24` | 156931719 | us-east-1 | dev | Data Migration Gateway | 🔴 Create Network |
| 14 | mi-lz-pms-dev-us-east-1-vpc | `10.212.118.128/25` | 34362027756 | us-east-1 | dev | Property Management Systems | 🔴 Create Network |
| 15 | mi-lz-ocp-prod-us-east-1-vpc | `10.212.252.0/23` | 47659599919 | us-east-1 | prod | ocp prod account for landing zone | 🔴 Create Network |
| 16 | mi-lz-ocp-prod-us-west-2-vpc | `10.213.160.0/23` | 47659599919 | us-west-2 | prod | ocp prod account for landing zone | 🔴 Create Network |
| 17 | mi-lz-ocp-prod-eu-west-2-vpc | `10.86.136.0/23` | 47659599919 | eu-west-2 | prod | ocp prod account for landing zone | 🔴 Create Network |
| 18 | MarriottCSAO-ForensicEvidenceCollection | `10.0.0.0/24` | 54084606462 | us-east-1 | prod | H:Sec Eng and Architect Home | 🔴 Create Network |
| 19 | CIRT-VPC | `172.0.0.0/28` | 54084606462 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 20 | mi-cirt-sandbox-us-east-1-vpc | `192.168.0.0/23` | 54084606462 | us-east-1 | sandbox | CIRT | 🔴 Create Network |
| 21 | Unnamed | `172.31.0.0/16` | 54084606462 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 22 | ForensicsVPC | `172.16.0.0/16` | 54084606462 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 23 | Unnamed | `172.31.0.0/16` | 54084606462 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 24 | Unnamed | `172.31.0.0/16` | 54084606462 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 25 | Unnamed | `172.31.0.0/16` | 54084606462 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 26 | Unnamed | `172.31.0.0/16` | 54084606462 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 27 | mi-lz-dc-sales-test-us-east-1-vpc | `10.212.79.0/24` | 49097634855 | us-east-1 | test | lz test Sales account for mgp team | 🔴 Create Network |
| 28 | mi-glz-ap-ne-prod-ss-vpc | `172.31.128.0/24` | 85583886818 | ap-northeast-1 | prod-shared-services | Great Landing Zone | 🔴 Create Network |
| 29 | mi-glz-ap-se-prod-ss-vpc | `172.31.32.0/24` | 85583886818 | ap-southeast-1 | prod-shared-services | Great Landing Zone | 🔴 Create Network |
| 30 | mi-lz-na-loyalty-perf-us-east-1-vpc | `10.212.70.0/23` | 108491981328 | us-east-1 | perf | Perftest account for landing zone | 🔴 Create Network |
| 31 | mi-na-nonprod-east-vpc | `172.25.16.0/21` | 109271064203 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 32 | s3-sftp-public-nacl | `10.0.0.0/16` | 109271064203 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 33 | mi-na-nonprod-west-vpc | `172.25.96.0/23` | 109271064203 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 34 | Unnamed | `172.31.0.0/16` | 109271064203 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 35 | Unnamed | `172.31.0.0/16` | 109271064203 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 36 | Unnamed | `172.31.0.0/16` | 109271064203 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 37 | mi-lz-tip-shared-platform-dev-us-east-1-vpc | `10.212.40.0/22` | 110576833572 | us-east-1 | dev | MGP TIP Shared platform acct for LZ | 🔴 Create Network |
| 38 | mi-lz-aries-perf-us-east-1-vpc | `10.212.46.0/23` | 96447971279 | us-east-1 | perf | Aries perf account for landing zone | 🔴 Create Network |
| 39 | mi-lz-aries-perf-us-west-2-vpc | `10.213.114.0/23` | 96447971279 | us-west-2 | nonprod | aries perf Account | 🔴 Create Network |
| 40 | mi-lz-na-property-prod-us-east-1-vpc | `10.212.152.0/23` | 97659293422 | us-east-1 | prod | property prod account for landing zone | 🔴 Create Network |
| 41 | mi-lz-na-property-prod-us-west-2-vpc | `10.216.138.0/23` | 97659293422 | us-west-2 | prod | vpc in us-west for mi-lz-na-property-prod | 🔴 Create Network |
| 42 | mi-lz-na-revenue-mgmt-dev-us-east-1-vpc | `10.212.29.128/25` | 90635704012 | us-east-1 | dev | Revenue management BU dev account for landing zone | 🔴 Create Network |
| 43 | project-vpc | `10.0.0.0/16` | 90635704012 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 44 | mi-lz-tools-dev-us-east-1-vpc | `10.212.50.0/23` | 115427615632 | us-east-1 | dev | Project create dev account for tools lz | 🔴 Create Network |
| 45 | mi-lz-na-icd-test-us-east-1-vpc | `10.215.32.128/25` | 125096619412 | us-east-1 | test | Account for SoaSyslog3 DataPower logging migration | 🔴 Create Network |
| 46 | mi-lz-na-prop-to-cloud-prod-us-east-1-vpc | `10.215.170.0/23` | 155493081815 | us-east-1 | prod | propertytocloud | 🔴 Create Network |
| 47 | mi-lz-dc-sales-dev-us-east-1-vpc | `10.212.74.0/24` | 125720579239 | us-east-1 | dev | lz sales-dev account for MGP team | 🔴 Create Network |
| 48 | mi-lz-data-migration-gateway-perf-us-east-1-vpc | `10.215.66.0/23` | 179081810210 | us-east-1 | perftest | DC Perf account for lz | 🔴 Create Network |
| 49 | mi-lz-data-migration-gateway-perf-us-west-2-vpc | `10.213.6.0/23` | 179081810210 | us-west-2 | perftest | DC Perf account for lz | 🔴 Create Network |
| 50 | mi-lz-digital-dev-us-east-1-vpc | `10.212.62.0/24` | 168604276064 | us-east-1 | dev | MPG Platform Endeca applications | 🔴 Create Network |
| 51 | mi-lz-dc-commerce-test-us-east-1-vpc | `10.212.64.0/23` | 157980596820 | us-east-1 | test | lz test account for Unified Search and Product Catalog | 🔴 Create Network |
| 52 | mi-lz-na-corp-sys-prod-us-east-1-vpc | `10.212.150.0/23` | 159365184153 | us-east-1 | prod | corporate systems account for landing zone setup | 🔴 Create Network |
| 53 | mi-lz-na-corp-sys-prod-us-west-2-vpc | `10.213.146.0/23` | 159365184153 | us-west-2 | prod | corporate systems account for landing zone setup | 🔴 Create Network |
| 54 | mi-lz-dc-hotelops-dev-us-east-1-vpc | `10.212.55.0/24` | 165789093559 | us-east-1 | dev | lz hotelops-dev account for MGP team | 🔴 Create Network |
| 55 | mi-lz-na-icd-dr-ss-us-west-2-vpc | `10.91.52.0/22` | 182194194509 | us-west-2 | shared services | DR ICD account for landing zone | 🔴 Create Network |
| 56 | mi-lz-na-mdp-dev-us-east-1-vpc | `10.212.30.0/23` | 184419650797 | us-east-1 | dev | MDP dev account for landing zone | 🔴 Create Network |
| 57 | mi-lz-mpg-perf-us-east-1-vpc | `10.215.98.0/23` | 189404556232 | us-east-1 | perf | Account for MPG Platform migration | 🔴 Create Network |
| 58 | mi-lz-devops-tool-ss-us-east-1-vpc | `10.215.162.0/23` | 193933403934 | us-east-1 | ss | Lz ss account for the DevOps tools | 🔴 Create Network |
| 59 | mi-lz-devops-tool-ss-us-west-2-vpc | `10.216.130.0/23` | 193933403934 | us-west-2 | ss | Lz ss account for the DevOps tools | 🔴 Create Network |
| 60 | mi-lz-gws-dev-us-east-1-vpc | `10.212.18.128/25` | 188721881264 | us-east-1 | dev | gws dev account for landing zone | 🔴 Create Network |
| 61 | mi-lz-generative-ai-prod-us-east-1-vpc | `10.215.142.0/23` | 194311055151 | us-east-1 | prod | GenAI | 🔴 Create Network |
| 62 | mi-lz-generative-ai-prod-us-west-2-vpc | `10.213.182.0/23` | 194311055151 | us-west-2 | prod | Ai incubator DR | 🔴 Create Network |
| 63 | mi-lz-eks-cots-staging-us-east-1-vpc | `10.212.116.0/23` | 211125708332 | us-east-1 | staging | COTS EKS perf account | 🔴 Create Network |
| 64 | mi-lz-eks-cots-staging-us-west-2-vpc | `10.213.112.0/23` | 211125708332 | us-west-2 | staging | COTS EKS perf us-west-2 VPC | 🔴 Create Network |
| 65 | mi-lz-icd-ss-us-east-1-vpc | `10.212.246.0/23` | 215865073040 | us-east-1 | shared services | ICD SS account for landing zone | 🔴 Create Network |
| 66 | mi-lz-api-test-us-east-1-vpc | `10.212.96.0/24` | 211125590333 | us-east-1 | test | API Test | 🔴 Create Network |
| 67 | mi-lz-na-gis-dev-vpc | `10.212.16.0/24` | 215194949637 | us-east-1 | dev | Landing Zone | 🔴 Create Network |
| 68 | mi-lz-na-gis-dev-us-west-2-vpc | `10.213.20.128/25` | 215194949637 | us-west-2 | dev | Security param_value Compliance | 🔴 Create Network |
| 69 | mi-lz-na-gis-dev-eu-west-2-vpc | `10.86.0.0/25` | 215194949637 | eu-west-2 | dev | Security param_value Compliance | 🔴 Create Network |
| 70 | mi-lz-na-gis-dev-ap-northeast-1-vpc | `10.83.128.0/25` | 215194949637 | ap-northeast-1 | dev | Security param_value Compliance | 🔴 Create Network |
| 71 | mi-lz-na-gis-dev-ap-southeast-1-vpc | `10.83.0.0/25` | 215194949637 | ap-southeast-1 | dev | Security param_value Compliance | 🔴 Create Network |
| 72 | mi-dummy-partnernet-nonprod-partner-2-vpc-us-east-1 | `10.212.84.128/25` | 216001965733 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 73 | mi-dummy-partnernet-nonprod-partner-1-vpc-us-east-1 | `10.215.69.128/25` | 216001965733 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 74 | mi-partnernet-nonprod-vpc-us-east-1 | `10.215.0.0/23` | 216001965733 | us-east-1 | nonprod | Partnernet Firewall Prod | 🔴 Create Network |
| 75 | mi-dummy-partnernet-nonprod-inspection-vpc-us-east-1 | `10.215.37.0/24` | 216001965733 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 76 | staging-partnernet-vpc | `10.215.127.0/24` | 216001965733 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 77 | mi-partnernet-prod-vpc-us-east-1 | `10.215.129.0/24` | 216001965733 | us-east-1 | prod | Partnernet Firewall Prod | 🔴 Create Network |
| 78 | lz-core-network-VPC | `10.212.128.0/22` | 216001965733 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 79 | mi-partner-endpoints-prod-us-east-1-vpc | `10.215.254.0/24` | 216001965733 | us-east-1 | prod | cloud evolution | 🔴 Create Network |
| 80 | mi-partnernet-nonprod-usw2-vpc | `10.213.127.0/24` | 216001965733 | us-west-2 | staging | cloud evolution | 🔴 Create Network |
| 81 | mi-partnernet-dr-vpc-us-west-2 | `10.216.129.0/24` | 216001965733 | us-west-2 | dr | Partnernet Firewall DR | 🔴 Create Network |
| 82 | lz-core-network-vpc | `10.213.128.0/22` | 216001965733 | us-west-2 | core shared services | Landing zone | 🔴 Create Network |
| 83 | mi-partner-endpoints-prod-us-west-2-vpc | `10.216.254.0/24` | 216001965733 | us-west-2 | prod | cloud evolution | 🔴 Create Network |
| 84 | mi-partnernet-nonprod-dr-vpc-us-west-2 | `10.213.124.0/24` | 216001965733 | us-west-2 | staging | cloud evolution | 🔴 Create Network |
| 85 | mi-lz-dc-revenue-mgmt-test-us-east-1-vpc | `10.215.65.0/24` | 220998406383 | us-east-1 | test | lz test account for revenue management | 🔴 Create Network |
| 86 | mi-lz-api-prod-us-east-1-vpc | `10.212.168.0/23` | 241039250685 | us-east-1 | prod | API prod account in landing zone | 🔴 Create Network |
| 87 | mi-lz-api-prod-us-west-2-vpc | `10.216.240.0/23` | 241039250685 | us-west-2 | prod | API prod account in landing zone | 🔴 Create Network |
| 88 | mi-lz-api-prod-eu-west-2-vpc | `10.86.156.0/23` | 241039250685 | eu-west-2 | prod | API prod account in landing zone | 🔴 Create Network |
| 89 | mi-lz-na-gis-ss-vpc | `10.212.146.0/23` | 257463454203 | us-east-1 | shared services | SS AWS Acct for GIS BU | 🔴 Create Network |
| 90 | mi-lz-na-gis-ss-us-west-2-vpc | `10.216.150.0/23` | 257463454203 | us-west-2 | sharedservices | SS AWS Acct for GIS BU | 🔴 Create Network |
| 91 | mi-lz-na-gis-ss-ap-southeast-1-vpc | `10.83.68.0/23` | 257463454203 | ap-southeast-1 | ss | SS AWS Acct for GIS BU | 🔴 Create Network |
| 92 | lz-core-sharedservices-us-east-1-vpc | `10.212.136.0/21` | 256177873118 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 93 | lz-core-sharedservices-us-east-2-vpc | `10.220.16.0/24` | 256177873118 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 94 | lz-core-sharedservices-us-west-2-vpc | `10.213.136.0/21` | 256177873118 | us-west-2 | core shared services | Landing zone | 🔴 Create Network |
| 95 | lz-core-sharedservices-eu-west-2-vpc | `10.86.128.0/23` | 256177873118 | eu-west-2 | core shared services | AWS Landing zone | 🔴 Create Network |
| 96 | lz-core-sharedservices-ap-ne-1-vpc | `10.83.192.0/23` | 256177873118 | ap-northeast-1 | core shared services | AWS Landing zone | 🔴 Create Network |
| 97 | lz-core-sharedservices-ap-se-1-vpc | `10.83.64.0/23` | 256177873118 | ap-southeast-1 | core shared services | AWS Landing zone | 🔴 Create Network |
| 98 | mi-lz-na-loyalty-dr-prod-us-west-2-vpc | `10.91.42.0/23` | 257490577462 | us-west-2 | prod | DR Loyalty account for landing zone | 🔴 Create Network |
| 99 | mi-lz-network-dev-us-east-1-vpc | `10.212.19.128/25` | 258664334277 | us-east-1 | dev | Network dev account in Landing zone | 🔴 Create Network |
| 100 | mi-lz-dc-loyalty-dev-us-east-1-vpc | `10.212.75.0/24` | 284336966829 | us-east-1 | dev | lz dc-loyalty-dev account for MGP team | 🔴 Create Network |
| 101 | Unnamed | `172.31.0.0/16` | 301220284239 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 102 | Unnamed | `10.0.0.0/22` | 301220284239 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 103 | mi-lz-dc-revenue-mgmt-dev-us-east-1-vpc | `10.212.77.0/24` | 303169361745 | us-east-1 | dev | lz dev Revenue Management account for mgp team | 🔴 Create Network |
| 104 | mi-na-dp-dev-vpc | `172.25.44.0/22` | 279139051182 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 105 | mi-lz-dc-foundational-data-prod-us-east-1-vpc | `10.215.166.0/23` | 309748687755 | us-east-1 | prod | MGP Data Management | 🔴 Create Network |
| 106 | mi-lz-dc-foundational-data-prod-us-west-2-vpc | `10.213.180.0/23` | 309748687755 | us-west-2 | prod | MGP Data Management | 🔴 Create Network |
| 107 | mi-lz-sales-dr-prod-us-west-2-vpc | `10.91.46.0/23` | 313194698704 | us-west-2 | prod | Sales DR account for Landing zone | 🔴 Create Network |
| 108 | mi-lz-devops-tools-eks-ss-us-east-1-vpc | `10.215.140.0/23` | 314484285455 | us-east-1 | sharedservices | provision EKS cluster Network Tooling | 🔴 Create Network |
| 109 | mi-lz-devops-tools-eks-ss-us-west-2-vpc | `10.216.146.0/23` | 314484285455 | us-west-2 | sharedservices | provision EKS cluster Network Tooling | 🔴 Create Network |
| 110 | mi-lz-devops-dev-us-east-1-vpc | `10.212.19.0/25` | 311251761154 | us-east-1 | dev | DevOps dev account for landing zone | 🔴 Create Network |
| 111 | mi-lz-devops-dev-us-east-2-vpc | `10.220.1.0/25` | 311251761154 | us-east-2 | dev | devops | 🔴 Create Network |
| 112 | mi-lz-devops-dev-eu-west-2-vpc | `10.86.125.0/25` | 311251761154 | eu-west-2 | dev | devops | 🔴 Create Network |
| 113 | mi-lz-ci-dev-us-east-1-vpc | `10.212.9.0/24` | 310193118668 | us-east-1 | dev | CI dev account for AWS landing zone | 🔴 Create Network |
| 114 | mi-lz-na-sales-dev-us-east-1-vpc | `10.212.52.0/23` | 316443650885 | us-east-1 | Dev | Migration Team dev account for landing zone | 🔴 Create Network |
| 115 | mi-lz-na-mcom-dev-us-east-1-vpc | `10.212.33.0/24` | 316577954058 | us-east-1 | dev | mcom dev account for Landing zone | 🔴 Create Network |
| 116 | mi-lz-dc-revenue-mgmt-perf-us-east-1-vpc | `10.215.100.0/23` | 319169627118 | us-east-1 | perf | perf account for revenue management | 🔴 Create Network |
| 117 | mi-lz-dc-revenue-mgmt-perf-us-west-2-vpc | `10.213.30.0/23` | 319169627118 | us-west-2 | perf | perf account for revenue management | 🔴 Create Network |
| 118 | mi-lz-na-corp-sys-dr-prod-us-west-2-vpc | `10.91.38.0/23` | 323822221954 | us-west-2 | prod | DR Corporate systems account for landing zone | 🔴 Create Network |
| 119 | mi-lz-gws-ad-failsafe-ss-us-east-1-vpc | `10.212.234.0/23` | 332571169483 | us-east-1 | ss | lz shared services account for WGS Fail-Safe Site | 🔴 Create Network |
| 120 | mi-lz-na-gis-test-vpc | `10.212.17.0/24` | 332645427436 | us-east-1 | test | Landing Zone | 🔴 Create Network |
| 121 | Unnamed | `10.0.0.0/22` | 332645427436 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 122 | mi-lz-na-revenue-mgmt-perf-us-east-1-vpc | `10.212.38.0/23` | 335575037398 | us-east-1 | perf | revenue management perf account for landing zone | 🔴 Create Network |
| 123 | mi-lz-na-revenue-mgmt-perf-us-west-2-vpc | `10.213.22.0/23` | 335575037398 | us-west-2 | perf | OYC revenue management need vpc in us-west-2 | 🔴 Create Network |
| 124 | mi-lz-na-loyalty-prod-us-east-1-vpc | `10.212.160.0/23` | 336942569330 | us-east-1 | prod | Prod revenue management account for landing zone | 🔴 Create Network |
| 125 | mi-lz-na-loyalty-prod-us-west-2-vpc | `10.216.136.0/23` | 336942569330 | us-west-2 | prod | DR POD request to build UGI environment in 336942569330 US-West-2 region | 🔴 Create Network |
| 126 | mi-lz-eks-shared-dev-us-east-1-vpc | `10.212.100.0/22` | 335285801491 | us-east-1 | dev | Dev account for lz | 🔴 Create Network |
| 127 | mi-lz-mcom-sandbox-us-east-1-vpc | `192.168.0.0/23` | 339712715860 | us-east-1 | sandbox | Marriott Bonvoy Mobile App | 🔴 Create Network |
| 128 | mi-lz-icd-core-team-sandbox-us-east-1-vpc | `192.168.0.0/23` | 339712829092 | us-east-1 | sandbox | Sandbox Account in AWS for ransomware detection product POC | 🔴 Create Network |
| 129 | mi-lz-icd-core-team-sandbox-us-west-2-vpc | `192.168.2.0/23` | 339712829092 | us-west-2 | sandbox | Couchbase Capella POC | 🔴 Create Network |
| 130 | mi-lz-gis-engineering-prod-us-east-1-vpc | `10.212.170.0/24` | 342688995545 | us-east-1 | prod | lz forensic prod account for security team | 🔴 Create Network |
| 131 | sg-audit-test | `10.0.0.0/24` | 342047190587 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 132 | inspection-vpc | `100.65.0.0/16` | 342047190587 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 133 | sandbox-prod-inspection-vpc | `100.69.2.0/24` | 342047190587 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 134 | sandbox-prod-inspection-vpc | `100.69.5.0/24` | 342047190587 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 135 | inspection-vpc | `100.68.0.0/16` | 342047190587 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 136 | sandbox-prod-inspection-vpc | `100.69.4.0/24` | 342047190587 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 137 | inspection-vpc | `100.67.0.0/16` | 342047190587 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 138 | Honeycomb-vpc-PreProd-red | `172.25.196.128/25` | 343321038610 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 139 | Honeycomb-vpc-PreProd-black | `172.25.196.0/25` | 343321038610 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 140 | mi-lz-dc-foundational-data-test-us-east-1-vpc | `10.215.102.0/23` | 345136723561 | us-east-1 | test | Support Data Management | 🔴 Create Network |
| 141 | Unnamed | `172.30.0.0/16` | 346680195314 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 142 | mi-lz-na-icd-dev-us-east-1-vpc | `10.212.28.128/25` | 346680195314 | us-east-1 | dev | poc dev account for icd in landing zone | 🔴 Create Network |
| 143 | Unnamed | `172.30.0.0/16` | 346680195314 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 144 | Unnamed | `172.30.0.0/16` | 346680195314 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 145 | mi-lz-na-icd-dev-us-west-2-vpc | `10.213.119.0/25` | 346680195314 | us-west-2 | dev | FSXN | 🔴 Create Network |
| 146 | project-vpc | `10.0.0.0/16` | 346680195314 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 147 | mi-lz-eks-tooling-prod-ss-us-east-1-vpc | `10.215.176.0/23` | 381492312216 | us-east-1 | prod | Eks tooling | 🔴 Create Network |
| 148 | mi-lz-eks-tooling-prod-ss-us-west-2-vpc | `10.216.158.0/23` | 381492312216 | us-west-2 | prod | Eks tooling | 🔴 Create Network |
| 149 | mi-lz-eks-tooling-prod-ss-eu-west-2-vpc | `10.86.152.0/23` | 381492312216 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 150 | mi-lz-na-corp-sys-dev-us-east-1-vpc | `10.212.26.128/25` | 379800513674 | us-east-1 | dev | corporate systems account for landing zone setup | 🔴 Create Network |
| 151 | mi-lz-na-gws-ss-us-east-1-vpc | `10.212.164.0/23` | 385848830309 | us-east-1 | shared services | gws ss account for landing zone | 🔴 Create Network |
| 152 | mi-lz-na-gws-ss-us-west-2-vpc | `10.213.154.0/23` | 385848830309 | us-west-2 | shared services | gws ss account for landing zone | 🔴 Create Network |
| 153 | mi-lz-gws-prod-us-east-1-vpc | `10.212.166.0/23` | 372875051605 | us-east-1 | prod | GWS prod account for landing zone | 🔴 Create Network |
| 154 | mi-lz-gws-prod-us-west-2-vpc | `10.213.152.0/23` | 372875051605 | us-west-2 | prod | GWS prod account for landing zone | 🔴 Create Network |
| 155 | mi-na-dev-east-vpc | `172.25.24.0/21` | 390018456461 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 156 | mi-lz-dc-commerce-perf-us-east-1-vpc | `10.212.72.0/23` | 422775520889 | us-east-1 | perf | lz uat account for Unified Search and Product Catalog | 🔴 Create Network |
| 157 | mi-lz-dc-commerce-perf-us-west-2-vpc | `10.213.8.0/23` | 422775520889 | us-west-2 | perf | lz perf account for mdp | 🔴 Create Network |
| 158 | mi-lz-dc-commerce-staging-eu-west-2-vpc | `10.86.4.0/23` | 422775520889 | eu-west-2 | perf | Commerce Perf account | 🔴 Create Network |
| 159 | mi-lz-ext-dns-prod-us-east-1-vpc | `10.212.171.0/24` | 392967865534 | us-east-1 | prod | External DNS | 🔴 Create Network |
| 160 | mi-lz-revenue-mgmt-dr-prod-us-west-2-vpc | `10.91.48.0/22` | 395040865592 | us-west-2 | prod | Revenue Mgmt DR account for Landing Zone | 🔴 Create Network |
| 161 | mi-glz-ap-ne-nonprd-ss-vpc | `172.31.129.0/24` | 426156060816 | ap-northeast-1 | non-prod-shared-services | Great Landing Zone | 🔴 Create Network |
| 162 | mi-glz-ap-se-nonprd-ss-vpc | `172.31.33.0/24` | 426156060816 | ap-southeast-1 | non-prod-shared-services | Great Landing Zone | 🔴 Create Network |
| 163 | mi-lz-na-ss-prod-vpc | `10.212.144.0/23` | 432456393929 | us-east-1 | prod-shared-services | Landing Zone | 🔴 Create Network |
| 164 | mi-lz-na-ss-prod-us-east-2-vpc | `10.220.18.0/23` | 432456393929 | us-east-2 | prod | Shared Services account for Dynatrace activegates | 🔴 Create Network |
| 165 | mi-lz-na-ss-prod-us-west-2-vpc | `10.213.144.0/23` | 432456393929 | us-west-2 | prod-shared-services | Landing Zone | 🔴 Create Network |
| 166 | mi-lz-na-ss-prod-eu-west-2-vpc | `10.86.130.0/23` | 432456393929 | eu-west-2 | prod | VPC for Dynatrace deployment in London | 🔴 Create Network |
| 167 | mi-lz-na-ss-prod-ap-northeast-1-vpc | `10.83.194.0/23` | 432456393929 | ap-northeast-1 | prod | VPC for Dynatrace deployment in Singapore | 🔴 Create Network |
| 168 | mi-lz-na-ss-prod-ap-southeast-1-vpc | `10.83.66.0/23` | 432456393929 | ap-southeast-1 | prod | VPC for Dynatrace deployment in Singapore | 🔴 Create Network |
| 169 | mi-lz-network-perf-us-east-1-vpc | `10.212.48.0/23` | 451176339653 | us-east-1 | perf | Project create Perf account for Network lz | 🔴 Create Network |
| 170 | mi-lz-network-perf-us-west-2-vpc | `10.213.32.0/23` | 451176339653 | us-west-2 | perf | Network Perf | 🔴 Create Network |
| 171 | avm-test-20-us-east-1-vpc | `10.215.69.0/25` | 438850684269 | us-east-1 | test | Test East VPC NonProd Test | 🔴 Create Network |
| 172 | avm-test-20-vpc3-dev-VPC | `10.215.40.0/23` | 438850684269 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 173 | avm-test-20-vpc2-VPC | `10.215.148.0/23` | 438850684269 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 174 | avm-test-20-us-west-2-vpc | `10.213.21.128/25` | 438850684269 | us-west-2 | test | Test Tagging Unmanaged resources | 🔴 Create Network |
| 175 | mi-lz-devops-RandD-dev-us-east-1-vpc | `10.215.68.0/24` | 444610583456 | us-east-1 | dev | DevSecOps account for team Research and Automation scripts executions | 🔴 Create Network |
| 176 | mi-lz-devops-RandD-dev-us-west-2-vpc | `10.213.28.0/24` | 444610583456 | us-west-2 | dev | DevSecOps account for team Research and Automation scripts executions | 🔴 Create Network |
| 177 | mi-na-iam-nonprod-east-vpc | `172.25.204.0/23` | 457352897684 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 178 | mi-na-iam-nonprod-east2-vpc | `172.25.208.0/24` | 457352897684 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 179 | mi-na-iam-nonprod-west-vpc | `172.25.212.0/23` | 457352897684 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 180 | data-migration-vpc | `172.25.212.0/23` | 457352897684 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 181 | mi-lz-ocp-dev-us-east-1-vpc | `10.212.68.0/23` | 448347543675 | us-east-1 | dev | OSE Upgrade Pilot | 🔴 Create Network |
| 182 | mi-lz-na-ocp-dev-vpc | `10.212.12.0/24` | 448347543675 | us-east-1 | dev | OSE Upgrade Pilot | 🔴 Create Network |
| 183 | csao-test | `10.0.0.0/24` | 448347543675 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 184 | mi-lz-eks-cots-prod-us-east-1-vpc | `10.215.146.0/23` | 471112557909 | us-east-1 | prodpci | COTS EKS prod | 🔴 Create Network |
| 185 | mi-lz-eks-cots-prod-pci-us-east-2-vpc | `10.220.64.0/23` | 471112557909 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 186 | mi-lz-eks-cots-prod-us-west-2-vpc | `10.216.164.0/23` | 471112557909 | us-west-2 | prodpci | COTS EKS prod | 🔴 Create Network |
| 187 | mi-lz-eks-cots-prod-eu-west-2-vpc | `10.86.148.0/23` | 471112557909 | eu-west-2 | prodpci | COTS EKS prod | 🔴 Create Network |
| 188 | mi-lz-dc-foundational-tip-prod-us-east-1-vpc | `10.212.236.0/22` | 466623320682 | us-east-1 | prod | lz foundational-tip prod accoun for mgp team | 🔴 Create Network |
| 189 | mi-lz-dc-foundational-tip-prod-us-west-2-vpc | `10.213.172.0/22` | 466623320682 | us-west-2 | prod | lz foundational-tip prod accoun for mgp team | 🔴 Create Network |
| 190 | mi-lz-na-loyalty-dev-us-east-1-vpc | `10.212.27.128/25` | 471255908350 | us-east-1 | dev | loyalty account for landing zone | 🔴 Create Network |
| 191 | mi-na-admin-east-vpc | `172.25.12.0/22` | 472401338797 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 192 | mi-na-admin-west-vpc | `172.25.76.0/24` | 472401338797 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 193 | mi-lz-ci-perf-us-east-1-vpc | `10.212.0.0/23` | 494067041866 | us-east-1 | perf | CI perf account for landing zone | 🔴 Create Network |
| 194 | mi-lz-devops-prod-us-east-1-vpc | `10.212.242.0/23` | 495432954560 | us-east-1 | prod | DevOps prod account for landing zone | 🔴 Create Network |
| 195 | mi-lz-devops-prod-us-west-2-vpc | `10.216.152.0/23` | 495432954560 | us-west-2 | prod | selectorAI | 🔴 Create Network |
| 196 | Unnamed | `172.30.0.0/16` | 485982219833 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 197 | mi-lz-dc-hotelops-perf-us-east-1-vpc | `10.215.2.0/23` | 472536607926 | us-east-1 | nonprod | MGP Hotel Ops | 🔴 Create Network |
| 198 | mi-lz-dc-hotelops-perf-us-west-2-vpc | `10.213.24.0/23` | 472536607926 | us-west-2 | nonprod | MGP Hotel Ops | 🔴 Create Network |
| 199 | mi-lz-dc-hotelops-staging-eu-west-2-vpc | `10.86.2.0/23` | 472536607926 | eu-west-2 | staging | MGP Hotel Ops | 🔴 Create Network |
| 200 | mi-na-iam-prod-east-vpc | `172.25.202.0/23` | 477893803077 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 201 | mi-na-iam-prod-east2-vpc | `172.25.209.0/24` | 477893803077 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 202 | mi-na-iam-prod-west-vpc | `172.25.210.0/23` | 477893803077 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 203 | data-migration-vpc-temp | `172.25.210.0/23` | 477893803077 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 204 | mi-iam-na-prod-ap-southeast-1-vpc | `10.83.73.0/26` | 477893803077 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 205 | mi-lz-na-shared-platform-dev-vpc | `10.212.24.0/23` | 482478851458 | us-east-1 | dev | AWS Landing zone | 🔴 Create Network |
| 206 | CL-PrimaryStack/ESVPC | `10.0.0.0/16` | 482478851458 | us-east-1 | dev | opensearch-poc | 🔴 Create Network |
| 207 | project-vpc | `172.16.0.0/16` | 482478851458 | us-west-2 | nonprod | fromEDR | 🔴 Create Network |
| 208 | mi-lz-Icd-core-team-hold-dev-us-east-1-vpc | `10.215.64.128/25` | 478689028988 | us-east-1 | dev | Backup Account in AWS for Cloud backup implementation | 🔴 Create Network |
| 209 | mi-lz-Icd-core-team-hold-dev-us-west-2-vpc | `10.213.20.0/25` | 478689028988 | us-west-2 | dev | Backup Account creation in AWS for Cloud backup implementation | 🔴 Create Network |
| 210 | Security_Public_Internet | `192.168.2.0/24` | 481426791384 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 211 | RlSecTestVPC | `10.0.0.0/16` | 481426791384 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 212 | Default | `172.31.0.0/16` | 481426791384 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 213 | Malware | `172.16.70.0/24` | 481426791384 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 214 | MyVPC | `10.0.0.0/16` | 481426791384 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 215 | Unnamed | `172.31.0.0/16` | 481426791384 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 216 | lesson02-vpc | `10.0.0.0/16` | 481426791384 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 217 | Unnamed | `10.0.0.0/16` | 481426791384 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 218 | Unnamed | `172.31.0.0/16` | 481426791384 | us-west-1 | N/A | N/A | 🔴 Create Network |
| 219 | Unnamed | `10.0.0.0/16` | 481426791384 | us-west-1 | N/A | N/A | 🔴 Create Network |
| 220 | my-vpc | `10.0.0.0/16` | 481426791384 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 221 | MyVPC | `10.0.0.0/16` | 481426791384 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 222 | Unnamed | `172.31.0.0/16` | 481426791384 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 223 | Unnamed | `172.31.0.0/16` | 481426791384 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 224 | Unnamed | `172.31.0.0/16` | 481426791384 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 225 | Unnamed | `172.31.0.0/16` | 481426791384 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 226 | mi-lz-dc-customer-dev-us-east-1-vpc | `10.212.78.0/24` | 504974177539 | us-east-1 | dev | lz dev Customer account for mgp team | 🔴 Create Network |
| 227 | mi-lz-eks-shared-prod-pci-us-east-1-vpc | `10.215.136.0/22` | 507687848137 | us-east-1 | prodpci | Prod lz account for shared EKS | 🔴 Create Network |
| 228 | mi-lz-eks-shared-prod-pci-us-east-2-vpc | `10.220.20.0/22` | 507687848137 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 229 | mi-lz-eks-shared-prod-pci-us-west-2-vpc | `10.216.132.0/22` | 507687848137 | us-west-2 | prodpci | Prod PCI lz account for shared EKS | 🔴 Create Network |
| 230 | mi-lz-eks-shared-prod-pci-eu-west-2-vpc | `10.86.140.0/22` | 507687848137 | eu-west-2 | prodpci | Prod PCI lz account for shared EKS | 🔴 Create Network |
| 231 | r53-demo-sandbox4-vpc | `10.53.55.0/24` | 512192324534 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 232 | mi-honeycomb-web-dev-vpc | `172.25.198.0/25` | 513911627701 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 233 | mi-honeycomb-webhook-dev-vpc | `172.25.198.128/25` | 513911627701 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 234 | mi-lz-na-enterprise-dev-vpc | `10.212.13.0/24` | 519202142219 | us-east-1 | dev | Enterprise BU Dev account | 🔴 Create Network |
| 235 | mi-lz-enterprise-prod-us-east-1-vpc | `10.212.240.0/23` | 512678669104 | us-east-1 | prod | Enterprise prod account for new landing zone | 🔴 Create Network |
| 236 | mi-lz-enterprise-prod-us-west-2-vpc | `10.213.134.0/23` | 512678669104 | us-west-2 | prod | Enterprise prod account for new landing zone | 🔴 Create Network |
| 237 | mi-lz-dc-commerce-prod-us-east-1-vpc | `10.212.232.0/23` | 521951334657 | us-east-1 | prod | lz commerce-prod for mgp team | 🔴 Create Network |
| 238 | mi-lz-dc-commerce-prod-us-west-2-vpc | `10.213.164.0/23` | 521951334657 | us-west-2 | prod | lz commerce-prod for mgp team | 🔴 Create Network |
| 239 | mi-lz-dc-commerce-prod-eu-west-2-vpc | `10.86.248.0/23` | 521951334657 | eu-west-2 | prod | Commerce Prod account | 🔴 Create Network |
| 240 | mi-lz-data-migration-gateway-prod-us-east-1-vpc | `10.215.150.0/23` | 533267294216 | us-east-1 | prod | DC Prod account DMG | 🔴 Create Network |
| 241 | mi-lz-data-migration-gateway-prod-us-west-2-vpc | `10.216.250.0/23` | 533267294216 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 242 | mi-na-dp-nonprod-vpc | `172.25.40.0/22` | 521221133174 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 243 | mi-na-dp-nonprod-west-vpc | `172.25.88.0/22` | 521221133174 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 244 | mi-lz-mobile-app-prod-pci-us-east-1-vpc | `10.212.180.0/23` | 520018980644 | us-east-1 | prod | Couchbase | 🔴 Create Network |
| 245 | mi-lz-mobile-app-prod-pci-us-east-2-vpc | `10.220.24.0/22` | 520018980644 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 246 | mi-lz-mobile-app-prod-eu-west-2-vpc | `10.86.134.0/23` | 520018980644 | eu-west-2 | prod | mobile app prod account for landing zone | 🔴 Create Network |
| 247 | avm-test-01-vpc-us-east-1 | `10.212.37.128/25` | 521690539751 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 248 | prod-inspection-vpc | `10.84.130.0/24` | 533267360957 | us-east-1 | prod | cloud evolution | 🔴 Create Network |
| 249 | egress-vpc-us-east-1-vpc | `10.84.129.0/24` | 533267360957 | us-east-1 | prod | cloud evolution | 🔴 Create Network |
| 250 | egress-vpc-us-east-2-vpc | `10.84.146.0/24` | 533267360957 | us-east-2 | prod | cloud evolution | 🔴 Create Network |
| 251 | prod-inspection-vpc | `10.84.145.0/24` | 533267360957 | us-east-2 | prod | cloud evolution | 🔴 Create Network |
| 252 | egress-vpc-us-west-2-vpc | `10.84.137.0/24` | 533267360957 | us-west-2 | prod | cloud evolution | 🔴 Create Network |
| 253 | prod-inspection-vpc | `10.84.138.0/24` | 533267360957 | us-west-2 | prod | cloud evolution | 🔴 Create Network |
| 254 | prod-inspection-vpc | `10.84.161.0/24` | 533267360957 | ap-southeast-1 | prod | cloud evolution | 🔴 Create Network |
| 255 | egress-vpc-ap-southeast-1-vpc | `10.84.162.0/24` | 533267360957 | ap-southeast-1 | prod | cloud evolution | 🔴 Create Network |
| 256 | partnernet-inspection-vpc | `10.215.126.0/25` | 533267425031 | us-east-1 | staging | cloud evolution | 🔴 Create Network |
| 257 | staging-ingress-vpc | `10.215.125.0/24` | 533267425031 | us-east-1 | staging | cloud evolution | 🔴 Create Network |
| 258 | partnernet-inspection-usw2-vpc | `10.213.126.0/25` | 533267425031 | us-west-2 | staging | cloud evolution | 🔴 Create Network |
| 259 | staging-ingress-usw2-vpc | `10.213.125.0/24` | 533267425031 | us-west-2 | staging | cloud evolution | 🔴 Create Network |
| 260 | mi-lz-na-shared-platform-prod-us-east-1-vpc | `10.212.156.0/23` | 537546261936 | us-east-1 | prod | AWS Landing zone | 🔴 Create Network |
| 261 | mi-lz-na-shared-platform-prod-us-west-2-vpc | `10.213.156.0/22` | 537546261936 | us-west-2 | prod | AWS Landing zone | 🔴 Create Network |
| 262 | mi-lz-na-gis-dr-prod-us-west-2-vpc | `10.91.34.0/23` | 556822949751 | us-west-2 | prod | DR GIS account for landing zone | 🔴 Create Network |
| 263 | mi-lz-mpg-test-us-east-1-vpc | `10.215.97.0/24` | 554738860625 | us-east-1 | test | MPG Platform account | 🔴 Create Network |
| 264 | mi-lz-na-res-dr-prod-us-west-2-vpc | `10.91.32.0/23` | 558912401267 | us-west-2 | prod | DR reservation account for landing zone | 🔴 Create Network |
| 265 | mi-lz-na-migration-dev-us-east-1-vpc | `10.212.35.0/25` | 562086429047 | us-east-1 | dev | migration dev account for AWS landing zone | 🔴 Create Network |
| 266 | mi-lz-pms-prod-us-east-1-vpc | `10.215.240.0/23` | 559050208314 | us-east-1 | prod | Property Management Systems | 🔴 Create Network |
| 267 | Unnamed | `172.31.0.0/16` | 557978034415 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 268 | Rimini VPC | `10.204.67.128/25` | 557978034415 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 269 | Unnamed | `172.31.0.0/16` | 557978034415 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 270 | Unnamed | `172.31.0.0/16` | 557978034415 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 271 | Unnamed | `172.31.0.0/16` | 557978034415 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 272 | Unnamed | `172.31.0.0/16` | 557978034415 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 273 | mi-lz-ocp-test-us-east-1-vpc | `10.212.10.0/23` | 585382900701 | us-east-1 | test | ocp test account for landing zone | 🔴 Create Network |
| 274 | mi-lz-ocp-test-us-west-2-vpc | `10.213.0.0/23` | 585382900701 | us-west-2 | test | ocp test account for landing zone | 🔴 Create Network |
| 275 | mi-lz-dc-commerce-uat-us-east-1-vpc | `10.212.66.0/23` | 573009580851 | us-east-1 | uat | lz uat account for Unified Search and Product Catalog | 🔴 Create Network |
| 276 | mi-lz-dc-commerce-uat-us-west-2-vpc | `10.213.68.0/23` | 573009580851 | us-west-2 | uat | lz uat account for Unified Search and Product Catalog | 🔴 Create Network |
| 277 | mi-lz-dc-foundational-data-dev-us-east-1-vpc | `10.212.89.0/24` | 589930560890 | us-east-1 | dev | lz foundational data dev account for mgp team | 🔴 Create Network |
| 278 | mi-lz-dc-loyalty-prod-us-east-1-vpc | `10.215.182.0/23` | 590184007287 | us-east-1 | prod | MGP Loyalty | 🔴 Create Network |
| 279 | mi-lz-dc-loyalty-prod-us-west-2-vpc | `10.213.184.0/23` | 590184007287 | us-west-2 | prod | MGP Loyalty | 🔴 Create Network |
| 280 | mi-na-gis-prod-east-vpc | `172.25.224.0/23` | 594559298110 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 281 | mi-na-gis-prod-west-vpc | `172.25.98.0/23` | 594559298110 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 282 | mi-lz-generative-ai-dev-us-east-1-vpc | `10.215.34.0/23` | 610469709024 | us-east-1 | dev | OpenAI | 🔴 Create Network |
| 283 | mi-lz-dc-finance-dev-us-east-1-vpc | `10.212.86.0/24` | 615678013363 | us-east-1 | dev | lz finance dev account for mgp team | 🔴 Create Network |
| 284 | mi-lz-na-dr-devtest-vpc | `10.212.15.0/25` | 622766443493 | us-east-1 | dev | Landing Zone DR | 🔴 Create Network |
| 285 | mi-lz-na-dr-devtest-us-west-2-vpc | `10.213.3.128/25` | 622766443493 | us-west-2 | dev | Landing Zone DR | 🔴 Create Network |
| 286 | mi-lz-dc-foundational-tip-test-us-east-1-vpc | `10.212.92.0/23` | 597351379612 | us-east-1 | test | lz foundational-tip test accoun for mgp team | 🔴 Create Network |
| 287 | mi-lz-res-prod-us-east-1-vpc | `10.212.250.0/23` | 618923836678 | us-east-1 | prod | reservation prod account for landing zone | 🔴 Create Network |
| 288 | mi-lz-dc-loyalty-test-us-east-1-vpc | `10.212.80.0/24` | 621289554965 | us-east-1 | test | lz test Loyalty account for mgp team | 🔴 Create Network |
| 289 | mi-lz-generative-ai-sandbox-us-east-1-vpc | `192.168.0.0/23` | 618653283510 | us-east-1 | sandbox | OpenAI | 🔴 Create Network |
| 290 | mi-lz-na-api-dev-us-east-1-vpc | `10.212.32.0/24` | 625308820683 | us-east-1 | dev | API dev account for Landing zone | 🔴 Create Network |
| 291 | mi-lz-api-perf-us-east-1-vpc | `10.212.2.0/23` | 635424421791 | us-east-1 | perf | API perf account for landing zone | 🔴 Create Network |
| 292 | mi-lz-api-perf-us-west-2-vpc | `10.213.42.0/23` | 635424421791 | us-west-2 | staging | API Perf West | 🔴 Create Network |
| 293 | mi-lz-eks-tooling-dev-ss-us-east-1-vpc | `10.215.174.0/23` | 637423303103 | us-east-1 | dev | Eks tooling | 🔴 Create Network |
| 294 | mi-lz-eks-tooling-dev-ss-us-west-2-vpc | `10.213.176.0/23` | 637423303103 | us-west-2 | dev | EKS tooling | 🔴 Create Network |
| 295 | nonprod-inspection-vpc | `10.215.119.0/24` | 637423621093 | us-east-1 | nonprod | cloud evolution | 🔴 Create Network |
| 296 | egress-vpc-us-east-1-vpc | `10.215.124.0/24` | 637423621093 | us-east-1 | nonprod | cloud evolution | 🔴 Create Network |
| 297 | nonprod-inspection-vpc | `10.213.116.0/24` | 637423621093 | us-west-2 | nonprod | cloud evolution | 🔴 Create Network |
| 298 | egress-vpc-us-west-2-vpc | `10.213.118.0/24` | 637423621093 | us-west-2 | nonprod | cloud evolution | 🔴 Create Network |
| 299 | mi-lz-nsee-ss-aprop-us-east-1-vpc | `10.212.185.0/24` | 637423529757 | us-east-1 | prod | CORP-NSSE | 🔴 Create Network |
| 300 | mi-lz-nsee-ss-aprop-us-west-2-vpc | `10.216.170.0/24` | 637423529757 | us-west-2 | prod | CORP-NSSE | 🔴 Create Network |
| 301 | mi-lz-nsee-ss-aprop-vion-ap-southeast-1-vpc | `10.83.72.0/24` | 637423529757 | ap-southeast-1 | prod | Corp-NSEE | 🔴 Create Network |
| 302 | mi-lz-eks-shared-perf-us-east-1-vpc | `10.212.56.0/22` | 644474402441 | us-east-1 | nonprod | Perf account for lz | 🔴 Create Network |
| 303 | mi-lz-eks-shared-perf-us-west-2-vpc | `10.213.16.0/22` | 644474402441 | us-west-2 | nonprod | Perf account for lz | 🔴 Create Network |
| 304 | mi-lz-dc-foundational-qe-test-us-east-1-vpc | `10.212.63.0/24` | 646477401365 | us-east-1 | nonprod | MGP Quality Engineering | 🔴 Create Network |
| 305 | mi-na-dp-prod-vpc | `172.25.32.0/21` | 654607264796 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 306 | mi-na-dp-prod-west-vpc | `172.25.80.0/21` | 654607264796 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 307 | mi-lz-dc-customer-staging-us-east-1-vpc | `10.212.94.0/23` | 637423629817 | us-east-1 | staging | lz staging Customer account for mgp team | 🔴 Create Network |
| 308 | mi-lz-dc-customer-staging-us-west-2-vpc | `10.213.40.0/23` | 637423629817 | us-west-2 | staging | lz staging Customer account for mgp team | 🔴 Create Network |
| 309 | mi-lz-shared-platform-perf-us-east-1-vpc | `10.212.44.0/23` | 638866681188 | us-east-1 | perf | Perf shared platform account for landing zone | 🔴 Create Network |
| 310 | mi-lz-dc-finance-staging-us-east-1-vpc | `10.215.6.0/23` | 654654484139 | us-east-1 | staging | lz Finance uat account for mgp team | 🔴 Create Network |
| 311 | mi-lz-dc-finance-staging-us-west-2-vpc | `10.213.34.0/23` | 654654484139 | us-west-2 | staging | lz Finance uat account for mgp team | 🔴 Create Network |
| 312 | mi-lz-dc-finance-prod-us-east-1-vpc | `10.215.180.0/23` | 654654524884 | us-east-1 | prod | lz Finance prod account for mgp team | 🔴 Create Network |
| 313 | mi-lz-dc-finance-prod-us-west-2-vpc | `10.216.162.0/23` | 654654524884 | us-west-2 | prod | lz Finance prod account for mgp team | 🔴 Create Network |
| 314 | mi-lz-iam-dev-us-east-1-vpc | `10.212.36.128/25` | 655852181272 | us-east-1 | dev | IAM dev account for landing zone | 🔴 Create Network |
| 315 | mi-lz-iam-dev-us-west-2-vpc | `10.213.21.0/25` | 655852181272 | us-west-2 | dev | DR POC | 🔴 Create Network |
| 316 | mi-lz-na-revenue-mgmt-prod-us-east-1-vpc | `10.212.158.0/23` | 666958959537 | us-east-1 | prod | Prod revenue management account for landing zone | 🔴 Create Network |
| 317 | mi-lz-na-revenue-mgmt-prod-us-west-2-vpc | `10.216.144.0/23` | 666958959537 | us-west-2 | prod | OYC revenue management need vpc in us-west-2 | 🔴 Create Network |
| 318 | mi-lz-dr-factory-ss-us-west-2-vpc | `10.91.56.0/24` | 656963443190 | us-west-2 | shared services | DR migration factory ss account for landing zone | 🔴 Create Network |
| 319 | Unnamed | `172.31.0.0/16` | 684837204429 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 320 | Unnamed | `172.31.0.0/16` | 684837204429 | us-west-1 | N/A | N/A | 🔴 Create Network |
| 321 | Unnamed | `10.0.0.0/16` | 684837204429 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 322 | mi-lz-na-digital-prod-us-east-1-vpc | `10.212.162.0/23` | 684105869352 | us-east-1 | prod | Prod digital account for landing zone | 🔴 Create Network |
| 323 | r53-spoke-vpc | `10.53.1.0/24` | 690872919680 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 324 | r53-onprem-vpc | `10.53.2.0/24` | 690872919680 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 325 | r53-hub-vpc | `10.53.0.0/24` | 690872919680 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 326 | cwan-test-vpc | `10.215.16.0/24` | 690872919680 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 327 | cwan-test-vpc | `10.216.16.0/24` | 690872919680 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 328 | project-vpc | `10.0.0.0/16` | 690872919680 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 329 | mi-lz-mcom-prod-eu-west-2-vpc | `10.86.132.0/23` | 696171720625 | eu-west-2 | prod | mcom prod account for landing zone | 🔴 Create Network |
| 330 | mi-lz-mdp-prod-us-east-1-vpc | `10.212.248.0/23` | 705385216787 | us-east-1 | prod | MDP prod account for landing zone | 🔴 Create Network |
| 331 | mi-lz-dc-customer-test-us-east-1-vpc | `10.212.81.0/24` | 706607083863 | us-east-1 | test | lz Customer test account for mgp team | 🔴 Create Network |
| 332 | mi-lz-na-property-dev-us-east-1-vpc | `10.212.28.0/25` | 712164335367 | us-east-1 | dev | property dev account for landing zone | 🔴 Create Network |
| 333 | mi-lz-dc-loyalty-perf-us-east-1-vpc | `10.212.108.0/23` | 724433859310 | us-east-1 | nonprod | MGP Loyalty | 🔴 Create Network |
| 334 | mi-lz-dc-loyalty-perf-us-west-2-vpc | `10.213.26.0/23` | 724433859310 | us-west-2 | nonprod | MGP Loyalty | 🔴 Create Network |
| 335 | mi-lz-dc-sales-staging-us-east-1-vpc | `10.215.4.0/23` | 730335291707 | us-east-1 | staging | lz Sales uat account for mgp team | 🔴 Create Network |
| 336 | mi-lz-dc-sales-staging-us-west-2-vpc | `10.213.36.0/23` | 730335291707 | us-west-2 | staging | lz Sales uat account for mgp team | 🔴 Create Network |
| 337 | mi-lz-dr-sandbox-us-east-1-vpc | `192.168.0.0/23` | 759752224209 | us-east-1 | sandbox | lz sandbox account for mini-pocs for DR related products | 🔴 Create Network |
| 338 | mi-lz-dr-sandbox-us-west-2-vpc | `192.168.0.0/23` | 759752224209 | us-west-2 | sandbox | lz sandbox account for mini-pocs for DR related products | 🔴 Create Network |
| 339 | mi-lz-gns-partner-ingress-prod-inspection-us-east-1-vpc | `10.215.255.0/25` | 730335501116 | us-east-1 | prod | cloud evolution | 🔴 Create Network |
| 340 | mi-lz-gns-partner-ingress-prod-us-east-1-vpc | `10.215.253.0/24` | 730335501116 | us-east-1 | prod | cloud evolution | 🔴 Create Network |
| 341 | mi-lz-gns-partner-ingress-prod-us-west-2-vpc | `10.216.253.0/24` | 730335501116 | us-west-2 | prod | cloud evolution | 🔴 Create Network |
| 342 | mi-lz-gns-partner-ingress-prod-inspection-us-west-2-vpc | `10.216.255.0/25` | 730335501116 | us-west-2 | prod | cloud evolution | 🔴 Create Network |
| 343 | mi-lz-gns-partner-ingress-prod-inspection-eu-west-2-vpc | `10.86.253.128/25` | 730335501116 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 344 | mi-lz-gns-partner-ingress-prod-eu-west-2-vpc | `10.86.254.0/23` | 730335501116 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 345 | mi-lz-icd-core-team-hold-prod-us-east-1-vpc | `10.215.164.0/23` | 757803349776 | us-east-1 | prod | Backup Account in AWS for Cloud backup implementation | 🔴 Create Network |
| 346 | mi-lz-icd-core-team-hold-prod-us-west-2-vpc | `10.216.142.0/23` | 757803349776 | us-west-2 | prod | Backup Account creation in AWS for Cloud backup implementation | 🔴 Create Network |
| 347 | mi-na-gis-nonprod-east-vpc | `172.25.226.0/24` | 752043461897 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 348 | mi-na-stfpoc | `172.23.194.0/23` | 752043461897 | us-west-1 | non-prod | I:Semi Trusted Framework | 🔴 Create Network |
| 349 | mi-na-gis-nonprod-west-vpc | `172.25.100.0/24` | 752043461897 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 350 | mi-jp-stfpoc | `172.23.198.0/23` | 752043461897 | ap-northeast-1 | non-prod | I:Semi Trusted Framework | 🔴 Create Network |
| 351 | mi-sg-stfpoc | `172.23.196.0/23` | 752043461897 | ap-southeast-1 | non-prod | I:Semi Trusted Framework | 🔴 Create Network |
| 352 | mi-lz-network-shared-prod-us-east-1-vpc | `10.215.190.0/23` | 767398107153 | us-east-1 | shared-services | network shared services | 🔴 Create Network |
| 353 | mi-lz-network-shared-prod-us-west-2-vpc | `10.216.160.0/23` | 767398107153 | us-west-2 | shared-services | network shared services | 🔴 Create Network |
| 354 | mi-lz-network-shared-prod-nsee-ss-ap-southeast-1-vpc | `10.83.70.0/23` | 767398107153 | ap-southeast-1 | prod | SS-NSEE | 🔴 Create Network |
| 355 | mi-lz-dc-hotelops-test-us-east-1-vpc | `10.212.76.0/24` | 777050211007 | us-east-1 | test | lz hotelops-dev account for MGP team | 🔴 Create Network |
| 356 | mi-s3-sftp-public-nacl | `10.0.0.0/16` | 780727336067 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 357 | mi-na-druva-restore-public-dmz | `10.0.0.0/16` | 780727336067 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 358 | mi-na-druva-restore-private-idmz | `172.25.255.192/26` | 780727336067 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 359 | mi-na-prod-east-vpc | `172.25.0.0/21` | 780727336067 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 360 | mi-na-prod-west-vpc | `172.25.64.0/21` | 780727336067 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 361 | mi-lz-eks-shared-prod-us-east-1-vpc | `10.215.132.0/22` | 785272838649 | us-east-1 | prod | Prod lz account for shared EKS | 🔴 Create Network |
| 362 | mi-lz-eks-shared-prod-us-east-2-vpc | `10.220.28.0/22` | 785272838649 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 363 | mi-lz-eks-shared-prod-us-west-2-vpc | `10.213.168.0/22` | 785272838649 | us-west-2 | prod | Prod lz account for shared EKS | 🔴 Create Network |
| 364 | mi-lz-eks-shared-prod-eu-west-2-vpc | `10.86.144.0/22` | 785272838649 | eu-west-2 | prod | Prod lz account for shared EKS | 🔴 Create Network |
| 365 | mi-lz-na-migration-ss-us-east-1-vpc | `10.212.154.0/23` | 794753028649 | us-east-1 | shared services | migration shared services account for AWS landing zone | 🔴 Create Network |
| 366 | mi-lz-dc-commerce-dev-us-east-1-vpc | `10.212.20.0/22` | 795441659942 | us-east-1 | dev | AWS Acct for Digital BU dev | 🔴 Create Network |
| 367 | mi-lz-na-digital-dr-prod-us-west-2-vpc | `10.91.40.0/23` | 798245798281 | us-west-2 | prod | DR Digital account for landing zone | 🔴 Create Network |
| 368 | mi-lz-dc-foundational-tip-perf-us-east-1-vpc | `10.212.104.0/22` | 806717236186 | us-east-1 | nonprod | lz foundational-tip perf account for mgp team | 🔴 Create Network |
| 369 | mi-lz-dc-foundational-tip-perf-us-west-2-vpc | `10.213.12.0/22` | 806717236186 | us-west-2 | nonprod | lz foundational-tip perf account for mgp team | 🔴 Create Network |
| 370 | mi-lz-na-network-dr-prod-us-west-2-vpc | `10.91.36.0/23` | 815790908052 | us-west-2 | prod | DR Network account for landing zone | 🔴 Create Network |
| 371 | mi-lz-na-gis-prod-vpc | `10.212.148.0/23` | 798268158912 | us-east-1 | prod | landing zone | 🔴 Create Network |
| 372 | mi-lz-na-gis-prod-us-west-2-vpc | `10.213.132.0/23` | 798268158912 | us-west-2 | prod | Landing zone setup up GIS prod west region | 🔴 Create Network |
| 373 | mi-lz-aad-dev-us-east-1-vpc | `10.215.36.0/24` | 838470345955 | us-east-1 | dev | Domain Collection Account for DevCon EKS | 🔴 Create Network |
| 374 | Unnamed | `172.30.0.0/16` | 838470345955 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 375 | mi-lz-aad-dev-us-west-2-vpc | `10.213.29.0/24` | 838470345955 | us-west-2 | dev | Domain Collection Account for DevCon EKS | 🔴 Create Network |
| 376 | mi-lz-aad-dev-eu-west-2-vpc | `10.86.1.0/24` | 838470345955 | eu-west-2 | dev | Domain Collection Account for DevCon EKS | 🔴 Create Network |
| 377 | mi-lz-dc-foundational-eventhub-test-us-east-1-vpc | `10.212.90.0/23` | 840513069010 | us-east-1 | test | lz EventHub account for mgp team | 🔴 Create Network |
| 378 | mi-na-prod-pci-east-vpc | `172.25.8.0/22` | 846809438626 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 379 | mi-na-prod-pci-west-vpc | `172.25.72.0/22` | 846809438626 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 380 | mi-lz-gis-perf-us-east-1-vpc | `10.212.6.0/23` | 857595017610 | us-east-1 | perf | Network Perf account for lz | 🔴 Create Network |
| 381 | mi-lz-gis-perf-us-west-2-vpc | `10.213.10.0/23` | 857595017610 | us-west-2 | perf | Network Perf account for lz | 🔴 Create Network |
| 382 | mi-lz-res-dev-us-east-1-vpc | `10.212.27.0/25` | 860971767160 | us-east-1 | dev | reservation dev account for landing zone | 🔴 Create Network |
| 383 | mi-lz-property-dr-prod-us-west-2-vpc | `10.91.44.0/23` | 860912043256 | us-west-2 | prod | Property DR account for Landing Zone | 🔴 Create Network |
| 384 | mi-lz-dc-foundational-data-perf-us-east-1-vpc | `10.212.98.0/23` | 865028170173 | us-east-1 | perf | lz foundational Perf account for mgp team | 🔴 Create Network |
| 385 | mi-lz-dc-foundational-data-perf-us-west-2-vpc | `10.213.4.0/23` | 865028170173 | us-west-2 | perf | lz foundational data Perf account for mgp team | 🔴 Create Network |
| 386 | Tennable | `172.31.0.0/16` | 883113265457 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 387 | SecurityVPC | `10.1.0.0/16` | 883113265457 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 388 | ForensicsVPC | `172.16.0.0/16` | 883113265457 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 389 | MI-NHLAB01 | `100.100.0.0/16` | 883113265457 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 390 | CS-SecurityHub | `10.199.0.0/16` | 883113265457 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 391 | Unnamed | `172.31.0.0/16` | 883113265457 | us-east-2 | N/A | N/A | 🔴 Create Network |
| 392 | Unified-VPC | `10.0.0.0/16` | 883113265457 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 393 | network-firewall-poc-application-private | `172.16.0.0/16` | 883113265457 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 394 | Unnamed | `10.0.0.0/16` | 883113265457 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 395 | Unnamed | `172.31.0.0/16` | 883113265457 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 396 | Shirong-Network-Firewall-POC-Automation-Inspection-VPC | `192.168.0.0/16` | 883113265457 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 397 | testVpc | `10.0.0.0/24` | 883113265457 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 398 | mi-lz-security-lake-poc-dev-us-east-1-vpc | `10.215.96.128/25` | 876646277615 | us-east-1 | dev | lz security dev account for POC | 🔴 Create Network |
| 399 | Unnamed | `172.31.0.0/16` | 871216462967 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 400 | SecurityAutomation | `10.0.0.0/16` | 871216462967 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 401 | Unnamed | `172.31.0.0/16` | 871216462967 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 402 | Unnamed | `172.31.0.0/16` | 871216462967 | eu-west-2 | N/A | N/A | 🔴 Create Network |
| 403 | Unnamed | `172.31.0.0/16` | 871216462967 | ap-northeast-1 | N/A | N/A | 🔴 Create Network |
| 404 | Unnamed | `172.31.0.0/16` | 871216462967 | ap-southeast-1 | N/A | N/A | 🔴 Create Network |
| 405 | mi-lz-enterprise-storage-prod-us-east-1-vpc | `10.215.130.0/23` | 873599636883 | us-east-1 | prod | AWS Prod account in US East1 to host department shared drive in AWS | 🔴 Create Network |
| 406 | mi-lz-enterprise-storage-prod-us-west-2-vpc | `10.213.178.0/23` | 873599636883 | us-west-2 | prod | AWS Prod account in US West2 to host department shared drive in AWS | 🔴 Create Network |
| 407 | mi-na-iam-dev-east-vpc | `172.25.206.0/23` | 902792996277 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 408 | mi-lz-security-lake-subscriber-prod-us-west-2-vpc | `10.216.157.0/24` | 905418299649 | us-west-2 | prod | Security DataLake Subscriber Prod Account | 🔴 Create Network |
| 409 | mi-lz-dc-hotelops-prod-us-east-1-vpc | `10.215.188.0/23` | 905418469135 | us-east-1 | prod | MGP Hotel Ops | 🔴 Create Network |
| 410 | mi-lz-dc-hotelops-prod-us-west-2-vpc | `10.213.190.0/23` | 905418469135 | us-west-2 | prod | MGP Hotel Ops | 🔴 Create Network |
| 411 | mi-lz-dc-hotelops-prod-eu-west-2-vpc | `10.86.158.0/23` | 905418469135 | eu-west-2 | prod | MGP Hotel Ops | 🔴 Create Network |
| 412 | mi-lz-data-migration-gateway-test-us-east-1-vpc | `10.212.54.0/24` | 914069279993 | us-east-1 | test | Data Migration Gateway account for lz | 🔴 Create Network |
| 413 | mi-lz-terraform-modules-dev-us-east-1-vpc | `10.212.97.0/24` | 914029847638 | us-east-1 | dev | lz account for terraform modules | 🔴 Create Network |
| 414 | nsee-vpc-test-us-east-1-vpc | `10.215.105.0/24` | 914029847638 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 415 | aws-cli-test-us-east-1-vpc | `10.212.121.128/25` | 914029847638 | us-east-1 | dev | N/A | 🔴 Create Network |
| 416 | nsee-ss-vpc-test-us-east-1-vpc | `10.215.72.0/23` | 914029847638 | us-east-1 | N/A | N/A | 🔴 Create Network |
| 417 | axon-test-vpc-nsee-ss-us-east-1-vpc | `10.215.74.0/23` | 914029847638 | us-east-1 | dev | cloud_evolution | 🔴 Create Network |
| 418 | cns-test-vpc | `10.213.80.0/22` | 914029847638 | us-west-2 | N/A | N/A | 🔴 Create Network |
| 419 | mi-lz-na-shared-platform-test-us-east-1-vpc | `10.212.29.0/25` | 945659386755 | us-east-1 | test | shared platform test account for landing zone | 🔴 Create Network |
| 420 | mi-lz-na-shared-platform-test-us-west-2-vpc | `10.213.3.0/25` | 945659386755 | us-west-2 | test | shared platform test account for landing zone | 🔴 Create Network |
| 421 | mi-lz-icd-prod-us-east-1-vpc | `10.212.254.0/23` | 916151928633 | us-east-1 | prod | lz prod account for icd | 🔴 Create Network |
| 422 | mi-lz-ci-prod-us-east-1-vpc | `10.212.132.0/23` | 931061904753 | us-east-1 | prod | CI prod account in landing zone | 🔴 Create Network |
| 423 | mi-lz-na-revenue-mgmt-test-us-east-1-vpc | `10.212.36.0/25` | 914758853005 | us-east-1 | test | revenue management test account for landing zone | 🔴 Create Network |
| 424 | mi-lz-na-aries-dev-us-east-1-vpc | `10.212.18.0/25` | 948350162498 | us-east-1 | dev | Aries dev account for landing zone | 🔴 Create Network |
| 425 | mi-lz-devops-aad-ss-us-east-1-vpc | `10.215.172.0/23` | 953149742123 | us-east-1 | shared services | EKS Cluster Account | 🔴 Create Network |
| 426 | mi-lz-devops-aad-ss-us-east-2-vpc | `10.220.17.0/24` | 953149742123 | us-east-2 | prod | devops | 🔴 Create Network |
| 427 | mi-lz-devops-aad-ss-us-west-2-vpc | `10.216.154.0/23` | 953149742123 | us-west-2 | shared services | EKS Cluster Account | 🔴 Create Network |
| 428 | mi-lz-devops-aad-ss-eu-west-2-vpc | `10.86.154.0/23` | 953149742123 | eu-west-2 | shared-services | EKS Cluster Account | 🔴 Create Network |
| 429 | mi-lz-dc-foundational-tip-prod-pci-us-east-1-vpc | `10.212.172.0/22` | 969977572712 | us-east-1 | prodpci | Pro PCI account for foundational Tip | 🔴 Create Network |
| 430 | mi-lz-dc-foundational-tip-prod-pci-us-west-2-vpc | `10.213.148.0/22` | 969977572712 | us-west-2 | prodpci | Pro PCI account for foundational Tip | 🔴 Create Network |
| 431 | mi-lz-eks-cots-dev-us-east-1-vpc | `10.215.43.0/25` | 975050154436 | us-east-1 | dev | COTS EKS dev account | 🔴 Create Network |
| 432 | mi-lz-dc-sales-prod-us-east-1-vpc | `10.215.178.0/23` | 992382368138 | us-east-1 | prod | lz Sales Prod account for mgp team | 🔴 Create Network |
| 433 | mi-lz-dc-sales-prod-us-west-2-vpc | `10.216.244.0/23` | 992382368138 | us-west-2 | prod | MGP | 🔴 Create Network |
| 434 | mi-lz-gpos-prod-us-east-1-vpc | `10.215.144.0/23` | 975049925496 | us-east-1 | prod | Global Point of Sale | 🔴 Create Network |
| 435 | mi-lz-dc-customer-prod-us-east-1-vpc | `10.215.184.0/23` | 992382728944 | us-east-1 | prod | lz prod customer account for mgp team | 🔴 Create Network |
| 436 | mi-lz-dc-customer-prod-us-west-2-vpc | `10.213.186.0/23` | 992382728944 | us-west-2 | prod | lz prod customer account for mgp team | 🔴 Create Network |
| 437 | mi-lz-na-ss-nonprod-vpc | `10.212.14.0/24` | 996573413692 | us-east-1 | non-prod-shared-services | Landing Zone | 🔴 Create Network |
| 438 | mi-lz-na-ss-nonprod-us-east-2-vpc | `10.220.0.0/24` | 996573413692 | us-east-2 | nonprod | Nonprod account for Dynatrace activegates | 🔴 Create Network |
| 439 | mi-lz-na-ss-nonprod-us-west-2-vpc | `10.213.2.0/24` | 996573413692 | us-west-2 | non-prod-shared-services | Landing Zone | 🔴 Create Network |
| 440 | mi-lz-na-ss-nonprod-eu-west-2-vpc | `10.86.0.128/25` | 996573413692 | eu-west-2 | nonprod | Landing Zone | 🔴 Create Network |
| 441 | mi-lz-na-ss-nonprod-ap-northeast-1-vpc | `10.83.128.128/25` | 996573413692 | ap-northeast-1 | nonprod | Landing Zone | 🔴 Create Network |
| 442 | mi-lz-na-ss-nonprod-ap-southeast-1-vpc | `10.83.0.128/25` | 996573413692 | ap-southeast-1 | nonprod | Landing Zone | 🔴 Create Network |
| 443 | mi-lz-iam-prod-us-east-1-vpc | `10.212.134.0/23` | 998976438556 | us-east-1 | prod | IAM prod account for landing zone | 🔴 Create Network |
| 444 | mi-lz-dc-revenue-mgmt-prod-us-east-1-vpc | `10.215.186.0/23` | 992382662310 | us-east-1 | prod | prod account for revenue management | 🔴 Create Network |
| 445 | mi-lz-dc-revenue-mgmt-prod-us-west-2-vpc | `10.213.188.0/23` | 992382662310 | us-west-2 | prod | prod account for revenue management | 🔴 Create Network |

#### 🎯 Quick Actions for Missing Networks:
```bash
# Create all missing networks (dry-run first)
python aws_infoblox_vpc_manager.py --network-view WedView --create-missing --dry-run

# Create all missing networks (actual)
python aws_infoblox_vpc_manager.py --network-view WedView --create-missing
```


## 🌎 Regional Distribution

| AWS Region | VPC Count | Percentage |
|------------|-----------|------------|
| us-east-1 | 225 | 50.6% |
| us-west-2 | 132 | 29.7% |
| eu-west-2 | 29 | 6.5% |
| ap-southeast-1 | 21 | 4.7% |
| us-east-2 | 19 | 4.3% |
| ap-northeast-1 | 15 | 3.4% |
| us-west-1 | 4 | 0.9% |

## 🏗️ Environment Distribution

| Environment | VPC Count | Percentage |
|-------------|-----------|------------|
| Unknown | 138 | 31.0% |
| prod | 107 | 24.0% |
| dev | 62 | 13.9% |
| test | 23 | 5.2% |
| nonprod | 20 | 4.5% |
| perf | 19 | 4.3% |
| staging | 16 | 3.6% |
| prodpci | 10 | 2.2% |
| shared services | 10 | 2.2% |
| sandbox | 7 | 1.6% |
| core shared services | 5 | 1.1% |
| prod-shared-services | 4 | 0.9% |
| ss | 4 | 0.9% |
| non-prod-shared-services | 4 | 0.9% |
| sharedservices | 3 | 0.7% |
| non-prod | 3 | 0.7% |
| shared-services | 3 | 0.7% |
| Dev | 2 | 0.4% |
| perftest | 2 | 0.4% |
| uat | 2 | 0.4% |
| dr | 1 | 0.2% |

---

## 📌 Recommendations

### 1. Create Missing Networks
- **Count**: 445 networks
- **Priority**: High
- **Action**: Run the create command shown above

---

*Report generated by AWS-InfoBlox VPC Manager on 2025-06-04 12:24:40*
*Network View: WedView*