# GST Audit Cases - 100 Cases across 6 Categories
# Generated for Indian GST Audit Training and AI Agent Testing
# Based on CGST Act 2017

# =============================================================================
# CATEGORY 1: TASK1_CASES - GSTR-1 vs GSTR-3B Mismatches (20 Cases)
# =============================================================================

TASK1_CASES = [
    {
        "id": "case_001",
        "description": (
            "Sunrise Textiles Pvt Ltd (GSTIN: 27AABCS1234A1Z5), Mumbai, is a textile manufacturer. "
            "For July 2023, GSTR-1 shows taxable outward supplies of ₹12,45,000 at 5% GST, implying "
            "GST liability of ₹62,250. However, GSTR-3B filed for the same period declares tax payable "
            "of only ₹48,500. The difference of ₹13,750 has not been paid. "
            "The company claims it was a typographical error during GSTR-3B filing."
        ),
        "question": (
            "Calculate the GST mismatch amount between GSTR-1 and GSTR-3B for Sunrise Textiles Pvt Ltd "
            "for July 2023. What enforcement action should be taken and under which section of CGST Act 2017?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 13750,
            "gstr1_liability": 62250,
            "gstr3b_declared": 48500,
            "action": "Issue SCN under Section 73 of CGST Act 2017 for short payment of tax; Interest applicable under Section 50 at 18% per annum from due date",
            "penalty": "Section 73(9) - 10% of tax short paid (₹1,375) if paid before SCN adjudication",
        },
    },
    {
        "id": "case_002",
        "description": (
            "Arogya Pharma LLP (GSTIN: 06AABCA5678B1Z3), Gurugram, is a pharmaceutical distributor. "
            "For August 2023, GSTR-1 reflects B2B invoices of ₹38,72,500 at 12% GST (₹4,64,700 tax). "
            "GSTR-3B for the same month shows outward tax liability of ₹4,64,700 — exactly matching. "
            "Both returns were filed on time. The company has clean ITC reconciliation records."
        ),
        "question": (
            "Verify if there is any mismatch between GSTR-1 and GSTR-3B for Arogya Pharma LLP for "
            "August 2023. What is the GST difference and recommended action?"
        ),
        "correct_answer": {
            "mismatch": False,
            "gst_difference": 0,
            "gstr1_liability": 464700,
            "gstr3b_declared": 464700,
            "action": "No action required. Returns are reconciled. File compliance acknowledgment.",
            "penalty": "Nil",
        },
    },
    {
        "id": "case_003",
        "description": (
            "Bharat Auto Components Pvt Ltd (GSTIN: 09AABCB2345C1Z7), Noida, manufactures auto parts. "
            "For September 2023, GSTR-1 shows taxable supplies of ₹87,34,200 at 28% GST, "
            "implying liability of ₹24,45,576. GSTR-3B declares only ₹21,80,000 as output tax. "
            "The company claims some credit notes were not reflected in GSTR-1. "
            "However, no credit notes were uploaded in GSTR-1 for this period."
        ),
        "question": (
            "Calculate the mismatch in output tax liability for Bharat Auto Components Pvt Ltd for "
            "September 2023. Identify applicable sections and calculate interest for 45-day delay."
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 265576,
            "gstr1_liability": 2445576,
            "gstr3b_declared": 2180000,
            "interest_days": 45,
            "interest_amount": round(265576 * 0.18 * 45 / 365),
            "action": "Issue SCN under Section 73 CGST Act; Demand tax shortfall ₹2,65,576 + interest ₹5,896 under Section 50(1)",
            "penalty": "Section 73(9) - 10% of ₹2,65,576 = ₹26,558 if paid within 30 days of SCN",
        },
    },
    {
        "id": "case_004",
        "description": (
            "Nestfresh Foods Pvt Ltd (GSTIN: 33AABCN7890D1Z2), Chennai, is an FMCG company. "
            "For October 2023, GSTR-1 shows B2C large supplies of ₹1,24,67,800 split across 5% and 12% brackets. "
            "Taxable value at 5%: ₹72,45,600 (GST ₹3,62,280); at 12%: ₹52,22,200 (GST ₹6,26,664). "
            "Total GSTR-1 liability: ₹9,88,944. GSTR-3B declares ₹10,23,500. "
            "The excess declaration in GSTR-3B benefits the government."
        ),
        "question": (
            "Analyze the GSTR-1 vs GSTR-3B position for Nestfresh Foods Pvt Ltd for October 2023. "
            "Is there a mismatch, and if so, is any legal action required?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": -34556,
            "gstr1_liability": 988944,
            "gstr3b_declared": 1023500,
            "action": "Excess tax paid in GSTR-3B (₹34,556). Taxpayer can claim refund of excess under Section 54 CGST Act or adjust in subsequent month. No penalty applicable as no revenue loss to government.",
            "penalty": "Nil - excess payment, not short payment",
        },
    },
    {
        "id": "case_005",
        "description": (
            "Techwave IT Solutions LLP (GSTIN: 29AABCT3456E1Z8), Bengaluru, provides IT services. "
            "For November 2023, GSTR-1 shows export of services (zero rated with LUT) of ₹45,32,000 "
            "and domestic B2B supplies at 18%: ₹23,17,500 (GST ₹4,17,150). "
            "GSTR-3B declares output tax of ₹3,95,000 only. "
            "The company could not explain the ₹22,150 difference in the domestic supply tax."
        ),
        "question": (
            "Determine the GST mismatch for Techwave IT Solutions LLP for November 2023, "
            "separating the zero-rated export component from domestic supplies. "
            "What is the correct action under CGST Act 2017?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 22150,
            "gstr1_liability": 417150,
            "gstr3b_declared": 395000,
            "export_component": "Zero-rated LUT exports correctly declared at nil tax",
            "action": "Issue notice for short payment of ₹22,150 on domestic supplies under Section 73 CGST Act. Section 50 interest applicable from November due date.",
            "penalty": "10% of ₹22,150 = ₹2,215 under Section 73(9)",
        },
    },
    {
        "id": "case_006",
        "description": (
            "Annapurna Restaurants Pvt Ltd (GSTIN: 36AABCA4321F1Z6), Hyderabad, operates restaurant chains. "
            "For December 2023, GSTR-1 shows dining services at 5% (no ITC): taxable value ₹34,56,200, "
            "GST ₹1,72,810. GSTR-3B correctly shows ₹1,72,810 tax liability. "
            "All returns filed before due dates. Reconciliation matches perfectly."
        ),
        "question": (
            "Verify GSTR-1 vs GSTR-3B reconciliation for Annapurna Restaurants Pvt Ltd for December 2023. "
            "What is the mismatch amount and applicable action?"
        ),
        "correct_answer": {
            "mismatch": False,
            "gst_difference": 0,
            "gstr1_liability": 172810,
            "gstr3b_declared": 172810,
            "action": "No mismatch. Returns reconciled. Note: Restaurant under composition-like 5% scheme cannot avail ITC on inputs.",
            "penalty": "Nil",
        },
    },
    {
        "id": "case_007",
        "description": (
            "Skyline Construction Pvt Ltd (GSTIN: 07AABCS5678G1Z4), Delhi, undertakes civil works contracts. "
            "For January 2024, GSTR-1 shows works contract services at 18%: taxable ₹1,56,78,900, "
            "GST ₹28,22,202. GSTR-3B shows output tax of ₹25,67,000. "
            "The company's accountant filed GSTR-3B incorrectly classifying some supplies at 12% instead of 18%. "
            "The difference of ₹2,55,202 remains unpaid."
        ),
        "question": (
            "Calculate the total GST mismatch and interest liability for Skyline Construction Pvt Ltd "
            "for January 2024 (assume 60-day delay). Reference applicable CGST Act sections."
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 255202,
            "gstr1_liability": 2822202,
            "gstr3b_declared": 2567000,
            "interest_amount": round(255202 * 0.18 * 60 / 365),
            "action": "SCN under Section 73 CGST Act for misclassification and short payment. Demand ₹2,55,202 + interest ₹7,558 under Section 50.",
            "penalty": "Section 73(9) - ₹25,520 (10% of tax short paid)",
        },
    },
    {
        "id": "case_008",
        "description": (
            "Kapoor Textile Mills Pvt Ltd (GSTIN: 24AABCK2109H1Z1), Surat, exports fabrics. "
            "For February 2024, GSTR-1 shows: zero-rated exports ₹2,34,56,000 (IGST paid ₹42,22,080 at 18%), "
            "and domestic sales at 5%: ₹18,43,200 (GST ₹92,160). Total GSTR-1 liability: ₹43,14,240. "
            "GSTR-3B shows only ₹92,160 (only domestic). "
            "The company claims IGST on exports is refundable so it need not show in GSTR-3B."
        ),
        "question": (
            "Evaluate whether Kapoor Textile Mills Pvt Ltd correctly excluded IGST paid on exports "
            "from GSTR-3B for February 2024. What is the mismatch and legal position?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 4222080,
            "gstr1_liability": 4314240,
            "gstr3b_declared": 92160,
            "action": "IGST paid on exports MUST be declared in GSTR-3B Table 3.1(b). Mismatch of ₹42,22,080 must be reported. Refund claim under Section 54(3) must be filed separately. Issue notice under Section 73 for non-disclosure.",
            "penalty": "Interest under Section 50 if IGST was not actually paid to government",
        },
    },
    {
        "id": "case_009",
        "description": (
            "PharmaPlus Distributors (Proprietorship, GSTIN: 19AABCP6543I1Z9), Kolkata, distributes medicines. "
            "For March 2024, GSTR-1 shows: 12% GST supplies ₹23,45,600 (tax ₹2,81,472), "
            "5% GST supplies ₹14,67,300 (tax ₹73,365). Total tax: ₹3,54,837. "
            "GSTR-3B shows ₹3,54,837 — exact match. Returns filed 2 days late but tax paid on time via challan."
        ),
        "question": (
            "Assess the GSTR-1 vs GSTR-3B position for PharmaPlus Distributors for March 2024. "
            "Is there a mismatch? What is the implication of late filing?"
        ),
        "correct_answer": {
            "mismatch": False,
            "gst_difference": 0,
            "gstr1_liability": 354837,
            "gstr3b_declared": 354837,
            "action": "No tax mismatch. Late filing fee applicable under Section 47: ₹50/day for CGST + ₹50/day for SGST (max ₹5,000 each) = ₹100/day for 2 days = ₹200 total late fee.",
            "penalty": "Late fee ₹200 under Section 47 CGST Act",
        },
    },
    {
        "id": "case_010",
        "description": (
            "RapidBuild Infrastructure LLP (GSTIN: 08AABCR3217J1Z6), Jaipur, is in construction business. "
            "For April 2024, GSTR-1 reflects: mixed supplies including 18% works contract ₹67,89,400 "
            "(tax ₹12,22,092) and 12% real estate supply ₹43,21,600 (tax ₹5,18,592). "
            "Total GSTR-1 tax: ₹17,40,684. GSTR-3B shows ₹17,40,000 — difference of ₹684. "
            "The tiny difference is due to rounding in the software."
        ),
        "question": (
            "Determine the mismatch for RapidBuild Infrastructure LLP for April 2024. "
            "Is a rounding difference of ₹684 actionable under CGST Act?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 684,
            "gstr1_liability": 1740684,
            "gstr3b_declared": 1740000,
            "action": "Technical mismatch of ₹684 due to rounding. Under CGST Rules, rounding differences up to ₹1 per transaction are acceptable. Taxpayer should rectify in next return. No formal SCN warranted but reconciliation note should be maintained.",
            "penalty": "Minimal — advisory notice only; no penalty for de minimis rounding error",
        },
    },
    {
        "id": "case_011",
        "description": (
            "Vasundhara Agro Pvt Ltd (GSTIN: 20AABCV4532K1Z3), Bhubaneswar, processes agricultural goods. "
            "For May 2024, GSTR-1 shows nil-rated supplies ₹45,67,000 (0% GST), "
            "exempt supplies ₹12,34,500, and 5% taxable supplies ₹8,92,300 (tax ₹44,615). "
            "GSTR-3B declares total output tax ₹44,615 — which matches. "
            "However, the company incorrectly included exempt supplies in Table 3.1(a) instead of 3.1(c)."
        ),
        "question": (
            "Analyze Vasundhara Agro Pvt Ltd's GSTR-3B filing error for May 2024. "
            "Is there a tax mismatch? What corrective action and ITC reversal implications exist?"
        ),
        "correct_answer": {
            "mismatch": False,
            "gst_difference": 0,
            "gstr1_liability": 44615,
            "gstr3b_declared": 44615,
            "action": "No tax mismatch but classification error in GSTR-3B. Exempt supplies must be in Table 3.1(c) not 3.1(a). ITC reversal required under Rule 42 for exempt supplies proportion. Issue advisory for correction in future returns.",
            "penalty": "ITC reversal may create additional liability; advisory notice recommended",
        },
    },
    {
        "id": "case_012",
        "description": (
            "Galaxy Electronics Pvt Ltd (GSTIN: 27AABCG7654L1Z7), Pune, is an electronics retailer. "
            "For June 2024, GSTR-1 shows consumer electronics at 18% GST: taxable ₹2,34,56,700 (tax ₹42,22,206). "
            "GSTR-3B declares ₹38,45,000. Difference: ₹3,77,206. "
            "Investigation reveals the company collected ₹42,22,206 from customers but remitted only ₹38,45,000. "
            "The balance ₹3,77,206 was retained by the company."
        ),
        "question": (
            "Evaluate the mismatch for Galaxy Electronics Pvt Ltd for June 2024. "
            "If tax was collected but not remitted, what enhanced penalty provisions apply under CGST Act?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 377206,
            "gstr1_liability": 4222206,
            "gstr3b_declared": 3845000,
            "action": "Collected tax not remitted is an aggravated offense. Section 76 CGST Act applies — person who collects tax must pay to government. Also attracts Section 74 (fraud/suppression) with 100% penalty + Section 132 criminal prosecution possible.",
            "penalty": "100% of ₹3,77,206 = ₹3,77,206 under Section 74 + criminal liability under Section 132(1)(e)",
        },
    },
    {
        "id": "case_013",
        "description": (
            "Himalayan Beverages Pvt Ltd (GSTIN: 05AABCH8901M1Z2), Dehradun, manufactures aerated drinks. "
            "For July 2024, GSTR-1 shows aerated drinks at 28% + 12% cess: "
            "taxable ₹89,23,400, GST ₹24,98,552 (28%), cess ₹10,70,808 (12%). Total: ₹35,69,360. "
            "GSTR-3B shows GST ₹24,98,552 correctly but cess of only ₹8,92,340 — cess underpaid by ₹1,78,468."
        ),
        "question": (
            "Calculate the cess mismatch for Himalayan Beverages Pvt Ltd for July 2024. "
            "Does cess short payment attract separate penalty provisions under CGST Act?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 178468,
            "gstr1_liability": 3569360,
            "gstr3b_declared": 3390892,
            "action": "Cess short payment of ₹1,78,468. GST Compensation Cess Act 2017 applies. Section 73/74 CGST Act applies mutatis mutandis. SCN to be issued for cess recovery + interest under Section 50.",
            "penalty": "10% of ₹1,78,468 = ₹17,847 under Section 73(9) for cess short payment",
        },
    },
    {
        "id": "case_014",
        "description": (
            "Megha IT Services Pvt Ltd (GSTIN: 29AABCM2345N1Z5), Bengaluru, provides software services. "
            "For August 2024, GSTR-1 shows: domestic B2B at 18%: ₹1,23,45,600 (tax ₹22,22,208), "
            "SEZ supplies (zero rated): ₹34,56,700. GSTR-3B shows ₹22,22,208. "
            "Reconciliation is perfect. All supplies correctly classified. Returns filed on time."
        ),
        "question": (
            "Confirm whether GSTR-1 vs GSTR-3B is reconciled for Megha IT Services Pvt Ltd for August 2024. "
            "What is the correct treatment of SEZ supplies in returns?"
        ),
        "correct_answer": {
            "mismatch": False,
            "gst_difference": 0,
            "gstr1_liability": 2222208,
            "gstr3b_declared": 2222208,
            "action": "No mismatch. SEZ supplies correctly shown as zero-rated in GSTR-1 Table 6A and GSTR-3B Table 3.1(b). No tax on SEZ supplies under Section 16(1)(b) IGST Act. Clean compliance.",
            "penalty": "Nil",
        },
    },
    {
        "id": "case_015",
        "description": (
            "Swiftpack FMCG Pvt Ltd (GSTIN: 06AABCS9012O1Z8), Gurgaon, is an FMCG manufacturer. "
            "For September 2024, GSTR-1 shows: 12% supplies ₹45,67,800 (tax ₹5,48,136), "
            "18% supplies ₹67,89,200 (tax ₹12,22,056), 28% supplies ₹23,45,600 (tax ₹6,56,768). "
            "Total GSTR-1: ₹24,26,960. GSTR-3B shows ₹21,89,450. Shortfall: ₹2,37,510. "
            "The company's CFO admits the 28% slab was mistakenly calculated at 18%."
        ),
        "question": (
            "Calculate the mismatch due to rate misclassification for Swiftpack FMCG Pvt Ltd "
            "for September 2024. What are the cumulative penalties for repeated misclassification (3rd time)?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 237510,
            "gstr1_liability": 2426960,
            "gstr3b_declared": 2189450,
            "action": "Third instance of rate misclassification. Section 73 SCN issued. Repeat offense may trigger Section 74 (fraud/deliberate misstatement) with 100% penalty. Section 122(1) additional penalty of ₹10,000 or tax evaded, whichever higher.",
            "penalty": "100% of ₹2,37,510 = ₹2,37,510 under Section 74 for repeated/deliberate misclassification",
        },
    },
    {
        "id": "case_016",
        "description": (
            "Deepak Engineering Works LLP (GSTIN: 09AABCD1234P1Z4), Kanpur, manufactures industrial equipment. "
            "For October 2024, GSTR-1 shows supplies at 18%: ₹3,45,67,800 (tax ₹62,22,204). "
            "GSTR-3B shows ₹55,00,000 — shortfall of ₹7,22,204. "
            "The company made advance payments in earlier months which it claims should be adjusted. "
            "However, no advance tax was paid in prior periods as confirmed by the tax portal."
        ),
        "question": (
            "Analyze the mismatch for Deepak Engineering Works LLP for October 2024. "
            "Can prior advance payments be adjusted against current liability without portal records?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 722204,
            "gstr1_liability": 6222204,
            "gstr3b_declared": 5500000,
            "action": "No evidence of advance tax payment on portal. Claim rejected. SCN under Section 73 for ₹7,22,204 shortfall + interest under Section 50. Advance tax payments must be in challan (PMT-06) to be adjusted.",
            "penalty": "Section 73(9) - ₹72,220 (10% of short paid tax) + interest from due date",
        },
    },
    {
        "id": "case_017",
        "description": (
            "Priya Fashion House (Proprietorship, GSTIN: 24AABCP5678Q1Z1), Ahmedabad, sells garments. "
            "For November 2024, GSTR-1 shows: exempt supplies (cotton fabric) ₹34,56,000, "
            "5% taxable (blended fabric) ₹23,45,600 (tax ₹1,17,280), "
            "12% taxable (branded apparel) ₹15,67,800 (tax ₹1,88,136). "
            "Total GSTR-1 tax: ₹3,05,416. GSTR-3B: ₹3,05,416. Perfect match."
        ),
        "question": (
            "Verify the GSTR-1 vs GSTR-3B position for Priya Fashion House for November 2024. "
            "Are there any ITC reversal implications for the exempt supplies?"
        ),
        "correct_answer": {
            "mismatch": False,
            "gst_difference": 0,
            "gstr1_liability": 305416,
            "gstr3b_declared": 305416,
            "action": "No mismatch. ITC reversal required under Rule 42 for exempt supplies (cotton fabric ₹34,56,000). Reversal ratio = Exempt / Total turnover = 34,56,000 / 73,69,400 = 46.9%. ITC on common inputs must be proportionally reversed.",
            "penalty": "If ITC not reversed proportionally, demand under Section 73/74 for excess ITC",
        },
    },
    {
        "id": "case_018",
        "description": (
            "Coromandel Chemicals Pvt Ltd (GSTIN: 33AABCC3456R1Z9), Chennai, manufactures specialty chemicals. "
            "For December 2024, GSTR-1 shows: domestic 18% supplies ₹1,89,45,600 (tax ₹34,10,208), "
            "exports under LUT ₹67,89,400 (zero rated). GSTR-3B shows output tax ₹34,10,208. "
            "Additionally, the company received advance for future supplies but did not declare in GSTR-1 or GSTR-3B. "
            "Advance received: ₹23,45,000."
        ),
        "question": (
            "Identify all mismatches for Coromandel Chemicals Pvt Ltd for December 2024, "
            "including the treatment of advance receipts. What section governs tax on advances?"
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 422100,
            "gstr1_liability": 3410208,
            "gstr3b_declared": 3410208,
            "advance_tax_due": 422100,
            "action": "GSTR-1 vs GSTR-3B match for actual supplies. However, advance receipt of ₹23,45,000 @ 18% = ₹4,22,100 tax must be declared in GSTR-1 Table 11A and GSTR-3B Table 3.1(a) per Section 12(2) CGST Act. SCN under Section 73 for advance tax non-disclosure.",
            "penalty": "10% of ₹4,22,100 = ₹42,210 + interest under Section 50",
        },
    },
    {
        "id": "case_019",
        "description": (
            "Pinnacle Steel LLP (GSTIN: 20AABCP7890S1Z6), Rourkela, is a steel products manufacturer. "
            "For January 2025, GSTR-1 shows: 18% GST supplies ₹4,56,78,900 (tax ₹82,22,202). "
            "GSTR-3B shows ₹79,89,500. Shortfall: ₹2,32,702. "
            "Company claims ₹2,32,702 relates to credit notes issued post-filing of GSTR-1 "
            "but admits credit notes are not uploaded to portal."
        ),
        "question": (
            "Evaluate whether unuploaded credit notes can reduce GSTR-3B liability for Pinnacle Steel LLP "
            "for January 2025. Calculate mismatch and applicable remedy."
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 232702,
            "gstr1_liability": 8222202,
            "gstr3b_declared": 7989500,
            "action": "Credit notes must be uploaded in GSTR-1 Table 9B to be valid. Unuploaded credit notes cannot reduce output liability in GSTR-3B. SCN under Section 73 for ₹2,32,702. Company may upload credit notes in subsequent GSTR-1 and claim adjustment then.",
            "penalty": "Section 73(9) ₹23,270 + interest under Section 50 until payment",
        },
    },
    {
        "id": "case_020",
        "description": (
            "Orion Hospitality Pvt Ltd (GSTIN: 07AABCO5432T1Z3), Delhi, operates luxury hotels. "
            "For February 2025, GSTR-1 shows: hotel accommodation at 18% (tariff >₹7,500): "
            "₹2,34,56,700 (tax ₹42,22,206); restaurant services at 5%: ₹89,34,500 (tax ₹4,46,725); "
            "banquet hall at 18%: ₹67,23,400 (tax ₹12,10,212). Total GSTR-1 tax: ₹58,79,143. "
            "GSTR-3B shows ₹42,22,206 only (restaurant and banquet omitted). "
            "Shortfall: ₹16,56,937. Investigation reveals deliberate omission to reduce tax."
        ),
        "question": (
            "Calculate the total mismatch for Orion Hospitality Pvt Ltd for February 2025 "
            "and determine whether Section 73 or Section 74 applies given evidence of deliberate omission."
        ),
        "correct_answer": {
            "mismatch": True,
            "gst_difference": 1656937,
            "gstr1_liability": 5879143,
            "gstr3b_declared": 4222206,
            "action": "Deliberate omission of ₹16,56,937 attracts Section 74 CGST Act (fraud/suppression of facts). 100% penalty applicable. Section 132(1)(b) — evasion exceeding ₹5 crore is non-bailable offense; however ₹1.66 crore is below criminal threshold. Civil prosecution under Section 74 with 100% penalty.",
            "penalty": "100% of ₹16,56,937 = ₹16,56,937 under Section 74 + interest under Section 50(3) at 24% per annum",
        },
    },
]

