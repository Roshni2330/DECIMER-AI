class Statistics:

    def __init__(self):
        pass

    def run(
        self,
        metadata_df,
        metadata,
        rendered_pages
    ):

        statistics = {

            "doc_id": metadata["doc_id"],

            "pdf_name": metadata["pdf_name"],

            "total_pages": len(rendered_pages),

            "total_structures": len(metadata_df),

            "successful_predictions": int(
                metadata_df["processed"].sum()
            ),

            "failed_predictions": int(
                (~metadata_df["processed"]).sum()
            )

        }

        return statistics