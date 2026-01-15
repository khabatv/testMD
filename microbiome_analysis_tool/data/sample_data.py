
import pandas as pd
import os

# --- Load the new comprehensive example files ---

# Define the path to the data files relative to this script's location
data_dir = os.path.dirname(__file__)

metadata_path = os.path.join(data_dir, 'example-metadata.tsv')
feature_table_path = os.path.join(data_dir, 'example-feature-table.tsv')
taxonomy_path = os.path.join(data_dir, 'example-taxonomy.tsv')

# Load the dataframes
sample_metadata_df = pd.read_csv(metadata_path, sep='\t', index_col=0)
# The feature table needs to be transposed to match the original format (samples x ASVs)
sample_seqtab = pd.read_csv(feature_table_path, sep='\t', index_col=0)
sample_taxa = pd.read_csv(taxonomy_path, sep='\t', index_col=0)

# Ensure consistent naming of index columns
sample_metadata_df.index.name = 'SampleID'
sample_seqtab.index.name = 'SampleID'
sample_taxa.index.name = 'ASV'

# Sample filenames are no longer needed as we are not simulating a FASTQ run with this data
sample_filenames = []
