from DECIMER import predict_SMILES


class SMILESGenerator:

    def __init__(self):
        pass

    def generate_smiles(self, metadata_df):

        for index in metadata_df.index:

            image = metadata_df.loc[index, "clean_path"]

            try:

                smiles = predict_SMILES(image)

                metadata_df.loc[index, "smiles"] = smiles

                metadata_df.loc[index, "processed"] = True

                metadata_df.loc[index, "image_type"] = "chemical_structure"

                metadata_df.loc[index, "is_formula"] = True

            except Exception as e:

                print(f"Error processing {image}: {e}")

                metadata_df.loc[index, "smiles"] = ""

                metadata_df.loc[index, "processed"] = False

                metadata_df.loc[index, "image_type"] = "unknown"

                metadata_df.loc[index, "is_formula"] = False

        return metadata_df