# =============================================================================
# CATEGORY 2: TASK2_CASES - ITC Eligibility under Section 17(5) (25 Cases)
# =============================================================================

TASK2_CASES = [
    {
        "id": "case_021",
        "description": (
            "Shreeji Motors Pvt Ltd (GSTIN: 24AABCS2109A1Z6), Ahmedabad, is an auto dealership. "
            "For Q1 FY2024-25, the company purchased 5 passenger cars for directors at ₹12,45,000 each "
            "plus 28% GST (₹3,48,600 per car). Total cars: ₹62,25,000 + GST ₹17,43,000. "
            "The company also purchased 3 commercial vehicles (goods transport) at ₹18,50,000 each + 28% GST. "
            "GST on commercial vehicles: ₹15,54,000. Company claimed full ITC of ₹32,97,000."
        ),
        "question": (
            "Determine the eligible and ineligible ITC for Shreeji Motors Pvt Ltd under Section 17(5) CGST Act. "
            "Classify passenger car ITC and commercial vehicle ITC separately."
        ),
        "correct_answer": {
            "eligible_itc": 1554000,
            "ineligible_itc": 1743000,
            "blocked_items": ["Passenger cars for director use — Section 17(5)(a) blocked credit"],
            "excess_claimed": 1743000,
            "action": "ITC on 5 passenger cars ₹17,43,000 fully blocked under Section 17(5)(a). ITC on 3 commercial goods vehicles ₹15,54,000 fully eligible. Reverse ₹17,43,000 + interest under Section 50.",
        },
    },
    {
        "id": "case_022",
        "description": (
            "Infospark Technologies LLP (GSTIN: 29AABCI3456B1Z2), Bengaluru, is an IT company. "
            "For April 2024, the company paid ₹4,56,780 (+ 18% GST ₹82,220) for employee food catering. "
            "The same month, it purchased laptops for employees at ₹45,67,800 + 18% GST ₹8,22,204. "
            "It also paid club membership for senior executives: ₹2,34,000 + 18% GST ₹42,120. "
            "Total ITC claimed: ₹9,46,544."
        ),
        "question": (
            "Analyze ITC eligibility for Infospark Technologies LLP for April 2024 under Section 17(5). "
            "Calculate eligible, ineligible, and excess ITC claimed."
        ),
        "correct_answer": {
            "eligible_itc": 822204,
            "ineligible_itc": 124340,
            "blocked_items": [
                "Food catering for employees ₹82,220 — Section 17(5)(b)(i) blocked",
                "Club membership ₹42,120 — Section 17(5)(b)(ii) blocked",
            ],
            "excess_claimed": 124340,
            "action": "Laptop ITC ₹8,22,204 fully eligible (capital goods for business). Food catering and club memberships blocked under Section 17(5)(b). Reverse ₹1,24,340 with interest.",
        },
    },
    {
        "id": "case_023",
        "description": (
            "Greenfield Builders Pvt Ltd (GSTIN: 07AABCG4567C1Z8), Delhi, is a real estate developer. "
            "For May 2024, the company incurred: cement and steel for under-construction flats ₹89,45,600 + 18% GST ₹16,10,208; "
            "architect fees ₹12,34,500 + 18% GST ₹2,22,210; "
            "interior works (works contract) for own office ₹8,90,000 + 18% GST ₹1,60,200. "
            "Total ITC claimed: ₹19,92,618."
        ),
        "question": (
            "Determine ITC eligibility for Greenfield Builders Pvt Ltd for May 2024. "
            "How does Section 17(5)(c) and 17(5)(d) apply to construction inputs?"
        ),
        "correct_answer": {
            "eligible_itc": 222210,
            "ineligible_itc": 1770408,
            "blocked_items": [
                "Cement/steel for residential flat construction ₹16,10,208 — Section 17(5)(d) blocked (immovable property)",
                "Works contract for own office construction ₹1,60,200 — Section 17(5)(c) blocked",
            ],
            "excess_claimed": 1770408,
            "action": "Only architect fees ITC ₹2,22,210 eligible (professional services). Construction materials and works contract for immovable property blocked under Section 17(5)(c) and (d). Reverse ₹17,70,408.",
        },
    },
    {
        "id": "case_024",
        "description": (
            "SecureLife Insurance Pvt Ltd (GSTIN: 27AABCS6789D1Z5), Mumbai, is an insurance company. "
            "For June 2024, the company paid health insurance premium for 200 employees: "
            "₹15,67,800 + 18% GST ₹2,82,204 (mandatory health cover as per company policy). "
            "It also paid life insurance for 5 directors: ₹3,45,000 + 18% GST ₹62,100. "
            "Total ITC claimed: ₹3,44,304."
        ),
        "question": (
            "Assess ITC eligibility for SecureLife Insurance Pvt Ltd for June 2024 under Section 17(5). "
            "Is employee health insurance ITC blocked or allowed under any exception?"
        ),
        "correct_answer": {
            "eligible_itc": 282204,
            "ineligible_itc": 62100,
            "blocked_items": ["Life insurance for directors ₹62,100 — Section 17(5)(b)(iii) blocked (not mandatory obligation)"],
            "excess_claimed": 62100,
            "action": "Employee health insurance ₹2,82,204 is ELIGIBLE under Section 17(5)(b) exception — if employer obligated by law (e.g., ESI Act or company policy mandating health cover). Directors' life insurance ₹62,100 blocked — not a statutory obligation.",
        },
    },
    {
        "id": "case_025",
        "description": (
            "Royal Hospitality Pvt Ltd (GSTIN: 36AABCR7890E1Z1), Hyderabad, operates hotels. "
            "For July 2024, the company incurred: food supplies for hotel restaurant kitchen ₹23,45,600 + 5% GST ₹1,17,280; "
            "outdoor catering for a client event ₹8,90,000 + 18% GST ₹1,60,200; "
            "beverages for hotel bar (taxable supply): ₹12,34,500 + 18% GST ₹2,22,210. "
            "Total ITC claimed: ₹4,99,690."
        ),
        "question": (
            "Determine ITC eligibility for Royal Hospitality Pvt Ltd for July 2024. "
            "How does the nature of the hotel business affect food and beverage ITC eligibility under Section 17(5)?"
        ),
        "correct_answer": {
            "eligible_itc": 222210,
            "ineligible_itc": 277480,
            "blocked_items": [
                "Food supplies for kitchen ₹1,17,280 — Section 17(5)(b)(i) blocked unless output is taxable food supply",
                "Outdoor catering ₹1,60,200 — Section 17(5)(b)(i) blocked (catering services)",
            ],
            "excess_claimed": 277480,
            "action": "Beverages for hotel bar ITC ₹2,22,210 eligible (used to make taxable alcoholic beverage supply). Food/catering blocked under Section 17(5)(b)(i). However, if hotel makes taxable restaurant supply and food is input — partial eligibility arguable. Conservative approach: reverse ₹2,77,480.",
        },
    },
    {
        "id": "case_026",
        "description": (
            "Paramount Pharmaceuticals Pvt Ltd (GSTIN: 06AABCP1234F1Z7), Gurugram, manufactures medicines. "
            "For August 2024, it purchased: manufacturing machinery ₹1,23,45,600 + 18% GST ₹22,22,208; "
            "ambulance for factory health center: ₹18,50,000 + 28% GST ₹5,18,000; "
            "personal car for MD: ₹32,00,000 + 28% GST ₹8,96,000. "
            "Total ITC claimed: ₹36,36,208."
        ),
        "question": (
            "Calculate eligible and blocked ITC for Paramount Pharmaceuticals for August 2024. "
            "What is the GST treatment of ambulance procurement under Section 17(5)?"
        ),
        "correct_answer": {
            "eligible_itc": 2222208,
            "ineligible_itc": 1414000,
            "blocked_items": [
                "Personal car for MD ₹8,96,000 — Section 17(5)(a) blocked",
                "Ambulance ₹5,18,000 — Section 17(5)(a) blocked (ambulance is a motor vehicle; exception only for vehicles used to transport goods/passengers as business)",
            ],
            "excess_claimed": 1414000,
            "action": "Manufacturing machinery ITC ₹22,22,208 fully eligible. Ambulance ITC blocked — Section 17(5)(a) exception for ambulances is NOT available unless specifically transporting goods commercially. Personal car blocked. Reverse ₹14,14,000.",
        },
    },
    {
        "id": "case_027",
        "description": (
            "Spectrum Events Pvt Ltd (GSTIN: 29AABCS2345G1Z4), Bengaluru, organizes corporate events. "
            "For September 2024, the company spent: venue decoration (works contract) ₹34,56,000 + 18% GST ₹6,22,080; "
            "entertainment services for client event ₹12,45,000 + 18% GST ₹2,24,100; "
            "office renovation (works contract) ₹23,00,000 + 18% GST ₹4,14,000. "
            "Claimed full ITC: ₹12,60,180."
        ),
        "question": (
            "Analyze ITC eligibility for Spectrum Events Pvt Ltd for September 2024. "
            "Distinguish between works contract for client projects and own office renovation."
        ),
        "correct_answer": {
            "eligible_itc": 622080,
            "ineligible_itc": 638100,
            "blocked_items": [
                "Entertainment services ₹2,24,100 — Section 17(5)(b)(iv) blocked",
                "Office renovation works contract ₹4,14,000 — Section 17(5)(c) blocked (immovable property on own account)",
            ],
            "excess_claimed": 638100,
            "action": "Venue decoration for client event is input to taxable output service — ₹6,22,080 eligible. Entertainment blocked under Section 17(5)(b)(iv). Own office renovation blocked under Section 17(5)(c). Reverse ₹6,38,100.",
        },
    },
    {
        "id": "case_028",
        "description": (
            "National Logistics LLP (GSTIN: 09AABCN3456H1Z3), Noida, is a goods transport company (GTA). "
            "For October 2024, it purchased: 10 trucks at ₹45,00,000 each + 28% GST; "
            "truck insurance ₹4,56,000 + 18% GST ₹82,080; "
            "diesel (no ITC available on petroleum products); "
            "driver welfare food ₹2,34,000 + 5% GST ₹11,700. "
            "GST on trucks: ₹1,26,00,000. Total ITC claimed: ₹1,26,93,780."
        ),
        "question": (
            "Determine ITC eligibility for National Logistics LLP for October 2024. "
            "Do the motor vehicle ITC restrictions apply to goods transport companies?"
        ),
        "correct_answer": {
            "eligible_itc": 12682080,
            "ineligible_itc": 11700,
            "blocked_items": [
                "Driver food/welfare ₹11,700 — Section 17(5)(b)(i) blocked",
                "Diesel: No ITC available under Section 17(6) read with Section 9(4) — petroleum products excluded",
            ],
            "excess_claimed": 11700,
            "action": "Trucks ITC ₹1,26,00,000 FULLY ELIGIBLE — Section 17(5)(a) exception applies for motor vehicles used for transportation of goods as business. Insurance ITC ₹82,080 eligible. Driver food ₹11,700 blocked. Reverse only ₹11,700.",
        },
    },
    {
        "id": "case_029",
        "description": (
            "Luxe Apparel Pvt Ltd (GSTIN: 08AABCL4567I1Z9), Jaipur, manufactures branded clothing. "
            "For November 2024, the company incurred: "
            "CSR expenditure — building school in village: ₹45,00,000 + 18% GST ₹8,10,000; "
            "employee uniform (non-transferable): ₹3,45,600 + 18% GST ₹62,208; "
            "gifts to employees on Diwali (market value ₹50,000 per employee, 20 employees): total ₹10,00,000 + GST ₹1,80,000."
        ),
        "question": (
            "Calculate ITC eligibility for Luxe Apparel Pvt Ltd for November 2024. "
            "What is the treatment of CSR expenditure, employee uniforms, and Diwali gifts under Section 17(5)?"
        ),
        "correct_answer": {
            "eligible_itc": 62208,
            "ineligible_itc": 990000,
            "blocked_items": [
                "CSR school construction ₹8,10,000 — Section 17(5)(d) blocked (immovable property not for business)",
                "Diwali gifts ₹1,80,000 — Section 17(5)(h) blocked (gifts/free samples when no GST charged)",
            ],
            "excess_claimed": 990000,
            "action": "Uniform ITC ₹62,208 eligible (mandatory work attire, not gifts). CSR construction blocked (immovable, not in course of business). Gifts blocked under Section 17(5)(h) as no tax charged to recipient. Reverse ₹9,90,000.",
        },
    },
    {
        "id": "case_030",
        "description": (
            "Aditya Steel Manufacturing Pvt Ltd (GSTIN: 20AABCA5678J1Z6), Rourkela, produces steel. "
            "For December 2024, it procured: iron ore (raw material) ₹2,34,56,000 + 18% GST ₹42,22,080; "
            "plant maintenance services ₹23,45,600 + 18% GST ₹4,22,208; "
            "personal computer for MD's home use: ₹1,56,000 + 18% GST ₹28,080; "
            "factory canteen food (statutory under Factories Act): ₹5,67,000 + 5% GST ₹28,350. "
            "Total ITC claimed: ₹47,00,718."
        ),
        "question": (
            "Determine eligible ITC for Aditya Steel for December 2024. "
            "Does the Factories Act obligation change the eligibility of canteen food ITC?"
        ),
        "correct_answer": {
            "eligible_itc": 4644288,
            "ineligible_itc": 56430,
            "blocked_items": [
                "MD's home computer ₹28,080 — Section 17(5) blocked (personal use, not business)",
                "Canteen food ₹28,350 — Section 17(5)(b)(i) blocked EVEN IF mandatory under Factories Act (no exception for statutory food obligation)",
            ],
            "excess_claimed": 56430,
            "action": "Raw material and maintenance ITC fully eligible. Factory canteen food blocked even though mandatory — no statutory exception in Section 17(5)(b)(i) for food. MD's home computer blocked. Reverse ₹56,430.",
        },
    },
    {
        "id": "case_031",
        "description": (
            "Pioneer Real Estate Pvt Ltd (GSTIN: 27AABCP6789K1Z2), Mumbai, is a real estate developer. "
            "For January 2025, it constructed: commercial offices (for sale) — inputs GST ₹45,67,000; "
            "residential apartments (for sale before completion) — inputs GST ₹34,56,000; "
            "residential apartments (for sale after completion — exempt): inputs GST ₹23,45,000; "
            "own corporate office: inputs GST ₹12,34,000. "
            "Total ITC claimed: ₹1,16,02,000."
        ),
        "question": (
            "Determine category-wise ITC eligibility for Pioneer Real Estate for January 2025. "
            "How does the real estate project type affect ITC eligibility under Section 17(5)?"
        ),
        "correct_answer": {
            "eligible_itc": 4567000,
            "ineligible_itc": 7035000,
            "blocked_items": [
                "Residential apartments for sale after completion ₹23,45,000 — Section 17(5)(d) + exempt supply",
                "Own corporate office construction ₹12,34,000 — Section 17(5)(d) blocked",
                "Residential pre-completion sale ₹34,56,000 — eligible as ongoing supply but reversal required upon completion without sale",
            ],
            "excess_claimed": 3579000,
            "action": "Commercial office for sale — ₹45,67,000 eligible (taxable supply). Pre-completion residential — partially eligible; track and reverse on completion. Post-completion exempt residential blocked. Own office blocked. Net excess ITC: ₹35,79,000 to reverse.",
        },
    },
    {
        "id": "case_032",
        "description": (
            "FreshBite Restaurants Pvt Ltd (GSTIN: 33AABCF7890L1Z8), Chennai, runs QSR chain. "
            "For February 2025, it claimed ITC on: kitchen equipment ₹45,67,000 + 18% GST ₹8,22,060; "
            "raw food ingredients ₹23,45,000 + 5% GST ₹1,17,250; "
            "AC units for restaurant ₹12,34,000 + 18% GST ₹2,22,120; "
            "outdoor hoarding advertising: ₹5,67,000 + 18% GST ₹1,02,060. "
            "Restaurant charges 5% GST (no ITC scheme for restaurants). Total ITC claimed: ₹12,63,490."
        ),
        "question": (
            "Analyze ITC eligibility for FreshBite Restaurants under 5% no-ITC restaurant scheme for February 2025. "
            "Can a restaurant charging 5% GST claim any ITC at all?"
        ),
        "correct_answer": {
            "eligible_itc": 0,
            "ineligible_itc": 1263490,
            "blocked_items": [
                "All ITC blocked — Section 17(5)(b)(i) blocked for food inputs",
                "Restaurant under 5% GST scheme cannot claim ITC on any inputs — condition of the scheme",
                "Kitchen equipment, AC, advertising — ITC restricted when opting 5% no-ITC scheme",
            ],
            "excess_claimed": 1263490,
            "action": "Restaurants charging 5% GST under Notification 11/2017 CANNOT avail any ITC. This is a scheme condition, not just Section 17(5). All ₹12,63,490 ITC must be reversed. Penalty under Section 122 for wrongful ITC claim.",
        },
    },
    {
        "id": "case_033",
        "description": (
            "Zephyr Telecom Pvt Ltd (GSTIN: 07AABCZ1234M1Z5), Delhi, provides telecom services. "
            "For March 2025, it purchased: telecom towers (immovable fixture) — GST paid ₹67,89,000; "
            "mobile handsets as employee benefits: 50 phones at ₹45,000 + 18% GST each; "
            "network routers and switches for business: ₹34,56,000 + 18% GST ₹6,22,080; "
            "employee health insurance (mandatory per HR policy): ₹8,90,000 + 18% GST ₹1,60,200. "
            "Total ITC claimed: ₹79,77,780."
        ),
        "question": (
            "Calculate blocked and eligible ITC for Zephyr Telecom for March 2025. "
            "How are telecom towers classified for ITC purposes and what about employee mobile phones?"
        ),
        "correct_answer": {
            "eligible_itc": 788280,
            "ineligible_itc": 7089000,
            "blocked_items": [
                "Telecom towers ₹67,89,000 — Section 17(5)(d) blocked if immovable property (towers embedded in ground are immovable)",
                "Mobile phones for employees as benefit ₹4,05,000 — Section 17(5)(h) blocked (personal benefit/perk)",
            ],
            "excess_claimed": 7089000,
            "action": "Routers/switches ITC ₹6,22,080 eligible (capital goods for telecom service). Health insurance ₹1,60,200 eligible (mandatory per policy — exception applies). Towers blocked as immovable. Employee phones blocked as personal perk. Reverse ₹70,89,000.",
        },
    },
    {
        "id": "case_034",
        "description": (
            "Marigold Hotel & Resorts Pvt Ltd (GSTIN: 08AABCM2345N1Z1), Udaipur, is a luxury hotel. "
            "For April 2024, it claimed ITC on: fitness center equipment for hotel gym ₹12,34,000 + 28% GST ₹3,45,520; "
            "swimming pool construction ₹45,00,000 + 18% GST ₹8,10,000; "
            "guest room renovation (works contract) ₹67,89,000 + 18% GST ₹12,22,020; "
            "liquor for hotel bar ₹18,56,000 (no GST — liquor outside GST). "
            "Total ITC claimed: ₹23,77,540."
        ),
        "question": (
            "Determine ITC eligibility for Marigold Hotel for April 2024 under Section 17(5). "
            "Are hotel guest room renovations eligible as part of taxable hotel services?"
        ),
        "correct_answer": {
            "eligible_itc": 345520,
            "ineligible_itc": 2032020,
            "blocked_items": [
                "Swimming pool construction ₹8,10,000 — Section 17(5)(d) blocked (immovable property)",
                "Guest room renovation ₹12,22,020 — Section 17(5)(c) blocked (works contract for immovable property)",
                "Liquor: outside GST scope — no ITC issue",
            ],
            "excess_claimed": 2032020,
            "action": "Gym equipment ₹3,45,520 eligible (movable capital goods for hotel service). Pool and room renovation blocked. Guest room renovation — though used for taxable hotel service, Section 17(5)(c) blocks works contract ITC for immovable property regardless of use. Reverse ₹20,32,020.",
        },
    },
    {
        "id": "case_035",
        "description": (
            "Vertex IT Consulting LLP (GSTIN: 29AABCV3456O1Z4), Bengaluru, provides IT consulting. "
            "For May 2024, it claimed ITC on: business class air tickets for client site visits ₹8,90,000 + 5% GST ₹44,500; "
            "economy air tickets for junior staff: ₹3,45,000 + 5% GST ₹17,250; "
            "hotel stay for outstation employees: ₹4,56,000 + 12% GST ₹54,720; "
            "employee team building trip (leisure): ₹2,34,000 + 18% GST ₹42,120. "
            "Total ITC claimed: ₹1,58,590."
        ),
        "question": (
            "Determine ITC eligibility for Vertex IT Consulting for May 2024. "
            "Is travel ITC restricted for employees and how does purpose of travel matter?"
        ),
        "correct_answer": {
            "eligible_itc": 116470,
            "ineligible_itc": 42120,
            "blocked_items": [
                "Team building leisure trip ₹42,120 — Section 17(5)(b) blocked (recreation/entertainment)",
            ],
            "excess_claimed": 42120,
            "action": "Business travel (air tickets + hotel) ITC ₹1,16,470 eligible — travel for business purposes is not blocked under Section 17(5). Leisure team trip blocked under Section 17(5)(b)(ii) entertainment. Reverse ₹42,120 only.",
        },
    },
    {
        "id": "case_036",
        "description": (
            "Sunrise Solar Pvt Ltd (GSTIN: 24AABCS4567P1Z7), Ahmedabad, installs solar panels. "
            "For June 2024, it purchased: solar panels (goods) for client installation ₹2,34,56,000 + 5% GST ₹11,72,800; "
            "installation services (works contract) for client projects: ₹45,67,000 + 18% GST ₹8,22,060; "
            "rooftop solar for own factory ₹23,45,000 + 5% GST ₹1,17,250; "
            "EV charging stations (capital goods) for own facility: ₹12,34,000 + 5% GST ₹61,700. "
            "Total ITC claimed: ₹21,73,810."
        ),
        "question": (
            "Calculate ITC eligibility for Sunrise Solar Pvt Ltd for June 2024. "
            "How is the works contract ITC treated when it is both an input and a service to clients?"
        ),
        "correct_answer": {
            "eligible_itc": 1994860,
            "ineligible_itc": 178950,
            "blocked_items": [
                "Own factory rooftop solar ₹1,17,250 — Section 17(5)(d) blocked (immovable property for own use)",
                "EV charging stations ₹61,700 — blocked if permanently affixed to building (immovable); eligible if movable",
            ],
            "excess_claimed": 178950,
            "action": "Solar panels for client ₹11,72,800 and works contract for clients ₹8,22,060 — eligible (inputs for taxable outward supply). Own factory solar blocked. EV stations — if movable, ₹61,700 eligible; if fixed, blocked. Conservative reversal: ₹1,78,950.",
        },
    },
    {
        "id": "case_037",
        "description": (
            "Bharat Cement Pvt Ltd (GSTIN: 33AABCB5678Q1Z3), Chennai, is a cement manufacturer. "
            "For July 2024, it claimed ITC on: raw limestone from mines ₹1,23,45,000 + 18% GST ₹22,22,100; "
            "mining explosives (used in quarry) ₹34,56,000 + 18% GST ₹6,22,080; "
            "company township construction for worker housing ₹89,00,000 + 18% GST ₹16,02,000; "
            "CSR project — bore wells in nearby village: ₹12,00,000 + 18% GST ₹2,16,000. "
            "Total ITC claimed: ₹46,62,180."
        ),
        "question": (
            "Determine ITC eligibility for Bharat Cement for July 2024. "
            "Are worker housing and CSR constructions eligible for ITC under any exception?"
        ),
        "correct_answer": {
            "eligible_itc": 2844180,
            "ineligible_itc": 1818000,
            "blocked_items": [
                "Worker township construction ₹16,02,000 — Section 17(5)(d) blocked (immovable property)",
                "CSR bore wells ₹2,16,000 — Section 17(5)(d) blocked (not in course of furtherance of business)",
            ],
            "excess_claimed": 1818000,
            "action": "Limestone and explosives ITC fully eligible (manufacturing inputs). Worker housing — blocked under Section 17(5)(d) regardless of being for employees. CSR bore wells — not business activity, blocked. Reverse ₹18,18,000.",
        },
    },
    {
        "id": "case_038",
        "description": (
            "QuickDeliver E-Commerce LLP (GSTIN: 27AABCQ6789R1Z9), Mumbai, is an e-commerce operator. "
            "For August 2024, it claimed ITC on: delivery motorcycles for last-mile: ₹45,67,000 + 28% GST ₹12,78,760; "
            "warehouse racking systems (steel): ₹23,45,000 + 18% GST ₹4,22,100; "
            "employee gym at warehouse: ₹5,67,000 + 18% GST ₹1,02,060; "
            "packaging material: ₹12,34,000 + 18% GST ₹2,22,120. "
            "Total ITC claimed: ₹20,25,040."
        ),
        "question": (
            "Assess ITC eligibility for QuickDeliver E-Commerce for August 2024. "
            "Do delivery motorcycles qualify for ITC under the goods transport exception in Section 17(5)(a)?"
        ),
        "correct_answer": {
            "eligible_itc": 1923980,
            "ineligible_itc": 102060,
            "blocked_items": [
                "Employee gym ₹1,02,060 — Section 17(5)(b)(ii) blocked (recreation facility)",
            ],
            "excess_claimed": 102060,
            "action": "Delivery motorcycles ₹12,78,760 ELIGIBLE — Section 17(5)(a) exception for vehicles used for transportation of goods. Warehouse racking (capital goods) ₹4,22,100 eligible. Packaging ₹2,22,120 eligible. Gym ₹1,02,060 blocked. Reverse only ₹1,02,060.",
        },
    },
    {
        "id": "case_039",
        "description": (
            "Aroha Legal Services LLP (GSTIN: 07AABCA7890S1Z6), Delhi, is a law firm. "
            "For September 2024, it claimed ITC on: office furniture ₹8,90,000 + 18% GST ₹1,60,200; "
            "client entertainment at restaurant: ₹2,34,000 + 5% GST ₹11,700; "
            "advocate subscription to legal database: ₹4,56,000 + 18% GST ₹82,080; "
            "foreign bar council membership: ₹3,45,000 + 18% GST ₹62,100. "
            "Total ITC claimed: ₹3,16,080."
        ),
        "question": (
            "Calculate ITC eligibility for Aroha Legal Services LLP for September 2024. "
            "Are professional subscriptions and foreign memberships eligible under Section 17(5)?"
        ),
        "correct_answer": {
            "eligible_itc": 242280,
            "ineligible_itc": 73800,
            "blocked_items": [
                "Client entertainment at restaurant ₹11,700 — Section 17(5)(b)(i)/(iv) blocked",
                "Foreign bar council membership ₹62,100 — Section 17(5)(b)(ii) blocked (club/professional body membership)",
            ],
            "excess_claimed": 73800,
            "action": "Office furniture ITC ₹1,60,200 eligible. Legal database subscription ₹82,080 eligible (professional input). Client entertainment and foreign membership blocked under Section 17(5)(b). Reverse ₹73,800.",
        },
    },
    {
        "id": "case_040",
        "description": (
            "Kaleidoscope Media Pvt Ltd (GSTIN: 29AABCK1234T1Z2), Bengaluru, is a media production company. "
            "For October 2024, it claimed ITC on: video cameras and production equipment: ₹67,89,000 + 18% GST ₹12,22,020; "
            "film set construction (temporary structures): ₹23,45,000 + 18% GST ₹4,22,100; "
            "actor costumes for production: ₹8,90,000 + 5% GST ₹44,500; "
            "director's personal vehicle: ₹45,00,000 + 28% GST ₹12,60,000; "
            "OTT platform subscription for content research: ₹1,23,000 + 18% GST ₹22,140. "
            "Total ITC claimed: ₹29,70,760."
        ),
        "question": (
            "Determine ITC eligibility for Kaleidoscope Media Pvt Ltd for October 2024 under Section 17(5). "
            "Are temporary film sets treated as immovable property? Are actor costumes eligible?"
        ),
        "correct_answer": {
            "eligible_itc": 1710760,
            "ineligible_itc": 1260000,
            "blocked_items": [
                "Director's personal vehicle ₹12,60,000 — Section 17(5)(a) blocked",
            ],
            "excess_claimed": 1260000,
            "action": "Production equipment ₹12,22,020 eligible. Temporary film sets ₹4,22,100 eligible (temporary structures are movable/not immovable — 17(5)(d) does not apply). Costumes ₹44,500 eligible (production input). OTT subscription ₹22,140 eligible. Only director car ₹12,60,000 blocked. Reverse ₹12,60,000.",
        },
    },
    {
        "id": "case_041",
        "description": (
            "Ashirwad Trading Co (Proprietorship, GSTIN: 09AABCA2345U1Z8), Agra, is a leather goods trader. "
            "For November 2024, it claimed ITC on: leather inputs ₹45,67,000 + 18% GST ₹8,22,060; "
            "showroom renovation (works contract): ₹12,34,000 + 18% GST ₹2,22,120; "
            "personal life insurance for proprietor: ₹89,000 + 18% GST ₹16,020; "
            "business travel expenses: ₹3,45,000 + 5% GST ₹17,250; "
            "donation of goods to charity (cost ₹2,34,000): GST paid ₹42,120. "
            "Total ITC claimed: ₹11,19,570."
        ),
        "question": (
            "Determine ITC eligibility for Ashirwad Trading Co for November 2024 under Section 17(5). "
            "What is the ITC treatment for donated goods and proprietor's life insurance?"
        ),
        "correct_answer": {
            "eligible_itc": 839310,
            "ineligible_itc": 280260,
            "blocked_items": [
                "Showroom renovation ₹2,22,120 — Section 17(5)(c) blocked (works contract for immovable property)",
                "Proprietor life insurance ₹16,020 — Section 17(5)(b)(iii) blocked (personal insurance)",
                "Donated goods ₹42,120 — Section 17(5)(h) blocked (gifts/free supplies without GST charge)",
            ],
            "excess_claimed": 280260,
            "action": "Leather inputs ₹8,22,060 and travel ₹17,250 eligible. Showroom renovation, life insurance, donated goods blocked. Note: Donated goods also attract output GST under Schedule I if ITC was claimed. Reverse ₹2,80,260 + check output GST on donation.",
        },
    },
    {
        "id": "case_042",
        "description": (
            "Velocity Automobile Pvt Ltd (GSTIN: 24AABCV3456V1Z5), Surat, is an auto manufacturer. "
            "For December 2024, it claimed ITC on: steel for car manufacturing ₹5,67,89,000 + 18% GST ₹1,02,22,020; "
            "test drive vehicles (new models): 10 cars at ₹8,50,000 each + 28% GST = ₹23,80,000 GST; "
            "demo vehicles for dealers: 5 cars at ₹12,00,000 each + 28% GST = ₹16,80,000 GST; "
            "employees' subsidized canteen: ₹8,90,000 + 5% GST ₹44,500. "
            "Total ITC claimed: ₹1,43,26,520."
        ),
        "question": (
            "Determine ITC eligibility for Velocity Automobile for December 2024. "
            "Are test drive and demo vehicles for a car manufacturer eligible under Section 17(5)?"
        ),
        "correct_answer": {
            "eligible_itc": 10222020,
            "ineligible_itc": 4024500,
            "blocked_items": [
                "Test drive vehicles ₹23,80,000 — Section 17(5)(a) blocked even for manufacturer (unless in motor vehicle sales business)",
                "Demo vehicles for dealers ₹16,80,000 — Section 17(5)(a) blocked",
                "Subsidized canteen ₹44,500 — Section 17(5)(b)(i) blocked",
            ],
            "excess_claimed": 4024500,
            "action": "Steel for manufacturing ₹1,02,22,020 fully eligible. Test drive and demo cars blocked — manufacturer is not in 'business of selling motor vehicles' for these vehicles; they are used internally. Canteen blocked. Reverse ₹40,24,500. AAR rulings have split opinions; recommend filing advance ruling.",
        },
    },
    {
        "id": "case_043",
        "description": (
            "Meridian Financial Services Pvt Ltd (GSTIN: 27AABCM4567W1Z1), Mumbai, provides financial services. "
            "For January 2025, it claimed ITC on: computer servers ₹34,56,000 + 18% GST ₹6,22,080; "
            "office lease deposit refurbishment (works contract): ₹23,45,000 + 18% GST ₹4,22,100; "
            "outdoor advertising for brand promotion: ₹12,34,000 + 18% GST ₹2,22,120; "
            "conference room AV equipment: ₹8,90,000 + 18% GST ₹1,60,200. "
            "Company provides both taxable (fee-based) and exempt (interest income) financial services. "
            "Exempt proportion: 65%; Taxable: 35%."
        ),
        "question": (
            "Calculate eligible ITC for Meridian Financial Services for January 2025 under Section 17(2) "
            "read with Rule 42 for proportionate ITC, and also apply Section 17(5) restrictions."
        ),
        "correct_answer": {
            "eligible_itc": 353901,
            "ineligible_itc": 1072599,
            "blocked_items": [
                "Office lease refurbishment (works contract) ₹4,22,100 — Section 17(5)(c) blocked entirely",
                "Remaining ITC (servers + advertising + AV) subject to 35% taxable proportion under Rule 42",
            ],
            "excess_claimed": 1072599,
            "action": "Works contract ₹4,22,100 fully blocked under Section 17(5)(c). Remaining eligible ITC (servers ₹6,22,080 + advertising ₹2,22,120 + AV ₹1,60,200 = ₹10,04,400) restricted to 35% taxable proportion = ₹3,51,540. Add Rule 42 reverse ₹6,52,860. Total eligible: ₹3,51,540. Reverse total: ₹10,74,660.",
        },
    },
    {
        "id": "case_044",
        "description": (
            "Sunrise Dairy Products Pvt Ltd (GSTIN: 06AABCS5678X1Z4), Karnal, manufactures dairy products. "
            "For February 2025, it claimed ITC on: milk processing plant machinery ₹2,34,56,000 + 18% GST ₹42,22,080; "
            "refrigerated trucks for milk distribution: 5 trucks at ₹35,00,000 + 12% GST; total GST ₹21,00,000; "
            "cold storage construction: ₹67,89,000 + 18% GST ₹12,22,020; "
            "veterinary services for dairy cattle: ₹4,56,000 + 18% GST ₹82,080. "
            "Total ITC claimed: ₹76,26,180."
        ),
        "question": (
            "Determine ITC eligibility for Sunrise Dairy Products for February 2025. "
            "Are veterinary services for cattle eligible as business inputs and how is cold storage classified?"
        ),
        "correct_answer": {
            "eligible_itc": 6344160,
            "ineligible_itc": 1222020,
            "blocked_items": [
                "Cold storage construction ₹12,22,020 — Section 17(5)(d) blocked (immovable property)",
            ],
            "excess_claimed": 1222020,
            "action": "Plant machinery ₹42,22,080 eligible. Refrigerated trucks ₹21,00,000 eligible (goods transport vehicles). Veterinary services ₹82,080 eligible (business input — cattle are production assets). Cold storage construction blocked as immovable property. Reverse ₹12,22,020.",
        },
    },
    {
        "id": "case_045",
        "description": (
            "Polaris Shipping Pvt Ltd (GSTIN: 27AABCP6789Y1Z7), Mumbai, operates coastal vessels. "
            "For March 2025, it claimed ITC on: vessel engine overhaul: ₹89,45,000 + 18% GST ₹16,10,100; "
            "passenger cruise ship purchase: ₹12,00,00,000 + 5% GST ₹60,00,000; "
            "crew uniforms: ₹3,45,000 + 5% GST ₹17,250; "
            "crew accommodation on vessel (food): ₹8,90,000 + 5% GST ₹44,500; "
            "port terminal construction: ₹2,34,00,000 + 18% GST ₹42,12,000. "
            "Total ITC claimed: ₹1,18,83,850."
        ),
        "question": (
            "Calculate ITC eligibility for Polaris Shipping for March 2025. "
            "Does the Section 17(5)(a) motor vehicle restriction apply to vessels and ships?"
        ),
        "correct_answer": {
            "eligible_itc": 7627350,
            "ineligible_itc": 4256500,
            "blocked_items": [
                "Port terminal construction ₹42,12,000 — Section 17(5)(d) blocked (immovable property)",
                "Crew food/accommodation ₹44,500 — Section 17(5)(b)(i) blocked",
            ],
            "excess_claimed": 4256500,
            "action": "Section 17(5)(a) restrictions on 'motor vehicles' do NOT apply to vessels/ships — motor vehicle definition excludes vessels. Cruise ship purchase ₹60,00,000 eligible. Engine overhaul ₹16,10,100 eligible. Crew uniforms ₹17,250 eligible. Crew food ₹44,500 blocked. Port terminal ₹42,12,000 blocked. Reverse ₹42,56,500.",
        },
    },
]

