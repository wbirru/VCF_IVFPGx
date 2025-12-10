# IVF Drug-Gene Interaction Analyser

## Overview

The **IVF Drug-Gene Interaction Analyser** is a clinical decision support tool designed for healthcare providers in reproductive medicine. It provides pharmacogenomic insights to guide personalised IVF medication selection and dosing based on patient genetic variants.

## 🎯 Purpose

This tool helps clinicians:
- Identify clinically significant pharmacogenetic variants affecting IVF medications
- Access evidence-based dosing recommendations
- Review scientific literature and clinical databases
- Integrate pharmacogenomics into treatment planning

## 🏥 Target Users

- Reproductive Endocrinologists
- Fertility Specialists
- Clinical Pharmacists in IVF settings
- Genetic Counselors working in reproductive medicine

## 📊 Covered Medications

The tool analyses **9 common IVF medications**:

1. **FSH (Follitropin alfa/delta)** - Genes: FSHR, FSHB
2. **Metformin** - Genes: SLC22A1, SLC47A1, ATM
3. **Clomiphene citrate** - Genes: CYP2D6
4. **Letrozole** - Genes: CYP2A6, CYP3A4
5. **LH supplementation** - Genes: LHCGR
6. **Corticosteroids** - Genes: NR3C1, ABCB1
7. **Growth Hormone** - Genes: GHR
8. **Coenzyme Q10** - Genes: NQO1, SOD2
9. **Melatonin** - Genes: MTNR1B, CYP1A2

## 🔬 Features

### Core Functionality
- **Variant Input**: Enter patient pharmacogenomic test results
- **Automated Analysis**: Cross-reference variants against comprehensive drug-gene database
- **Prioritised Results**: Clinically significant findings displayed first
- **Evidence Grading**: Tier A/B/C evidence classification
- **Database Links**: Direct access to ClinVar, PharmGKB, and PubMed

### Clinical Insights Provided
- **Metabolism Impact**: How variants affect drug processing
- **Efficacy Predictions**: Expected therapeutic response
- **Dosing Recommendations**: Evidence-based adjustments
- **Safety Considerations**: Adverse event risk factors

### Sample Patient Profiles
Pre-loaded examples for quick testing:
- 🔴 Poor Responder Profile
- 🟡 High Sensitivity Profile
- 🟢 Normal Metabolizer Profile

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Install Streamlit
```bash
pip install streamlit
```

### Step 2: Download the Application
Save the code as `variant_analyzer.py` in your desired directory.

### Step 3: Run the Application
```bash
streamlit run variant_analyzer.py
```

The application will open automatically in your default web browser at `http://localhost:8501`

## 💻 Usage Guide

### Basic Workflow

1. **Launch the Application**
   ```bash
   streamlit run variant_analyzer.py
   ```

2. **Input Patient Genetic Variants**
   - Enter one variant per line in the text area
   - Format examples:
     - `CYP2D6*4/*4`
     - `FSHR rs6166 Ser/Ser`
     - `SLC22A1 Met420del`

3. **Generate Report**
   - Click "🔬 Generate Pharmacogenomic Report"
   - Review medications with clinically significant variants (displayed first)
   - Access additional analysed medications in collapsible section

4. **Review Clinical Recommendations**
   - Read impact descriptions
   - Note dosing adjustments
   - Access reference databases for detailed evidence

### Input Format Examples

```text
CYP2D6*4/*4
FSHR rs6166 Ser/Ser
SLC22A1 Met420del
CYP2A6*4/*4
LHCGR rs2293275 A/G
NR3C1 N363S Ser/Ser
GHR d3/d3
```

### Understanding Results

#### Impact Categories
- 🔽 **Reduced Response**: Consider dose escalation or alternatives
- 🔽 **Reduced Metabolism**: Altered drug processing
- 🔼 **Increased Exposure**: Enhanced drug levels, monitor closely
- ✅ **Increased Response**: Better therapeutic response expected
- ➖ **Normal/Moderate**: Standard protocols appropriate
- ⚠️ **Altered**: Variable response, individualised monitoring

#### Evidence Tiers
- **Tier A**: Strong evidence from multiple studies/meta-analyses
- **Tier B**: Consistent evidence from multiple studies
- **Tier C**: Limited evidence, biological plausibility

## 📁 File Structure

```
ivf-drug-gene-analyzer/
│
├── variant_analyzer.py          # Main application file
├── README.md                     # This file
└── requirements.txt              # Python dependencies (optional)
```

## 📦 Optional: Requirements File

