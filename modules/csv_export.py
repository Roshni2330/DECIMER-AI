from config import OUTPUT_FOLDER


class CSVExporter:

    def __init__(self):
        pass

    def export(
        self,
        metadata,
        metadata_df
    ):

        output_file = OUTPUT_FOLDER / (
            f"{metadata['doc_id']}_results.csv"
        )

        metadata_df.to_csv(
            output_file,
            index=False
        )

        return str(output_file)