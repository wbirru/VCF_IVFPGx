"""
IVF Drug-Gene Interaction Analyser
A tool for analysing genetic variants and their impact on IVF medications

Installation:
pip install streamlit

Run:
streamlit run variant_analyzer.py
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="IVF Drug-Gene Analyser",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .impact-high { background-color: #989191; border-left: 5px solid #dc2626; padding: 1rem; border-radius: 0.5rem; }
    .impact-moderate { background-color: #99968d; border-left: 5px solid #f59e0b; padding: 1rem; border-radius: 0.5rem; }
    .impact-mild { background-color: #8f9399; border-left: 5px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; }
    .impact-none { background-color: #959696; border-left: 5px solid #6b7280; padding: 1rem; border-radius: 0.5rem; }
    .impact-positive { background-color: #909792; border-left: 5px solid #16a34a; padding: 1rem; border-radius: 0.5rem; }
    .database-link { 
        display: inline-block; 
        padding: 0.5rem 1rem; 
        margin: 0.25rem; 
        border-radius: 0.375rem; 
        text-decoration: none; 
        font-weight: 500;
        transition: all 0.2s;
    }
    .clinvar-link { background-color: #fecaca; color: #991b1b; }
    .pharmgkb-link { background-color: #bbf7d0; color: #166534; }
    .pubmed-link { background-color: #bfdbfe; color: #1e40af; }
    .database-link:hover { opacity: 0.8; }
</style>
""", unsafe_allow_html=True)