# =============================================================================
# CATEGORY 3: TASK3_CASES - Fraud Detection (15 Cases)
# =============================================================================

TASK3_CASES = [
    {
        "id": "case_046",
        "description": (
            "Phantom Traders Pvt Ltd (GSTIN: 07AABCP1234A1Z6), Delhi, registered in January 2023. "
            "The company claimed ₹3,45,67,000 ITC in 6 months from non-existent suppliers. "
            "Physical verification found no business premises. All directors have multiple GSTINs. "
            "Supplier GSTINs are cancelled or never-filed entities. "
            "The company transferred all ITC to downstream buyers immediately without any genuine supply."
        ),
        "question": (
            "Identify fraud indicators for Phantom Traders and recommend enforcement actions with specific CGST Act sections."
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Missing Trader / Fake ITC Generator",
            "indicators": [
                "No physical business premises",
                "ITC claimed from cancelled/non-filing suppliers",
                "Immediate ITC transfer without genuine supply",
                "Multiple GSTINs for same directors",
                "New registration with massive ITC in short time",
            ],
            "fake_itc_amount": 34567000,
            "enforcement_actions": [
                "Provisional attachment under Section 83 CGST Act",
                "Arrest under Section 69 read with Section 132 (ITC fraud > ₹5 crore — cognizable and non-bailable)",
                "Demand + 100% penalty under Section 74",
                "Cancellation of registration under Section 29(2)(e)",
                "CGST Rule 21A suspension of GSTIN",
            ],
        },
    },
    {
        "id": "case_047",
        "description": (
            "Alpha Enterprises (GSTIN: 27AABCA2345B1Z2) and Beta Traders (GSTIN: 27AABCB3456C1Z8) "
            "and Gamma Pvt Ltd (GSTIN: 27AABCG4567D1Z5) are Mumbai-based entities with common directors. "
            "Alpha sells to Beta (invoice ₹2,34,56,000 + 18% GST), Beta sells to Gamma (₹2,40,00,000 + 18%), "
            "Gamma sells back to Alpha (₹2,50,00,000 + 18%). "
            "Physical goods worth ₹12,34,000 only actually moved. All three claim full ITC."
        ),
        "question": (
            "Detect the fraud type for the Alpha-Beta-Gamma transaction cycle. "
            "Calculate the fake ITC amount generated and recommend enforcement actions."
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Circular Trading / Round Tripping",
            "indicators": [
                "Common directors across all 3 entities",
                "Invoice values escalating in circular pattern",
                "Physical goods worth only ₹12,34,000 vs invoices of ₹7,24,56,000",
                "ITC claimed by all three on circular invoices",
                "No economic substance in transactions",
            ],
            "fake_itc_amount": round(
                (23456000 + 24000000 + 25000000) * 0.18 - 1234000 * 0.18
            ),
            "enforcement_actions": [
                "Section 74 — Fraud and suppression, 100% penalty",
                "Section 132(1)(b) — Circular trading for fake ITC — cognizable offense",
                "Section 83 — Provisional attachment of all three entities' assets",
                "Joint prosecution of all common directors",
                "Section 28 — Amendment/cancellation of all registrations",
            ],
        },
    },
    {
        "id": "case_048",
        "description": (
            "Reliable Goods Pvt Ltd (GSTIN: 29AABCR5678E1Z1), Bengaluru, is a genuine 15-year-old trading company. "
            "For FY2023-24, turnover is ₹23,45,67,000 with ITC of ₹3,45,78,000 (14.7% of turnover — normal for trading). "
            "Physical verification confirms active business with 45 employees, proper warehouse, and regular customers. "
            "All supplier GSTINs are active and filing returns. No common directors with suspicious entities. "
            "GSTR-2B fully matches claimed ITC."
        ),
        "question": (
            "Evaluate whether Reliable Goods Pvt Ltd is a fraud case based on the given indicators. "
            "What distinguishes this from a fraudulent entity?"
        ),
        "correct_answer": {
            "is_fraud": False,
            "fraud_type": "Genuine Business — Not Fraud",
            "indicators": [
                "15-year operating history",
                "Physical presence confirmed with 45 employees",
                "ITC proportion normal for trading business",
                "All supplier GSTINs active and compliant",
                "GSTR-2B and claimed ITC match exactly",
            ],
            "fake_itc_amount": 0,
            "enforcement_actions": [
                "No enforcement action required",
                "Mark as low-risk taxpayer in GSTN system",
                "Standard scrutiny assessment only",
            ],
        },
    },
    {
        "id": "case_049",
        "description": (
            "Suncrest Exports Pvt Ltd (GSTIN: 33AABCS6789F1Z7), Chennai, claims export refunds. "
            "For FY2023-24, it claims exports of ₹45,67,89,000 to fictitious foreign buyers. "
            "Shipping bills filed show exports to 'Dubai General Trading LLC' — a shell company. "
            "Forex realization not received within RBI-prescribed timelines. "
            "ITC of ₹8,23,02,000 claimed and refund of ₹8,23,02,000 sought. "
            "Investigation reveals goods never actually left India — warehouse records show continuous stock."
        ),
        "question": (
            "Identify fraud type for Suncrest Exports and determine enforcement actions. "
            "What specific CGST and Customs Act provisions apply for fake export fraud?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Fake Exports / Export Refund Fraud",
            "indicators": [
                "Shipping bills to shell company abroad",
                "Forex not received within RBI timeline (FEMA violation)",
                "Warehouse stock records inconsistent with claimed exports",
                "No actual movement of goods verified",
                "Disproportionate export value for company size",
            ],
            "fake_itc_amount": 82302000,
            "enforcement_actions": [
                "Section 74 CGST Act — 100% penalty on fraudulently claimed refund",
                "Section 132(1)(l) — Fake export fraudulent refund — non-bailable offense",
                "Section 54(15) — Recovery of refund wrongly granted + 24% interest",
                "Coordination with Customs (Customs Act Section 135) for export document fraud",
                "FEMA action for forex non-repatriation through ED",
                "Provisional attachment under Section 83",
            ],
        },
    },
    {
        "id": "case_050",
        "description": (
            "Brightway Commodities LLP (GSTIN: 06AABCB7890G1Z4), Gurgaon, purchased goods from "
            "12 different suppliers, all registered on the same date in the same locality with different PANs. "
            "All 12 suppliers show identical turnover patterns and file returns only for 2 months then go dormant. "
            "Brightway's ITC of ₹67,89,45,000 is sourced 89% from these 12 suppliers. "
            "GST portal GSTR-2B matches as suppliers filed GSTR-1 before cancellation. "
            "However, e-way bills show goods transported to locations different from buyer's registered address."
        ),
        "question": (
            "Analyze the Brightway Commodities fraud pattern. Does GSTR-2B match protect the buyer from ITC reversal?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Fake Invoice / Shell Supplier Network",
            "indicators": [
                "12 suppliers registered same date, same locality",
                "Identical turnover patterns across all 12 (coordinated fraud)",
                "89% ITC concentration from suspicious suppliers",
                "Suppliers go dormant after 2 months",
                "E-way bill destinations don't match buyer address",
            ],
            "fake_itc_amount": round(6789450000 * 0.89),
            "enforcement_actions": [
                "Section 74 — ITC reversal + 100% penalty despite GSTR-2B match (GSTR-2B match is necessary but NOT sufficient if fraud proven)",
                "Circular No. 171/03/2022-GST — Buyer responsibility to verify supplier genuineness",
                "Section 132(1)(c) — Fraudulent availment of ITC",
                "Attachment of Brightway's assets under Section 83",
                "Recovery from buyer under Section 74 — knowledge of fraud attributed",
            ],
        },
    },
    {
        "id": "case_051",
        "description": (
            "Mahalaxmi Textiles Pvt Ltd (GSTIN: 24AABCM1234H1Z3), Surat, is a 20-year-old textile company. "
            "Annual turnover: ₹1,23,45,67,000. For FY2023-24, ITC claimed: ₹8,90,12,000 (7.2% — normal for textiles). "
            "One supplier, recently suspended, provided invoices of ₹45,67,000 (GST ₹2,28,350). "
            "Mahalaxmi had no knowledge of supplier's suspension. Payment made via banking channels. "
            "Physical goods received and used in production. All other 47 suppliers are clean."
        ),
        "question": (
            "Evaluate fraud risk for Mahalaxmi Textiles regarding the suspended supplier's ITC. "
            "What protection is available to a bona fide buyer?"
        ),
        "correct_answer": {
            "is_fraud": False,
            "fraud_type": "Not Fraud — Bona Fide Buyer with Suspended Supplier Issue",
            "indicators": [
                "20-year established business with clean history",
                "ITC proportion normal (7.2%)",
                "Payment through banking channels",
                "Physical goods received and used",
                "Only 1 out of 48 suppliers is problematic",
            ],
            "fake_itc_amount": 0,
            "enforcement_actions": [
                "ITC of ₹2,28,350 from suspended supplier may be recovered under Rule 86A",
                "Buyer can contest if can prove goods received and no knowledge of fraud",
                "Section 73 (not 74) applicable — no mens rea established",
                "Mahalaxmi should obtain indemnity from supplier and pursue civil remedy",
                "No criminal prosecution — bona fide buyer",
            ],
        },
    },
    {
        "id": "case_052",
        "description": (
            "Futura Steel Trading (Proprietorship, GSTIN: 09AABCF2345I1Z9), Kanpur, claims purchases of "
            "industrial steel coils at ₹3,45,67,890 + 18% GST ₹62,22,220 from a single supplier. "
            "Claimed ITC: ₹62,22,220. However, the supplier (GSTIN: 09AABCS3456J1Z6) has annual turnover "
            "of only ₹23,45,000 in its own GSTR-1. The alleged sale of ₹3,45,67,890 is 14.7 times the "
            "supplier's total declared turnover. No transport records or e-way bills found for this consignment."
        ),
        "question": (
            "Identify fraud indicators for Futura Steel Trading. What is the maximum ITC that could be genuine "
            "and what enforcement actions are applicable?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Inflated ITC / Fake Purchase Invoice",
            "indicators": [
                "Purchase amount 14.7x the supplier's total declared turnover",
                "No e-way bills for steel coil transport",
                "No transport records for heavy goods",
                "Supplier incapable of fulfilling order of this magnitude",
                "Proprietorship with no physical verification",
            ],
            "fake_itc_amount": 6222220,
            "enforcement_actions": [
                "Section 74 — Full ITC reversal ₹62,22,220 + 100% penalty",
                "Section 132(1)(c) — Fraudulent availment of ITC",
                "Cross-examination of supplier under Section 70",
                "Bank account attachment under Section 83",
                "FIR in coordination with state GST authorities for large-scale fraud",
            ],
        },
    },
    {
        "id": "case_053",
        "description": (
            "Apex Chemicals Pvt Ltd (GSTIN: 27AABCA4567K1Z6), Mumbai, has 23 employees and one factory unit. "
            "In FY2023-24, it claimed ITC of ₹4,56,78,000 from 8 suppliers. "
            "All 8 suppliers have GSTIN, filed GSTR-1, and payment made by RTGS. "
            "However, the company's electricity bill shows factory consumption of only 3,200 units/month — "
            "insufficient for the claimed production volume requiring 45,000 units/month. "
            "Physical stock is only ₹12,34,000 vs claimed purchases of ₹25,67,89,000."
        ),
        "question": (
            "Detect fraud for Apex Chemicals based on energy consumption and stock discrepancy. "
            "What forensic indicators are used and what is the estimated fake ITC?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Inflated Purchases / ITC Fraud via Paper Transactions",
            "indicators": [
                "Electricity consumption 3,200 units vs required 45,000 units for claimed production",
                "Physical stock ₹12.34L vs claimed purchases ₹25.67Cr (99.95% discrepancy)",
                "23 employees insufficient for claimed production volume",
                "Energy-to-production ratio forensic test fails",
                "Paper trail exists but physical reality contradicts",
            ],
            "fake_itc_amount": round(45678000 * 0.93),
            "enforcement_actions": [
                "Section 74 — Fraud by misrepresentation",
                "Forensic audit under Section 66 (special audit)",
                "Section 132(1)(b) — Issuance of invoice without actual supply",
                "Third party data correlation (electricity, labor, logistics) as evidence",
                "Demand full reversal + 100% penalty + interest at 24% under Section 50(3)",
            ],
        },
    },
    {
        "id": "case_054",
        "description": (
            "Neptune Gems & Jewellery Pvt Ltd (GSTIN: 24AABCN5678L1Z2), Surat, exports cut diamonds. "
            "It claims deemed export benefits under Notification 48/2017-CT for supplies to SEZ unit. "
            "Refund claimed: ₹34,56,78,000. SEZ unit (buyer) has separately claimed the same tax as ITC. "
            "Both the supplier and SEZ buyer filed refund/ITC claims for the identical tax amount — "
            "double benefit of ₹34,56,78,000. Investigation reveals collusion between the two entities' management."
        ),
        "question": (
            "Identify the fraud type for Neptune Gems and calculate the total government revenue loss. "
            "What sections apply for double-claiming tax benefits?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Double Benefit Fraud — Deemed Export + Buyer ITC",
            "indicators": [
                "Same tax claimed twice — as refund by supplier and ITC by SEZ buyer",
                "Management collusion between supplier and SEZ buyer",
                "Deemed export notification misuse",
                "Unusually high refund claim to turnover ratio",
                "Coordinated filing of refund and ITC claims for same transaction",
            ],
            "fake_itc_amount": 345678000,
            "enforcement_actions": [
                "Section 74 — Fraud in refund claim + fraudulent ITC",
                "Section 54(15) — Recovery of wrongly granted refund + 24% interest",
                "Section 132(1)(l) — Fraudulent refund by misrepresentation",
                "Joint action against both Neptune and SEZ buyer under Section 122(1A) — abetment",
                "DGGSTI referral for organized refund fraud",
                "Provisional attachment of both companies under Section 83",
            ],
        },
    },
    {
        "id": "case_055",
        "description": (
            "Kiran Enterprises (Proprietorship, GSTIN: 33AABCK6789M1Z8), Coimbatore, is a genuine textile trader. "
            "Annual turnover ₹3,45,67,000. ITC claimed ₹18,23,000 (5.3% — reasonable for textiles). "
            "Tax intelligence flagged the proprietor's name appearing in a fraud network list from another state. "
            "However, investigation reveals this is a different person with same name. "
            "All transactions verified with physical goods movement, banking payments, and active customers."
        ),
        "question": (
            "Evaluate the fraud allegation against Kiran Enterprises. "
            "What risk mitigation process should GST authorities follow to avoid false positives?"
        ),
        "correct_answer": {
            "is_fraud": False,
            "fraud_type": "Not Fraud — False Positive from Name Match",
            "indicators": [
                "Different person from the one in fraud network list",
                "Genuine trading activity with physical verification",
                "Normal ITC-to-turnover ratio",
                "All payments through banking channels",
                "Active customer base with regular supplies",
            ],
            "fake_itc_amount": 0,
            "enforcement_actions": [
                "Close investigation with a clean chit",
                "Update GSTN risk profiling system to differentiate by PAN/Aadhaar",
                "Issue advisory to taxpayer about the confusion",
                "No penalty — genuine taxpayer",
                "Mark case in system to prevent future false flagging",
            ],
        },
    },
    {
        "id": "case_056",
        "description": (
            "Vardhman Exports LLP (GSTIN: 08AABCV7890N1Z5), Jaipur, claims IGST refund on exports. "
            "Exports: ₹12,34,56,000 to UAE. IGST paid at 18%: ₹2,22,22,080. Refund claimed: ₹2,22,22,080. "
            "However, the company exported 'handicrafts' but shipping bills show commodity code for 'chemicals.' "
            "The UAE importer confirms receiving chemicals, not handicrafts. "
            "GST rate on handicrafts: 5%; on chemicals: 18%. "
            "The company deliberately used wrong HS code to get higher refund on a lower-taxed item."
        ),
        "question": (
            "Determine the fraud amount and correct refund for Vardhman Exports LLP. "
            "What is the excess refund claimed by exploiting HS code manipulation?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "HS Code Manipulation for Excess Refund",
            "indicators": [
                "Commodity description mismatch between GST invoice and shipping bill",
                "UAE importer confirms different goods received",
                "18% tax rate used for goods actually chargeable at 5%",
                "Excess refund of ₹1,60,16,880 (difference between 18% and 5% on ₹12.34Cr)",
                "Deliberate misclassification for monetary benefit",
            ],
            "fake_itc_amount": round(12345600 * 0.13),
            "enforcement_actions": [
                "Correct refund: ₹12,34,56,000 × 5% = ₹61,72,800 only",
                "Excess refund sought: ₹1,60,49,280 — Section 74 + Section 132(1)(l)",
                "Customs Act Section 135 for wrong HS code declaration",
                "Recovery of ₹1,60,49,280 already refunded with 24% interest",
                "Penalty: 100% of ₹1,60,49,280 = ₹1,60,49,280 under Section 74",
            ],
        },
    },
    {
        "id": "case_057",
        "description": (
            "Diamond Wire Industries Pvt Ltd (GSTIN: 27AABCD1234O1Z1), Thane, manufactures industrial wire. "
            "In FY2023-24, the company purchased scrap from 45 small unregistered dealers, "
            "but created invoices showing purchases from 3 registered suppliers (fake suppliers). "
            "Total ITC claimed from fake invoices: ₹89,34,56,000. "
            "Actual legitimate purchases: ₹12,34,56,000 from genuine suppliers. "
            "The company issued FORM GSTR-3B suppressing actual unregistered dealer purchases."
        ),
        "question": (
            "Determine fraud type and total tax impact for Diamond Wire Industries. "
            "What are the implications of suppressing unregistered dealer purchases (RCM liability)?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Fake Invoice Fraud + RCM Suppression",
            "indicators": [
                "₹89.34Cr ITC from fake registered supplier invoices",
                "Actual purchases from 45 unregistered dealers suppressed",
                "No genuine supply from claimed registered suppliers",
                "RCM liability suppressed on unregistered dealer purchases",
                "Double manipulation — fake ITC + RCM evasion",
            ],
            "fake_itc_amount": round(8934560000 - 1234560000),
            "enforcement_actions": [
                "Section 74 — Fake ITC ₹77,00,00,000 + 100% penalty",
                "Section 9(4) — RCM liability on unregistered dealer purchases (state-specific)",
                "Section 132(1)(b) and (c) — Fake invoices and fraudulent ITC",
                "Non-bailable cognizable offense given quantum > ₹5 Crore",
                "Special audit under Section 66 for full forensic audit",
                "Arrest powers under Section 69 CGST Act",
            ],
        },
    },
    {
        "id": "case_058",
        "description": (
            "Trustworthy Agri Products (Proprietorship, GSTIN: 20AABCT2345P1Z4), Bhubaneswar, is a genuine agricultural trader. "
            "Turnover ₹89,34,000. ITC: ₹4,45,700 (5%). Tax intelligence flagged 'unusually high' ITC. "
            "Physical verification: active business, regular stock movement, proper accounts. "
            "ITC source: fertilizer purchases (12% GST) for resale. All suppliers genuine. "
            "The 5% ITC ratio on agricultural trading is actually normal for this business model."
        ),
        "question": (
            "Evaluate fraud risk for Trustworthy Agri Products. "
            "What constitutes normal ITC benchmarks for agricultural trading and how should this case be classified?"
        ),
        "correct_answer": {
            "is_fraud": False,
            "fraud_type": "Not Fraud — Normal Business Activity Flagged by Algorithm",
            "indicators": [
                "Physical business presence confirmed",
                "5% ITC ratio is normal for agri-trading (fertilizer at 12%)",
                "All supplier GSTINs active and compliant",
                "Proportionate to business size",
                "Regular stock movement records maintained",
            ],
            "fake_itc_amount": 0,
            "enforcement_actions": [
                "No action required",
                "Update risk algorithm with industry-specific ITC benchmarks",
                "Issue compliance certificate to taxpayer",
                "Classify as low-risk for future assessment",
            ],
        },
    },
    {
        "id": "case_059",
        "description": (
            "Stellar Impex Pvt Ltd (GSTIN: 07AABCS3456Q1Z7), Delhi, imports goods from China. "
            "For FY2023-24, it paid IGST on imports of ₹2,34,56,78,000 @ 18% = ₹42,22,22,040 to Customs. "
            "The company claims ITC of ₹42,22,22,040 in GSTR-3B. "
            "However, it then re-exported identical goods to UAE paying zero IGST under LUT "
            "and claims refund under Section 54(3). "
            "Total claim: IGST import credit (₹42.22Cr) utilized + refund of ITC on re-export — effectively double recovery."
        ),
        "question": (
            "Analyze the import-export ITC cycle for Stellar Impex. Is there a legal mechanism being exploited "
            "or is this genuine ITC utilization and refund?"
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "Import-Export ITC Manipulation / Inverted Duty Refund Fraud",
            "indicators": [
                "Same goods imported and exported without value addition",
                "Import IGST claimed as ITC and simultaneously seeking refund on LUT exports",
                "Circular flow — import at high value, export at similar value without value addition",
                "No genuine business purpose evident in import-re-export at same price",
                "Refund claim appears to be for round-tripping arbitrage",
            ],
            "fake_itc_amount": 4222220040,
            "enforcement_actions": [
                "Section 54(3) refund — legitimate IF import duty paid and goods genuinely exported",
                "HOWEVER if import-export is circular/fictitious — Section 74 + Section 132",
                "Customs verification of actual import and export",
                "Transfer pricing analysis — import and export price comparison",
                "If prices manipulated: Customs valuation fraud + GST fraud",
                "DGRI (Directorate of Revenue Intelligence) referral",
            ],
        },
    },
    {
        "id": "case_060",
        "description": (
            "Horizon Healthcare Pvt Ltd (GSTIN: 29AABCH4567R1Z3), Bengaluru, operates hospitals. "
            "For FY2023-24, it claimed ITC of ₹23,45,67,000 on medical equipment, drugs, and hospital supplies. "
            "However, healthcare services are predominantly exempt from GST. "
            "The company is claiming ITC on inputs used for providing exempt healthcare services, "
            "which is specifically blocked. ITC on inputs for taxable pharmacy services is being lumped together. "
            "Legitimate ITC (for taxable supplies): ₹3,45,67,000 only."
        ),
        "question": (
            "Identify whether Horizon Healthcare's ITC overclaim is fraud or genuine error. "
            "Calculate excess ITC and determine applicable sections for recovery."
        ),
        "correct_answer": {
            "is_fraud": True,
            "fraud_type": "ITC on Exempt Supplies — Deliberate Overclaim",
            "indicators": [
                "Healthcare services predominantly exempt — ITC not eligible",
                "ITC claimed 6.78x the legitimate amount (₹23.45Cr vs legitimate ₹3.45Cr)",
                "No proportional reversal done under Rule 42",
                "Repeated over multiple years (deliberate pattern)",
                "CFO aware of exempt supply ITC restriction per interview records",
            ],
            "fake_itc_amount": 20000000,
            "enforcement_actions": [
                "Section 74 — Deliberate ITC overclaim with knowledge = fraud",
                "Rule 42 — ITC reversal for common inputs used for exempt supplies",
                "Section 17(2) — ITC restricted to taxable supply proportion",
                "Demand ₹2,00,00,000 + 100% penalty + interest at 24% under Section 50(3)",
                "Prosecution under Section 132(1)(c) given quantum and repetition",
            ],
        },
    },
]

