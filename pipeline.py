from modules.pdf_loader import PDFLoader
from modules.duplicate_checker import DuplicateChecker
from modules.renderer import Renderer
from modules.segmentation import Segmentation
from modules.dataframe_builder import DataFrameBuilder
from modules.cleaner import Cleaner
from modules.smiles_generator import SMILESGenerator
from modules.statistics import Statistics
from modules.csv_export import CSVExporter


class Pipeline:

    def __init__(self):

        self.pdf_loader = PDFLoader()

        self.duplicate_checker = DuplicateChecker()

        self.renderer = Renderer()

        self.segmentation = Segmentation()

        self.dataframe_builder = DataFrameBuilder()

        self.cleaner = Cleaner()

        self.smiles_generator = SMILESGenerator()

        self.statistics = Statistics()

        self.csv_export = CSVExporter()

    def run(self, pdf_path):

        # STEP 1
        metadata = self.pdf_loader.load_pdf(pdf_path)

        # STEP 2
        self.duplicate_checker.check_duplicate(
            metadata["pdf_hash"]
        )

        self.duplicate_checker.save_document(
            metadata
        )

        # STEP 3
        rendered_pages = self.renderer.render_pdf(
            metadata
        )

        # STEP 4
        segmented_metadata = self.segmentation.segment_pages(
            metadata,
            rendered_pages
        )

        # STEP 5
        metadata_df = self.dataframe_builder.build_dataframe(
            metadata,
            segmented_metadata
        )

        # STEP 6
        metadata_df = self.cleaner.clean_images(
            metadata,
            metadata_df
        )

        # STEP 7
        metadata_df = self.smiles_generator.generate_smiles(
            metadata_df
        )

        # STEP 8
        statistics = self.statistics.run(
            metadata_df,
            metadata,
            rendered_pages
        )

        # STEP 9
        csv_path = self.csv_export.export(
            metadata,
            metadata_df
        )

        return {

            "metadata": metadata,

            "statistics": statistics,

            "dataframe": metadata_df,

            "csv_path": csv_path

        }