# Drug-Gene-Impact Database
DRUG_GENE_DATABASE = {
    "FSH (Follitropin alfa/delta)": {
        "genes": ["FSHR", "FSHB"],
        "impacts": {
            "FSHR_rs6166_Ser/Ser": {
                "impact": "REDUCED_RESPONSE",
                "severity": "moderate",
                "description": "Patients with Ser/Ser genotype show reduced sensitivity to FSH medications. May require higher doses for optimal ovarian response.",
                "metabolism": "No direct effect on metabolism",
                "efficacy": "20-30% reduction in ovarian response at standard doses",
                "evidence": "Tier A - Multiple meta-analyses in IVF populations",
                "recommendation": "Consider starting with higher FSH dose or more frequent monitoring",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs6166",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA28670",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=FSHR+rs6166+IVF"
                }
            },
            "FSHR_rs6166_Asn/Ser": {
                "impact": "MODERATE_RESPONSE",
                "severity": "mild",
                "description": "Heterozygous carriers show intermediate FSH sensitivity between Asn/Asn and Ser/Ser genotypes.",
                "metabolism": "No direct effect on metabolism",
                "efficacy": "Normal to slightly reduced response expected",
                "evidence": "Tier A - Well-replicated in multiple populations",
                "recommendation": "Standard dosing with close monitoring",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs6166",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA28670",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=FSHR+rs6166+IVF"
                }
            },
            "FSHB_rs10835638_T/T": {
                "impact": "ALTERED_RESPONSE",
                "severity": "mild",
                "description": "T allele associated with lower baseline FSH levels, which may affect ovarian reserve assessment and stimulation planning.",
                "metabolism": "No direct effect on medication metabolism",
                "efficacy": "May influence baseline FSH testing results",
                "evidence": "Tier B - Consistent associations in reproductive phenotypes",
                "recommendation": "Consider baseline FSH context when planning stimulation",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs10835638",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=FSHB+rs10835638"
                }
            }
        }
    },
    "Metformin": {
        "genes": ["SLC22A1", "SLC47A1", "ATM"],
        "impacts": {
            "SLC22A1_Met420del": {
                "impact": "REDUCED_RESPONSE",
                "severity": "high",
                "description": "Loss-of-function variant in OCT1 transporter. Significantly reduces metformin uptake into liver cells, decreasing glucose-lowering effect.",
                "metabolism": "REDUCED hepatic uptake - 50-70% decrease in liver exposure",
                "efficacy": "Reduced glucose-lowering efficacy; increased GI side effects",
                "evidence": "Tier A - Replicated in multiple diabetes cohorts",
                "recommendation": "Consider alternative PCOS treatments or higher metformin doses with careful GI monitoring",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=SLC22A1+Met420del",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA134865839",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=SLC22A1+metformin+pharmacogenetics"
                }
            },
            "SLC22A1_Arg61Cys": {
                "impact": "REDUCED_RESPONSE",
                "severity": "high",
                "description": "Another loss-of-function OCT1 variant. Impairs metformin transport similar to Met420del.",
                "metabolism": "REDUCED hepatic uptake - significant decrease in therapeutic effect",
                "efficacy": "Poor response to standard metformin doses",
                "evidence": "Tier A - Strong functional evidence",
                "recommendation": "Alternative therapy may be more effective",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=SLC22A1+Arg61Cys",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA134865839",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=SLC22A1+metformin"
                }
            },
            "SLC47A1_rs2289669": {
                "impact": "ALTERED_METABOLISM",
                "severity": "moderate",
                "description": "MATE1 transporter variant affecting metformin renal excretion and distribution.",
                "metabolism": "ALTERED renal excretion - may affect drug levels",
                "efficacy": "Variable glucose-lowering response",
                "evidence": "Tier B - Mixed results across studies",
                "recommendation": "Standard dosing with monitoring",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs2289669",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA134952057",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=SLC47A1+metformin"
                }
            }
        }
    },
    "Clomiphene citrate": {
        "genes": ["CYP2D6"],
        "impacts": {
            "CYP2D6_*4/*4": {
                "impact": "REDUCED_METABOLISM",
                "severity": "high",
                "description": "Poor metabolizer (PM) phenotype. Significantly impaired conversion to active hydroxylated metabolites.",
                "metabolism": "POOR METABOLIZER - Very slow conversion to active forms",
                "efficacy": "Reduced therapeutic effect due to lower active metabolite levels",
                "evidence": "Tier B - Strong PK evidence, mixed clinical outcomes",
                "recommendation": "May require higher doses or alternative ovulation induction agent (e.g., letrozole)",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2D6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA128",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2D6+clomiphene"
                }
            },
            "CYP2D6_*4/*5": {
                "impact": "REDUCED_METABOLISM",
                "severity": "high",
                "description": "Poor metabolizer - gene deletion plus loss-of-function allele. Minimal enzyme activity.",
                "metabolism": "POOR METABOLIZER - Minimal active metabolite formation",
                "efficacy": "Significantly reduced clomiphene efficacy",
                "evidence": "Tier B - Strong functional prediction",
                "recommendation": "Consider letrozole as first-line instead",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2D6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA128",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2D6+clomiphene"
                }
            },
            "CYP2D6_*1/*4": {
                "impact": "INTERMEDIATE_METABOLISM",
                "severity": "moderate",
                "description": "Intermediate metabolizer (IM). Reduced but not absent enzyme activity.",
                "metabolism": "INTERMEDIATE METABOLIZER - Reduced active metabolite formation",
                "efficacy": "Possibly reduced ovulation response",
                "evidence": "Tier B-C - Limited IVF-specific data",
                "recommendation": "Standard dosing with close monitoring for ovulation",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2D6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA128",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2D6+clomiphene"
                }
            },
            "CYP2D6_*1/*1": {
                "impact": "NORMAL_METABOLISM",
                "severity": "none",
                "description": "Normal metabolizer (NM). Standard enzyme activity and clomiphene metabolism.",
                "metabolism": "NORMAL METABOLIZER - Standard conversion to active metabolites",
                "efficacy": "Normal therapeutic response expected",
                "evidence": "Reference phenotype",
                "recommendation": "Standard dosing appropriate",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2D6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA128",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2D6+clomiphene"
                }
            }
        }
    },
    "Letrozole": {
        "genes": ["CYP2A6", "CYP3A4"],
        "impacts": {
            "CYP2A6_*4/*4": {
                "impact": "INCREASED_EXPOSURE",
                "severity": "moderate",
                "description": "Poor metabolizer - complete loss of CYP2A6 function. Letrozole clearance is significantly reduced.",
                "metabolism": "POOR METABOLIZER - Very slow letrozole elimination",
                "efficacy": "INCREASED drug exposure - higher steady-state levels (2-3x normal)",
                "evidence": "Tier B - Strong PK evidence from oncology",
                "recommendation": "Consider lower starting dose; monitor for side effects (fatigue, hot flashes, joint pain)",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2A6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA27093",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2A6+letrozole"
                }
            },
            "CYP2A6_*1/*4": {
                "impact": "INTERMEDIATE_METABOLISM",
                "severity": "mild",
                "description": "Intermediate metabolizer - reduced CYP2A6 activity. Moderately slower letrozole clearance.",
                "metabolism": "INTERMEDIATE METABOLIZER - Moderately reduced clearance",
                "efficacy": "Slightly increased drug exposure (1.5x normal)",
                "evidence": "Tier B - Consistent PK findings",
                "recommendation": "Standard dosing with monitoring for tolerability",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2A6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA27093",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2A6+letrozole"
                }
            },
            "CYP2A6_*1/*1": {
                "impact": "NORMAL_METABOLISM",
                "severity": "none",
                "description": "Normal metabolizer - standard CYP2A6 function and letrozole clearance.",
                "metabolism": "NORMAL METABOLIZER - Standard drug elimination",
                "efficacy": "Normal therapeutic levels and response",
                "evidence": "Reference phenotype",
                "recommendation": "Standard dosing (2.5-5mg daily)",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP2A6",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA27093",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP2A6+letrozole"
                }
            }
        }
    },
    "LH supplementation": {
        "genes": ["LHCGR"],
        "impacts": {
            "LHCGR_rs2293275_A/G": {
                "impact": "ALTERED_RESPONSE",
                "severity": "moderate",
                "description": "N312S variant - AG genotype associated with altered LH receptor sensitivity.",
                "metabolism": "No direct metabolic effect",
                "efficacy": "May show reduced response to GnRH-agonist trigger; variable LH supplementation response",
                "evidence": "Tier B - Emerging evidence in IVF settings",
                "recommendation": "Consider hCG trigger over GnRH-agonist; monitor post-trigger hormone levels",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs2293275",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=LHCGR+rs2293275+IVF"
                }
            },
            "LHCGR_rs2293275_G/G": {
                "impact": "POTENTIALLY_REDUCED_RESPONSE",
                "severity": "moderate",
                "description": "Homozygous for variant allele - may affect LH/hCG receptor responsiveness.",
                "metabolism": "No direct metabolic effect",
                "efficacy": "Potentially reduced response to LH supplementation and trigger",
                "evidence": "Tier B-C - Limited but suggestive data",
                "recommendation": "Preferentially use hCG trigger; consider LH supplementation if poor responder",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs2293275",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=LHCGR+IVF"
                }
            }
        }
    },
    "Corticosteroids": {
        "genes": ["NR3C1", "ABCB1"],
        "impacts": {
            "NR3C1_N363S_Asn/Ser": {
                "impact": "INCREASED_SENSITIVITY",
                "severity": "moderate",
                "description": "Variant associated with increased glucocorticoid receptor sensitivity and enhanced response.",
                "metabolism": "No direct effect on drug metabolism",
                "efficacy": "INCREASED glucocorticoid effects - both therapeutic and adverse",
                "evidence": "Tier B - Replicated in various clinical settings",
                "recommendation": "Monitor closely for side effects (glucose, blood pressure); lower doses may be effective",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=NR3C1+N363S",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA31",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=NR3C1+glucocorticoid+sensitivity"
                }
            },
            "NR3C1_N363S_Ser/Ser": {
                "impact": "INCREASED_SENSITIVITY",
                "severity": "high",
                "description": "Homozygous variant - markedly increased receptor sensitivity to corticosteroids.",
                "metabolism": "No direct metabolic effect",
                "efficacy": "SIGNIFICANTLY INCREASED sensitivity to glucocorticoids",
                "evidence": "Tier B - Strong functional prediction",
                "recommendation": "Consider lower doses; close monitoring of glucose and blood pressure mandatory",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=NR3C1+N363S",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA31",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=NR3C1+glucocorticoid"
                }
            }
        }
    },
    "Growth Hormone": {
        "genes": ["GHR"],
        "impacts": {
            "GHR_d3/d3": {
                "impact": "INCREASED_RESPONSE",
                "severity": "moderate",
                "description": "Exon-3 deletion homozygous - associated with enhanced GH receptor sensitivity.",
                "metabolism": "No direct metabolic effect",
                "efficacy": "ENHANCED response to growth hormone therapy in other indications",
                "evidence": "Tier B - Strong evidence in growth disorders; IVF data limited",
                "recommendation": "May benefit more from GH adjunct in poor responder protocols",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=GHR+exon+3",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA28671",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=GHR+d3+growth+hormone+response"
                }
            },
            "GHR_FL/d3": {
                "impact": "INTERMEDIATE_RESPONSE",
                "severity": "mild",
                "description": "Heterozygous for exon-3 deletion - intermediate GH sensitivity.",
                "metabolism": "No direct metabolic effect",
                "efficacy": "Normal to moderately enhanced GH response",
                "evidence": "Tier B-C - Mixed evidence",
                "recommendation": "Standard GH protocols if indicated",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=GHR+exon+3",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=GHR+growth+hormone"
                }
            }
        }
    },
    "Coenzyme Q10": {
        "genes": ["NQO1", "SOD2"],
        "impacts": {
            "NQO1_*2/*2": {
                "impact": "ALTERED_RESPONSE",
                "severity": "mild",
                "description": "Homozygous for loss-of-function NQO1 variant. Reduced antioxidant enzyme activity.",
                "metabolism": "No direct effect on CoQ10 metabolism",
                "efficacy": "THEORETICAL benefit - reduced endogenous antioxidant capacity may benefit more from supplementation",
                "evidence": "Tier C - Biological plausibility; limited clinical data",
                "recommendation": "CoQ10 supplementation may provide additional benefit in poor responders",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=NQO1+rs1800566",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=NQO1+oxidative+stress+IVF"
                }
            },
            "SOD2_Val16Ala_Ala/Ala": {
                "impact": "POTENTIAL_BENEFIT",
                "severity": "mild",
                "description": "Variant affecting mitochondrial superoxide dismutase targeting and activity.",
                "metabolism": "No direct effect on CoQ10 metabolism",
                "efficacy": "May benefit from antioxidant supplementation - exploratory",
                "evidence": "Tier C - Limited IVF-specific evidence",
                "recommendation": "Consider CoQ10 as adjunct therapy in diminished ovarian reserve",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=SOD2+rs4880",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=SOD2+IVF+pregnancy"
                }
            }
        }
    },
    "Melatonin": {
        "genes": ["MTNR1B", "CYP1A2"],
        "impacts": {
            "MTNR1B_rs10830963_G/G": {
                "impact": "METABOLIC_CONSIDERATION",
                "severity": "mild",
                "description": "Risk allele homozygous - associated with impaired glucose metabolism and insulin secretion.",
                "metabolism": "No direct effect on melatonin metabolism",
                "efficacy": "No direct impact on melatonin effectiveness; METABOLIC MONITORING advised",
                "evidence": "Tier B - Strong GWAS evidence for glucose phenotype",
                "recommendation": "Monitor fasting glucose if using melatonin; be aware of diabetes risk",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=rs10830963",
                    "pharmgkb": "https://www.pharmgkb.org/variant/PA166153757",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=MTNR1B+rs10830963+glucose"
                }
            },
            "CYP1A2_*1F/*1F": {
                "impact": "SLOW_METABOLISM",
                "severity": "mild",
                "description": "Slow caffeine metabolizer genotype - may affect evening alertness if taking melatonin with caffeine.",
                "metabolism": "SLOW metabolizer of caffeine and related compounds",
                "efficacy": "No direct melatonin impact; relevant for lifestyle counseling",
                "evidence": "Tier A for caffeine; Tier C for melatonin interaction",
                "recommendation": "Avoid caffeine in evening; melatonin timing may need adjustment",
                "databases": {
                    "clinvar": "https://www.ncbi.nlm.nih.gov/clinvar/?term=CYP1A2",
                    "pharmgkb": "https://www.pharmgkb.org/gene/PA27093",
                    "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term=CYP1A2+caffeine+metabolism"
                }
            }
        }
    }
}

