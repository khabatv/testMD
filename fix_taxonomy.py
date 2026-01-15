import pandas as pd

# Load the taxonomy file
taxonomy_df = pd.read_csv("microbiome_analysis_tool/data/example-taxonomy.tsv", sep='\t', index_col=0)

# Add the 'Kingdom' column
taxonomy_df.insert(0, 'Kingdom', 'Bacteria')

# Save the corrected file
taxonomy_df.to_csv("microbiome_analysis_tool/data/example-taxonomy.tsv", sep='\t')

print("Successfully added the 'Kingdom' column to the taxonomy file.")