# =============================================================================
# CATEGORY 4: TASK4_CASES - E-Way Bill Violations (15 Cases)
# =============================================================================

TASK4_CASES = [
    {
        "id": "case_061",
        "description": (
            "A consignment of cotton yarn worth ₹4,56,700 was being transported by Primus Textiles Pvt Ltd "
            "(GSTIN: 24AABCP1234A1Z3) from Ahmedabad to Surat. E-way bill generated on 15 March 2024 "
            "valid for 1 day (distance < 100 km). Vehicle intercepted on 17 March 2024 — 2 days after expiry. "
            "GST on consignment: 5% = ₹22,835. Driver could not explain the delay. "
            "This is the first such violation for the company."
        ),
        "question": (
            "Calculate the penalty for the expired e-way bill violation for Primus Textiles. "
            "Apply the correct penalty formula under Section 129 CGST Act."
        ),
        "correct_answer": {
            "violation_type": "Expired E-Way Bill",
            "tax_amount": 22835,
            "penalty_amount": max(10000, 22835),
            "penalty_formula": "Higher of ₹10,000 or tax amount (₹22,835) = ₹22,835",
            "section_reference": "Section 129(1)(b) CGST Act — goods detained, penalty = higher of ₹10,000 or tax applicable",
            "additional_note": "Goods and vehicle to be released upon payment of penalty. No criminal liability for first offense.",
        },
    },
    {
        "id": "case_062",
        "description": (
            "National Cement Corp Pvt Ltd (GSTIN: 33AABCN2345B1Z9), Chennai, dispatched cement bags worth "
            "₹2,34,56,000 + 28% GST ₹65,67,680 to a construction site in Coimbatore. "
            "The e-way bill showed goods value as ₹89,45,000 (undervalued by ₹1,45,11,000). "
            "Interception found physical goods valued at ₹2,34,56,000 but e-way bill showed ₹89,45,000. "
            "The undervaluation was deliberate to avoid higher e-way bill threshold and reduce GST appearance."
        ),
        "question": (
            "Calculate penalty for the undervaluation in e-way bill for National Cement Corp. "
            "What is the tax evaded and applicable penalty under Section 129/130?"
        ),
        "correct_answer": {
            "violation_type": "Undervaluation in E-Way Bill",
            "tax_amount": round(14511000 * 0.28),
            "penalty_amount": max(10000, round(14511000 * 0.28)),
            "penalty_formula": "Tax on undervalued amount: ₹1,45,11,000 × 28% = ₹40,63,080. Penalty = higher of ₹10,000 or ₹40,63,080 = ₹40,63,080",
            "section_reference": "Section 129(1) CGST Act — penalty on tax evaded through undervaluation; Section 130 — confiscation if deliberate",
            "additional_note": "Deliberate undervaluation may invoke Section 130 confiscation in addition to Section 129 penalty",
        },
    },
    {
        "id": "case_063",
        "description": (
            "Deepak Auto Parts LLP (GSTIN: 09AABCD3456C1Z6), Delhi, transported auto components worth "
            "₹8,90,450 + 28% GST ₹2,49,326 from Delhi to Lucknow. "
            "E-way bill showed vehicle number HR-26-AB-1234. "
            "During interception, actual vehicle number was UP-78-CD-5678. "
            "The driver said the vehicle was changed at the last minute due to breakdown but e-way bill was not updated. "
            "No other discrepancy found in goods."
        ),
        "question": (
            "Determine the penalty for wrong vehicle number in the e-way bill for Deepak Auto Parts. "
            "Is a bona fide vehicle change defense accepted under GST rules?"
        ),
        "correct_answer": {
            "violation_type": "Wrong Vehicle Number in E-Way Bill",
            "tax_amount": 249326,
            "penalty_amount": max(10000, 249326),
            "penalty_formula": "Higher of ₹10,000 or tax (₹2,49,326) = ₹2,49,326",
            "section_reference": "Section 129(1) CGST Act; Rule 138(10) — vehicle change requires Part-B update in e-way bill",
            "additional_note": "Vehicle change due to breakdown is a valid defense but transporter must update Part-B of e-way bill within prescribed time. Failure to update is a technical violation. Penalty can be contested if genuine breakdown proved with documentation.",
        },
    },
    {
        "id": "case_064",
        "description": (
            "Bharat Food Products Pvt Ltd (GSTIN: 27AABCB4567D1Z2), Mumbai, was transporting biscuits "
            "(HSN 1905, 18% GST) worth ₹3,45,670 from Mumbai to Pune. "
            "E-way bill described goods as 'agricultural produce' (exempt). "
            "Interception confirmed the goods were packaged biscuits — a taxable item. "
            "GST applicable: 18% on ₹3,45,670 = ₹62,221. "
            "The mismatch between actual goods and e-way bill description is deliberate to avoid tax."
        ),
        "question": (
            "Calculate penalty for goods mismatch in e-way bill for Bharat Food Products. "
            "Does misclassification to avoid GST attract enhanced penalties?"
        ),
        "correct_answer": {
            "violation_type": "Goods Mismatch / Misclassification in E-Way Bill",
            "tax_amount": 62221,
            "penalty_amount": max(10000, 62221),
            "penalty_formula": "Higher of ₹10,000 or tax (₹62,221) = ₹62,221; plus potential Section 130 confiscation for deliberate misclassification",
            "section_reference": "Section 129 CGST Act — penalty for goods different from e-way bill; Section 130 — confiscation for deliberate misrepresentation",
            "additional_note": "Deliberate misclassification of biscuits as agricultural produce to avoid GST invites Section 130 confiscation of goods and vehicle in addition to Section 129 penalty.",
        },
    },
    {
        "id": "case_065",
        "description": (
            "Rajasthan Marble Exports Pvt Ltd (GSTIN: 08AABCR5678E1Z8), Jaipur, was transporting marble slabs "
            "worth ₹67,89,450 + 28% GST ₹19,01,046 from Jaipur to Delhi (approved route via NH48). "
            "Vehicle was intercepted in Agra — which is on an alternate route (NH19) not specified in the e-way bill. "
            "The driver claimed NH48 had an accident, so diverted. "
            "No prior intimation given to GST portal about route deviation."
        ),
        "question": (
            "Assess the route deviation violation for Rajasthan Marble Exports and calculate applicable penalty. "
            "Can emergency route deviation be used as a defense?"
        ),
        "correct_answer": {
            "violation_type": "Route Deviation from E-Way Bill",
            "tax_amount": 1901046,
            "penalty_amount": max(10000, 1901046),
            "penalty_formula": "Higher of ₹10,000 or tax (₹19,01,046) = ₹19,01,046",
            "section_reference": "Section 129(1) CGST Act; Rule 138A — goods must be transported on declared route; Rule 138C — re-generation allowed for route change",
            "additional_note": "Emergency route deviation can be a mitigating factor but not a complete defense. Transporter should have intimated via e-way bill portal update or generated fresh e-way bill for new route. Penalty can be reduced at adjudication if genuine emergency proved.",
        },
    },
    {
        "id": "case_066",
        "description": (
            "Sunrise Electronics Pvt Ltd (GSTIN: 29AABCS6789F1Z5), Bengaluru, transported televisions worth "
            "₹23,45,670 (18% GST = ₹4,22,221) from Bengaluru to Mysuru without generating any e-way bill. "
            "Distance: 145 km. Value exceeds ₹50,000 threshold. "
            "The company's logistics manager claimed he was unaware of the e-way bill requirement. "
            "Vehicle intercepted at a checkpost. Goods are genuine taxable supply with valid invoice."
        ),
        "question": (
            "Calculate penalty for missing e-way bill for Sunrise Electronics. "
            "Does ignorance of the e-way bill requirement reduce the penalty under Section 129?"
        ),
        "correct_answer": {
            "violation_type": "Missing E-Way Bill Above Threshold",
            "tax_amount": 422221,
            "penalty_amount": max(10000, 422221),
            "penalty_formula": "Higher of ₹10,000 or tax (₹4,22,221) = ₹4,22,221",
            "section_reference": "Section 129(1)(b) CGST Act; Rule 138 — e-way bill mandatory for goods > ₹50,000 transported > 50 km (state-specific thresholds may vary)",
            "additional_note": "Ignorance of law is not a valid defense under GST. Penalty of ₹4,22,221 applies. Goods and vehicle detained till penalty paid. Genuine transaction reduces risk of Section 130 confiscation.",
        },
    },
    {
        "id": "case_067",
        "description": (
            "Shree Chemicals Pvt Ltd (GSTIN: 24AABCS7890G1Z1), Vadodara, transported hazardous chemicals "
            "worth ₹89,45,670 + 18% GST ₹16,10,221 from Vadodara to Surat. "
            "E-way bill validity: 3 days for 320 km. Vehicle breakdown occurred on day 2; the goods were "
            "transferred to a new vehicle without generating a new e-way bill. "
            "The original e-way bill still showed the old vehicle number. Interception on day 3 (still valid e-way bill) "
            "but wrong vehicle number noted."
        ),
        "question": (
            "Analyze the violation type for Shree Chemicals — is this primarily an expired e-way bill "
            "or wrong vehicle number violation? Calculate the applicable penalty."
        ),
        "correct_answer": {
            "violation_type": "Wrong Vehicle Number (Transshipment without Part-B Update)",
            "tax_amount": 1610221,
            "penalty_amount": max(10000, 1610221),
            "penalty_formula": "E-way bill still valid (day 3 of 3). Violation is wrong vehicle number only. Penalty = higher of ₹10,000 or ₹16,10,221 = ₹16,10,221",
            "section_reference": "Section 129(1) CGST Act; Rule 138(10) — transshipment requires Part-B update with new vehicle number",
            "additional_note": "Since e-way bill was still valid, severity is lower than expired EWB. However, transshipment without updating Part-B is a technical violation. Transporter should have updated Part-B via EWB portal before continuing journey.",
        },
    },
    {
        "id": "case_068",
        "description": (
            "Metro Constructions LLP (GSTIN: 07AABCM1234H1Z4), Delhi, transported "
            "construction equipment (concrete mixers) worth ₹12,34,56,000 + 18% GST ₹2,22,22,080. "
            "E-way bill generated but showed taxable value as ₹1,23,45,600 (10x undervalued). "
            "Vehicle intercepted; the actual consignment value confirmed by invoices. "
            "The company claimed the e-way bill generator made a data entry error."
        ),
        "question": (
            "Calculate the penalty for Metro Constructions and evaluate whether the data entry error "
            "defense can be sustained. What is the tax evaded and confiscation risk?"
        ),
        "correct_answer": {
            "violation_type": "Undervaluation in E-Way Bill (10x Undervalued)",
            "tax_amount": round((123456000 - 12345600) * 0.18),
            "penalty_amount": max(10000, round((123456000 - 12345600) * 0.18)),
            "penalty_formula": "Tax on undervalued amount: (₹12,34,56,000 - ₹1,23,45,600) = ₹11,11,10,400 × 18% = ₹2,00,00,272. Penalty = ₹2,00,00,272",
            "section_reference": "Section 129 + Section 130 CGST Act — 10x undervaluation is extreme and likely attracts confiscation under Section 130",
            "additional_note": "10x undervaluation is too extreme for data entry error defense to succeed. Section 130 confiscation of goods and vehicle likely in addition to Section 129 penalty. Criminal prosecution under Section 132 possible for evasion of this magnitude.",
        },
    },
    {
        "id": "case_069",
        "description": (
            "Pearls Trading Co (Proprietorship, GSTIN: 20AABCP2345I1Z7), Bhubaneswar, transported "
            "rice (exempt from GST) worth ₹2,34,56,000 from Bhubaneswar to Kolkata. "
            "No e-way bill was generated as the proprietor believed exempt goods don't require e-way bills. "
            "Distance: 480 km. Vehicle intercepted. "
            "As per Odisha e-way bill rules, exempt goods above ₹50,000 still require e-way bill for inter-state movement."
        ),
        "question": (
            "Determine the e-way bill violation and penalty for Pearls Trading Co. "
            "What is the penalty when the goods themselves are exempt from GST?"
        ),
        "correct_answer": {
            "violation_type": "Missing E-Way Bill for Exempt Goods (Inter-State)",
            "tax_amount": 0,
            "penalty_amount": 10000,
            "penalty_formula": "Goods exempt — tax amount = ₹0. Penalty = higher of ₹10,000 or tax (₹0) = ₹10,000",
            "section_reference": "Section 129(1) CGST Act; Rule 138(14) — certain exempt goods still require e-way bill for inter-state movement above ₹50,000",
            "additional_note": "E-way bill is required for inter-state transport of goods above value threshold even if goods are exempt. Penalty = ₹10,000 minimum since tax amount is nil. State-specific e-way bill rules must be verified for exact applicability.",
        },
    },
    {
        "id": "case_070",
        "description": (
            "Orion Steel Pvt Ltd (GSTIN: 27AABCO3456J1Z3), Mumbai, transported TMT bars worth "
            "₹45,67,890 + 18% GST ₹8,22,220 from Mumbai to Nashik. "
            "E-way bill valid for 1 day (distance 162 km — should be 2 days). "
            "Vehicle was delayed due to traffic and arrived after e-way bill expiry. "
            "The company had applied for extension on the portal but extension was rejected due to a technical error."
        ),
        "question": (
            "Calculate penalty for Orion Steel and assess whether portal technical error "
            "during extension request provides any relief under Section 129."
        ),
        "correct_answer": {
            "violation_type": "Expired E-Way Bill (Extension Rejection due to Portal Error)",
            "tax_amount": 822220,
            "penalty_amount": max(10000, 822220),
            "penalty_formula": "Higher of ₹10,000 or tax (₹8,22,220) = ₹8,22,220",
            "section_reference": "Section 129(1) CGST Act; Rule 138(10) — extension must be obtained before expiry via portal",
            "additional_note": "Portal technical error is a mitigating circumstance. Taxpayer should preserve screenshots of failed extension attempt and raise technical glitch grievance with GSTN helpdesk. Penalty at adjudication may be waived if portal error documented. Penalty remains applicable until waiver granted.",
        },
    },
    {
        "id": "case_071",
        "description": (
            "Shiva Spices Exports LLP (GSTIN: 33AABCS4567K1Z9), Chennai, was transporting "
            "spices (12% GST) valued at ₹3,45,67,890 + 12% GST ₹41,48,147 from Chennai to Delhi. "
            "E-way bill was generated correctly. However, the consignment was split into 3 vehicles "
            "to avoid threshold detection, with each vehicle carrying goods worth ₹1,15,22,630. "
            "Only 1 e-way bill was generated for the full amount; the other 2 vehicles had no e-way bills."
        ),
        "question": (
            "Analyze the e-way bill violation for Shiva Spices for splitting consignment. "
            "Calculate penalty for the 2 vehicles without e-way bills."
        ),
        "correct_answer": {
            "violation_type": "Missing E-Way Bill for Split Consignment (2 of 3 Vehicles)",
            "tax_amount": round(11522630 * 2 * 0.12),
            "penalty_amount": max(10000 * 2, round(11522630 * 2 * 0.12)),
            "penalty_formula": "Tax on goods in 2 vehicles without EWB: ₹1,15,22,630 × 2 × 12% = ₹27,65,431. Penalty per vehicle: higher of ₹10,000 or proportionate tax. Total: ₹27,65,431",
            "section_reference": "Section 129(1) CGST Act; each vehicle must have its own e-way bill; splitting to evade EWB requirement may invoke Section 130 confiscation",
            "additional_note": "Deliberate splitting of consignment to evade e-way bill threshold is a planned evasion. Section 130 confiscation applicable for vehicles 2 and 3. Anti-evasion unit to investigate if this is part of a pattern.",
        },
    },
    {
        "id": "case_072",
        "description": (
            "Tata Global Beverages Pvt Ltd (GSTIN: 27AABCT5678L1Z6), Mumbai, transported tea "
            "worth ₹1,23,45,670 + 5% GST ₹6,17,284 from Mumbai to a distributor in Hyderabad. "
            "E-way bill was valid and correct. Vehicle intercepted; all documents in order. "
            "Officer notices that the driver's name on e-way bill does not match actual driver. "
            "Company policy requires registering driver details at the time of dispatch."
        ),
        "question": (
            "Determine if driver name mismatch in an otherwise valid e-way bill constitutes a violation "
            "under Section 129. Calculate any applicable penalty."
        ),
        "correct_answer": {
            "violation_type": "Minor Technical Error — Driver Name Mismatch (Not a Prescribed Field)",
            "tax_amount": 617284,
            "penalty_amount": 0,
            "penalty_formula": "Driver name is not a mandatory field in Form EWB-01. No penalty applicable under Section 129 for non-mandatory field mismatch.",
            "section_reference": "Section 129 read with Rule 138 — penalty only for violations of mandatory e-way bill requirements; driver name is not mandatory in EWB-01",
            "additional_note": "No penalty applicable. Officer should note and release vehicle. Mandatory fields: GSTIN of supplier/recipient, goods description, HSN, quantity, value, vehicle number. Driver name in company policy is internal compliance, not GST law requirement.",
        },
    },
    {
        "id": "case_073",
        "description": (
            "National Pharma Distributors Pvt Ltd (GSTIN: 06AABCN6789M1Z2), Gurgaon, transported "
            "medicines (12% GST) worth ₹89,34,560 + 12% GST ₹10,72,147 in a refrigerated van. "
            "The e-way bill showed goods description as 'general merchandise' instead of 'pharmaceutical products.' "
            "The consignment was genuine and all invoices correct. "
            "The mismatch was due to an auto-fill error in the EWB software."
        ),
        "question": (
            "Calculate the violation and penalty for National Pharma Distributors for "
            "goods description mismatch in e-way bill. Can a software auto-fill error reduce penalty?"
        ),
        "correct_answer": {
            "violation_type": "Goods Description Mismatch in E-Way Bill",
            "tax_amount": 1072147,
            "penalty_amount": max(10000, 1072147),
            "penalty_formula": "Higher of ₹10,000 or tax (₹10,72,147) = ₹10,72,147",
            "section_reference": "Section 129(1) CGST Act — goods description must match invoice; Rule 138(1)(iii) — goods description is mandatory",
            "additional_note": "Software auto-fill error is a mitigating factor. Company can produce evidence of software error (IT logs, screenshots) at adjudication. Penalty may be reduced to ₹10,000 minimum at adjudication discretion. Goods and vehicle to be detained till penalty/security deposit provided.",
        },
    },
    {
        "id": "case_074",
        "description": (
            "Delite FMCG Pvt Ltd (GSTIN: 24AABCD7890N1Z8), Ahmedabad, transported FMCG goods "
            "worth ₹4,56,78,900 + 18% GST ₹82,22,202 in 2 trucks. "
            "Both e-way bills were generated with valid vehicle numbers. "
            "The entire consignment was intercepted; one truck's e-way bill had expired by 4 hours. "
            "The second truck's e-way bill was valid. "
            "Total goods in expired EWB truck: ₹2,28,39,450 (half the total)."
        ),
        "question": (
            "Calculate penalty for Delite FMCG for partial e-way bill expiry (one of two trucks). "
            "Is the penalty on entire consignment or only on the truck with expired e-way bill?"
        ),
        "correct_answer": {
            "violation_type": "Expired E-Way Bill — One of Two Vehicles",
            "tax_amount": round(22839450 * 0.18),
            "penalty_amount": max(10000, round(22839450 * 0.18)),
            "penalty_formula": "Penalty only on goods in expired EWB truck: ₹2,28,39,450 × 18% = ₹41,11,101. Penalty = higher of ₹10,000 or ₹41,11,101 = ₹41,11,101",
            "section_reference": "Section 129(1) CGST Act — penalty applicable per vehicle/consignment with violation; compliant truck has no penalty",
            "additional_note": "Penalty and detention only for the non-compliant truck. Second truck with valid EWB should be released immediately. 4-hour expiry may be contestable if taxpayer demonstrates genuine delay beyond control.",
        },
    },
    {
        "id": "case_075",
        "description": (
            "Prime Construction Materials LLP (GSTIN: 07AABCP1234O1Z5), Delhi, transported "
            "construction materials including cement, steel, and PVC pipes totaling ₹3,45,67,890 + 28% GST ₹96,79,009. "
            "E-way bill generated showed only 'cement' with value ₹1,23,45,000. "
            "Missing from EWB: steel ₹1,45,00,000 (28% GST ₹40,60,000) and PVC pipes ₹77,22,890 (18% GST ₹13,90,120). "
            "Investigation reveals deliberate omission of high-value steel and PVC to reduce EWB declaration."
        ),
        "question": (
            "Calculate the total penalty for Prime Construction for deliberate partial e-way bill generation. "
            "What enhanced penalties apply for deliberately omitting goods from EWB?"
        ),
        "correct_answer": {
            "violation_type": "Partial E-Way Bill — Deliberate Omission of Goods",
            "tax_amount": round(14500000 * 0.28 + 7722890 * 0.18),
            "penalty_amount": max(10000, round(14500000 * 0.28 + 7722890 * 0.18)),
            "penalty_formula": "Tax on omitted goods: Steel ₹1,45,00,000 × 28% = ₹40,60,000 + PVC ₹77,22,890 × 18% = ₹13,90,120. Total = ₹54,50,120. Penalty = ₹54,50,120",
            "section_reference": "Section 129 + Section 130 CGST Act — deliberate omission of goods from EWB is intentional evasion; Section 130 confiscation of all goods (including cement) and vehicle applicable",
            "additional_note": "Deliberate partial EWB is treated as an evasion attempt for entire consignment. Section 130 confiscation of all goods (not just omitted ones) and conveyance. Penalty of ₹54,50,120 plus potential fine in lieu of confiscation.",
        },
    },
]

