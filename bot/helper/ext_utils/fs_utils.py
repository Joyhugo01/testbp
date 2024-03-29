import sys
from bot import aria2, LOGGER, DOWNLOAD_DIR
import shutil
import os
import pathlib
import mimetypes


def clean_download(path: str):
    pass


def start_cleanup():
    try:
        shutil.rmtree(DOWNLOAD_DIR)
    except FileNotFoundError:
        pass


def exit_clean_up(signal, frame):
    pass

def tar(orig_path: str):
    path = pathlib.PurePath(orig_path)
    base = path.name
    root = pathlib.Path(path.parent.as_posix()).absolute().as_posix()
    LOGGER.info(f'Tar: orig_path: {orig_path}, base: {base}, root: {root}')
    return shutil.make_archive(orig_path, 'tar', root, base)


def get_mime_type(file_path):
    mime_type = mimetypes.guess_type(file_path)[0]
    mime_type = mime_type if mime_type else "text/plain"
    return mime_type
