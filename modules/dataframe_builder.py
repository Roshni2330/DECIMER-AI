import pandas as pd


class DataFrameBuilder:

    def __init__(self):
        pass

    def build_dataframe(
        self,
        metadata,
        segmented_metadata
    ):

        rows = []

        for item in segmented_metadata:

            rows.append({

                "doc_id": metadata["doc_id"],

                "pdf_name": metadata["pdf_name"],

                "page_number": item["page_number"],

                "image_id": item["image_id"],

                "image_path": item["image_path"],

                "clean_path": "",

                "image_type": "",

                "is_formula": False,

                "smiles": "",

                "processed": False

            })

        metadata_df = pd.DataFrame(rows)

        return metadata_df