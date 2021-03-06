import os
import sys
from pathlib import Path
from dotenv import load_dotenv


# TODO: There has to be something better than this hack
program_name = Path(sys.argv[0]).parent.parts[-1]

if program_name == "pytest":
    load_dotenv(".test.env", override=True)
else:
    # load the environment file
    load_dotenv()


SUPERGLUE_S3_BUCKET = os.getenv("SUPERGLUE_S3_BUCKET")
SUPERGLUE_IAM_ROLE = os.getenv("SUPERGLUE_IAM_ROLE")

# for name validation
SUPERGLUE_JOB_PREFIX = os.getenv("SUPERGLUE_JOB_PREFIX", "")
SUPERGLUE_JOB_SUFFIX = os.getenv("SUPERGLUE_JOB_SUFFIX", "")

# For simple account validation
SUPERGLUE_AWS_ACCOUNT = int(os.getenv("SUPERGLUE_AWS_ACCOUNT"))

# keep this as we may want logging
SUPERGLUE_LOGGER_DIR = Path(os.getenv("SUPERGLUE_LOGGER_FILE", "./logs"))
# SUPERGLUE_LOGGER_DIR.mkdir(exist_ok=True, parents=True)

