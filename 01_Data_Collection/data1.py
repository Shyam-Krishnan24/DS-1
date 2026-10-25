
# pyrefly: ignore[missing-import]
import kagglehub

path = kagglehub.dataset_download(
    "olistbr/brazilian-ecommerce",
    output_dir="Datasets"
    )

print("Path to dataset files:", path)

