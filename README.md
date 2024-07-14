# Analysis of the Indian Health Budget (2023-24)

## Overview
This project focuses on the estimated budget allocations to the Ministry of Health and Family Welfare for the fiscal year 2023-24. Using a pie chart visualisation, it aims to analyze the distribution of funds across various major heads within the ministry.

## Introduction
The **Ministry of Health and Family Welfare (MoHFW)** is a ministry under the Government of India, charged with the formulation and implementation of policies and programs to improve the health and well-being of the country's population. It is also responsible for all government programs related to family planning in India. The Ministry comprises the (i) **Department of Health and Family Welfare**, which is responsible for implementing public health schemes and regulating medical education, and the (ii) **Department of Health Research** which is responsible for conducting medical research.

It is important to provide a *clear* and *transparent* representation of the national health budget for the general public. The pie chart is designed to make it easy to understand where the government is prioritizing its spending, helping everyone gain a clearer picture of how financial resources are being allocated to improve public health.

## Data Source
The dataset used in this project is titled **“Allocations to the Ministry of Health and Family Welfare for 2023-24 (in Rs crore)”**, obtained from Table 7. This is sourced from [PRS Legislative Research](https://prsindia.org/budgets/parliament/demand-for-grants-2023-24-analysis-health-and-family-welfare).

For this project, the data was processed to focus on the estimated budget for 2023-24 (2023-24 BE).

## Tools and Libraries
**Programming Language:** Python
- Pandas: Utilized for data manipulation and preparation.
- Matplotlib: Employed for creating the pie chart visualization.

## Program Code
The program was written in PyCharm. You can access the [Program](Program) file here on GitHub or run the code on Google Colab by clicking on the colab badge below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1eho1R537Vc36IOzRefcoL054mqZyGF11)

## Program Output
![Pie Chart](https://github.com/user-attachments/assets/dc981d46-fdeb-4461-9e60-dcae2e802ce8)

## Methodology
A grouped bar chart is plotted to compare the "before" and "after" mortality rates for the telemedicine program for each diagnosis group-- namely [AMI (Acute Myocardial Infarction)](https://en.wikipedia.org/wiki/Myocardial_infarction), [Septic Shock](https://en.wikipedia.org/wiki/Septic_shock), [Ischemic Stroke](https://en.wikipedia.org/wiki/Stroke#Classification) and [Hemorrhagic Stroke](https://en.wikipedia.org/wiki/Stroke#Classification).

A legend is added to distinguish between the two sets of bars, and data labels are placed above each bar to display the exact mortality rates.

## Observation
There is a notable change in mortality rates across all diagnoses:
  - AMI: 47.2% reduction
  - Septic Shock: 43.0% reduction
  - Ischemic Stroke: 57.5% reduction
  - Hemorrhagic Stroke: 57.7% reduction

## Inference
- There is a significant reduction in mortality rates across all diagnoses when telemedicine is implemented.
- The most substantial reductions are observed in ischemic stroke and septic shock.

## Conclusion
The chart demonstrates the positive impact of telemedicine on reducing mortality rates for several critical diagnoses. This could be one small step for IT, but one giant leap for Healthcare.

### Implications for Health Care Professionals
Healthcare professionals should advocate for and integrate telemedicine services into routine care, especially for managing critical conditions.

- **Policy and Implementation:**
  Health policies should encourage the adoption of telemedicine services, particularly in areas where access to immediate medical care is limited.
    
- **Future Research:**
  Further studies could explore the specific factors within telemedicine that contribute to these improved outcomes, aiming to optimize telemedicine practices.

## Author
Pragya Ghosh
