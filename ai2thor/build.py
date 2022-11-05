import zipfile
import logging
import io
from ai2thor.platform import STR_PLATFORM_MAP, OSXIntel64, Linux64, CloudRendering
import platform

logger = logging.getLogger(__name__)

PUBLIC_S3_BUCKET = "ai2-thor-public"
PUBLIC_WEBGL_S3_BUCKET = "ai2-thor-webgl-public"
PRIVATE_S3_BUCKET = "ai2-thor-private"
PYPI_S3_BUCKET = "ai2-thor-pypi"

TEST_OUTPUT_DIRECTORY = "../../images-debug"

LOCAL_BUILD_COMMIT_ID = "local"
AUTO_BUILD_PLATFORMS = [OSXIntel64, Linux64, CloudRendering]

COMMIT_ID = None
try:
    import ai2thor._builds

    COMMIT_ID = ai2thor._builds.COMMIT_ID
except ImportError:
    pass


platform_map = dict(Linux64="Linux", OSXIntel64="Darwin")
arch_platform_map = {v: k for k, v in platform_map.items()}