Create a `requirements.txt` file:
```text
streamlit>=1.28.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## 🔒 Clinical Use Disclaimer

**IMPORTANT**: This tool is designed as a **clinical decision support system** and should be used by qualified healthcare providers only.

### Key Points:
- Results must be integrated with comprehensive patient assessment
- Consider medical history, concurrent medications, and comorbidities
- Clinical judgment remains paramount in all treatment decisions
- Not a substitute for professional medical expertise
- Evidence levels vary by drug-gene interaction

## 🧬 Pharmacogenomic Database

The tool includes a comprehensive database with:
- **68+ genetic variants** across 15 pharmacogenes
- Evidence-based clinical recommendations
- Direct links to ClinVar, PharmGKB, and PubMed
- Regularly updated with latest pharmacogenomic research

### Key Pharmacogenes Covered
- **CYP450 Enzymes**: CYP2D6, CYP2A6, CYP3A4, CYP1A2
- **Transporters**: SLC22A1, SLC47A1, ABCB1
- **Receptors**: FSHR, LHCGR, NR3C1, GHR, MTNR1B
- **Other**: FSHB, ATM, NQO1, SOD2

## 🎨 Features Highlights

### Smart Result Display
- Medications with actionable findings shown first
- Non-significant results collapsed by default
- Clean, focused clinical interface

### Interactive Elements
- Sample patient profiles for quick testing
- Expandable sections for detailed information
- Clickable database links for evidence review

### Color-Coded Severity
- 🔴 High Impact (Red)
- 🟢 Moderate Impact (Green)
- 🔵 Mild Impact (Blue)
- ⚪ No Impact (Gray)

## 🔄 Updates and Maintenance

### Updating the Database
The drug-gene database is embedded in the code. To update:
1. Locate the `DRUG_GENE_DATABASE` dictionary in `variant_analyzer.py`
2. Add new variants following the existing structure
3. Include evidence tier and clinical recommendations
4. Add relevant database links

### Adding New Medications
```python
"New Drug Name": {
    "genes": ["GENE1", "GENE2"],
    "impacts": {
        "GENE1_variant": {
            "impact": "IMPACT_TYPE",
            "severity": "high/moderate/mild/none",
            "description": "Clinical description",
            "metabolism": "Metabolic effect",
            "efficacy": "Efficacy impact",
            "evidence": "Tier X - Evidence summary",
            "recommendation": "Clinical recommendation",
            "databases": {
                "clinvar": "URL",
                "pharmgkb": "URL",
                "pubmed": "URL"
            }
        }
    }
}
```

## 🐛 Troubleshooting

### Common Issues

**Application won't start:**
```bash
# Check Streamlit installation
pip show streamlit

# Reinstall if needed
pip install --upgrade streamlit
```

**Port already in use:**
```bash
# Use a different port
streamlit run variant_analyzer.py --server.port 8502
```

**Variants not matching:**
- Check spelling and formatting
- Use exact nomenclature (e.g., `*4/*4` not `*4*4`)
- Refer to sample profiles for correct format

## 📚 References

### Scientific Basis
This tool is based on peer-reviewed pharmacogenomic research from:
- Clinical Pharmacogenetics Implementation Consortium (CPIC)
- Pharmacogenomics Knowledge Base (PharmGKB)
- ClinVar - NCBI Genetic Variation Database
- Published reproductive medicine literature

### Recommended Reading
- PharmGKB Clinical Guidelines: https://www.pharmgkb.org
- CPIC Guidelines: https://cpicpgx.org
- ClinVar Database: https://www.ncbi.nlm.nih.gov/clinvar

## 👥 Support and Feedback

### For Technical Issues
- Check Python and Streamlit versions
- Review console error messages
- Ensure all dependencies are installed

### For Clinical Questions
- Consult with clinical pharmacology
- Review linked database entries
- Access original research publications

## 📄 License

This tool is provided for clinical educational and decision support purposes. Always verify findings with current clinical guidelines and individual patient circumstances.

## 🔮 Future Enhancements

Potential additions:
- [ ] Export reports as PDF
- [ ] Integration with EHR systems
- [ ] Batch patient analysis
- [ ] Additional IVF medications
- [ ] Interactive dosing calculators
- [ ] Multi-language support

## 📞 Version Information

**Current Version**: 1.0.0  
**Last Updated**: December 2024  
**Compatibility**: Python 3.7+, Streamlit 1.28+

---

## Quick Start Command

```bash
# Install and run in one command sequence
pip install streamlit && streamlit run variant_analyzer.py
```

---

**For Healthcare Professionals Only** | Evidence-Based Clinical Decision Support | Not for Patient Self-Assessment