def get_severity_style(severity):
    """Return CSS class based on severity"""
    severity_map = {
        'high': 'impact-high',
        'moderate': 'impact-positive',
        'mild': 'impact-mild',
        'none': 'impact-none'
    }
    return severity_map.get(severity, 'impact-positive')

def get_impact_emoji(impact_type):
    """Return emoji based on impact type"""
    emoji_map = {
        'REDUCED_RESPONSE': '🔽',
        'REDUCED_METABOLISM': '🔽',
        'INCREASED_EXPOSURE': '🔼',
        'INCREASED_SENSITIVITY': '🔼',
        'INCREASED_RESPONSE': '✅',
        'INTERMEDIATE_METABOLISM': '➖',
        'INTERMEDIATE_RESPONSE': '➖',
        'MODERATE_RESPONSE': '➖',
        'NORMAL_METABOLISM': '✅',
        'ALTERED_RESPONSE': '⚠️',
        'ALTERED_METABOLISM': '⚠️',
        'POTENTIALLY_REDUCED_RESPONSE': '⚠️',
        'METABOLIC_CONSIDERATION': 'ℹ️',
        'POTENTIAL_BENEFIT': '💚',
        'SLOW_METABOLISM': '🐢'
    }
    return emoji_map.get(impact_type, '📊')