# =============================================================================
# CATEGORY 5: TASK5_CASES - Export Refund Claims (15 Cases)
# =============================================================================

TASK5_CASES = [
    {
        "id": "case_076",
        "description": (
            "Sunrise Textiles Exports Pvt Ltd (GSTIN: 24AABCS1234A1Z3), Surat, exports cotton fabric. "
            "Exported goods worth ₹45,67,890 on 15 June 2022 under LUT (Letter of Undertaking). "
            "ITC accumulated on inputs: ₹2,34,567. "
            "The company filed refund claim on 20 July 2024 — over 2 years from export date. "
            "Applicable section: Section 54 CGST Act."
        ),
        "question": (
            "Determine if the export refund claim for Sunrise Textiles is eligible. "
            "What is the time limit for export refund claims and has it been breached?"
        ),
        "correct_answer": {
            "refund_eligible": False,
            "correct_refund_amount": 0,
            "refund_type": "LUT Export — ITC Refund (Zero Rated)",
            "timeline": "2 years from the date of export (15 June 2022). Claim filed 20 July 2024 — 2 years and 35 days late",
            "section_reference": "Section 54(1) CGST Act — refund application must be filed within 2 years from relevant date; Explanation (2)(a) — relevant date for export is date of despatch",
            "additional_note": "Claim is time-barred. No condonation of delay available under Section 54. Company loses refund of ₹2,34,567. Lesson: file within 2 years strictly.",
        },
    },
    {
        "id": "case_077",
        "description": (
            "Kiran Pharma Exports LLP (GSTIN: 27AABCK2345B1Z9), Mumbai, exports medicines. "
            "For March 2024 export: goods worth ₹89,34,560, IGST paid at 12% = ₹10,72,147. "
            "Shipping bill filed and IGST reflected in ICEGATE. "
            "Refund application filed on 15 May 2024 via GST portal (within 2 years). "
            "Bank account details provided. All shipping bills submitted."
        ),
        "question": (
            "Calculate the eligible IGST refund for Kiran Pharma Exports for March 2024 export. "
            "What is the refund type and timeline for receipt?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 1072147,
            "refund_type": "Export with IGST Payment — Full IGST Refund under Section 16(3)(b) IGST Act",
            "timeline": "Within 60 days from date of filing refund application; relevant date is date of filing shipping bill",
            "section_reference": "Section 54(1) CGST Act read with Rule 96 CGST Rules; Section 16(3)(b) IGST Act — refund of IGST paid on exports",
            "additional_note": "Fully eligible. ICEGATE-GSTN data matching will auto-process. Refund credited to bank account within 60 days. Interest at 6% applies if delayed beyond 60 days per Section 56.",
        },
    },
    {
        "id": "case_078",
        "description": (
            "Delta Engineering Pvt Ltd (GSTIN: 29AABCD3456C1Z6), Bengaluru, makes deemed exports "
            "to a mega power project. Supplies: ₹2,34,56,789 at 18% GST = ₹42,22,222. "
            "Deemed export notification: Notification 48/2017-CT. "
            "The recipient (power project) has claimed the same ITC of ₹42,22,222 in its returns. "
            "Now Delta also files refund claim for ₹42,22,222."
        ),
        "question": (
            "Determine if Delta Engineering's refund claim is eligible when the recipient has already claimed ITC. "
            "Who is entitled to the deemed export refund — supplier or recipient?"
        ),
        "correct_answer": {
            "refund_eligible": False,
            "correct_refund_amount": 0,
            "refund_type": "Deemed Export — Refund to Supplier OR Recipient (not both)",
            "timeline": "Either supplier or recipient can claim; not both",
            "section_reference": "Section 54(1) CGST Act; Rule 89(2)(g) — deemed export refund can be claimed by supplier or recipient by declaration; if recipient claims ITC, supplier cannot also claim refund",
            "additional_note": "Recipient has already availed ITC of ₹42,22,222. Supplier's refund claim must be rejected. Double benefit not permitted. Supplier should have obtained an undertaking from recipient that ITC not claimed before filing refund.",
        },
    },
    {
        "id": "case_079",
        "description": (
            "Vijay IT Software Pvt Ltd (GSTIN: 33AABCV4567D1Z2), Chennai, exports software services. "
            "Export of services (zero-rated) under LUT to US client: ₹1,23,45,678 for FY2023-24. "
            "ITC on inputs (servers, internet, rent): ₹12,34,567. "
            "The company seeks refund of accumulated ITC of ₹12,34,567. "
            "All foreign remittance received via FEMA-compliant channels within prescribed time."
        ),
        "question": (
            "Calculate the eligible refund for Vijay IT Software for FY2023-24 export of services. "
            "What documentation is required for service export refund?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 1234567,
            "refund_type": "Export of Services under LUT — Accumulated ITC Refund under Section 54(3)",
            "timeline": "Within 2 years from end of financial year in which export invoice issued",
            "section_reference": "Section 54(3) CGST Act — refund of unutilized ITC on zero-rated supplies; Rule 89(2)(b) — export of services with FIRA (Foreign Inward Remittance Advice) as proof",
            "additional_note": "Full ₹12,34,567 eligible. Documents: LUT copy, export invoices, FIRA/SWIFT documents, bank statement for forex receipt, GSTR-1 with export details, GSTR-2A/2B for ITC. Submit FORM RFD-01 online.",
        },
    },
    {
        "id": "case_080",
        "description": (
            "Zenith Gems & Jewellery Pvt Ltd (GSTIN: 24AABCZ5678E1Z8), Surat, exports cut diamonds. "
            "Export under LUT: ₹4,56,78,900. Input ITC accumulated: ₹89,34,560. "
            "The company calculates refund as: ITC ÷ (Turnover of zero-rated × Net ITC) × Total ITC. "
            "Company has domestic supplies also: ₹2,34,56,000 (taxable). "
            "Total turnover (adjusted): ₹6,91,34,900. Refund formula applied: ₹89,34,560 × (₹4,56,78,900 / ₹6,91,34,900)."
        ),
        "question": (
            "Verify the refund calculation for Zenith Gems under the ITC refund formula. "
            "Calculate the correct refund amount using Rule 89(4) formula."
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": round(8934560 * (45678900 / 69134900)),
            "refund_type": "LUT Export — Proportionate ITC Refund under Rule 89(4)",
            "timeline": "2 years from date of export",
            "section_reference": "Section 54(3) CGST Act; Rule 89(4) — Refund = (Net ITC × TOES/Adjusted Total Turnover) where TOES = Turnover of Zero-Rated Supplies",
            "additional_note": f"Refund = ₹89,34,560 × (₹4,56,78,900 / ₹6,91,34,900) = ₹59,04,118 (approx). Total ITC cannot be refunded — only proportionate to zero-rated supply ratio.",
        },
    },
    {
        "id": "case_081",
        "description": (
            "Aakash SEZ Suppliers Pvt Ltd (GSTIN: 07AABCA6789F1Z5), Delhi, supplies goods to "
            "a Special Economic Zone (SEZ) developer. Supply value: ₹78,90,560, IGST paid: 18% = ₹14,20,301. "
            "The SEZ developer has a valid LoA (Letter of Approval) from Development Commissioner. "
            "Supplier seeks refund of ₹14,20,301 IGST paid. "
            "Refund claim filed on 1 March 2024 for supplies made on 15 January 2022."
        ),
        "question": (
            "Assess the refund eligibility for Aakash SEZ Suppliers and check timeline compliance. "
            "What special rules apply for SEZ supply refunds?"
        ),
        "correct_answer": {
            "refund_eligible": False,
            "correct_refund_amount": 0,
            "refund_type": "SEZ Supply — IGST Refund (Zero Rated)",
            "timeline": "Claim filed 1 March 2024 for January 2022 supply — MORE than 2 years elapsed (2 years 45 days). Time-barred.",
            "section_reference": "Section 54(1) CGST Act — 2-year limit from relevant date; for SEZ supply, relevant date is date of invoice; Section 16(1)(b) IGST Act — zero-rated supply to SEZ",
            "additional_note": "Time-barred. Refund denied. SEZ supplies should be treated as zero-rated. Refund mechanism: supplier files RFD-01 within 2 years. If LUT used, no IGST payable; if IGST paid, refund available within time.",
        },
    },
    {
        "id": "case_082",
        "description": (
            "Meridian Auto Components Pvt Ltd (GSTIN: 27AABCM7890G1Z1), Mumbai, supplies auto parts "
            "to an EOU (Export Oriented Unit). Supply value: ₹34,56,780 + 18% GST ₹6,22,220. "
            "EOU claims this as deemed export benefit. Supplier seeks refund of ₹6,22,220. "
            "The EOU, however, was not re-exporting goods — they were selling in DTA (Domestic Tariff Area) "
            "after processing, claiming DTA sale entitlement."
        ),
        "question": (
            "Determine if the deemed export refund is eligible for Meridian Auto Components when "
            "the EOU is selling in DTA instead of exporting. What is the impact on deemed export status?"
        ),
        "correct_answer": {
            "refund_eligible": False,
            "correct_refund_amount": 0,
            "refund_type": "Deemed Export — Eligibility Conditional on EOU's Export Activity",
            "timeline": "Moot — not eligible",
            "section_reference": "Section 54 CGST Act; Notification 48/2017-CT — deemed export notification; EOU selling in DTA does not qualify as deemed export for GST refund purposes for supplier",
            "additional_note": "Deemed export benefit applies only when EOU actually exports or the supply qualifies under the notification. DTA sales by EOU don't confer deemed export status on the supplier's earlier supply. Refund rejected. Supplier may pursue rectification from EOU.",
        },
    },
    {
        "id": "case_083",
        "description": (
            "Coastal Fisheries Exports Pvt Ltd (GSTIN: 32AABCC1234H1Z7), Kochi, exports frozen fish. "
            "Export value: ₹89,45,670 (exempt commodity — fish is exempt under GST). "
            "ITC claimed on packaging materials (12% GST): ₹3,45,670; refrigeration services (18%): ₹1,23,456. "
            "The company seeks refund of accumulated ITC of ₹4,69,126 as it cannot be utilized "
            "against any output tax (exempt goods)."
        ),
        "question": (
            "Assess ITC refund eligibility for Coastal Fisheries Exports for accumulated ITC on exempt goods exports. "
            "Can a company exporting exempt goods claim ITC refund?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 469126,
            "refund_type": "Zero-Rated Supply (Export) — Refund of Accumulated ITC even for Exempt Goods",
            "timeline": "2 years from date of export",
            "section_reference": "Section 54(3) CGST Act — refund of unutilized ITC due to zero-rated supplies; Section 16 IGST Act — exports are zero-rated regardless of exemption status of goods domestically",
            "additional_note": "Fish may be exempt domestically but exports are always zero-rated. Refund of accumulated ITC ₹4,69,126 is fully eligible. File RFD-01 with export documents and ITC ledger. This is one of the key benefits of zero-rating vs exemption.",
        },
    },
    {
        "id": "case_084",
        "description": (
            "Skybridge Software LLP (GSTIN: 29AABCS2345I1Z4), Bengaluru, provides software development services. "
            "It claims export of services to its parent company in Singapore under an intercompany agreement. "
            "Forex received: USD 1,50,000 (₹1,24,50,000 at conversion). "
            "However, GSTN portal scrutiny reveals the 'export of services' is actually related-party transaction "
            "at below-market prices. Comparable market rate: ₹2,45,67,000 for same services."
        ),
        "question": (
            "Assess the refund eligibility for Skybridge Software's export claim. "
            "How does transfer pricing and below-market related-party pricing affect GST export refund?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": "ITC proportionate to ₹1,24,50,000 (actual forex received) only",
            "refund_type": "Export of Services — LUT/IGST; but value may be questioned under Section 15 read with Transfer Pricing",
            "timeline": "2 years from invoice date",
            "section_reference": "Section 15 CGST Act — transaction value for related parties must be at arm's length; Rule 28 — related party valuation; Section 54 — refund based on declared export value",
            "additional_note": "GST refund is based on actual transaction value (₹1,24,50,000). However, if Customs/FEMA flags undervaluation, GST authorities may re-examine. Transfer pricing adjustment from Income Tax can indirectly affect GST value. Refund eligible on declared value but risk of reassessment.",
        },
    },
    {
        "id": "case_085",
        "description": (
            "Himachal Handicrafts Exports Pvt Ltd (GSTIN: 02AABCH3456J1Z3), Shimla, exports handicrafts under IGST payment. "
            "Export value: ₹23,45,678, IGST paid at 12%: ₹2,81,481. "
            "Shipping bill filed with Customs but IGST amount on shipping bill shows ₹2,45,000 "
            "due to a data entry error at Customs port. "
            "Actual IGST paid to government: ₹2,81,481 (as per GSTR-3B and payment challan)."
        ),
        "question": (
            "Calculate the correct refund for Himachal Handicrafts when shipping bill shows wrong IGST amount. "
            "What is the process to correct the discrepancy?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 281481,
            "refund_type": "Export with IGST Payment — Full Refund of Actual IGST Paid",
            "timeline": "After correction of shipping bill; 2 years from export date",
            "section_reference": "Rule 96 CGST Rules — refund based on shipping bill IGST amount matched with GSTR-3B; discrepancy must be resolved before refund",
            "additional_note": "Correct process: (1) File amendment in Shipping Bill with Customs (Bill of Entry Amendment). (2) After Customs corrects IGST amount to ₹2,81,481, ICEGATE-GSTN matching will process refund. (3) Refund of full ₹2,81,481. Error on Customs side — taxpayer must initiate correction.",
        },
    },
    {
        "id": "case_086",
        "description": (
            "Pioneer Chemical Exports LLP (GSTIN: 24AABCP4567K1Z9), Vadodara, exports specialty chemicals. "
            "LUT filed; exports worth ₹3,45,67,890. Total ITC accumulated: ₹89,34,560. "
            "Of total ITC, ₹12,34,000 is on capital goods (plant purchased 2 years ago). "
            "Remaining ₹77,00,560 is on current inputs. "
            "The company claims refund of entire ₹89,34,560."
        ),
        "question": (
            "Calculate the correct refund for Pioneer Chemical Exports distinguishing between "
            "capital goods ITC and current input ITC for export refund purposes."
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 8934560,
            "refund_type": "LUT Export — Full Accumulated ITC Refund (inputs + capital goods)",
            "timeline": "2 years from export date",
            "section_reference": "Section 54(3) CGST Act — refund of unutilized ITC includes both input ITC and capital goods ITC; Rule 89(4) formula applies to total net ITC",
            "additional_note": "Both current input ITC (₹77,00,560) and capital goods ITC (₹12,34,000) are included in 'Net ITC' under Rule 89(4). Full ₹89,34,560 eligible subject to proportionate formula if mixed supply. If 100% exports, full ITC refundable.",
        },
    },
    {
        "id": "case_087",
        "description": (
            "Kalyana Silk Exports Pvt Ltd (GSTIN: 29AABCK5678L1Z6), Mysuru, exports silk sarees. "
            "For FY2023-24: export turnover ₹45,67,890; domestic taxable turnover ₹23,45,670. "
            "Total ITC: ₹4,56,789. "
            "The company applies for full ₹4,56,789 refund citing exports. "
            "However, under Rule 89(4), refund is restricted by adjusted total turnover formula."
        ),
        "question": (
            "Calculate the correct refund amount for Kalyana Silk Exports under Rule 89(4) formula. "
            "What portion of ITC is refundable when there are both export and domestic supplies?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": round(456789 * 4567890 / (4567890 + 2345670)),
            "refund_type": "LUT Export — Proportionate Refund under Rule 89(4)",
            "timeline": "2 years from export date",
            "section_reference": "Section 54(3) CGST Act; Rule 89(4) — Refund amount = Net ITC × (TOES / Adjusted Total Turnover)",
            "additional_note": f"Refund = ₹4,56,789 × (₹45,67,890 / ₹69,13,560) = ₹3,01,594 approx. Cannot claim full ₹4,56,789. Balance ₹1,55,195 to be carried forward or utilized against domestic supply tax.",
        },
    },
    {
        "id": "case_088",
        "description": (
            "Omkar Spices & Herbs Exports Pvt Ltd (GSTIN: 32AABCO6789M1Z2), Kochi, exports organic spices. "
            "Refund claim: ₹12,34,567 filed on 1 January 2024 for exports of April–June 2022. "
            "Claim for April 2022 exports (relevant date: 30 April 2022) — 20 months elapsed — within 2 years. "
            "Claim for May 2022 exports (relevant date: 31 May 2022) — 19 months — within 2 years. "
            "Claim for June 2022 exports (relevant date: 30 June 2022) — 18 months — within 2 years. "
            "All three months' refunds filed together in single RFD-01."
        ),
        "question": (
            "Confirm eligibility and calculate the refund for Omkar Spices for the combined quarterly refund claim. "
            "Is a combined RFD-01 for multiple months permissible?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 1234567,
            "refund_type": "LUT Export — Accumulated ITC Refund for Multiple Months",
            "timeline": "All three months within 2-year limit; April 2022 — 20 months elapsed (within limit); May and June — also within limit",
            "section_reference": "Section 54(1) CGST Act — 2-year limit calculated from relevant date for each shipping bill; Rule 89 — single RFD-01 can cover multiple tax periods",
            "additional_note": "Single RFD-01 for multiple months is permitted under Rule 89. All three months are within the 2-year limit. Full ₹12,34,567 eligible subject to GSTR verification. Process within 60 days.",
        },
    },
    {
        "id": "case_089",
        "description": (
            "Apex Biotech Exports Pvt Ltd (GSTIN: 27AABCA7890N1Z8), Mumbai, exports biotech products. "
            "IGST refund for 2022-23 exports: ₹45,67,890 claimed. "
            "The company had purchased some inputs from an unregistered supplier "
            "and paid GST under RCM (₹3,45,678). This RCM ITC is included in the refund claim. "
            "Refund authority questions whether RCM ITC can be included in export refund claim."
        ),
        "question": (
            "Determine if RCM ITC (tax paid under reverse charge) can be included in the export refund claim "
            "for Apex Biotech Exports. What is the eligible refund amount?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 4567890,
            "refund_type": "LUT Export — Full ITC Refund including RCM ITC",
            "timeline": "2 years from export date",
            "section_reference": "Section 54(3) CGST Act; Definition of 'Net ITC' under Explanation to Rule 89(4) — includes ITC availed on all inward supplies including RCM; Section 16(1) — ITC includes tax paid under reverse charge",
            "additional_note": "RCM ITC (₹3,45,678) is legitimate ITC and IS included in export refund calculation. Refund authority's objection is incorrect. Full ₹45,67,890 eligible. Provide GSTR-3B entries showing RCM payment and corresponding ITC availed as documentation.",
        },
    },
    {
        "id": "case_090",
        "description": (
            "Bravo Steel Exports LLP (GSTIN: 06AABCB1234O1Z5), Gurgaon, is a steel exporter. "
            "It exported steel at ₹2,34,56,780 under IGST payment (18%) = ₹42,22,220 and seeks refund. "
            "However, the exporter also received duty drawback of ₹8,90,456 from Customs on the same export. "
            "The company claims both IGST refund (₹42,22,220) and duty drawback (₹8,90,456) simultaneously."
        ),
        "question": (
            "Determine if both IGST refund and duty drawback can be claimed simultaneously for "
            "Bravo Steel Exports. What is the interplay between the two refund mechanisms?"
        ),
        "correct_answer": {
            "refund_eligible": True,
            "correct_refund_amount": 4222220,
            "refund_type": "Export with IGST Payment — IGST Refund; Duty Drawback (Customs) is Separate",
            "timeline": "IGST refund: 2 years from export; Drawback: 1 year from export",
            "section_reference": "Rule 96(10) CGST Rules — IGST refund available unless 'higher rate drawback' (pre-GST composite drawback) availed; if only 'lower rate' AIOC drawback, IGST refund also available",
            "additional_note": "Both can be claimed IF duty drawback availed is 'lower rate' (customs duties only, not GST component). If drawback covers GST, IGST refund denied under Rule 96(10). Company should check drawback rate — AIOC rate vs All Industry Rate with GST component. Assuming lower rate drawback: full ₹42,22,220 IGST refund eligible.",
        },
    },
]

