import zipfile
from pathlib import Path
from superglue.environment.variables import SUPERGLUE_S3_BUCKET
from superglue.core.fileio import BaseFileIO


class SuperGlueModule(BaseFileIO):
    def __init__(self, parent_dir: Path, module_name: str, bucket: str = SUPERGLUE_S3_BUCKET):
        self.module_name = module_name
        self.root_module = parent_dir / module_name
        self.module_path = parent_dir / module_name / module_name
        self.zip_path = self.root_module / f"{self.module_name}.zip"
        self.relative_root = Path.cwd()

        super(SuperGlueModule, self).__init__(
            parent_dir=parent_dir,
            dir_name=module_name,
            bucket_prefix="shared",
            bucket=bucket,
        )

    def create(self) -> None:
        if not self.module_path.exists():
            self.module_path.mkdir(parents=True, exist_ok=True)

            init_py = self.module_path / "__init__.py"
            init_py.touch(exist_ok=True)
        else:
            print(f"shared python module {self.module_name} already exists.")

    def delete(self) -> None:
        pass

    def create_zip(self) -> None:
        with zipfile.ZipFile(self.zip_path, mode="w") as zip_file:
            for file in self.module_path.glob("**/*.py"):
                content = file.read_text()
                content = content.encode("utf-8")
                rel_path = file.relative_to(self.root_module).as_posix()
                zip_file.writestr(rel_path, content)
