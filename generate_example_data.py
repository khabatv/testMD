import pandas as pd
import numpy as np

def generate_microbiome_dataset(num_samples=45, num_asvs=100):
    """
    Generates a comprehensive, structured microbiome dataset.
    """
    np.random.seed(42)

    # 1. Metadata Generation
    samples = [f"Sample{i+1}" for i in range(num_samples)]
    treatments = ['Control', 'TreatmentA', 'TreatmentB'] * (num_samples // 3)
    timepoints = np.tile([0, 1, 2], num_samples // 3)
    subjects = [f"Subject_{i//3 + 1}" for i in range(num_samples)]
    locations = ['Site1', 'Site2'] * (num_samples // 2) if num_samples % 2 == 0 else ['Site1', 'Site2'] * (num_samples // 2) + ['Site1']
    ph_values = np.round(np.random.normal(7.0, 0.5, num_samples), 2)
    runs = np.repeat([1, 2, 3], num_samples // 3)

    metadata_df = pd.DataFrame({
        'Treatment': treatments,
        'Timepoint': timepoints,
        'SubjectID': subjects,
        'Location': locations,
        'pH': ph_values,
        'Run': runs
    }, index=samples)

    # 2. Taxonomy Generation
    phyla = ['Firmicutes', 'Bacteroidetes', 'Proteobacteria', 'Actinobacteria', 'Verrucomicrobia']
    genera = ['Lactobacillus', 'Bacteroides', 'Escherichia', 'Bifidobacterium', 'Akkermansia', 'Faecalibacterium', 'Roseburia', 'Prevotella', 'Ruminococcus', 'Streptococcus']

    asv_names = [f"ASV_{i+1}" for i in range(num_asvs)]
    taxonomy_list = []
    for i in range(num_asvs):
        phylum = np.random.choice(phyla)
        genus = np.random.choice(genera) if phylum in ['Firmicutes', 'Bacteroidetes'] else 'Other'
        taxonomy_list.append({
            'ASV': asv_names[i],
            'Phylum': phylum,
            'Class': f"{phylum}_c",
            'Order': f"{phylum}_o",
            'Family': f"{genus}_f",
            'Genus': genus,
            'Species': f"{genus}_sp_{i%3+1}" if genus != 'Other' else np.nan
        })
    taxonomy_df = pd.DataFrame(taxonomy_list).set_index('ASV')

    # 3. ASV Table Generation (with deliberate structure)
    asv_table = pd.DataFrame(0, index=asv_names, columns=samples)

    # Baseline noise
    asv_table += np.random.randint(0, 50, size=asv_table.shape)

    # Add treatment-specific ASVs
    for i, asv in enumerate(['ASV_1', 'ASV_2', 'ASV_3']): # Indicator for Control
        asv_table.loc[asv, metadata_df[metadata_df['Treatment'] == 'Control'].index] += np.random.randint(100, 200)
    for i, asv in enumerate(['ASV_4', 'ASV_5', 'ASV_6']): # Indicator for TreatmentA
        asv_table.loc[asv, metadata_df[metadata_df['Treatment'] == 'TreatmentA'].index] += np.random.randint(150, 250)
    for i, asv in enumerate(['ASV_7', 'ASV_8', 'ASV_9']): # Indicator for TreatmentB
        asv_table.loc[asv, metadata_df[metadata_df['Treatment'] == 'TreatmentB'].index] += np.random.randint(120, 220)

    # Add time-dependent ASV
    for s in samples:
        timepoint = metadata_df.loc[s, 'Timepoint']
        asv_table.loc['ASV_10', s] += 50 * (timepoint + 1) + np.random.randint(0, 20)

    # Add ASV associated with a specific location and treatment
    loc_treat_samples = metadata_df[(metadata_df['Location'] == 'Site1') & (metadata_df['Treatment'] == 'TreatmentA')].index
    asv_table.loc['ASV_11', loc_treat_samples] += np.random.randint(200, 300)

    return metadata_df, asv_table.T, taxonomy_df # Transpose ASV table to have samples as rows

if __name__ == "__main__":
    metadata, feature_table, taxonomy = generate_microbiome_dataset()

    # Save to TSV files
    metadata.to_csv("example-metadata.tsv", sep='\t')
    feature_table.to_csv("example-feature-table.tsv", sep='\t')
    taxonomy.to_csv("example-taxonomy.tsv", sep='\t')

    print("Generated example files: example-metadata.tsv, example-feature-table.tsv, example-taxonomy.tsv")