# =============================================================================
# CATEGORY 6: TASK6_CASES - Reverse Charge Mechanism (RCM) (10 Cases)
# =============================================================================

TASK6_CASES = [
    {
        "id": "case_091",
        "description": (
            "Innovate IT Solutions Pvt Ltd (GSTIN: 29AABCI1234A1Z7), Bengaluru, subscribed to "
            "cloud services from Amazon Web Services (AWS) USA for ₹23,45,670 per month. "
            "AWS is a foreign supplier with no GST registration in India. "
            "The subscription fee is paid in USD equivalent. "
            "Innovate IT is a GST-registered entity providing taxable software services in India."
        ),
        "question": (
            "Determine RCM applicability for Innovate IT's AWS cloud subscription. "
            "Who pays the GST, what is the rate, and can ITC be claimed?"
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(2345670 * 0.18),
            "who_pays_tax": "Innovate IT Solutions Pvt Ltd (recipient) pays IGST under RCM as importer of services",
            "itc_available_after_payment": True,
            "section_reference": "Section 5(3) IGST Act read with Notification 10/2017-IT — import of services from foreign supplier attracts IGST under RCM; Section 16 CGST Act — ITC available on RCM tax paid",
            "tax_rate": "18% IGST",
            "additional_note": "IGST = ₹23,45,670 × 18% = ₹4,22,221 payable by Innovate IT. ITC of ₹4,22,221 available immediately in the same month after payment. Self-invoice (Section 31(3)(f)) must be raised by recipient.",
        },
    },
    {
        "id": "case_092",
        "description": (
            "Bharat Heavy Industries Pvt Ltd (GSTIN: 07AABCB2345B1Z3), Delhi, hired GTA "
            "(Goods Transport Agency) — Saraswati Roadlines (unregistered, GST not collected) "
            "to transport industrial equipment worth ₹89,34,560 from Delhi to Ahmedabad. "
            "Freight charged: ₹3,45,670. "
            "Bharat Heavy is GST-registered. Saraswati Roadlines does not collect GST."
        ),
        "question": (
            "Determine RCM liability for Bharat Heavy Industries for GTA services. "
            "Calculate tax amount and ITC availability."
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(345670 * 0.05),
            "who_pays_tax": "Bharat Heavy Industries Pvt Ltd (recipient/registered GST payer) pays GST under RCM on GTA services",
            "itc_available_after_payment": True,
            "section_reference": "Section 9(3) CGST Act; Notification 13/2017-CT — GTA services to registered person attracts RCM at 5% (without ITC to GTA) or 12% (with ITC); recipient pays",
            "tax_rate": "5% GST (CGST 2.5% + SGST 2.5%) or 12% — GTA to choose; common practice is 5%",
            "additional_note": "RCM GST = ₹3,45,670 × 5% = ₹17,284. Bharat Heavy pays and can claim same as ITC. If GTA opts for 12% forward charge (registered GTA), RCM does not apply — GTA collects directly.",
        },
    },
    {
        "id": "case_093",
        "description": (
            "Meridian Pharmaceuticals Pvt Ltd (GSTIN: 27AABCM3456C1Z9), Mumbai, engaged "
            "Sharma & Associates, Advocates (unregistered, individual advocates) for patent litigation. "
            "Legal fees: ₹8,90,450. Advocates rendered services to the pharma company (registered entity). "
            "Advocates do not collect or charge GST on their invoice."
        ),
        "question": (
            "Determine RCM applicability for Meridian Pharma's legal fees payment. "
            "What GST rate applies and can the company claim ITC after paying RCM?"
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(890450 * 0.18),
            "who_pays_tax": "Meridian Pharmaceuticals Pvt Ltd pays 18% GST under RCM on legal services from individual advocates",
            "itc_available_after_payment": True,
            "section_reference": "Section 9(3) CGST Act; Notification 13/2017-CT Entry 2 — Legal services by advocate to business entity attract RCM; recipient (registered business) pays GST",
            "tax_rate": "18% GST (CGST 9% + SGST 9%)",
            "additional_note": "RCM GST = ₹8,90,450 × 18% = ₹1,60,281. Self-invoice required. ITC of ₹1,60,281 available after payment. Exception: Advocate provides services to non-business individual — RCM not applicable in that case.",
        },
    },
    {
        "id": "case_094",
        "description": (
            "SecureFirst Corporate Pvt Ltd (GSTIN: 09AABCS4567D1Z6), Noida, hired "
            "Gurkha Security Services (unregistered firm) to provide 25 security guards. "
            "Monthly security charges: ₹5,67,890. "
            "SecureFirst is a registered GST entity in Noida providing IT services."
        ),
        "question": (
            "Analyze RCM applicability for security services from an unregistered supplier "
            "to SecureFirst Corporate. Calculate tax and ITC position."
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(567890 * 0.18),
            "who_pays_tax": "SecureFirst Corporate Pvt Ltd (registered recipient) pays 18% GST under RCM on security services from unregistered supplier",
            "itc_available_after_payment": True,
            "section_reference": "Section 9(3) CGST Act; Notification 13/2017-CT Entry 14 — Security services from unregistered to registered person attracts RCM",
            "tax_rate": "18% GST",
            "additional_note": "RCM GST = ₹5,67,890 × 18% = ₹1,02,220. If Gurkha Security becomes GST-registered and collects tax directly (forward charge), RCM ceases. ITC available. Self-invoice mandatory. Note: If security firm is registered and charges GST, RCM does NOT apply.",
        },
    },
    {
        "id": "case_095",
        "description": (
            "Galaxy Startups Pvt Ltd (GSTIN: 29AABCG5678E1Z2), Bengaluru, pays its three independent directors "
            "sitting fees of ₹2,50,000 per meeting per director. "
            "3 meetings held in Q2 FY2024-25. Total payment: ₹22,50,000. "
            "Directors are not employees and are paid as service providers. "
            "No GST charged by directors on their invoices."
        ),
        "question": (
            "Determine RCM liability for Galaxy Startups on director sitting fees. "
            "What is the GST amount and can the company claim ITC on this RCM?"
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(2250000 * 0.18),
            "who_pays_tax": "Galaxy Startups Pvt Ltd pays 18% GST under RCM on services provided by directors in their non-executive/independent capacity",
            "itc_available_after_payment": True,
            "section_reference": "Section 9(3) CGST Act; Notification 13/2017-CT Entry 6 — Services by director (other than whole-time director who is employee) to the company attracts RCM",
            "tax_rate": "18% GST (CGST 9% + SGST 9%)",
            "additional_note": "RCM GST = ₹22,50,000 × 18% = ₹4,05,000. Independent director sittings fees are subject to RCM. ITC of ₹4,05,000 available. Whole-time directors who are employees are NOT subject to RCM. Self-invoice required under Section 31(3)(f).",
        },
    },
    {
        "id": "case_096",
        "description": (
            "Spectrum Beverages Pvt Ltd (GSTIN: 27AABCS6789F1Z8), Mumbai, sponsored "
            "a cricket tournament organized by Mumbai Cricket Association (MCA) — an unregistered body. "
            "Sponsorship amount: ₹45,67,890. "
            "Spectrum receives brand visibility and advertising rights in return. "
            "MCA does not charge GST on the sponsorship invoice."
        ),
        "question": (
            "Determine RCM applicability for Spectrum Beverages' sports sponsorship payment. "
            "Calculate the GST and ITC position for the company."
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(4567890 * 0.18),
            "who_pays_tax": "Spectrum Beverages Pvt Ltd (sponsor/registered entity) pays 18% GST under RCM on sponsorship services",
            "itc_available_after_payment": True,
            "section_reference": "Section 9(3) CGST Act; Notification 13/2017-CT Entry 9(ii) — Sponsorship services provided by any person to body corporates and partnership firms attract RCM",
            "tax_rate": "18% GST",
            "additional_note": "RCM GST = ₹45,67,890 × 18% = ₹8,22,220. Sponsorship to any entity (registered or unregistered) provided to a body corporate attracts RCM. ITC ₹8,22,220 eligible for Spectrum as it's used for business promotion (taxable output). Self-invoice needed.",
        },
    },
    {
        "id": "case_097",
        "description": (
            "TechHub India Pvt Ltd (GSTIN: 07AABCT7890G1Z5), Delhi, received a royalty invoice "
            "from a German software company (no Indian GSTIN) for software licensing: ₹67,89,450. "
            "The payment is to the German company for intellectual property use. "
            "TechHub provides IT services (taxable) in India using this licensed software."
        ),
        "question": (
            "Determine RCM applicability for software royalty payment to a foreign company by TechHub India. "
            "Calculate IGST and explain ITC availability."
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(6789450 * 0.18),
            "who_pays_tax": "TechHub India Pvt Ltd pays IGST under RCM as importer of intellectual property/royalty service from foreign entity",
            "itc_available_after_payment": True,
            "section_reference": "Section 5(3) IGST Act; Notification 10/2017-IT — import of services (royalty/IP) from outside India attracts IGST under RCM; place of supply: India (location of recipient)",
            "tax_rate": "18% IGST",
            "additional_note": "IGST = ₹67,89,450 × 18% = ₹12,22,101. Payable by TechHub India. ITC of ₹12,22,101 immediately available in same month. Self-invoice required. FEMA remittance for royalty also requires Form 15CA/15CB for TDS under Income Tax Act — separate compliance.",
        },
    },
    {
        "id": "case_098",
        "description": (
            "Pinnacle Real Estate Pvt Ltd (GSTIN: 27AABCP1234H1Z1), Mumbai, purchased land "
            "from an individual landowner (unregistered) for ₹3,45,67,890. "
            "No GST was charged by the landowner. "
            "Pinnacle will develop apartments on this land for sale. "
            "The company's accountant suggests paying RCM GST on the land purchase."
        ),
        "question": (
            "Determine if RCM applies to land purchase from an individual by Pinnacle Real Estate. "
            "Is land sale subject to GST and does RCM apply?"
        ),
        "correct_answer": {
            "rcm_applicable": False,
            "tax_amount": 0,
            "who_pays_tax": "No one — land is not subject to GST",
            "itc_available_after_payment": False,
            "section_reference": "Schedule III of CGST Act 2017 — sale of land is neither supply of goods nor supply of services; not subject to GST at all; Section 9(3) RCM does not apply to non-GST supplies",
            "tax_rate": "Nil",
            "additional_note": "Land sale is outside the purview of GST per Schedule III Entry 5. RCM does not apply. Accountant's suggestion is incorrect. Only applicable tax: Stamp Duty (State subject, not GST). No ITC available as no GST paid.",
        },
    },
    {
        "id": "case_099",
        "description": (
            "Zenith Constructions LLP (GSTIN: 08AABCZ2345I1Z4), Jaipur, hired an unregistered architect "
            "for design services for a residential project. Fees: ₹12,34,560. "
            "Additionally, it hired a registered structural engineering firm (GSTIN: 08AABCR3456J1Z1) "
            "for ₹8,90,450 — which charged 18% GST of ₹1,60,281 on its invoice. "
            "Zenith paid both invoices. Accountant wants to know RCM liability on each."
        ),
        "question": (
            "Determine RCM applicability for Zenith Constructions on both the unregistered architect "
            "and the registered engineering firm. Calculate total GST payable and by whom."
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(1234560 * 0.18),
            "who_pays_tax": "Zenith Constructions pays RCM on unregistered architect fees only; registered firm's GST is forward charge paid by that firm",
            "itc_available_after_payment": True,
            "section_reference": "Section 9(4) CGST Act — services from unregistered supplier to registered person (currently applicable for specific notified services); Section 9(3) — specific RCM entries; Notification 13/2017-CT — architect services not in Section 9(3) list",
            "tax_rate": "18% GST on unregistered architect fees under Section 9(4) if applicable",
            "additional_note": "Unregistered architect: RCM under Section 9(4) may apply — ₹12,34,560 × 18% = ₹2,22,221 payable by Zenith. Registered engineering firm: Forward charge — firm collects ₹1,60,281 and pays to government; Zenith claims ITC. Total GST impact: ₹2,22,221 (RCM) + ₹1,60,281 (ITC from registered firm) = net ITC available ₹3,82,502.",
        },
    },
    {
        "id": "case_100",
        "description": (
            "Horizon Shipping Pvt Ltd (GSTIN: 27AABCH3456J1Z7), Mumbai, imports goods by ocean freight. "
            "The freight is paid to a foreign shipping company (non-resident): ₹34,56,780. "
            "The Indian importer (Horizon) bears the freight cost (CIF terms — cost insurance freight). "
            "The foreign shipping line has no GSTIN in India. "
            "Additionally, Horizon uses an Indian freight forwarder (GST-registered) "
            "who charges ₹3,45,678 + 18% GST ₹62,222 for local handling."
        ),
        "question": (
            "Determine RCM applicability for Horizon Shipping on: (a) ocean freight to foreign shipping line, "
            "and (b) services from Indian freight forwarder. "
            "Calculate total GST liability and ITC available."
        ),
        "correct_answer": {
            "rcm_applicable": True,
            "tax_amount": round(3456780 * 0.05),
            "who_pays_tax": "(a) Ocean freight: Horizon Shipping pays IGST 5% under RCM as importer; (b) Indian forwarder: Forward charge — forwarder charges GST, Horizon claims ITC",
            "itc_available_after_payment": True,
            "section_reference": "Notification 10/2017-IT — ocean freight import services from non-resident attract IGST 5% RCM; however note Mohit Minerals judgment (SC 2022) — RCM on ocean freight struck down for CIF imports; Indian forwarder: forward charge under Section 9(1)",
            "tax_rate": "Ocean freight: 5% IGST (but post-Supreme Court judgment in Mohit Minerals 2022 — NOT applicable for CIF imports); Indian forwarder: 18% GST",
            "additional_note": "IMPORTANT: Supreme Court in Union of India vs Mohit Minerals (May 2022) struck down RCM on ocean freight for CIF imports as unconstitutional. Post this judgment, RCM on CIF ocean freight is NOT applicable. Horizon should NOT pay RCM on ₹34,56,780. Indian forwarder GST ₹62,222 is forward charge — fully eligible ITC. This is a landmark case — professionals must be aware.",
        },
    },
]