def render_impact_card(variant_key, impact_data):
    """Render an impact card with all details"""
    severity_class = get_severity_style(impact_data['severity'])
    impact_emoji = get_impact_emoji(impact_data['impact'])
    
    st.markdown(f"""
    <div class="{severity_class}">
        <h4>{impact_emoji} {variant_key.replace('_', ' ')}</h4>
        <span style="background-color: rgba(0,0,0,0.1); padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.875rem; font-weight: 600;">
            {impact_data['impact'].replace('_', ' ')}
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"**📋 Description:**")
    st.write(impact_data['description'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**💊 Metabolism:**")
        st.info(impact_data['metabolism'])
    
    with col2:
        st.markdown("**🎯 Efficacy Impact:**")
        st.info(impact_data['efficacy'])
    
    st.markdown("**📊 Evidence Level:**")
    st.write(impact_data['evidence'])
    
    st.markdown("**💡 Clinical Recommendation:**")
    st.success(impact_data['recommendation'])
    
    st.markdown("**🔗 Reference Databases:**")
    
    # Create database links
    links_html = ""
    if 'clinvar' in impact_data['databases']:
        links_html += f'<a href="{impact_data["databases"]["clinvar"]}" target="_blank" class="database-link clinvar-link">📊 ClinVar ↗</a>'
    if 'pharmgkb' in impact_data['databases']:
        links_html += f'<a href="{impact_data["databases"]["pharmgkb"]}" target="_blank" class="database-link pharmgkb-link">💊 PharmGKB ↗</a>'
    if 'pubmed' in impact_data['databases']:
        links_html += f'<a href="{impact_data["databases"]["pubmed"]}" target="_blank" class="database-link pubmed-link">📚 PubMed ↗</a>'
    
    st.markdown(links_html, unsafe_allow_html=True)
    st.markdown("---")

def analyze_variants(variant_input):
    """Analyze input variants against drug database"""
    input_variants = [v.strip().upper() for v in variant_input.split('\n') if v.strip()]
    
    if not input_variants:
        return None
    
    drug_results = {}
    
    for drug, drug_data in DRUG_GENE_DATABASE.items():
        matched_impacts = []
        no_impact_genes = []
        
        # Check for matching variants
        for variant in input_variants:
            for impact_key, impact_data in drug_data['impacts'].items():
                # Flexible matching
                if (variant in impact_key.replace('_', ' ').upper() or 
                    impact_key.replace('_', ' ').upper() in variant or
                    variant.split('_')[0] in impact_key.split('_')[0]):
                    matched_impacts.append({
                        'key': impact_key,
                        'data': impact_data
                    })
        
        # Check for genes without impact
        for gene in drug_data['genes']:
            has_match = any(gene.upper() in v or v.split('_')[0] in gene for v in input_variants)
            has_impact = any(gene in m['key'] for m in matched_impacts)
            if has_match and not has_impact:
                no_impact_genes.append(gene)
        
        drug_results[drug] = {
            'impacts': matched_impacts,
            'no_impact_genes': no_impact_genes,
            'relevant_genes': drug_data['genes']
        }
    
    return drug_results

def main():
    # Initialize session state for variant input
    if 'variant_input' not in st.session_state:
        st.session_state.variant_input = ""
    
    # Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 1rem; color: white; margin-bottom: 2rem;">
        <h1 style="margin: 0; font-size: 2.5rem;">🧬 IVF Drug-Gene Interaction Analyser</h1>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Personalised medication insights based on your genetic variants</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Disclaimer
    st.warning("""
    ⚠️ **Clinical Decision Support Tool**
    
    This tool provides pharmacogenomic information to support evidence-based clinical decision-making. 
    Results should be interpreted in the context of complete patient history, clinical presentation, and current treatment protocols.
    """)
    
    # How It Works Section
    with st.expander("📚 Clinical Tool Overview (Click to Expand)", expanded=False):
        st.markdown("""
        ### 🧬 Step 1: Input Patient Genetic Variants
        Enter genetic variants identified from patient pharmacogenomic testing (e.g., CYP2D6*4/*4, FSHR rs6166 Ser/Ser)
        
        **Example format:** CYP2D6*4/*4, SLC22A1 Met420del, FSHR rs6166 Ser/Ser
        
        ### 🔍 Step 2: Pharmacogenomic Analysis
        The system evaluates how patient genetic variants affect 9 common IVF medications:
        - **Metabolism:** Drug processing and clearance rates
        - **Response:** Expected therapeutic efficacy
        - **Dosing Implications:** Adjustments to consider
        - **Safety:** Adverse event risk assessment
        
        ### 📊 Step 3: Evidence-Based Results
        For each drug, review:
        - **Impact Level:** Clinical significance of genetic variants
        - **Dosing Recommendations:** Evidence-based adjustments
        - **Evidence Quality:** Scientific evidence strength (Tier A/B/C)
        - **Reference Links:** Direct access to research and clinical databases
        
        ### 💡 Understanding Impact Categories:
        - 🔽 **Reduced Response:** Consider dose escalation or alternative agents
        - 🔽 **Reduced Metabolism:** Altered drug processing kinetics
        - 🔼 **Increased Exposure:** Extended drug half-life, monitor closely
        - ✅ **Increased Response:** May achieve therapeutic goals at standard doses
        - ➖ **Normal/Moderate:** Standard protocols appropriate
        - ⚠️ **Altered:** Variable response - individualized monitoring recommended
        """)
    
    # Input Section
    st.markdown("## 🔍 Enter Patient Genetic Variants")
    
    # Quick example buttons
    st.markdown("**💡 Sample Patient Profiles:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔴 Poor Responder Profile"):
            st.session_state.variant_input = "CYP2D6*4/*4\nFSHR rs6166 Ser/Ser\nSLC22A1 Met420del"
            st.rerun()
    
    with col2:
        if st.button("🟡 High Sensitivity Profile"):
            st.session_state.variant_input = "CYP2A6*4/*4\nNR3C1 N363S Ser/Ser\nGHR d3/d3"
            st.rerun()
    
    with col3:
        if st.button("🟢 Normal Metabolizer"):
            st.session_state.variant_input = "CYP2D6*1/*1\nCYP2A6*1/*1\nFSHR rs6166 Asn/Ser"
            st.rerun()
    
    # Text area with session state
    variant_input = st.text_area(
        "Enter patient genetic variants (one per line):",
        value=st.session_state.variant_input,
        height=200,
        placeholder="""Enter patient genetic variants (one per line):

Examples:
CYP2D6*4/*4
FSHR rs6166 Ser/Ser
SLC22A1 Met420del
CYP2A6*4/*4
LHCGR rs2293275 A/G""",
        help="Enter one variant per line. Examples: CYP2D6*4/*4, FSHR rs6166 Ser/Ser"
    )
    
    # Analyze button
    if st.button("🔬 Generate Pharmacogenomic Report", type="primary"):
        if not variant_input.strip():
            st.error("❌ Please enter at least one genetic variant")
        else:
            with st.spinner("Analyzing genetic variants..."):
                results = analyze_variants(variant_input)
                
                if results:
                    # Separate drugs into categories
                    drugs_with_impacts = []
                    drugs_no_impact = []
                    
                    for drug, data in results.items():
                        if data['impacts']:
                            drugs_with_impacts.append((drug, data))
                        elif data['no_impact_genes']:
                            drugs_no_impact.append((drug, data))
                    
                    # Show success message with count
                    if drugs_with_impacts:
                        st.success(f"✅ Pharmacogenomic Analysis Complete - {len(drugs_with_impacts)} medication(s) with clinically significant variants identified")
                    else:
                        st.info("ℹ️ Analysis Complete - No clinically significant variants detected for the provided genetic data")
                    
                    # Display drugs WITH impacts first
                    if drugs_with_impacts:
                        st.markdown("### 🎯 Medications with Clinically Significant Variants")
                        for drug, data in drugs_with_impacts:
                            st.markdown(f"## 💊 {drug}")
                            st.info(f"📊 {len(data['impacts'])} clinically significant variant(s) identified for this medication")
                            
                            for impact in data['impacts']:
                                render_impact_card(impact['key'], impact['data'])
                            
                            st.markdown("---")
                    
                    # Display drugs with NO impact at the bottom (optional - can be hidden)
                    if drugs_no_impact:
                        with st.expander(f"ℹ️ Additional Medications Analyzed ({len(drugs_no_impact)} drugs with no significant variants)", expanded=False):
                            for drug, data in drugs_no_impact:
                                st.markdown(f"### 💊 {drug}")
                                st.success(f"""
                                ✅ **No Clinically Significant Variants Detected**
                                
                                Patient genetic profile for **{', '.join(data['no_impact_genes'])}** shows no known variants 
                                affecting {drug} response or metabolism based on current pharmacogenomic evidence.
                                
                                ℹ️ Standard dosing protocols are appropriate for this patient.
                                """)
                                st.markdown("---")
                    
                    # Summary - only show if there are actionable findings
                    if drugs_with_impacts:
                        st.markdown("""
                        <div style="background-color: #1e293b; padding: 1.5rem; border-radius: 1rem; border: 2px solid #3b82f6; color: #ffffff;">
                            <h3 style="color: #60a5fa; margin-top: 0;">📋 Clinical Action Items</h3>
                            <ul style="color: #e2e8f0;">
                                <li>✅ Review pharmacogenomic impact levels for each medication</li>
                                <li>✅ Access referenced databases for detailed evidence review</li>
                                <li>✅ Integrate findings with patient's clinical history and current protocols</li>
                                <li>✅ Consider dose adjustments or alternative agents where indicated</li>
                                <li>✅ Document pharmacogenomic considerations in patient record</li>
                            </ul>
                            <div style="background-color: #fef3c7; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #f59e0b; margin-top: 1rem; color: #78350f;">
                                <p style="margin: 0; font-weight: 600;">⚠️ Clinical Interpretation Note:</p>
                                <p style="margin: 0.5rem 0 0 0;">These pharmacogenomic insights should be integrated with comprehensive patient assessment including medical history, concurrent medications, comorbidities, and individualized treatment goals. Clinical judgment remains paramount in all treatment decisions.</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
